from pydantic import Field
from instructor import OpenAISchema
from serpapi import GoogleSearch
import json
import os

class WebSearch(OpenAISchema):
    """
    Use this tool to perform a web search using SerpAPI and return the results. If you receive an error response, perhaps try again using different parameters.
    """
    query: str = Field(description="The search query to be used on SerpAPI")

    def run(self):
        api_key = os.environ['SERPAPI_API_KEY']
        try:
            search = GoogleSearch({
                "q": self.query,
                "api_key": api_key
            })
            result = search.get_dict()
            return json.dumps(result)
        except Exception as e:
            return str(e)
