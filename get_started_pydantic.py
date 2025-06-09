from pydantic import BaseModel, Field
from typing import Annotated

class Director(BaseModel):
    name: str
    age: int

class Movie(BaseModel):
    title: str
    year: Annotated[int, "This is the release year of the movie"]  # Annotated field with a description
    genre: list[str]
    duration: int  # Duration in minutes
    rating: float = Field(default=5, ge=0, le=10)  # Optional rating field with constraints
    director: Director | None = None  # Optional director field

movie1 = Movie(title="Inception", year=2010, genre=["Sci-Fi", "Thriller"], duration=148)
movie2 = Movie(title="The Matrix", year=1999, genre=["Sci-Fi", "Action"], duration=136, rating=8.7)
print(movie1)
print(movie2)

print(movie1.model_dump()) # Dumping the model as a dictionary
print(movie2.model_dump_json()) # Dumping the model as a JSON string

# Example of creating a Movie instance from a JSON-like dictionary
movie3_json = { 
        "title":"Mission: Impossible - Fallout",
        "year":2018,
        "genre":["Action","Adventure","Thriller"],
        "duration":147,
        "rating":7.8
    }

movie3 = Movie(**movie3_json)
print(movie3)

movie4_json = {
        "title": "The Dark Knight",
        "year": 2008,
        "genre": ["Action", "Crime", "Drama"],
        "duration": 152,
        "rating": 9.0,
        "director": {
            "name": "Christopher Nolan",
            "age": 52
        }
    }
movie4 = Movie(**movie4_json)
print(movie4)
