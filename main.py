import Movies
import Users, ratings


def display_menu():
    print("COMMAND MENU")
    print("L - List all movies")
    print("A -  Add a movie")
    print("R - Rate a movie")
    print("S - Search a movie")
    print("Q - Quit program")
    print()


def home_menu():
    a = input(" 1 to login: \n"
              " 2 to sign up: ")
    if a == "1":
        Users.login(User_details=Users.User_details)
    elif a == "2":
        Users.sign_up(User_details=Users.User_details)
    else:
        print("Please provide valid input")
        home_menu()


def main():
    home_menu()
    while True:
        command = input("Command: ")
        if command == "L":
            Movies.list(movie_list=Movies.movie_list)
        elif command == "A":
            Movies.add(movie_list=Movies.movie_list)
        elif command == "R":
            ratings.rate(ratings)

        elif command == "S":
            Movies.search(movie_list=Movies.movie_list)
        elif command == "Q":
            break
        else:
            print("Not a valid command. Please try again.\n")
            home_menu()
    print("Bye!")


if __name__ == "__main__":
    main()
