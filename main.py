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
            print(f"Index: {index}")
            print(f"Title: {item['title']}")
            print(f"Genre: {item['genre']}")
            print(f"Rating: {item['rating']}")
            print(f"Directed by: {item['director']}")
            print(f"Released: {item['release']}")
            return index
        index += 1
    print("Movie cannot be found.")
    return

def update_movie(records):
    index = search(records)

    if index == None:
        return
    
    movie = records[index]
    print("\nWhat do you want to update?")
    print("[1] Title")
    print("[2] Genre")
    print("[3] Rating")
    print("[4] Director")
    print("[5] Release")
    update_choice = int(input("Enter choice: "))

    match update_choice:
        case 1:
            movie["title"] = input("Enter new title: ").strip()
        case 2:
            movie["genre"] = input("Enter new genre: ").strip()
        case 3:
            movie["rating"] = float(input("Enter new rating: "))
        case 4:
            movie["director"] = input("Enter new director: ").strip()
        case 5:
            movie["release"] = int(input("Enter new release year: "))
        case _:
            print("Wrong input.")
            return
        
    print("Movie updated successfully.")

def delete_record(records):
    if not records:
        print("\nNo movie records to delete.")
        return

    while True:
        title = input("\nEnter the movie title to delete: ").strip().lower()

        for movie in records:
            if movie["title"].lower() == title:
                print(f"\nFound: {movie['title']} ({movie['release']})")
                
                confirm_in = input("Delete this movie? (yes/no): ")
                confirm = confirm_in.strip().lower()

                if confirm == "yes":
                    records.remove(movie)
                    print("\nMovie deleted successfully.")
                else:
                    print("\nMovie not deleted.")
                break
        else:
            print("\nMovie not found.")

        print("\nUpdated Movie Records:")
        list_all_records(records)

        if not records:
            print("\nNo more movies in the list.")
            break

        another = input("\nDelete another? (yes/no): ").strip().lower()
        if another != "yes":
            break

    input("\nPress Enter to continue...")

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
            update_movie(records)
        case '4':
            delete_record(records)
        case '5':
            search(records)
        case '6':
            print("Exiting...")
            break
        case _:
            print("Wrong Input")