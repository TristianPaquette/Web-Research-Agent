"""
agent.py - the main entrypoint. Run with python agent.py "question"
"""

import sys
import time

from search import search_web
from scraper import fetch_page_text
from llm import answer_question

def run(question: str) -> None:
    print(f"\n Searching the web for : {question}\n")
    results = search_web(question, max_results=5)

    if not results:
        print("No search results. Try a different question.")
        return
    
    print(f"Found {len(results)} results. Fetching pages...\n")

    pages = []
    for r in results:
        print(f" - {r['url']}")
        text = fetch_page_text(r["url"])
        if text:
            pages.append({
                "title": r.get("title", ""),
                "url": r["url"],
                "text": text,
            })

    if not pages:
        print("\nCouln't fetch any pages. Aborting.")
        return
    
    print(f"\n Asking Claude to answer using {len(pages)} pages...\n")
    answer = answer_question(question, pages)

    print("=" * 60)
    print(answer)
    print("=" * 60)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python agent.py "your question"')
        sys.exit(1)
        
    question = " ".join(sys.argv[1:])
    run(question)