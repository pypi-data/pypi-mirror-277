
from typing import List
from langchain_community.agent_toolkits.base import BaseToolkit
from langchain_core.tools import BaseTool

from langchain_community.tools.google_search import GoogleSearchResults
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_community.utilities.google_search import GoogleSearchAPIWrapper
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from .duck_duck_go_search import DuckDuckGoSearch
from .google_search_rag import GoogleSearchRag
from .crawler import SingleURLCrawler, MultiURLCrawler, GetHTMLContent

class BrowserToolkit(BaseToolkit):
    tools: List[BaseTool] = []
    @classmethod
    def get_toolkit(cls, selected_tools: list[str] | None = None, **kwargs):
        if selected_tools is None:
            selected_tools = []
        tools = []
            
        if len(selected_tools) == 0 or 'single_url_crawler' in selected_tools:
            tools.append(SingleURLCrawler())
        if len(selected_tools) == 0 or 'multi_url_crawler' in selected_tools:
            tools.append(MultiURLCrawler())
        if len(selected_tools) == 0 or 'get_html_content' in selected_tools:
            tools.append(GetHTMLContent())
        if len(selected_tools) == 0 or "google" in selected_tools:
            google_api_wrapper = GoogleSearchAPIWrapper(
                google_api_key=kwargs.get("google_api_key"),
                google_cse_id=kwargs.get("google_cse_id"),
            )
            tools.append(GoogleSearchResults(
                api_wrapper=google_api_wrapper)
            )
            tools.append(GoogleSearchRag(googleApiWrapper=google_api_wrapper))
        if len(selected_tools) == 0 or 'wiki' in selected_tools:
            tools.append(WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper()))
        if len(selected_tools) == 0 or 'ddg' in selected_tools:
            tools.append(DuckDuckGoSearch())
        return cls(tools=tools)
            
    def get_tools(self):
        return self.tools