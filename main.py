records = [
    {
        "title": "Snow white", 
        "genre": "fantasy", 
        "rating": 1.3, 
        "director": "Marc Webb",
        "release": 2025,
    },
    {
        "title": "Oppenheimer", 
        "genre": "historical", 
        "rating": 8.3, 
        "director": "Christopher Nolan",
        "release": 2023,
    },
    {
        "title": "The Dark Knight", 
        "genre": "superhero", 
        "rating": 9.0, 
        "director": "Christopher Nolan",
        "release": 2008,
    },
]

# TODO: (Bautista) Create the list all functionality and print the contents in
# a pleasant and formatted way

# TODO: (Managbanag) Create a function that will add new records to the list

# TODO: (Espinola) Create a search function that returns the index 
# of the found item

# TODO: (Banzali) Create an update function to change the 
# fields of the chosen record

# TODO: (Raymundo) Create a delete function that deletes the chosen record

while True:
    print("+ ========================== +")
    print("|    Welcome to MovieList    |")
    print("+ ========== Menu ========== +")
    print("|        [1] List All        |")
    print("|        [2] Add             |")
    print("|        [3] Update          |")
    print("|        [4] Delete          |")
    print("|        [5] Search          |")
    print("|        [6] Exit            |")
    print("+ ========================== +")
    user_choice = input("Enter your choice: ")
    
    match user_choice:
        case '1':
            print("List All")
        case '2':
            print("Add")
        case '3':
            print("Update") 
        case '4':
            print("Delete")
        case '5':
            print("Search")
        case '6':
            print("Exiting...")
            break
        case _:
            print("Wrong Input")