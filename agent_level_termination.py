import os
from autogen import AssistantAgent, UserProxyAgent, ConversableAgent
from dotenv import load_dotenv

# llm_config = {"config_list": [{"model": "gpt-4", "api_key" : os.environ.get("OPENAI_API_KEY")}]}

load_dotenv()

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


Jack = ConversableAgent(
    "Jack",
    system_message= "your name is jack and you are a part of duo of comedians",
    llm_config = llm_config,
    human_input_mode = 'NEVER'
)

Jill = ConversableAgent(
    "Jill",
    system_message= "your name is jack and you are a part of duo of comedians",
    llm_config = llm_config,
    human_input_mode = 'NEVER',
    max_consecutive_auto_reply= 1,
    # is_termination_msg = lambda msg: "good bye" in msg["content"].lower()
)


Jill.initiate_chat(Jack, message = "Jack, tell me a joke")

