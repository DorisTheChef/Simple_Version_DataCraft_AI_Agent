import os
import google.generativeai as genai
import json
import pandas as pd
import re

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

def generate_patients_with_gemini(count=10):
    prompt = (
        f"Please generate {count} virtual patient records, each patient including name, age, gender, disease. "
        "Please return in JSON array format, each element is an object with fields: name, age, gender, disease. "
        "Use mixed English names, and common diseases."
    )
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    raw_text = response.text
    print("Gemini response content:", raw_text)
    # Try to extract content between the first [ ... ]
    match = re.search(r"\[.*\]", raw_text, re.DOTALL)
    if match:
        cleaned = match.group(0)
    else:
        cleaned = raw_text
    print("Cleaned content:", cleaned)  # Added this line
    try:
        patients = json.loads(cleaned)
    except Exception as e:
        print("Unable to parse as JSON, reason:", e)
        patients = None
    return raw_text, patients

if __name__ == "__main__":
    count = 100  # You can modify the generation count as needed
    raw_text, patients = generate_patients_with_gemini(count)
    with open("gemini_virtual_patients_raw.txt", "w", encoding="utf-8") as f:
        f.write(raw_text)
    print("Saved raw Gemini response content to gemini_virtual_patients_raw.txt")
    # Save CSV
    if patients and isinstance(patients, list):
        df = pd.DataFrame(patients)
        df.to_csv("gemini_virtual_patients.csv", index=False)
        print(f"Generated {len(df)} virtual patient records and saved as gemini_virtual_patients.csv")
    else:
        print("Failed to generate valid patient data.")