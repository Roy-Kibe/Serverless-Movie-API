# API Console Application.
This is the **second phase** of a multi-phase project aimed at building a serverless API solution. I have created a console-based application that allows user to search for movies by title, release year, or director.
The project uses [The Movie Database API. ](https://www.themoviedb.org/) to retrieve movie data, and this is an exciting way to learn about APIs and JSON parsing.

## Project Files.
This project consists of three main files:
1. ```main.py```: The main python script that runs the console application and handles user input.
2. ```functions.py```: Contains the functions for displaying the menu and performing API searches by title and release year.
3. ```config.py```: Stores the configuration files i.e: The api_key and base_url.

## Features
1. Search by Title: Allows the user to enter a movie title to retrieve information like the release date and overview.
2. Search by Release Year: Allows the user to enter a release year to view the top five movies released in that year.
3. Search by Director: (Will be implemented in future.)

## Setup and Usage
1. Ensure you have the following prerequisites:
   - Python 3.6 installed.
   - **Requests** library (install using ```pip install requests```)
   - TMDB api key (Sign up for an API key [ here ](https://www.themoviedb.org/login?to=read_me&redirect_uri=/docs)and replace the placeholder in [config.py](/config.py)) 
2. Clone the repository.
   ```
    git clone https://github.com/Roy-Kibe/Serverless-Movie-API. git
   ```
3. Install dependencies.
4. Replace ```your_tmdb_api_key``` with your actual API key.
5. Run the application.
   ```
   python3 main.py
   ````
6. Choose an option from the menu.

## Example Session.
![Screenshot](/Pasted%20image.png)