import os
import google.generativeai as genai
import json

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

def generate_patients_with_gemini(count=10):
    prompt = (
        f"请生成{count}个虚拟病人信息，每个病人包含姓名、年龄、性别、疾病。"
        "请用JSON数组格式返回，每个元素是一个对象，字段为name, age, gender, disease。"
        "姓名用中英文混合，疾病可以常见疾病。"
    )
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    print("Gemini返回内容：", response.text)  # 新增这一行
    try:
        patients = json.loads(response.text)
    except Exception:
        patients = response.text
    return patients