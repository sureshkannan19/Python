from dotenv import load_dotenv
from google import genai

load_dotenv()

try:
    client = genai.Client()
except Exception as e:
    print("Error: The GEMINI_API_KEY environment variable is not set.", e)
    exit()

MODEL_NAME = 'gemini-2.5-flash'
prompt = "Explain why Java is a good choice for enterprise backend development in one sentence."

try:
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
    print(response.text)
except Exception as e:
    print(f"An error occurred during API call: {e}")
