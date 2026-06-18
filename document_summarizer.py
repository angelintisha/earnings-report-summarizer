# Nvidia Earnings Report Summarizer
# Tools: LangChain · Ollama (llama3.2) · PromptTemplate

from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

# ── 1. Load the Earnings Report ───────────────────────────────
# Place NVDA_2025Q2.txt in: data/mag7_earning_reports/
loader = TextLoader(
    'data/mag7_earning_reports/NVDA_2025Q2.txt',
    encoding='utf-8'
)
docs = loader.load()

# ── 2. Define LLM ─────────────────────────────────────────────
llama_model = OllamaLLM(model="llama3.2", temperature=0)

# ── 3. Modify the Summarization Prompt ────────────────────────
prompt = """Write a concise summary of the following:
{text}
Use overall header as 'NVIDIA Q4 FY2023 Earnings Call Highlights' without any description.
Use 3 marker bullet points (for Revenue: <value> (<up/down % YoY>), GAAP EPS: <value> (<up/down % YoY>), Non-GAAP EPS: <value> (<up/down % YoY>)) with header as 'Financial Highlights'.
Use 3 marker bullet points (for Datacenter segment revenue <grew/declined % YoY to $X, describe reason>, Gaming segment revenue <grew/declined % YoY to $X, describe reason>, Automotive segment revenue <grew/declined % YoY to $X, describe reason>) with header as 'Segment Highlights'.
Use 3 marker bullet points (Operating cash flow: <value> (<up/down % YoY>), Capital expenditures: <value> (<up/down % YoY>), Cash and equivalents: <value> (<up/down % YoY>)) with header as 'Cash Flow and Capex'.
Use 3 marker bullet points to describe strategic moves with header as 'Strategic Moves'.
Use 3 marker bullet points to describe key risks with header as 'Key Risks'.
"""

prompt_template = PromptTemplate.from_template(prompt)
parser = StrOutputParser()

# ── 4. Join documents into single text block ──────────────────
def join_docs(docs):
    return {"text": "\n\n".join(getattr(d, "page_content", str(d)) for d in docs)}

# ── 5. Build and run the chain ────────────────────────────────
chain = (
    join_docs
    | prompt_template
    | llama_model
    | parser
)

# ── 6. Generate and print the summary ────────────────────────
summary = chain.invoke(docs)
print(summary)
