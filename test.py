from dotenv import load_dotenv
import os

load_dotenv()
print("Environment variables:")
print(f"GEMINI_API_KEY exists: {'GEMINI_API_KEY' in os.environ}")
print(f"Key value: {os.getenv('GEMINI_API_KEY')}")
print(f"Current directory: {os.getcwd()}")