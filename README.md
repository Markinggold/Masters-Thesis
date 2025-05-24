# Masters-Thesis

# Resume Enhancement Suite

A set of Python scripts for enhancing resume texts using various language model APIs. Developed by Kia Gericke as part of masters thesis research, this collection demonstrates how to integrate different LLM-based services—DeepSeek, OpenAI GPT-4o-mini, and LlamaAPI—into a CSV-driven pipeline for resume enhancement. The dataset folder contains the resume enhancements that were used for this thesis.

## Repository Contents

* **deepseek\_enhance\_csv.py**
  Enhance resumes via the DeepSeek API using the OpenAI SDK.
  *Author:* Kia Gericke
  *Date:* 13/02/2025

* **gpt\_enhance\_csv.py**
  Enhance resumes using OpenAI’s GPT-4o-mini via HTTP requests.
  *Author:* Kia Gericke
  *Date:* 13/02/2025

* **llama\_enhance\_csv.py**
  Enhance resumes with the LlamaAPI (Llama 3.1 8B model), including retry logic.
  *Author:* Kia Gericke
  *Date:* 2025-02-17

* **generate\_standard\_resumes.py**
  Create standard resume dataset.
  *Author:* Kia Gericke
  *Date:* 2025-01-27

* **generate\_anti\_resumes.py**
  Create anti-stereotypical resume dataset.
  *Author:* Kia Gericke
  *Date:* 2025-01-27
  
* **Dataset Folder**
  This folder contains the ehanced resumes for each model and base resumes that were used for analysis in this thesis.  

## Features

* **CSV-driven workflow:**  Read input resumes from a CSV file, process each entry, and write enhanced output back to a new CSV.
* **API modularity:**  Easily switch between DeepSeek, GPT-4o-mini, or LlamaAPI by running the corresponding script.
* **CSV-safe formatting:**  Post-process model outputs to remove or replace problematic characters (newlines, commas) for seamless CSV compatibility.

## Prerequisites

* Python 3.11 or later
* Pip dependencies (see Installation)
* Valid API credentials for DeepSeek, OpenAI, and/or LlamaAPI

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/KiaGericke/resume-enhancement-suite.git
   cd resume-enhancement-suite
   ```
2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate   # Windows
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Set API keys**

   * DeepSeek: Update `DEEPSEEK_API_KEY` in `resume_enhancer_deepseek.py`.
   * OpenAI: Set `openai.api_key` in `resume_enhancer_gpt4o.py` or via the `OPENAI_API_KEY` environment variable.
   * LlamaAPI: Provide `api_token` in `resume_enhancer_llama.py`.

2. **Define file paths**

   * In each script, replace `INPUT_CSV_FILE` and `OUTPUT_CSV_FILE` placeholders with your actual file paths.

## Usage

Run the script of your choice maunally within the python editor of your choice.

Each script reads from the configured input CSV, processes every resume entry, and writes an enhanced CSV output to the specified path.

## Example CSV Format

```csv
ID,Name,Email,Phone,Resume
1,Jane Doe,jane.doe@example.com,555-1234,"Experienced mechanical engineer..."
```

## Contributing

Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License.

---

*Part of Kia Gericke’s thesis research on gendered differences between AI-enhanced resumes.*
