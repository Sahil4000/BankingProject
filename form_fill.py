
import json
import openai
from config import AZURE_OPENAI_KEY

openai.api_key = AZURE_OPENAI_KEY

def load_form_template(filename):
    with open(f"templates/{filename}", "r") as file:
        return json.load(file)

def fill_form_with_gpt(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5
    )
    return response.choices[0].text.strip()
