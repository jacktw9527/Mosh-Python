from ninja import Schema

class GenreSchema(Schema):
    id: int
    name: str


class MovieSchema(Schema):
    id: int
    title: str
    release_year: int
    number_in_stock: int
    daily_rate: float
    genre: GenreSchema
