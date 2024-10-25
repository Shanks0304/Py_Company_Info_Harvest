from langchain.prompts import PromptTemplate

company_info_prompt = PromptTemplate(
    input_variables=["company_name"],
    template="""
Search for information about {company_name}. You will receive three items as a result.
Analyze all items and synthesize the most comprehensive and accurate information about the company.
Provide your analysis in the following format:
- Link: [The most informative URL among the items]
- Main Products: [List of main products or services offered by the company, collected from all relevant items]
- Head Office Location: [City and Country of the company's headquarters]

If the company name includes a specific location, use that information to infer the country even if it's not explicitly mentioned in the search results.
Explain your reasoning for the information you've compiled, citing which items contributed to each piece of information.

IMPORTANT: Every <Thought:> must either come with an <Action: and Action Input:> or <Final Answer:>
"""
)

final_prompt = PromptTemplate(
    input_variables=["company_name", "search_results"],
    template="""
Given the company name: {company_name}
And the following search results: {search_results}

Please extract and provide the following information:
"Website": "The most informative URL from the search results",
"Description of Products/Services": "main products or services offered by the company",
"Head office location (City, Country)": "City and Country of the company's headquarters"

If you can't find specific information, please state "Not found" for that item.
Provide the information in a JSON format.

Ensure your response is a valid JSON object.

IMPORTANT: Every <Thought:> must either come with an <Action: and Action Input:> or <Final Answer:>
"""
)