# AI Web Search Agent

A simple Python web research agent that searches the web, fetches webpage text, and uses Claude to generate an answer based on the sources it finds.

I built this project as a portfolio/resume project to practice working with APIs, environment variables, web scraping, and AI tools in Python. The app takes a user question, searches the web using Tavily, pulls readable text from the result pages, and sends that information to Claude to create a clear answer.

## Features

- Ask a question from the command line
- Search the web using the Tavily API
- Fetch readable text from webpage results
- Remove unnecessary webpage content like scripts and styling
- Send gathered source text to Claude using the Anthropic API
- Generate an answer based on the scraped web context

## Why I Built This

This project was made to help me practice building a small AI-powered Python application with real API usage.

The main goal was to better understand how different parts of a program work together, including searching the web, fetching webpage data, cleaning text, sending context to an AI model, and returning a useful answer to the user.

I also wanted more practice with organizing a Python project into separate files instead of putting everything into one large script.

## Tech Stack

### Language

- Python

### APIs

- Tavily API
- Anthropic Claude API

### Python Libraries

- requests
- beautifulsoup4
- python-dotenv
- anthropic
