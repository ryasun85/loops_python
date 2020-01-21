# import random

# for i in range(6):
#     print(random.randint(1,51))

# print("\n")

# for i in range(9,-1,-1):
#     print(i)

#new option
#for i in range(10):

#    print(9-i)

fav_movies= [
    "Her",
    "Jumanji",
    "Gentelmans",
    "Bad Boys"
]

fav_movies.extend(["Star wars", "Startrek"])

print(fav_movies)

for movie_index in fav_movies:
    print(movie_index)

def film_check():

    if fav_movies[2] == "Ghostbusters":
        print("yey is ghostbuster")
    else:
        print("boo,we want ghostbusters")

film_check()

