"""
LLM客户端封装
统一使用OpenAI格式调用
"""

import json
import re
import time
import uuid
import urllib.request
from typing import Optional, Dict, Any, List
from openai import OpenAI

from ..config import Config
from .logger import get_logger

logger = get_logger('mirofish.llm_client')

DEBUG_LOG_PATH = r"c:\Users\abhin\OneDrive\Desktop\BTech S2\HTML\MiroFish-main\.cursor\debug.log"


def _debug_log(run_id: str, hypothesis_id: str, location: str, message: str, data: Dict[str, Any]) -> None:
    # region agent log
    payload = {
        "id": f"log_{int(time.time() * 1000)}_{uuid.uuid4().hex[:8]}",
        "runId": run_id,
        "hypothesisId": hypothesis_id,
        "location": location,
        "message": message,
        "data": data,
        "timestamp": int(time.time() * 1000),
    }
    try:
        req = urllib.request.Request(
            "http://127.0.0.1:7242/ingest/da22a715-252e-4065-a0d9-3f79c32fbb11",
            data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=2):
            pass
    except Exception:
        pass
    try:
        import os
        os.makedirs(os.path.dirname(DEBUG_LOG_PATH), exist_ok=True)
        with open(DEBUG_LOG_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(payload, ensure_ascii=False) + "\n")
    except Exception:
        pass
    # endregion


class LLMClient:
    """LLM客户端"""
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        model: Optional[str] = None
    ):
        run_id = "pre-fix"
        self.api_key = api_key or Config.LLM_API_KEY
        self.base_url = base_url or Config.LLM_BASE_URL
        self.model = model or Config.LLM_MODEL_NAME
        
        # Fallback configs
        self.fallback_api_key = Config.LLM_FALLBACK_API_KEY
        self.fallback_base_url = Config.LLM_FALLBACK_BASE_URL
        self.fallback_model = Config.LLM_FALLBACK_MODEL_NAME
        self.using_fallback = False
        _debug_log(
            run_id=run_id,
            hypothesis_id="H1_H2",
            location="backend/app/utils/llm_client.py:LLMClient.__init__",
            message="LLM client initialized with runtime config",
            data={
                "base_url": self.base_url,
                "model": self.model,
                "api_key_present": bool(self.api_key),
            },
        )
        
        if not self.api_key:
            raise ValueError("LLM_API_KEY 未配置")
        
        # default headers including optional OpenRouter headers
        default_headers = None
        if self.base_url and "openrouter.ai" in self.base_url:
            default_headers = {
                "HTTP-Referer": "http://localhost:5173",  # Local dev URL for frontend integration
                "X-OpenRouter-Title": "MiroFish",  # Your App Name
            }
        
        self.client = OpenAI(
            api_key=self.api_key,
            base_url=self.base_url,
            default_headers=default_headers
        )
    
    def chat(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        max_tokens: int = 4096,
        response_format: Optional[Dict] = None
    ) -> str:
        """
        发送聊天请求
        
        Args:
            messages: 消息列表
            temperature: 温度参数
            max_tokens: 最大token数
            response_format: 响应格式（如JSON模式）
            
        Returns:
            模型响应文本
        """
        run_id = "pre-fix"
        logger.debug(f"LLM请求: model={self.model}, base_url={self.base_url}, messages={len(messages)}")
        _debug_log(
            run_id=run_id,
            hypothesis_id="H1_H2_H3",
            location="backend/app/utils/llm_client.py:LLMClient.chat",
            message="Preparing chat.completions request",
            data={
                "base_url": self.base_url,
                "model": self.model,
                "temperature": temperature,
                "max_tokens": max_tokens,
                "messages_count": len(messages),
                "last_role": messages[-1].get("role") if messages else None,
                "last_content_len": len(messages[-1].get("content", "")) if messages else 0,
                "has_response_format": bool(response_format),
            },
        )
        kwargs = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }
        
        if response_format:
            kwargs["response_format"] = response_format
        
        max_retries = 3
        retry_delays = [15, 30, 60]  # seconds between retries
        
        for attempt in range(max_retries + 1):
            try:
                response = self.client.chat.completions.create(**kwargs)
                break  # Success, exit retry loop
            except Exception as e:
                error_text = str(e)
                _debug_log(
                    run_id=run_id,
                    hypothesis_id="H1_H2_H4",
                    location="backend/app/utils/llm_client.py:LLMClient.chat",
                    message=f"chat.completions request failed (attempt {attempt + 1}/{max_retries + 1})",
                    data={
                        "error_type": type(e).__name__,
                        "error_text": error_text[:500],
                        "base_url": self.base_url,
                        "model": self.model,
                        "attempt": attempt + 1,
                    },
                )
                lowered = error_text.lower()
                is_rate_limit = "resource_exhausted" in lowered or "quota" in lowered or "error code: 429" in lowered or "429" in lowered
                
                if is_rate_limit:
                    if self.fallback_api_key and not self.using_fallback:
                        logger.warning(f"Rate limit/quota hit (429) on primary key. Switching to fallback API key & model.")
                        # Swap parameters to fallback
                        self.api_key = self.fallback_api_key
                        self.base_url = self.fallback_base_url
                        self.model = self.fallback_model
                        self.using_fallback = True
                        
                        # Re-initialize the client
                        default_headers = None
                        if self.base_url and "openrouter.ai" in self.base_url:
                            default_headers = {
                                "HTTP-Referer": "http://localhost:5173", 
                                "X-OpenRouter-Title": "MiroFish",
                            }
                        self.client = OpenAI(
                            api_key=self.api_key,
                            base_url=self.base_url,
                            default_headers=default_headers
                        )
                        # Re-update kwargs model
                        kwargs["model"] = self.model
                        continue  # Immediately retry with the fallback client
                        
                    if attempt < max_retries:
                        delay = retry_delays[attempt]
                        logger.warning(
                            f"Rate limit hit (429). Retrying in {delay}s... "
                            f"(attempt {attempt + 1}/{max_retries})"
                        )
                        time.sleep(delay)
                        continue  # Retry
                    else:
                        raise RuntimeError(
                            f"LLM quota exhausted (429) after {max_retries + 1} attempts. "
                            "Please enable billing/increase quota for your API key, then retry report generation."
                        ) from e
                
                raise  # Non-rate-limit errors propagate immediately
        
        content = response.choices[0].message.content
        # 部分模型（如MiniMax M2.5）会在content中包含<think>思考内容，需要移除
        content = re.sub(r'<think>[\s\S]*?</think>', '', content).strip()
        return content
    
    def chat_json(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.3,
        max_tokens: int = 4096
    ) -> Dict[str, Any]:
        """
        发送聊天请求并返回JSON
        
        Args:
            messages: 消息列表
            temperature: 温度参数
            max_tokens: 最大token数
            
        Returns:
            解析后的JSON对象
        """
        response = self.chat(
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            response_format={"type": "json_object"}
        )
        # 清理markdown代码块标记
        cleaned_response = response.strip()
        cleaned_response = re.sub(r'^```(?:json)?\s*\n?', '', cleaned_response, flags=re.IGNORECASE)
        cleaned_response = re.sub(r'\n?```\s*$', '', cleaned_response)
        cleaned_response = cleaned_response.strip()

        try:
            return json.loads(cleaned_response)
        except json.JSONDecodeError:
            raise ValueError(f"LLM返回的JSON格式无效: {cleaned_response}")

