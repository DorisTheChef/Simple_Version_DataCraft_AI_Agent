import os
import google.generativeai as genai
import json
import pandas as pd
import re

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
    raw_text = response.text
    print("Gemini返回内容：", raw_text)
    # 尝试提取第一个 [ ... ] 之间的内容
    match = re.search(r"\[.*\]", raw_text, re.DOTALL)
    if match:
        cleaned = match.group(0)
    else:
        cleaned = raw_text
    print("清理后的内容：", cleaned)  # 新增这一行
    try:
        patients = json.loads(cleaned)
    except Exception as e:
        print("无法解析为JSON, 原因：", e)
        patients = None
    return raw_text, patients

if __name__ == "__main__":
    count = 100  # 你可以根据需要修改生成数量
    raw_text, patients = generate_patients_with_gemini(count)
    with open("gemini_virtual_patients_raw.txt", "w", encoding="utf-8") as f:
        f.write(raw_text)
    print("已保存原始Gemini返回内容到 gemini_virtual_patients_raw.txt")
    # 保存CSV
    if patients and isinstance(patients, list):
        df = pd.DataFrame(patients)
        df.to_csv("gemini_virtual_patients.csv", index=False)
        print(f"已生成 {len(df)} 条虚拟病人数据，并保存为 gemini_virtual_patients.csv")
    else:
        print("未能生成有效的病人数据。")