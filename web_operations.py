import os
import json
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

tavily_api_key = os.getenv("TAVILY_API_KEY")
tavily = TavilyClient(api_key=tavily_api_key)

def serp_search(query, engine="google"):
    """
    Performs a general web search using Tavily.
    The 'engine' param is kept for compatibility but Tavily handles the search logic.
    """
    print(f" Web Search ({engine}): {query} ---")
    try:
        response = tavily.search(query=query, search_depth="basic", max_results=5)
        
        return json.dumps(response.get('results', []), indent=2)
    except Exception as e:
        print(f"Error in serp_search: {e}")
        return "[]"


def reddit_search_api(keyword):
    """
    Searches specifically for Reddit threads using Tavily's domain filtering.
    """
    print(f" Reddit Search: {keyword} ---")
    try:
        response = tavily.search(
            query=keyword, 
            include_domains=['reddit.com'], 
            search_depth="advanced", 
            max_results=10
        )
        results = response.get('results', [])
        return results
    except Exception as e:
        print(f"Error in reddit_search_api: {e}")
        return []


def reddit_post_retrieval(urls):
    """
    Extracts content from specific Reddit URLs using Tavily's Extract API.
    """
    print(f"--- Extracting content from {len(urls)} Reddit URLs ---")
    if not urls:
        return []

    try:
        response = tavily.extract(urls=urls)
        formatted_posts = []
        for result in response.get('results', []):
            if result.get('raw_content'):
                formatted_posts.append({
                    "url": result.get("url"),
                    "content": result.get("raw_content"),
                    "parsed_text": result.get("raw_content")[:5000] 
                })
        
        return formatted_posts

    except Exception as e:
        print(f"Error in reddit_post_retrieval: {e}")
        return []