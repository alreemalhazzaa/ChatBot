import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def load_guideline():
    try:
        with open("prompts/writing_guideline.txt", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "You are a helpful AI assistant."

def summarize_file(filepath, model, temperature, top_p, max_tokens):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "Summarize the following document clearly."},
            {"role": "user", "content": content}
        ],
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens
    )

    summary = response.choices[0].message.content

    output_path = "outputs/sample_doc_summary.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(summary)

    print("\n--- SUMMARY ---")
    print(summary)
    print(f"\nSaved to {output_path}")


def main():
    print("=== LLM Chatbot (Groq + Llama 3) ===")

    model = input("Model name [llama3-8b-8192]: ") or "llama3-8b-8192"
    temperature = float(input("Temperature [0.7]: ") or 0.7)
    top_p = float(input("Top-p [0.9]: ") or 0.9)
    max_tokens = int(input("Max tokens [512]: ") or 512)
    history_limit = int(input("History limit [10]: ") or 10)

    system_prompt = load_guideline()

    messages = [{"role": "system", "content": system_prompt}]

    print("\nType /help for commands\n")

    while True:
        user_input = input("You: ")

        if user_input == "/exit":
            break

        elif user_input == "/help":
            print("""
Commands:
/exit       Exit chatbot
/clear      Clear conversation memory
/save       Save conversation to outputs/chat.txt
/summarize  Summarize docs/sample_doc.txt
""")
            continue

        elif user_input == "/clear":
            messages = [{"role": "system", "content": system_prompt}]
            print("Memory cleared.")
            continue

        elif user_input == "/save":
            with open("outputs/chat.txt", "w", encoding="utf-8") as f:
                for msg in messages:
                    f.write(f"{msg['role'].upper()}: {msg['content']}\n\n")
            print("Conversation saved.")
            continue

        elif user_input.startswith("/summarize"):
            summarize_file(
                "docs/sample_doc.txt",
                model,
                temperature,
                top_p,
                max_tokens
            )
            continue

       
        active_messages = [messages[0]] + messages[-(history_limit-1):] if len(messages) > 1 else messages

        response = client.chat.completions.create(
            model=model,
            messages=active_messages,
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_tokens
        )

        reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})

        print("Bot:", reply)

if __name__ == "__main__":
    main()
