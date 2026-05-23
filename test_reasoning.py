import os
from openai import OpenAI
from dotenv import load_dotenv

# Load env variables
load_dotenv()

client = OpenAI(
  base_url=os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1"),
  api_key=os.getenv("OPENROUTER_API_KEY", ""),
)

print("Making the first API call...")
try:
    # First API call with reasoning
    response = client.chat.completions.create(
      model="qwen/qwen3-coder:free",
      timeout=15, # Stop hanging forever
      messages=[
              {
                "role": "user",
                "content": "How many r's are in the word 'strawberry'?"
              }
            ],
      extra_body={"reasoning": {"enabled": True}}
    )

    # Extract the assistant message with reasoning_details
    message = response.choices[0].message
    print("\n--- FIRST RESPONSE ---")
    print(message.content)

    # Preserve the assistant message with reasoning_details
    messages = [
      {"role": "user", "content": "How many r's are in the word 'strawberry'?"},
      {
        "role": "assistant",
        "content": message.content,
      },
      {"role": "user", "content": "Are you sure? Think carefully."}
    ]
    
    # Only add reasoning_details if the API returned it
    if hasattr(message, 'reasoning_details') and message.reasoning_details:
         messages[1]["reasoning_details"] = message.reasoning_details

    print("\nMaking the second API call to continue the logic...")
    # Second API call - model continues reasoning from where it left off
    response2 = client.chat.completions.create(
      model="qwen/qwen3-coder:free",
      timeout=15, # Stop hanging forever
      messages=messages,
      extra_body={"reasoning": {"enabled": True}}
    )
    
    print("\n--- SECOND RESPONSE ---")
    print(response2.choices[0].message.content)

except Exception as e:
    print(f"\nAn error occurred: {e}")
