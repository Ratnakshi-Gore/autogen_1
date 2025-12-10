import os
from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv

# llm_config = {"config_list": [{"model": "gpt-4", "api_key" : os.environ.get("OPENAI_API_KEY")}]}


llm_config = {
    "config_list": [
        {
            "model": "llama3.2",  # This is your Ollama model name
            "api_key": os.getenv("OLLAMA_API_KEY", "ollama"),
            "base_url": os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1"),
            "api_type": "openai",  # keep it simple + compatible
            "price": [0, 0]
        }
    ]
}

assistant = AssistantAgent(
    "assistant",
    llm_config=llm_config,
    system_message="You are a helpful assistant. Reply in natural language. Do not write code unless explicitly asked."
    )

user_proxy = UserProxyAgent(
    "user_proxy",
    human_input_mode="ALWAYS",
    code_execution_config=False)

user_proxy.initiate_chat(
    assistant,
    message="tell me fun fact about cats"
    )