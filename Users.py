import Movies
import main
User_details = [{"id":  1, "name": "john Doe", "phone": "1111111111", "password": "pass1", "email":
                "Johndoe@gmail.com"}]


def sign_up(User_details):
    name = input("Name: ")
    phone = input("Phone: ")
    password = input("password : ")
    email = input("email: ")

    users = {}
    users["name"] = name
    users["phone"] = phone
    users["password"] = password
    users["email"] = email
    User_details.append(users)
    print("Congratulations " + users["name"] +
          ", Sign Up successful, Now You can login.\n")
    login(User_details)


def login(User_details):

    email = input("Enter registered email: ")
    password = input("Enter password: ")

    for items in User_details:
        if email == items["email"] and password == items["password"]:
            main.display_menu()
            break
    else:
        print("Error")
        main.home_menu()


