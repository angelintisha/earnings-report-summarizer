# Earnings Report Summarizer — LangChain & LLM

`Python` `LangChain` `Ollama (llama3.2)` `Prompt Engineering`

Structured summarization of financial earnings reports using a locally hosted LLM. Built with LangChain document loaders, a custom prompt template, and Ollama (llama3.2) for inference — no external API or internet connection required at runtime.

Applied to Nvidia's Q2 FY2025 earnings report to generate a structured summary across six sections: Financial Highlights, Segment Highlights, Cash Flow & Capex, Strategic Moves, and Key Risks.

---

## How It Works

1. Loads a `.txt` earnings report using LangChain's `TextLoader`
2. Joins document pages into a single text block
3. Passes the text through a structured `PromptTemplate` that enforces a specific output format
4. Runs inference locally using `OllamaLLM` (llama3.2)
5. Parses and prints the structured summary

---

## Project Structure

```
earnings-report-summarizer/
├── document_summarizer.py     # Main script
├── data/
│   └── mag7_earning_reports/
│       └── NVDA_2025Q2.txt    # Nvidia Q2 FY2025 earnings report (not included)
└── README.md
```

---

## Requirements

```bash
pip install langchain langchain-community langchain-ollama
```

Ollama must be installed and running locally with llama3.2 pulled:

```bash
ollama pull llama3.2
ollama serve
```

---

## Usage

Place your earnings report `.txt` file in `data/mag7_earning_reports/` and run:

```bash
python document_summarizer.py
```

---

## Sample Output Format

```
NVIDIA Q4 FY2023 Earnings Call Highlights

Financial Highlights
• Revenue: $X.XB (up/down X% YoY)
• GAAP EPS: $X.XX (up/down X% YoY)
• Non-GAAP EPS: $X.XX (up/down X% YoY)

Segment Highlights
• Datacenter segment revenue grew/declined X% YoY to $X.XB, driven by ...
...
```

---

## Key Concepts

- **LangChain document loaders** — ingesting unstructured text documents
- **Prompt engineering** — enforcing structured output format from an LLM
- **Local LLM inference** — running llama3.2 locally via Ollama, no API key needed
- **LangChain Expression Language (LCEL)** — composing chains with `|` operator
