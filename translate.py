import os

home_path = r"c:\Users\abhin\OneDrive\Desktop\BTech S2\HTML\MiroFish-main\frontend\src\views\Home.vue"
index_path = r"c:\Users\abhin\OneDrive\Desktop\BTech S2\HTML\MiroFish-main\frontend\index.html"

# Dictionary of translations
translations_home = {
    "访问我们的Github主页": "Visit our Github page",
    "简洁通用的群体智能引擎": "Simple and Universal Swarm Intelligence Engine",
    "v0.1-预览版": "v0.1-Preview",
    "上传任意报告<br>": "Upload Any Report<br>",
    "即刻推演未来": "Deduce the Future Instantly",
    "即使只有一段文字，<span class=\"highlight-bold\">MiroFish</span> 也能基于其中的现实种子，全自动生成与之对应的至多<span class=\"highlight-orange\">百万级Agent</span>构成的平行世界。通过上帝视角注入变量，在复杂的群体交互中寻找动态环境下的<span class=\"highlight-code\">“局部最优解”</span>": "Even with just a paragraph of text, <span class=\"highlight-bold\">MiroFish</span> can use it as a reality seed to automatically generate a parallel world of up to <span class=\"highlight-orange\">millions of Agents</span>. Inject variables from a God's-eye view, and find the <span class=\"highlight-code\">\"local optimal solution\"</span> in dynamic environments through complex swarm interactions.",
    "让未来在 Agent 群中预演，让决策在百战后胜出": "Rehearse the future among Agents, let the decision win after hundred battles",
    "系统状态": "System Status",
    "准备就绪": "Ready",
    "预测引擎待命中，可上传多份非结构化数据以初始化模拟序列": "Prediction engine on standby. Upload multiple unstructured data to initialize simulation sequences.",
    "低成本": "Low Cost",
    "常规模拟平均5$/次": "Avg $5/simulation",
    "高可用": "High Availability",
    "最多百万级Agent模拟": "Up to millions of Agents",
    "工作流序列": "Workflow Sequence",
    "图谱构建": "Graph Building",
    "现实种子提取 & 个体与群体记忆注入 & GraphRAG构建": "Reality seed extraction & Individual/collective memory injection & GraphRAG construction",
    "环境搭建": "Environment Setup",
    "实体关系抽取 & 人设生成 & 环境配置Agent注入仿真参数": "Entity relationship extraction & Persona generation & Agent config injection",
    "开始模拟": "Start Simulation",
    "双平台并行模拟 & 自动解析预测需求 & 动态更新时序记忆": "Dual-platform simulation & Auto-parse predictions & Dynamic memory updates",
    "报告生成": "Report Generation",
    "ReportAgent拥有丰富的工具集与模拟后环境进行深度交互": "ReportAgent has a rich toolset to interact with the post-simulation environment",
    "深度互动": "Deep Interaction",
    "与模拟世界中的任意一位进行对话 & 与ReportAgent进行对话": "Chat with any agent in the simulated world & Interact with ReportAgent",
    "01 / 现实种子": "01 / Reality Seeds",
    "支持格式: PDF, MD, TXT": "Supported formats: PDF, MD, TXT",
    "拖拽文件上传": "Drag and Drop to Upload",
    "或点击浏览文件系统": "Or click to browse file system",
    "输入参数": "Input Parameters",
    "02 / 模拟提示词": "02 / Simulation Prompt",
    "用自然语言输入模拟或预测需求（例.武大若发布撤销肖某处分的公告，会引发什么舆情走向）": "Describe simulation or prediction requirements in natural language (e.g., What public opinion trend will emerge if Wuhan University announces the revocation of an expulsion?)",
    "引擎: MiroFish-V1.0": "Engine: MiroFish-V1.0",
    "启动引擎": "Start Engine",
    "初始化中...": "Initializing..."
}

translations_index = {
    "zh-CN": "en",
    "社交媒体舆论模拟系统": "Social Media Public Opinion Simulation System",
    "预测万物": "Predict Everything"
}

def translate_file(path, translations):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for zh, en in translations.items():
        content = content.replace(zh, en)
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Translated {path}")

translate_file(home_path, translations_home)
translate_file(index_path, translations_index)
