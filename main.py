records = [
    {
        "title": "Snow white", 
        "genre": "Fantasy", 
        "rating": 1.3, 
        "director": "Marc Webb",
        "release": 2025,
    },
    {
        "title": "Oppenheimer", 
        "genre": "Historical", 
        "rating": 8.3, 
        "director": "Christopher Nolan",
        "release": 2023,
    },
    {
        "title": "The Dark Knight", 
        "genre": "Superhero", 
        "rating": 9.0, 
        "director": "Christopher Nolan",
        "release": 2008,
    },
    {
        "title": "The Karate Kid", 
        "genre": "Action", 
        "rating": 6.2, 
        "director": "Harald Zwart",
        "release": 2010,
    },
    {
        "title": "Hachi: A Dog's Tale", 
        "genre": "Animal adventure", 
        "rating": 8.1, 
        "director": "Lasse Hallström",
        "release": 2009,
    },
]

def list_all_records(records):
    print("=" * 80)
    print("|      Title         |      Genre      | Rating |    Director    |",
            "    Date    |")
    print("=" * 80)
    for item in records:
        print(f"{item['title']:^20}{item['genre']:^20}{item['rating']:^6.1f}",
                f" {item['director']:^20}{item['release']:^6}")    

    print("=" * 80)
    input("\nPress any key to continue...")

def add_movie(records):
    title = input("Enter Title: ").strip()
    genre = input("Enter Genre: ").strip()

    rating_input = float(input("Enter Rating: ").strip())
    if rating_input:
        rating = float(rating_input)
    else:
        print("Invalid rating. Setting to 0.0")
        rating = 0.0

    director = input("Enter Director: ").strip()

    release_input = input("Enter Release Year: ").strip()
    if release_input.isdigit():
        release = int(release_input)
    else:
        print("Invalid release year. Setting to 2025")
        release = 2025

    new_movie = {
        "title": title,
        "genre": genre,
        "rating": rating,
        "director": director,
        "release": release,
    }
    records.append(new_movie)
    print(f"Movie '{title}' added successfully!")
    return records

def search(records):
    title = input("Enter movie title to find: ").strip().lower()
    index = 0
    for item in records:
        if item["title"].lower() == title:
            print(f"The index is {index}.")
            print(f"The genre is {item['genre']}.")
            print(f"The rating is {item['rating']}.")
            print(f"The director is {item['director']}.")
            print(f"The release date was on {item['release']}.")
            return index
        index += 1
    print("Movie cannot be found.")
    return

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
            list_all_records(records)
        case '2':
            records = add_movie(records)
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