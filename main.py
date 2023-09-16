import requests
import openai

api_key = "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"
openai.api_key = api_key


def fetch_website_data(website_url):
    response = requests.get(website_url)

    if response.status_code == 200:
        website_data = response.json()
        title = website_data.get("title", "")
        body = website_data.get("body", "")
    else:
        print("Failed to fetch website data.")
        title, body = "", ""

    return title, body


website_url = "https://jsonplaceholder.typicode.com/posts/1"
title, body = fetch_website_data(website_url)

context = f"Website Title: {title}\n\nWebsite Content: {body}\n\nUser: "


def get_chatbot_response(user_input, context):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{context}{user_input}\n",
        max_tokens=50,
        temperature=0.7,
        stop=None
    )
    return response.choices[0].text.strip()



print("Chatbot: Hello! How can I assist you?")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = get_chatbot_response(user_input, context)
    print(f"Chatbot: {response}")
