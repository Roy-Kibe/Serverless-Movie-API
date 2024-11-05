 # Movie Console Application.
 This is a command line Application that allows users to search for movies by title, release date, or director from a CSV file.

## Features
1. Load CSV Data: Reads movie data from a CSV file with columns like title, year, and director.
2. Search by Title: Allows searching for movies by entering a partial or complete title.
3. Search by Release Year: Filters movies by a specific release year.
4. Search by Director: Finds movies directed by a specified director.
5. Error Handling: Alerts the user if the file is not found or if the search returns no results.

## Prerequisites.
All that is needed to run this application is a [CSV file](/phase-1/movies.csv) with movie data, and python installed on your machine.


## Usage.
1. Clone the Repository.
   ```
   git clone https://github.com/Roy-Kibe/Serverless-Movie-API. git
   ```
2. Prepare a **CSV File** in the project directory that contains your movie data, in [this format](#example-csv-format)
3. Open a terminal in the project directory and run:
   ```
   python3 app.py
   ```
## Examples.
### 1. Example CSV Format
|Title     | year  | director |
| -------- | ----- | ---------|
|The Shawshank Redemption| 1994| Frank Darabont|
|Inception| 2010| Christopher Nolan|

- **Column Headers** should be all lower cased.
- **Encoding** use UTF-8 if the data contains special characters.
### 2. Example Output.
![Example output](/phase-1/Screenshot%20from%202024-11-05%2014-23-00.png)

## Contributing.
Contributions and feedback are welcome!! Just fork the repo, create a new branch and submit a pull request.