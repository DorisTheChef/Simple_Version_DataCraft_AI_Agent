# Simple Version DataCraft AI Agent

This project is a virtual patient data generator powered by Google Gemini LLM. It includes a backend API, a frontend web page, and one-click startup scripts.

## Features

- Instantly generate any number of virtual patient records (name, age, gender, disease)
- Supports mixed Chinese/English names and common diseases
- Visualize and download CSV data from the frontend
- Backend built with Flask, using Gemini API for data generation
- One-click startup scripts that automatically open the frontend

## Project Structure

```
SimpleVersion_DataCraft/
├── app.py                        # Flask backend main program
├── generate_patients.py          # Gemini data generation logic
├── frontend/index.html           # Frontend web page
├── start.sh                      # One-click shell startup script (recommended)
├── start_app.py                  # One-click Python startup script
├── gemini_virtual_patients.csv   # Generated patient data (CSV)
├── gemini_virtual_patients_raw.txt # Raw Gemini API output
├── patients.json                 # Example patient data
├── ...
```

## Quick Start

1. **Install dependencies** (recommended: use a virtual environment)
   ```bash
   pip install flask flask-cors google-generativeai pandas
   ```

2. **Set your Google Gemini API Key**
   ```bash
   export GOOGLE_API_KEY=your_api_key_here
   ```

3. **Start the system**
   ```bash
   ./start.sh
   # or
   python3 start_app.py
   ```

4. **How to use**
   - The frontend page will open automatically in your browser
   - Enter the number of records to generate and click "Generate"
   - View the results and download as CSV

## API

- `GET /generate_patients?count=10`
  - Parameter: `count` (number of records to generate, default 10)
  - Returns: JSON array of patient records

## Contact

For questions or suggestions, please open an [issue on GitHub](https://github.com/DorisTheChef/Simple_Version_DataCraft_AI_Agent/issues).

---

**This project is for learning and research purposes only.** 