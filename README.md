# 🤖 Multi-Agent System Using LangChain

> A Multi-Agent Research System built with **Python, LangChain, and Generative AI**.

This project uses multiple AI agents and chains to **research a given topic, collect relevant information, generate a structured research report, and review the final report**.

---

## 🚀 Features

- 🔎 **Search Agent**  
  Searches for recent and relevant information about a given research topic.

- 📖 **Reader Agent**  
  Selects a useful source from the search results and extracts detailed information.

- ✍️ **Writer Chain**  
  Uses the collected research information to generate a structured research report.

- 🧐 **Critic Chain**  
  Reviews the generated report and provides feedback about its quality.

- 🔗 **LangChain Integration**  
  Connects agents, tools, prompts, and LLMs into a complete research workflow.

- 🌐 **Web Research**  
  Uses web search and scraping tools to collect information from online sources.

---

## 🔄 How It Works

The project follows a sequential **Multi-Agent Research Pipeline**:

```text
User enters a research topic
            ↓
       Search Agent
            ↓
       Search Results
            ↓
       Reader Agent
            ↓
   Extracted Web Content
            ↓
       Writer Chain
            ↓
      Research Report
            ↓
       Critic Chain
            ↓
        Feedback

📌 Workflow
The user enters a research topic.
The Search Agent searches the web for relevant information.
The Reader Agent selects a useful source and extracts detailed content.
The Writer Chain combines the collected information and generates a research report.
The Critic Chain reviews the generated report.
The system provides feedback on the final report.

📁 Project Structure
Multi_Agent_System-Using-Langchain/
│
├── agents.py
│   └── Creates the AI agents and LangChain chains
│
├── tools.py
│   └── Contains the tools used by the agents
│
├── pipeline.py
│   └── Runs the complete research pipeline
│
├── app.py
│   └── Application entry point
│
├── requirements.txt
│   └── Contains the required Python packages
│
├── .gitignore
│   └── Specifies files ignored by Git
│
└── README.md
    └── Project documentation

🛠️ Technologies Used
Python
LangChain
Large Language Models (LLMs)
Generative AI
Web Search Tools
Web Scraping
Tavily Search API
Google Gemini API


⚙️ Installation
1. Clone the Repository
git clone https://github.com/Ritika-Debnath/Multi_Agent_System-Using-Langchain.git
2. Open the Project Folder
cd Multi_Agent_System-Using-Langchain
3. Create a Virtual Environment
python -m venv .venv
4. Activate the Virtual Environment

For Windows:

.venv\Scripts\activate
5. Install Required Packages
pip install -r requirements.txt
🔑 API Keys

Create a .env file in the project folder and add your API keys:

GEMINI_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key

⚠️ Important: Never upload your .env file or API keys to GitHub.

Make sure .env is included in your .gitignore file.

▶️ Run the Project

Run the main pipeline using:

python pipeline.py

The program will ask you to enter a research topic.

Example
Enter a research topic: Artificial Intelligence

The system will then:

Search for information
        ↓
Read and extract relevant content
        ↓
Generate a research report
        ↓
Review the report
        ↓
Provide feedback
🧩 Main Components
🔎 Search Agent

The Search Agent finds recent and relevant information about the user's research topic using web search tools.

📖 Reader Agent

The Reader Agent uses the search results to identify a relevant source and collect more detailed information from it.

✍️ Writer Chain

The Writer Chain combines the collected research and generates a structured research report.

🧐 Critic Chain

The Critic Chain reviews the generated report and provides feedback about its quality, clarity, and completeness.

📌 Example
Input
Artificial Intelligence
Process
Search Agent
    ↓
Finds relevant sources
    ↓
Reader Agent
    ↓
Extracts useful information
    ↓
Writer Chain
    ↓
Creates research report
    ↓
Critic Chain
    ↓
Reviews the report
Output

The system generates a structured research report based on the collected information and provides feedback through the Critic Chain.

🎯 Project Objective

The main objective of this project is to demonstrate how multiple AI agents can work together to perform an automated research workflow.

Instead of relying on a single AI agent, different agents and chains are given specific responsibilities such as:

Searching for information
Reading and extracting content
Writing the report
Reviewing the final result

This creates a modular and organized Multi-Agent AI workflow using LangChain.

👩‍💻 Author

Ritika Debnath

BCA Student | AI & Machine Learning Enthusiast
