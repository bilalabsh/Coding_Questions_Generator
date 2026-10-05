# Coding Questions Generator

Generates a coding test from a plain-English request. Tell it the topic and difficulty ("3 medium questions on binary trees") and it returns a set of relevant coding questions.

Built as my submission for an internship assessment at CodeInterview.io.

## Features

- Takes a topic and difficulty level as a natural-language prompt
- Uses an OpenAI model through LangChain with structured prompts to keep questions on topic
- Works from the command line or a simple Tkinter desktop window

## Tech stack

Python · LangChain · OpenAI API · Tkinter

## Run it

```bash
pip install -r requirements.txt
# add OPENAI_API_KEY to a .env file
python app.py      # command line
python gui.py      # desktop window
```
