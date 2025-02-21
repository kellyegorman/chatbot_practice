import requests
import json

# Set your Google Gemini API Key
api_key = "AIzaSyAcJc4UIJkjVZMe926br2W63KwLf6L44fo"  # Replace with your actual key
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

def chat_with_gemini(prompt):
    headers = {
        "Content-Type": "application/json"
    }

    # Construct the request body
    body = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    # Send a request to the Gemini API, passing the API key as a query parameter
    response = requests.post(url, headers=headers, params={"key": api_key}, json=body)

    if response.status_code == 200:
        response_data = response.json()
        return response_data["candidates"][0]["content"]["parts"][0]["text"]
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return "Sorry, I couldn't get a response."

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_gemini(user_input)
        print("Chatbot:", response)
