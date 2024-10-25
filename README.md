# 🚀 CompanyInfoHarvester

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/downloads/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--powered-brightgreen)](https://openai.com/)
[![Google Custom Search](https://img.shields.io/badge/Google-Custom%20Search%20API-4285F4)](https://developers.google.com/custom-search)

CompanyInfoHarvester is an intelligent automation tool that leverages the power of OpenAI's GPT model and Google Custom Search API to extract and enrich company information from Excel spreadsheets.

## 🌟 Features

- 📊 Parse Excel files to extract company names
- 🔍 Utilize Google Custom Search API to fetch comprehensive company information
- 🧠 Employ a ReAct agent with OpenAI's GPT model for intelligent data analysis
- 🏢 Extract key company details: Website, Products/Services, and Head Office Location
- 📝 Automatically update Excel files with enriched company data
- 🤖 Streamline the data enrichment process with minimal human intervention

## 🛠️ How It Works

1. **Excel Parsing**: The system reads an input Excel file containing company names.
2. **Google Search**: For each company, it performs a Google Custom Search to fetch relevant information.
3. **Intelligent Analysis**: A ReAct agent, powered by OpenAI's GPT model, analyzes the search results.
4. **Data Extraction**: The agent extracts key information such as the company's website, main products/services, and head office location.
5. **JSON Generation**: The extracted information is formatted into a JSON object.
6. **Excel Update**: The original Excel file is updated with the newly gathered information.

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- OpenAI API key
- Google Custom Search API key and Search Engine ID

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/Shanks0304/Py_AI-agent-with-Google-Search.git
   cd Py_AI-agent-with-Google-Search
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the project root and add your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   GOOGLE_API_KEY=your_google_api_key
   GOOGLE_CSE_ID=your_google_custom_search_engine_id
   ```

### Usage

1. Place your input Excel file in the `input` directory.
2. Run the main script:
   ```
   python main.py
   ```
3. Find the updated Excel file in the `output` directory.

## 🧰 Project Structure

- `agent/tools.py`: Contains the Google Custom Search tool implementation.
- `agent/prompts.py`: Defines the prompts used by the ReAct agent.
- `main.py`: The main script that orchestrates the entire process.

## 📚 Code Highlights

### Google Custom Search Tool

python:agent/tools.py
startLine: 13
endLine: 38

This code snippet shows the implementation of the Google Custom Search tool, which is crucial for fetching initial company information.

### ReAct Agent Prompts

python:agent/prompts.py
startLine: 3
endLine: 38


These prompts guide the ReAct agent in analyzing search results and extracting relevant company information.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/yourusername/CompanyInfoHarvester/issues).

## 📜 License

This project is [MIT](https://opensource.org/licenses/MIT) licensed.

## 🙏 Acknowledgements

- OpenAI for their powerful GPT model
- Google for the Custom Search API
- The open-source community for inspiration and tools

---

Made with ❤️ by [Shanks0304](https://github.com/Shanks0304)