import random
import json

first_names = ["John", "Jane", "Alex", "Emily", "Chris", "Katie", "Mike", "Laura", "David", "Sophia"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Martinez", "Lee"]
genders = ["Male", "Female"]
diseases = ["Diabetes", "Hypertension", "Asthma", "Flu", "COVID-19", "Cancer", "Allergy", "Arthritis"]

def generate_patient():
    return {
        "name": f"{random.choice(first_names)} {random.choice(last_names)}",
        "age": random.randint(1, 100),
        "gender": random.choice(genders),
        "disease": random.choice(diseases)
    }

def generate_patients(n=100):
    return [generate_patient() for _ in range(n)]

if __name__ == "__main__":
    patients = generate_patients(100)
    with open("patients.json", "w") as f:
        json.dump(patients, f, indent=2)
    print("Generated 100 virtual patients and saved to patients.json")