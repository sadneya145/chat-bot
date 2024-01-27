import requests
import json

url = "https://chatgpt-42.p.rapidapi.com/conversationgpt4"
headers = {
    "Content-Type": "application/json",
    "X-RapidAPI-Key": "68ff9939c8msh2c3041494ed290dp148805jsn89dbb091c75b",
    "X-RapidAPI-Host": "chatgpt-42.p.rapidapi.com",
}

def chat_with_chatgpt(prompt):
    data = {
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "system_prompt": "",
        "temperature": 0.9,
        "top_k": 5,
        "top_p": 0.9,
        "max_tokens": 256,
        "web_access": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        # Print the entire response content for debugging
        print(response.text)

        # Check if 'choices' and 'message' keys exist
        choices = response.json().get('choices', [])
        if choices and len(choices) > 0:
            message = choices[0].get('message', '')
            return message.strip()
        else:
            return "Error: Unexpected response format"
    else:
        return f"Error: {response.status_code}, {response.text}"

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_chatgpt(user_input)
        print("Chatbot:", response)
