"""
This script enhances resume texts by calling the LlamaAPI. 
It reads in resume data from a CSV file, sends each resume's text to the Llama API for enhancement, 
and writes the enhanced resumes into a new CSV file.

Usage:
1) Update the INPUT_CSV_FILE and OUTPUT_CSV_FILE paths in the "Configuration" section as needed.
2) Ensure that you have the `llamaapi` package installed and a valid API token.
3) Run the script: `python resume_enhancer.py`

Dependencies:
- Python 3.11.8
- llamaapi
- csv
- os
- json
- time

Author: Kia Gericke
Date: 2025-02-17
"""

import csv
import os
from llamaapi import LlamaAPI
import json
import time

# ----------------------------------
# Configuration
# ----------------------------------

# Input and output CSV paths
INPUT_CSV_FILE = "INSERT PATH" # Update with your input file path
OUTPUT_CSV_FILE = "INSERT PATH"  # Update with your output file path

# Ensure output directory exists
os.makedirs(os.path.dirname(OUTPUT_CSV_FILE), exist_ok=True)

# Initialize LlamaAPI
llama = LlamaAPI(
    api_token="INSERT API KEY"
)


def enhance_cv_llama(cv_text, retries=3):
    """
    Uses LlamaAPI (Llama 3.1 8B) to enhance the resume text while ensuring CSV-safe output.
    Retries the API call if it fails, which it does on occasion.

    Parameters
    ----------
    cv_text : str
        The original resume text to be enhanced.
    retries : int, optional
        Number of times to retry the API call in case of failure, by default 3.

    Returns
    -------
    str
        The enhanced resume text, made CSV-safe by replacing newlines and commas.
    """
    payload = {
        "model": "llama3.1-8b",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a highly creative professional resume enhancer with a talent "
                    "for dynamic, engaging writing. Your goal is to improve the following "
                    "resume text with flair and personality, but you must keep it CSV-safe "
                    "and maintain its original sections (Name, Email, Phone, etc.)."
                ),
            },
            {
                "role": "user",
                "content": f"""Please enhance the following resume to be more compelling and descriptive, 
                while strictly following these rules:
                1. Preserve the resume’s CSV structure, including fields like Name, Email, Phone, Role Title, City/Location, Personal Summary, Education, Experience, Skills, and Additional Information. Do not alter or remove these fields.
                2. Keep the applicant’s name, email, and phone number exactly as they appear.
                3. Use a dynamic and engaging writing style, highlighting the applicant's strengths and achievements in a natural and persuasive way.
                4. Use vivid language that captures the applicant’s unique qualifications, professional focus, and personality, without deviating from the existing bullet points or major headings.
                5. Avoid adding any comments or explanations; return only the improved resume content, with minimal commas or newlines to ensure CSV compatibility.
                6. If a section is short, feel free to expand it with relevant, imaginative details that remain consistent with the applicant’s field and the original context.

                Here is the resume:
                {cv_text}
                """,
            },
        ],
        "max_tokens": 2500,
        "temperature": 1,
    }
    for attempt in range(retries):
        try:
            response = llama.run(payload)

            # DEBUG: Print raw response status and content
            print(
                f"DEBUG: Attempt {attempt + 1} - Raw API Response Status: {response.status_code}"
            )
            print(
                f"DEBUG: Attempt {attempt + 1} - Raw API Response Content: {response.text}"
            )

            # Convert response to JSON safely
            try:
                response_json = response.json()
            except Exception as e:
                print(
                    f"WARNING: Failed to parse JSON on attempt {attempt + 1}. Retrying..."
                )
                time.sleep(2)  # Wait before retrying
                continue  # Retry the request

            # Extract enhanced text safely
            choices = response_json.get("choices", [])
            if (
                choices
                and "message" in choices[0]
                and "content" in choices[0]["message"]
            ):
                enhanced_text = choices[0]["message"]["content"]
                break  # Exit loop if successful
            else:
                print(
                    f"WARNING: No valid response from Llama API on attempt {attempt + 1}. Retrying..."
                )
                time.sleep(2)
                continue

        except Exception as e:
            print(
                f"ERROR: Failed API call on attempt {attempt + 1}. Retrying... Details: {str(e)}"
            )
            time.sleep(2)

    else:
        print(f"ERROR: All {retries} attempts failed. Skipping this resume.")
        return "ERROR: API call failed"

    # Postprocess to make it CSV-safe
    enhanced_text = enhanced_text.replace("\n", " ").replace(",", " ").strip()

    return enhanced_text


def main():
    """
    Main function that reads resumes from an input CSV file, enhances them using the LlamaAPI,
    and writes the enhanced resumes to an output CSV file.

    Steps:
    1. Reads all rows from the input CSV using csv.DictReader.
    2. For each row, calls enhance_cv_llama() to get the enhanced resume text.
    3. Replaces the original resume text in the row with the enhanced text.
    4. Writes all updated rows to the output CSV using csv.DictWriter.

    Returns
    -------
    None
    """
    # Read all rows from the input CSV
    with open(INPUT_CSV_FILE, "r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        fieldnames = reader.fieldnames  # Get column names from the input CSV
        rows = list(reader)  # Read all rows

    # Enhance resumes for all rows
    for row in rows:
        print(f"Enhancing resume for ID {row['ID']}...")
        enhanced_resume = enhance_cv_llama(row["Resume"])
        row["Resume"] = enhanced_resume  # Keep all other fields unchanged

    # Write all enhanced rows to the output CSV
    with open(OUTPUT_CSV_FILE, "w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(
            csv_file, fieldnames=fieldnames
        )  # Maintain original headers
        writer.writeheader()
        writer.writerows(rows)  # Keep all other data unchanged

    print(f"Enhanced resumes saved to: {OUTPUT_CSV_FILE}")


if __name__ == "__main__":
    main()
