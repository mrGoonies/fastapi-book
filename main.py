from fastapi import FastAPI
from models.books import Book

app = FastAPI()

BOOKS = [
    Book(
        1,
        "Cien años de soledad",
        "Gabriel García Márquez",
        "Una novela épica que narra la historia de la familia Buendía a través de siete generaciones.",
        4.5,
    ),
    Book(
        2,
        "El Principito",
        "Antoine de Saint-Exupéry",
        "Un cuento poético que explora la amistad, el amor y el sentido de la vida.",
        4.8,
    ),
    Book(
        3,
        "1984",
        "George Orwell",
        "Una novela distópica que describe un mundo totalitario donde la libertad individual es suprimida.",
        4.3,
    ),
    Book(
        4,
        "El Señor de los Anillos",
        "J.R.R. Tolkien",
        "Una trilogía de fantasía épica que narra la lucha del bien contra el mal en la Tierra Media.",
        4.9,
    ),
    Book(
        5,
        "Harry Potter y la piedra filosofal",
        "J.K. Rowling",
        "Una novela de fantasía que narra las aventuras de un joven mago llamado Harry Potter.",
        4.7,
    ),
    Book(
        6,
        "Orgullo y prejuicio",
        "Jane Austen",
        "Una novela romántica que explora las relaciones sociales y el matrimonio en la Inglaterra del siglo XIX.",
        4.2,
    ),
]


@app.get("/api/v1/books")
async def get_all_books():
    return BOOKS
