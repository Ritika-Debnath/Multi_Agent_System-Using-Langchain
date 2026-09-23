# Multi-Agent System Using LangChain

A Multi-Agent Research System built with **Python and LangChain**.

This project uses multiple AI agents and chains to research a given topic, collect detailed information, generate a report, and review the final report.

## 🚀 Features

- 🔎 **Search Agent** – Finds recent and reliable information about a given topic.
- 📖 **Reader Agent** – Selects a useful source and scrapes it for detailed content.
- ✍️ **Writer Chain** – Uses the collected research to generate a structured report.
- 🧐 **Critic Chain** – Reviews the generated report and provides feedback.
- 🔗 Uses **LangChain** to connect agents, tools, and LLMs.

## 🔄 How It Works


User enters a topic
        ↓
Search Agent
        ↓
Search Results
        ↓
Reader Agent
        ↓
Scraped Content
        ↓
Writer Chain
        ↓
Research Report
        ↓
Critic Chain
        ↓
Feedback
📁 Project Structure
Multi_Agent_System-Using-Langchain/
│
├── agents.py          # Creates the agents and LangChain chains
├── tools.py           # Contains tools used by the agents
├── pipeline.py        # Runs the complete research pipeline
├── app.py             # Application entry point
├── requirements.txt   # Required Python packages
├── .gitignore         # Files ignored by Git
└── README.md          # Project documentation
🛠️ Technologies Used
Python
LangChain
Large Language Model (LLM)
Search / Web tools
Web scraping
Generative AI
⚙️ Installation
1. Clone the repository
git clone https://github.com/Ritika-Debnath/Multi_Agent_System-Using-Langchain.git
2. Open the project folder
cd Multi_Agent_System-Using-Langchain
3. Create a virtual environment
python -m venv .venv
4. Activate the virtual environment

Windows:

.venv\Scripts\activate
5. Install the required packages
pip install -r requirements.txt
🔑 API Keys

Create a .env file in the project folder and add your API keys.

Example:

GEMINI_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key

Never upload your .env file or API keys to GitHub.

▶️ Run the Project

Run the pipeline:

python pipeline.py

Then enter a research topic when asked.

Example:

Enter a research topic: Artificial Intelligence

The system will then:

Search for information.
Read/scrape a relevant source.
Generate a research report.
Review the report and provide feedback.
🧠 Main Components
Search Agent

Finds recent and reliable information about the user's topic.

Reader Agent

Uses the search results to identify a relevant source and collect deeper information.

Writer Chain

Combines the search results and scraped content to create the research report.

Critic Chain

Reviews the generated report and provides feedback about its quality.

📌 Example

Input:

Artificial Intelligence

Output:

Search Results
      ↓
Scraped Content
      ↓
Generated Research Report
      ↓
Critic Feedback
👩‍💻 Author

Ritika Debnath

3rd Year BCA Student | AI & Machine Learning Enthusiast

GitHub:
https://github.com/Ritika-Debnath
