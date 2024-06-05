from pydantic import Field
from instructor import OpenAISchema
from firecrawl import FirecrawlApp
import json
import os

class WebScrape(OpenAISchema):
    """
    Use this tool to scrape a webpage and extract the content.

    ## When to use this tool
    - When you need to extract content from a webpage that may contain javascript or other dynamic content.
    - It is fairly robust and can handle most content-based webpages.

    ## Limitations
    - Can not interact with the page, it is only a scraper.
    """
    url: str = Field(description="The URL of the web page to scrape")

    def run(self):
        api_key = os.environ['FIRECRAWL_API_KEY']
        try:
            app = FirecrawlApp(api_key=api_key)
            params = {
            'pageOptions': {
                'onlyMainContent': True
                }
            }
            text = app.scrape_url(url=self.url, params=params)
            return json.dumps(text)
        except Exception as e:
            return str(e)
