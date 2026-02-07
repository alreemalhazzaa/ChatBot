# LLM Chatbot Training (Groq + Llama 3)

## Description

The LLM Chatbot is a Python-based console application that demonstrates how to build an AI assistant using Groq’s high-speed Llama 3 API. It features a conversational loop, customizable model parameters, and a system for following specific writing guidelines.

This project serves as a hands-on assignment to master API integration, file handling, and prompt engineering.
Features

    Dynamic Model Settings: User-controlled temperature, top-p, and max tokens at startup.

    Persona Management: Loads an editable writing-guideline file to set the bot's behavior.

    Conversation Memory: Maintains a message history with a user-defined limit.

    File Summarization: A specialized command to process and summarize text files.

    Utility Commands: Includes features to save logs, clear memory, and show help.

## Technologies Used

    Python

    Groq API (OpenAI-compatible client)

    python-dotenv (Environment variable management)

    Llama 3 8B Model 

## How the Program Works

    The script loads the API key from a .env file and reads the writing_guideline.txt.

    The user configures the model parameters (e.g., temperature and history limit).

    The program enters a loop where it reads user input and sends it to the LLM.

    Special commands are handled separately:

        /summarize: Reads a document, generates a summary, and saves it to a file.

        /save: Exports the current chat history to a text file.

        /clear: Wipes the current message history.

## How to Run

    Create the folder structure: prompts/, docs/, and outputs/.

    Install requirements: pip install openai python-dotenv.

    Add your GROQ_API_KEY to a .env file.

    Run the script: python app.py.

## Example Output

    User: /summarize docs/sample_doc.txt

    Bot: Generates a clear summary based on the document content

    System: Saved to outputs/sample_doc_summary.txt 

## Author

Al-Reem Al-Hazza
