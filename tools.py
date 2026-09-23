from dotenv import load_dotenv      
load_dotenv()
from langchain.tools import tool
import requests                     # Used to send HTTP requests and get webpage content
from bs4 import BeautifulSoup       # Used to read and extract useful text from HTML webpages
from tavily import TavilyClient     # Used to connect to the Tavily search API
import os                           # Used to access environment variables such as API keys
from rich import print              # Used to display output in a nicer format in the terminal

# Create a Tavily client using the Tavily API key
# os.getenv() gets the value of TAVILY_API_KEY from the environment
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


# @tool converts this normal Python function into a LangChain tool
# ==========  TOOL : 1  =============
@tool
def web_search(query: str) -> str:
    """Search the web for recent and reliable information on a topic.   
    Returns Titles, URLs and snippets.
    """     # -----> "docstring"

    # Send the user's search query to Tavily
    # max_results=5 means Tavily will return at most 5 search results
    result = tavily.search(
        query= query,
        max_results= 5
    )

    # Create an empty list to store the formatted search results
    out = []

    # Loop through every search result returned by Tavily
    for r in result['results']:

        # Extract the title, URL and first 300 characters of content from the current search result
        out.append(
            f"Title: {r['title']}\n"
            f"URL: {r['url']}\n"
            f"Snippet: {r['content'][:300]}\n"
        )

    # Join all search results together
    # "\n-----\n" creates a separator between each result
    # Finally, return the complete formatted search result
    return "\n-----\n".join(out)


# ==========  TOOL : 2  =============
@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""

    # try is used because webpage requests can sometimes fail
    try:
        # Send a GET request to the provided URL
        # timeout=8 means wait at most 8 seconds for a response
        # User-Agent makes the request look like it is coming from a normal browser
        resp = requests.get(
            url,
            timeout=8,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        # Convert the HTML response into a BeautifulSoup object
        # "html.parser" tells BeautifulSoup to use Python's built-in HTML parser
        soup = BeautifulSoup(
            resp.text,
            "html.parser"
        )

        # Find unwanted HTML elements such as:
        # script, style, navigation and footer
        # and remove them from the webpage
        for tag in soup(["script", "style", "nav", "footer"]):
            # Remove the current unwanted HTML element
            tag.decompose()

        # Extract only the visible text from the webpage
        # separator=" " puts spaces between different pieces of text
        # strip=True :- removes unnecessary spaces
        # [:3000] keeps only the first 3000 characters
        return soup.get_text(
            separator=" ",
            strip=True
        )[:3000]

    # If something goes wrong while scraping the webpage,
    # this block will handle the error instead of crashing the program
    except Exception as e:
        # Return a readable error message
        # str(e) converts the error into normal text
        return f"Could not scrape URL: {str(e)}"