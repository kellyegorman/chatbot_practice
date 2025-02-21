import openai

client = openai.OpenAI(api_key="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")

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__=="__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)