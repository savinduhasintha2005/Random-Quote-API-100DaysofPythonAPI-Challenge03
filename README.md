# 🚀 100 Days of Python API Challenge

Build one API every day and gradually move from beginner to advanced topics.

This challenge covers:
- REST APIs  
- Databases  
- Authentication  
- Caching  
- External APIs  
- AI APIs  
- Real-time systems  
- Microservices  

---

# 🚀 Random Quote API 

This project will teach you:

- ✅ Creating API endpoints  
- ✅ Returning JSON responses  
- ✅ Working with lists and dictionaries  
- ✅ Using path operations (GET)  
- ✅ Running a FastAPI server  
- ✅ Testing APIs with Swagger UI  

---

## ⚙️ Step 1: Install FastAPI and Uvicorn

```bash
pip install fastapi uvicorn
````

Check installed packages:

```bash
pip list
```

---

## 📁 Step 2: Create Project Structure

```
random_quote_api/
│
├── main.py
├── requirements.txt

```

Save dependencies:

```bash
pip freeze > requirements.txt
```

---

## 🧠 Step 3: Write Your First API

### `main.py`

```python
from fastapi import FastAPI
import random

app = FastAPI()

quotes = [
    {
        "author": "Albert Einstein",
        "quote": "Life is like riding a bicycle. To keep your balance, you must keep moving."
    },
    {
        "author": "Steve Jobs",
        "quote": "Stay hungry, stay foolish."
    },
    {
        "author": "Nelson Mandela",
        "quote": "It always seems impossible until it's done."
    },
    {
        "author": "Mahatma Gandhi",
        "quote": "Be the change you wish to see in the world."
    },
    {
        "author": "Confucius",
        "quote": "It does not matter how slowly you go as long as you do not stop."
    }
]

@app.get("/")
def home():
    return {"message": "Welcome to Random Quote API"}

@app.get("/quote")
def get_random_quote():
    return random.choice(quotes)
```

---

## 🚀 Step 4: Run the Server

```bash
uvicorn main:app --reload
```

Output:

```
INFO: Uvicorn running on http://127.0.0.1:8000
```

---

## 🌐 Step 5: Test in Browser

### Home Endpoint

```
http://127.0.0.1:8000/
```

Response:

```json
{
  "message": "Welcome to Random Quote API"
}
```

---

### 🎲 Random Quote Endpoint

```
http://127.0.0.1:8000/quote
```

Example response:

```json
{
  "author": "Steve Jobs",
  "quote": "Stay hungry, stay foolish."
}
```

---

## 📚 Step 6: Interactive API Docs (Swagger)

FastAPI automatically generates docs:

```
http://127.0.0.1:8000/docs
```

You can test APIs without Postman.

---

## 👤 Step 7: Add Quote by Author

```python
@app.get("/quotes/{author}")
def get_quote_by_author(author: str):
    for q in quotes:
        if q["author"].lower() == author.lower():
            return q

    return {"message": "Author not found"}
```

Example:

```
/quotes/Steve Jobs
```

---

## 👥 Step 8: Multiple Quotes Per Author

```python
@app.get("/quotes/{author}")
def get_quotes_by_author(author: str):
    result = [
        q for q in quotes
        if q["author"].lower() == author.lower()
    ]

    if result:
        return result

    return {"message": "Author not found"}
```

---

## 🏷️ Step 9: Category Feature

```python
@app.get("/category/{category}")
def get_quote_by_category(category: str):
    filtered = [
        q for q in quotes
        if q["category"].lower() == category.lower()
    ]

    if filtered:
        return random.choice(filtered)

    return {"message": "Category not found"}
```

---

## 📦 Final Project Structure

```
random_quote_api/
│
├── main.py
├── requirements.txt
```

---

## 📡 API Endpoints

| Method | Endpoint             | Description       |
| ------ | -------------------- | ----------------- |
| GET    | /                    | Welcome message   |
| GET    | /quote               | Random quote      |
| GET    | /quotes/{author}     | Quotes by author  |
| GET    | /category/{category} | Quote by category |

---

## 🎯 Skills Learned

* FastAPI setup
* GET endpoints
* JSON responses
* Path parameters
* Lists & dictionaries
* Random module
* Swagger documentation




