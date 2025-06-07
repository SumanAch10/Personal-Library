from fastapi import FastAPI, HTTPException
from book import book_list as book_db, Book
import random

app = FastAPI()

# Helper
def find_book(book_id: int):
    for book in book_db:
        if book["bk_id"] == book_id:
            return book
    return None

def generate_unique_id():
    existing_ids = {book["bk_id"] for book in book_db}
    while True:
        new_id = random.randint(1, 10000)
        if new_id not in existing_ids:
            return new_id

@app.get("/")
def show_response():
    return {"status": "200", "message": "Everything OK"}

@app.get("/get_books")
def show_all_books():
    return book_db

@app.post("/add_books")
def add_books(book: Book):
    book_data = book.dict()
    book_data["bk_id"] = generate_unique_id()
    try:
        book_db.append(book_data)
        return {"message": f"Book with id: {book_data['bk_id']} added successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.get("/get_book/{id}")
def get_book_by_id(id: int):
    book = find_book(id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found in the database")
    return book

@app.delete("/delete_book/{id}")
def del_book(id:int):
    book = find_book(id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found in the database")
    book_db.remove(book)
    return {f"Book with id: {book['bk_id']} deleted succesfully"}
    
