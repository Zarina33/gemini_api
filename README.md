Certainly. **Rewritten:**

# Language Translation Script

This project provides a Python script that translates the text content of a JSON file from English to Kyrgyz using the **Gemini 1.5 Flash API**.
It is designed for conversational data, translating only the message values while preserving the original JSON structure and metadata.
A Docker setup is included for portability and reproducibility.

---

### Prerequisites

* **Python 3.6+** (if running without Docker)
* **Gemini API Key** (obtain from [Google AI for Developers](https://ai.google.dev/))
* **Docker** (if using the containerized approach)

---

### Project Structure

Your project folder should include:

* `translate_values.py` — Python script for translation
* `input.json` — JSON file with source data
* `Dockerfile` — Docker build instructions

---

### Usage

#### Option 1: Run Directly (without Docker)

1. Install dependencies:

   ```bash
   pip install google-generativeai
   ```

2. Set your Gemini API key:

   * macOS / Linux:

     ```bash
     export YOUR_GEMINI_API_KEY="[YOUR_API_KEY]"
     ```
   * Windows (Command Prompt):

     ```bash
     set YOUR_GEMINI_API_KEY="[YOUR_API_KEY]"
     ```

3. Run the script:

   ```bash
   python translate_values.py
   ```

The script will output both the original and translated JSON to your terminal.

---

#### Option 2: Run with Docker

1. Build the Docker image (run from the project directory):

   ```bash
   docker build -t translator-app .
   ```

2. Run the container:

   ```bash
   docker run --rm -e YOUR_GEMINI_API_KEY="[YOUR_API_KEY]" translator-app
   ```

The `--rm` flag removes the container after execution. The translated JSON will be shown in your terminal.

---

Recommendation: Save this as `README.md` in your project root.
Next step: Run either Option 1 or Option 2 depending on your environment.
