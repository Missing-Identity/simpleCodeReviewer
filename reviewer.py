import openai
import os
from dotenv import load_dotenv
import argparse


prompt = """You will recieve a file's contents as text.
Generate a code review for the file. Indicate what changes should be made to improve its style, performance,
 readability and maintainability. If there are any reputable libraries that could be introduced to improve the
code, suggest them. Be kind and constructive in your feedback. For each suggested change, include the 
line numbers to which you are referring."""


filecontent = """
def mystery(x,y):
    return x**y
"""

def code_review_request(filecontent, model):
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": f"Code Review the following file: {filecontent}"},
    ]

    response = openai.ChatCompletion.create(model=model, messages=messages, max_tokens=2000)

    return response.choices[0].message.content


def code_review(filepath, model):
    with open(filepath, 'r') as f:
        content = f.read()
    generated_code_review = code_review_request(content, model)
    print(generated_code_review)


def main():
    # Setup Arguments Parser for command line
    parser = argparse.ArgumentParser(description='Generate a code review for a file.')
    parser.add_argument("file")
    parser.add_argument("--model", default="gpt-3.5-turbo")
    args = parser.parse_args()
    code_review(args.file, args.model)


if __name__ == '__main__':
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    main()
