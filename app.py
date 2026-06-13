from fastapi import FastAPI
import random

app = FastAPI()

quotes = [
    {
        "author": "Albert Einstein",
        "category": "motivation",
        "quote": "Life is like riding a bicycle. To keep your balance, you must keep moving."
    },
    {
        "author": "Steve Jobs",
        "category": "motivation",
        "quote": "Stay hungry, stay foolish."
    },
    {
        "author": "Nelson Mandela",
        "category": "motivation",
        "quote": "It always seems impossible until it's done."
    },
    {
        "author": "Mahatma Gandhi",
        "category": "motivation",
        "quote": "Be the change you wish to see in the world."
    },
    {
        "author": "Confucius",
        "category": "motivation",
        "quote": "It does not matter how slowly you go as long as you do not stop."
    },
{
        "author": "Steve Jobs",
    "category": "motivation",
        "quote": "Stay hungry, stay foolish."
    },
    {
        "author": "Steve Jobs",
        "category": "motivation",
        "quote": "Innovation distinguishes between a leader and a follower."
    },
    {
        "author": "Albert Einstein",
        "category": "motivation",
        "quote": "Life is like riding a bicycle."
    },
{
        "author": "Steve Jobs",
        "category": "success",
        "quote": "Stay hungry, stay foolish."
    },
    {
        "author": "Nelson Mandela",
        "category": "motivation",
        "quote": "It always seems impossible until it's done."
    }
]

@app.get("/")
def home():
    return {"message" : "Welcome to Random Quote API"}

@app.get("/quote")
def get_random_quote():
    return random.choice(quotes)

""""
@app.get("/quotes/{author}")
def get_quote_by_author(author : str):
    for q in quotes:
        if q["author"].lower() == author.lower():
            return q
    return {"Message": " Author Not Found"}
"""

#Get multiple quotes per author
@app.get("/quotes/{author}")
def get_quotes_by_author(author:str):
    result = [
        q for q in quotes
        if q["author"].lower() == author.lower()
    ]

    if result:
        return result

    return {"message" : "Author Not Found"}

@app.get("/category/{category}")
def get_quote_by_category(category:str):
    filtered = [
        q for q in quotes
        if q["category"].lower() == category.lower()
    ]

    if filtered:
        return random.choice(filtered)

    return {"message" : "Category Not Found"}




