import main

movie_list = [
        {"name": "Inception", "genre": "Fiction", "rating": "PG", "year": 1954}]


def add(movie_list):
    name = input("Name: ")
    genre = input("genre: ")
    rating = input("rating: ")
    release_year = input("Year: ")

    movie = {}
    movie["name"] = name
    movie["genre"] = genre
    movie["rating"] = rating
    movie["year"] = release_year

    movie_list.append(movie)
    print(movie["name"] + " was added.\n")
    main.display_menu()


def list(movie_list):
    if len(movie_list) == 0:
        print("There are no movies in the list.\n")
        return
    else:
        i = 1
        for row in movie_list:
            id = str(i)
            print(id + ". " + row["name"])
            i += 1
        print()


def search(movie_list):
    name = input("Enter a movie: ")
    for items in movie_list:
        if name == items["name"]:
            print(" NAME:   " + items["name"], "\n"
                  " GENRE:  " + items["genre"], "\n"
                  " RATING: " + items["rating"], "\n"
                  " Release_Year:" + str(items["year"]))
            break

        else:
            print(name + "Not present in the list :( ")

