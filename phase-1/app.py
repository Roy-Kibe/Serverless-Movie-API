import csv

def movie_load(csv_file):
    movies = []  # Empty list to store each row of data
    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)  # Debug: Print each row to verify structure
                movies.append(row)
    except FileNotFoundError:
        print(f"Error: The file {csv_file} does not exist")   
    return movies 

def menu():
    print("\n=== Serverless Movies API Console Application ===")
    print("1. Search by title.")
    print("2. Search by release year")
    print("3. Search by director")
    print("4. Exit")

def search_by_title(movies):
    title = input("Please enter the movie title: ").lower().strip()
    found = False
    for movie in movies:
        # Check if 'title' key exists in movie dictionary
        if 'title' in movie and title in movie['title'].lower():
            print(f"\nMovie Found: {movie['title']} (Year: {movie.get('year', 'Unknown')}, Director: {movie.get('director', 'Unknown')})")
            found = True
    if not found:
        print("Sorry, no movies found with that title.")

def search_by_year(movies):
    year = input("Please enter the release year: ").strip()
    found = False
    for movie in movies:
        # Check if 'year' key exists in movie dictionary
        if 'year' in movie and movie['year'] == year:
            print(f"\nMovie Found: {movie['title']} (Year: {movie['year']}, Director: {movie.get('director', 'Unknown')})")
            found = True
    if not found:
        print("Sorry, no movies found for that year.")

def search_by_director(movies):
    director = input("What is the name of the movie director?").lower().strip()
    found = False
    for movie in movies:
        # Check if 'director' key exists in movie dictionary
        if 'director' in movie and director in movie['director'].lower():
            print(f"\nMovie Found: {movie['title']} (Year: {movie.get('year', 'Unknown')}, Director: {movie['director']})")
            found = True
            
    if not found:
        print("Sorry, no movies found directed by that person.")
    
    
def main():
    
    movies = movie_load('/home/kibe/Desktop/projects/Serverless-movie-api/phase-1/movies.csv')
    while True:
        menu()
        response = input("Please select a number from the menu: ").strip()
        if response == "1":
            search_by_title(movies)
        elif response == "2":
            search_by_year(movies)
        elif response == "3":
            search_by_director(movies)
        elif response == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Please select a valid number from the menu.")

main()
