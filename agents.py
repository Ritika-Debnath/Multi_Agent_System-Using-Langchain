from dotenv import load_dotenv
load_dotenv()

# Import LangChain's agent creation function
from langchain.agents import create_agent

# Import Gemini model for LangChain
from langchain_google_genai import ChatGoogleGenerativeAI

# Used to create prompts with variables
from langchain_core.prompts import ChatPromptTemplate

# Converts the model's output into a simple string
from langchain_core.output_parsers import StrOutputParser

# Import our custom web search and scraping tools
from tools import web_search, scrape_url


# Create the Gemini LLM
# temperature=0 gives more consistent responses
llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0
)


# Create the 1st Agent: Search Agent
def build_search_agent():
    # Create an agent that can use the web search tool
    return create_agent(
        model=llm,
        tools=[web_search]
    )


# Create the 2nd Agent: Reader Agent
def build_reader_agent():
    # Create an agent that can use the webpage scraping tool
    return create_agent(
        model=llm,
        tools=[scrape_url]
    )


# ---------------- Writer Chain ----------------

# Create the prompt used by the writer
writer_prompt = ChatPromptTemplate.from_messages([

    # Tell the LLM its role
    ("system",
     "You are an expert research writer. "
     "Write clear, structured and insightful reports."),

    # Give the LLM the research and writing instructions
    ("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional."""),
])

# Connect prompt → Gemini → string output
# This is LCEL (LangChain Expression Language)
writer_chain = writer_prompt | llm | StrOutputParser()


# ---------------- Critic Chain ----------------

# Create the prompt used by the critic
critic_prompt = ChatPromptTemplate.from_messages([

    # Tell the LLM its role as a critic
    ("system",
     "You are a sharp and constructive research critic. "
     "Be honest and specific."),

    # Give the report and instructions for reviewing it
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

# Connect prompt → Gemini → string output
critic_chain = critic_prompt | llm | StrOutputParser()