import google.generativeai as genai
import os
import json

# 设置你的 Gemini API 密钥
import os

api_key = os.environ.get("GOOGLE_API_KEY")
print(api_key)

def generate_patients_with_gemini(count=100):
    prompt = (
        f"请生成{count}个虚拟病人信息，每个病人包含姓名、年龄、性别、疾病。"
        "请用JSON数组格式返回，每个元素是一个对象，字段为name, age, gender, disease。"
        "姓名用中英文混合，疾病可以常见疾病。"
    )
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    # 解析 Gemini 返回的 JSON
    try:
        patients = json.loads(response.text)
    except Exception:
        patients = response.text
    return patients

if __name__ == "__main__":
    patients = generate_patients_with_gemini(100)
    with open("gemini_patients.json", "w") as f:
        json.dump(patients, f, ensure_ascii=False, indent=2)
    print("Generated 100 virtual patients using Gemini API and saved to gemini_patients.json")