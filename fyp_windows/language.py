from openai import OpenAI
import json

client = OpenAI(
    base_url="https://api.deepseek.com",
    api_key="sk-64c254ce5055444c81584282b4ed47c9",
)

"""client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="YOUR-KEY-IN-THIS-PLATFORM",
)"""

"""client = OpenAI(
    base_url="https://api.openai.com/v1/",
    api_key="YOUR-KEY-IN-THIS-PLATFORM",
)"""

def is_json(text):
    """
    identify the string is json or not
    """
    try:
        json.loads(text)
        return True
    except json.JSONDecodeError:
        return False

def read_system_prompts(file_path):
    """
    load the txt format system prompt
    """
    with open(file_path, "r", encoding="utf-8") as file:
        system_prompts = file.read()
    return system_prompts

system_prompt = read_system_prompts("sources/prompts/prompt1.txt")
send_messages = [
    {"role": "system", "content": system_prompt}
]

def reStart():
    """
    clear the conversation context crash
    :return:
    """
    send_messages.clear()
    send_messages.append({"role": "system", "content": system_prompt})

def chat_with_model(user_input):
    """
    app chatting mode
    """
    send_messages.append({"role": "user", "content": user_input+"(must reply in json format)"})
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=send_messages,
        temperature=1
    )
    while True:
        try:
            response = response.choices[0].message.content.replace("`","").replace("json","")
            assistant_reply_json = json.loads(response)
            break
        except json.JSONDecodeError:
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=send_messages,
                temperature=1
            )

    assistant_reply = assistant_reply_json["response"]
    positive = assistant_reply_json["isValid"]
    send_messages.append({"role": "assistant", "content": assistant_reply})
    keywords = ["sword","shield","dagger","blade","wand"]
    matched_words = [word for word in keywords if word in assistant_reply]

    if any(matched_words):
        return assistant_reply, True, matched_words[0], positive
    else:
        return assistant_reply, False, None, positive

def prompt_with_model(user_input):
    """
    evaluation chatting mode
    """
    eval_messages = [
        {"role": "system", "content": system_prompt}
    ]
    for item in user_input:
        eval_messages.append(item)

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=eval_messages
    )

    assistant_reply = response.choices[0].message.content

    return assistant_reply

