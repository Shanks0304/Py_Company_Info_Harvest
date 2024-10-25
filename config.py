import os

# OpenAI API key
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Google Custom Search API credentials
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.environ.get("GOOGLE_CSE_ID")

# Input and output file paths
INPUT_FILE = "data/input_companies.xlsx"
OUTPUT_FILE = "data/output_results.json"