# main/gemini_api.py
import os
import google.generativeai as genai

# Configure the API key
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
)

def generate_proposal_with_gemini(prompt):
    try:
        response = model.generate_content([prompt])
        return response.text
    except Exception as e:
        print(f"Error during API request: {e}")
        return f"Error generating proposal: {e}"
