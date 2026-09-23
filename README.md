# 🤖 Multi-Agent System Using LangChain

> A Multi-Agent Research System built with **Python, LangChain, and Generative AI**.

This project uses multiple AI agents and chains to **research a given topic, collect relevant information, generate a structured research report, and review the final report**.

---

## 🚀 Features

- 🔎 **Search Agent** — Searches for recent and relevant information about a given research topic.
- 📖 **Reader Agent** — Selects a useful source from the search results and extracts detailed information.
- ✍️ **Writer Chain** — Uses the collected research information to generate a structured research report.
- 🧐 **Critic Chain** — Reviews the generated report and provides feedback about its quality.
- 🔗 **LangChain Integration** — Connects agents, tools, prompts, and LLMs into a complete research workflow.
- 🌐 **Web Research** — Uses web search and scraping tools to collect information from online sources.

---

## 🔄 How It Works

The project follows a sequential **Multi-Agent Research Pipeline**:

```
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
```

### 📌 Workflow

1. The user enters a research topic.
2. The **Search Agent** searches the web for relevant information.
3. The **Reader Agent** selects a useful source and extracts detailed content.
4. The **Writer Chain** combines the collected information and generates a research report.
5. The **Critic Chain** reviews the generated report.
6. The system provides feedback on the final report.

---

## 📁 Project Structure

```
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
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 Python | Main programming language |
| 🔗 LangChain | Building and connecting AI agents and chains |
| 🤖 Google Gemini | Large Language Model |
| 🔎 Tavily Search | Web search and information retrieval |
| 🌐 Web Scraping | Extracting information from web pages |
| 🧠 Generative AI | Generating and reviewing research content |

---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Ritika-Debnath/Multi_Agent_System-Using-Langchain.git
```

### 2. Open the Project Folder
```bash
cd Multi_Agent_System-Using-Langchain
```

### 3. Create a Virtual Environment
```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

For Windows:
```bash
.venv\Scripts\activate
```

### 5. Install the Required Packages
```bash
pip install -r requirements.txt
```

---

## 🔑 API Keys

Create a `.env` file in the root directory of the project.

Add your API keys:

```
GEMINI_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
```

⚠️ **Important:** Never upload your `.env` file or API keys to GitHub.
Make sure `.env` is included in your `.gitignore` file.

---

## ▶️ Run the Project

After completing the installation and adding your API keys, run:

```bash
python pipeline.py
```

The program will ask you to enter a research topic.

### Example
```
Enter a research topic: Artificial Intelligence
```

The system will then automatically perform the following steps:

```
🔎 Search for information
        ↓
📖 Read and extract relevant content
        ↓
✍️ Generate a research report
        ↓
🧐 Review the generated report
        ↓
💬 Provide feedback
```

---

## 🧩 Main Components

### 🔎 Search Agent
The Search Agent searches for recent and relevant information about the user's research topic. It uses web search tools to find useful sources that can be used for further research.

### 📖 Reader Agent
The Reader Agent uses the search results to identify a relevant source. It then extracts and collects detailed information from that source.

### ✍️ Writer Chain
The Writer Chain combines the information collected by the research agents. It uses this information to generate a structured and readable research report.

### 🧐 Critic Chain
The Critic Chain reviews the generated research report. It provides feedback about the report's:
- Accuracy
- Clarity
- Structure
- Completeness
- Overall quality

---

## 📌 Example

**Input**
```
Artificial Intelligence
```

**Research Process**
```
🔎 Search Agent
      ↓
Finds relevant sources
      ↓
📖 Reader Agent
      ↓
Extracts useful information
      ↓
✍️ Writer Chain
      ↓
Creates research report
      ↓
🧐 Critic Chain
      ↓
Reviews the report
```

**Output**

The system generates a structured research report based on the collected information and provides feedback from the Critic Chain.

---

## 🎯 Project Objective

The main objective of this project is to demonstrate how multiple AI agents can work together to perform an automated research workflow.

Instead of using a single AI agent for the entire task, different agents and chains are responsible for different stages of the workflow:

- 🔎 Searching for information
- 📖 Reading and extracting useful content
- ✍️ Writing the research report
- 🧐 Reviewing the generated report

This approach demonstrates how LangChain can be used to build modular Multi-Agent AI systems.

---

## 👩‍💻 Author

**Ritika Debnath**
BCA Student | AI & Machine Learning Enthusiast
