import main
Ratings = [{
    "id": 1, "user_id": 1, "movie_id": 1, "rating": 5}]


def rate(Ratings):
    user_id = input("Enter user id: ")
    movie_id = input("Enter Movie id: ")
    rating = int(input("Rate this movie: "))
    if rating <= 5:
        print("Rated " + str(rating) + "Movie NO " + movie_id)
        main.display_menu()
    else:
        print(" value should be less that or equal 5")
        return






