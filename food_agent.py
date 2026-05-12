from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def food_ai_agent(user_input):
    """
    Food AI Agent Function
    """

    system_prompt = """
    You are an intelligent Food AI Assistant.

    Your tasks:
    - Recommend recipes
    - Suggest healthy meals
    - Provide cooking tips
    - Suggest foods based on ingredients
    - Recommend vegetarian, vegan, keto, or protein-rich meals
    - Keep responses clear and friendly
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7,
        max_tokens=500
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    print("🍔 Food AI Agent Started")
    print("Type 'exit' to stop")

    while True:
        user_query = input("\nYou: ")

        if user_query.lower() == "exit":
            print("Goodbye!")
            break

        answer = food_ai_agent(user_query)

        print("\nFood AI:")
        print(answer)
