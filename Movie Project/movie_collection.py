import csv
import re

def load_movies():
    movies = []

    with open("movies.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            movies.append(row)

    return movies


def display_movies(movies):
    if not movies:
        print("No movies found.")
        return

    print("\n=== MOVIE COLLECTION ===")

    for movie in movies:
        print("Movie ID :", movie["MovieID"])
        print("Title    :", movie["Title"])
        print("Year     :", movie["Year"])
        print("Genre    :", movie["Genre"])
        print("Rating   :", movie["Rating"])
        print("---")

def search_by_id(movies, movie_id):
    for movie in movies:
        if movie["MovieID"] == movie_id:
            print("\nMovie Found!")
            print("Movie ID :", movie["MovieID"])
            print("Title    :", movie["Title"])
            print("Year     :", movie["Year"])
            print("Genre    :", movie["Genre"])
            print("Rating   :", movie["Rating"])
            return

    print("\nMovie with ID", movie_id, "not found.")

def search_by_title(movies, pattern):
    print("\n== SEARCH RESULTS ==")

    found = False

    try:
        for movie in movies:
          
            if re.search(pattern, movie["Title"], re.IGNORECASE):
                print("Movie ID :", movie["MovieID"])
                print("Title    :", movie["Title"])
                print("Year     :", movie["Year"])
                print("Genre    :", movie["Genre"])
                print("Rating   :", movie["Rating"])
                print("---")
                found = True

    except re.error:
        print("Invalid Regular Expression!")

    if not found:
        print("No movies found matching the pattern.")

def main():
    movies = load_movies()

    while True:
        print("\n=== MOVIE COLLECTION SYSTEM ===")
        print("1. Display All Movies")
        print("2. Search Movie by ID")
        print("3. Search Movie by Title (Regex)")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_movies(movies)

        elif choice == "2":
            movie_id = input("Enter Movie ID: ")
            search_by_id(movies, movie_id)

        elif choice == "3":
            pattern = input("Enter title search pattern: ")
            search_by_title(movies, pattern)

        elif choice == "4":
            print("Exiting Movie Collection System...")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()