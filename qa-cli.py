import argparse
from qa import setup, query

chain = setup()

parser = argparse.ArgumentParser(description='Zeptejte se na co vás zajímá.')
parser.add_argument('question', type=str, help='Otázka pro vyhledávání v Akademii solidpixels')
args = parser.parse_args()

response = query(chain, question)

if response and response['answer']:
    print(f"{response['answer']}")
    response['answer'] = markdown.markdown(response['answer'])

print()

if response and response['sources']:
    print(f"{response['sources']}")