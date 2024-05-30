from fastapi import FastAPI, HTTPException
import database , models
from sqlmodel import Session, select

app = FastAPI()

@app.get('/')
async def get_all():
    with Session(database.engine) as session:  
         statement = select(models.Book) 
         results = session.exec(statement)
         books = []
         for book in results:
             books.append(book)
    return books

@app.post('/add_book')
async def add_book(book: models.BookCreate):
    new_book = models.Book(**book.model_dump())
    with Session(database.engine) as session:
        session.add(new_book)
        session.commit()
        session.refresh(new_book)
    return new_book

@app.delete('/delete_book/{book_id}')
async def delete_book(book_id: int):
    with Session(database.engine) as session:
        statement = select(models.Book).where(models.Book.id == book_id)
        results = session.exec(statement)
        book = results.one_or_none()
        
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        
        session.delete(book)
        session.commit()
    
    return {"message": "Book deleted successfully"}

@app.put('/update_book/{book_id}')
async def update_book(book_id: int, book_data: models.BookUpdate):
    with Session(database.engine) as session:
        statement = select(models.Book).where(models.Book.id == book_id)
        results = session.exec(statement)
        book = results.one_or_none()
        
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        
        for key, value in book_data.model_dump(exclude_unset=True).items():
            setattr(book, key, value)
        
        session.add(book)
        session.commit()
    
    return {"message": "Book updated successfully"}