class Book:
    def __init__(
        self, id: int, title: str, author: str, description: str, rating: float
    ):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
