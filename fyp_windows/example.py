import json

if __name__ == "__main__":
    print("Hello, world!")

    example = [[ [ {"role": "user", "content": "What's your name?"},
                   {"role": "assistant", "content": "My name is LLM."},
                   {"role": "user", "content": "What's the capital of France?"},
                   {"role": "assistant", "content": "The capital of France is Paris."}],

                   "My name is LLM"],

               [ [],

                "The capital of France is Paris"]]

    """with open("sources/data.json", "w") as json_file:
        json.dump(example, json_file, indent=4)
    """
    with open("sources/data.json", "r") as json_file:
        data = json.load(json_file)

    questions = [item[0] for item in data]

    answers = [item[1] for item in data]

    messages = [
        {"role": "system", "content": "hhhhh"}
    ]
    for i in questions[0]:
        messages.append(i)
    print(messages)


    def read_system_prompts(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            system_prompts = file.read()
        return system_prompts


    file_path = "sources/prompts/prompt1.txt"
    system_prompts = read_system_prompts(file_path)

    print(system_prompts)