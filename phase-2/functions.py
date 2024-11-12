from config import api_key, base_url
import requests
def menu():
    print("\n=== Serverless Movies API Console Application ===")
    print("1. Search by title.")
    print("2. Search by release year")
    print("3. Search by director")
    print("4. Exit")
def search_by_title():
    title = input("Enter the movie title: ")
    url = f"{base_url}/search/movie"
    params = {'api_key': api_key, 'query': title}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            movie = data['results'][0]
            print(f"Title: {movie['original_title']}")
            print(f"Release data: {movie['release_date']}")
            print(f"Overview: {movie['overview']}")
        else:
            print("No result found.")
    else:
        print(f"Error: {response.status_code}")
def search_by_year():
    year = input("Enter the year: ")
    url = f"{base_url}/discover/movie"
    params = {'api_key': api_key, 'release_year': year}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            for movie in data['results'][:5]:
                print(f"Title: {movie['title']}, Release date: {movie['release_date']}")
        else:
            print("No movies found for that year")
    else:
        print(f"Error: {response.status_code}")
