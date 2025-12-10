import os
from autogen import ConversableAgent
from llm_config import llm_config
from dotenv import load_dotenv

# llm_config = {"config_list": [{"model": "gpt-4", "api_key" : os.environ.get("OPENAI_API_KEY")}]}

load_dotenv()


## termination using is_termination flag
Player_1 = ConversableAgent(
    "Player_1",
    system_message= (
       "You are playing a game of guess-my-number. You have the number 66 in your mind, "
        "and I will try to guess it.\n"
        "If my guess is much higher than your number, say 'too high'.\n"
        "If my guess is much lower than your number, say 'too low'.\n"
        "If my guess is only slightly higher than your number (within 5), say 'high'.\n"
        "If my guess is only slightly lower than your number(within 5), say 'low'.\n"
        "If I guess your number correctly, say 'correct'."
    ),
    llm_config = llm_config,
    is_termination_msg = lambda msg: "correct" in msg["content"],  # this will make the conversation end when the correct number is guessed
    human_input_mode = 'NEVER'
)


Player_2 = ConversableAgent(
    "Player_2",
    system_message=(
        "I have a number in my mind, and you will try to guess it.\n"
        "If I say 'too high', you should guess a much lower number.\n"
        "If I say 'high', you should guess a slightly lower number.\n"
        "If I say 'too low', you should guess a much higher number.\n"
        "If I say 'low', you should guess a slightly higher number.\n"
        "Keep adjusting your guess based on the feedback until you get it right."
    ),
    llm_config=llm_config,
    human_input_mode="NEVER",
)


# Player_1.initiate_chat(
#     Player_2,
#     message = " I have a number between 1 and 100, Guess it!! "
# )


# ALWAYS method
human_proxy = ConversableAgent(
    "human_proxy",
    llm_config=False,  # no LLM used for human proxy
    human_input_mode="ALWAYS"   # always ask for human input
)


# TERMINATE method

Player_1_with_term = ConversableAgent(
    "Player_1",
    system_message= (
       "You are playing a game of guess-my-number. You have the number 66 in your mind, "
        "and I will try to guess it.\n"
        "If my guess is much higher than your number, say 'too high'.\n"
        "If my guess is much lower than your number, say 'too low'.\n"
        "If my guess is only slightly higher than your number (within 5), say 'high'.\n"
        "If my guess is only slightly lower than your number(within 5), say 'low'.\n"
        "If I guess your number correctly, say 'correct'."
    ),
    llm_config = llm_config,
    max_consecutive_auto_reply= 1,
    is_termination_msg = lambda msg: "correct" in msg["content"],  # this will make the conversation end when the correct number is guessed
    human_input_mode = 'TERMINATE'
)



if __name__ == "__main__":
    # Player_1.initiate_chat(
    #     Player_2,
    #     message=" I have a number between 1 and 100. Guess it!"

    # )
    # result = human_proxy.initiate_chat(
    #     Player_1,
    #     message='11'
    # )

    result = Player_1_with_term.initiate_chat(
        Player_2,
        message='I have a number between 1 and 100, guess it'
    )