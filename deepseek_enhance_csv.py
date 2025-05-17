"""
Resume Enhancement Script using DeepSeek

This script reads resumes from an input CSV file, enhances them using DeepSeek's API,
and writes the improved resumes to an output CSV file while ensuring CSV-safe formatting.

Author: Kia Gericke
Date: 13/02/2025
"""

import csv
import os

# Import the OpenAI SDK, which is used for DeepSeek’s API
from openai import OpenAI

# ----------------------------------
# Configuration
# ----------------------------------

# Replace with your actual DeepSeek API key
DEEPSEEK_API_KEY = "INSERT API KEY"

# Input and output CSV paths
INPUT_CSV_FILE = (
    "INSERT PATH"
)
OUTPUT_CSV_FILE = "INSERT PATH"

# Ensure output directory exists
os.makedirs(os.path.dirname(OUTPUT_CSV_FILE), exist_ok=True)


def enhance_cv_deepseek(cv_text):
    """
    Enhances a given resume text using DeepSeek while ensuring CSV-safe output.

    Parameters:
        cv_text (str): The raw resume text to be improved.

    Returns:
        str: The enhanced resume text with better structure, improved language,
             and CSV-safe formatting.
    """
    # Create a DeepSeek client using the OpenAI SDK
    client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com/v1")

    # Build the message list for the chat completion request
    messages = [
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
            "content": (
                "Please enhance the following resume to be more compelling and descriptive, "
                "while strictly following these rules:\n"
                "1. Preserve the resume’s CSV structure, including fields like Name, Email, Phone, "
                "   Role Title, City/Location, Personal Summary, Education, Experience, Skills, "
                "   and Additional Information. Do not alter or remove these fields.\n"
                "2. Keep the applicant’s name, email, and phone number exactly as they appear.\n"
                "3. Use a dynamic and engaging writing style, highlighting the applicant's strengths "
                "   and achievements in a natural and persuasive way.\n"
                "4. Use vivid language that captures the applicant’s unique "
                "   qualifications, professional focus, and personality, without deviating from "
                "   the existing bullet points or major headings.\n"
                "5. Avoid adding any comments or explanations; return only the improved resume content, "
                "   with minimal commas or newlines to ensure CSV compatibility.\n"
                "6. If a section is short, feel free to expand it with relevant, imaginative details "
                "   that remain consistent with the applicant’s field and the original context.\n\n"
                f"Here is the resume:\n{cv_text}"
            ),
        },
    ]

    # Send the request to DeepSeek
    response = client.chat.completions.create(
        model="deepseek-chat",  # Ensure this is the correct model name for DeepSeek
        messages=messages,
        stream=False,
    )

    # Extract the enhanced text from the response
    enhanced_text = response.choices[0].message.content.strip()

    # Post-process the output to remove problematic CSV characters
    enhanced_text = enhanced_text.replace("\n", " ").replace(",", " ").strip()

    return enhanced_text


def main():
    """
    Reads resumes from the input CSV, enhances them using DeepSeek,
    and writes the improved resumes to an output CSV file.
    """
    # Read all rows from the input CSV
    with open(INPUT_CSV_FILE, "r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)  # Read all rows

    # Enhance resumes for all rows
    for row in rows:
        print(f"Enhancing resume for ID {row['ID']}...")
        enhanced_resume = enhance_cv_deepseek(row["Resume"])
        row["Resume"] = enhanced_resume

    # Write all enhanced rows to the output CSV
    with open(OUTPUT_CSV_FILE, "w", encoding="utf-8", newline="") as csv_file:
        fieldnames = ["ID", "Name", "Email", "Phone", "Resume"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Enhanced resumes saved to: {OUTPUT_CSV_FILE}")


if __name__ == "__main__":
    main()
