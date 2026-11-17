
import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()


def generate_health_remark(glucose, haemoglobin, cholesterol):

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return "AI API key is not configured."

    try:
        client = genai.Client(api_key=api_key)

        prompt = f"""
Analyse these blood test values for a demonstration application:

Glucose: {glucose}
Haemoglobin: {haemoglobin}
Cholesterol: {cholesterol}

Give a short general health observation in 1 or 2 sentences.
Do not provide a medical diagnosis.
Mention that this is an AI-generated observation.
Recommend consulting a qualified healthcare professional.
"""

        for attempt in range(3):
            try:
                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt
                )

                if response.text:
                    return response.text.strip()

                return "AI response was empty. Please try again."

            except Exception as e:
                error = str(e)
                print("Gemini API Error:", error)

                if "503" in error or "UNAVAILABLE" in error:
                    if attempt < 2:
                        time.sleep(3)
                        continue

                return (
                    "AI service is temporarily unavailable. "
                    "Please try again later. This is not a medical diagnosis."
                )

    except Exception as e:
        print("Gemini API Error:", str(e))
        return "AI service is temporarily unavailable. Please try again later."
