from langchain_core.tools import tool
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os
import re

load_dotenv()

# Set these as environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")

@tool("company_info_search")
def company_info_search(company_name: str) -> str:
    """
    Useful for searching information about companies. Input should be a company name.
    """
    try:
        service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
        result = service.cse().list(
            q=company_name,
            cx=GOOGLE_CSE_ID,
            num=3
        ).execute()

        if 'items' in result:
            search_results = []
            for item in result['items']:
                title = item.get('title', 'No title')
                snippet = item.get('snippet', 'No snippet')
                link = item.get('link', 'No link')
                search_results.append(f"Title: {title}\nSnippet: {snippet}\nLink: {link}\n")
            results = "\n".join(search_results)
            return results
        else:
            return "No results found for the given company."
    except Exception as e:
        return f"An error occurred: {str(e)}"

@tool("final_answer")
def final_answer(answer: str) -> str:
    """
    Provide the final answer to the user's question.
    """
    return answer

