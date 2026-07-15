import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env
load_dotenv()

# Read API key
api_key = os.getenv("GROQ_API_KEY")

# Check if API key exists
if not api_key:
    raise ValueError("GROQ_API_KEY is missing from the .env file")

print("✅ API key loaded successfully.")

# Create Groq client
client = Groq(api_key=api_key)

try:
    # Send request to Groq
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            },
            {
                "role": "user",
                "content": "Explain what Python is in one paragraph."
            }
        ],
        temperature=0.5,
        max_tokens=300
    )

    # Print response
    print("\n========== RESPONSE ==========\n")
    print(response.choices[0].message.content)

except Exception as e:
    print(f"❌ Error: {e}")