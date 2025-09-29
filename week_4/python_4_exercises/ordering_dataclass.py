from dataclasses import dataclass


@dataclass(order=True)
class Movie:
    rating: float
    title: str


m1 = Movie(8.9, "movie1")
m2 = Movie(7.2, "movie2")
m3 = Movie(9.4, "movie3")


movies = [m1, m2, m3]

# No need for key function, rating is compared first as order=True
for movie in sorted(movies):
    print(movie)

# Movie(rating=7.2, title='movie2')
# Movie(rating=8.9, title='movie1')
# Movie(rating=9.4, title='movie3')
