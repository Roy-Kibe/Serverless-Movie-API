# Serveless Movie API.
## Overview.
This project is a hands-on learning journey aimed at progressively building a serverless API solution for movie data. It begins with a simple console application that reads data from a local CSV file and gradually evolves into a fully functional serverless API deployed using AWS Cloud services. The project was inspired by [this video](https://www.youtube.com/watch?v=AZhINW89kbM), which provided the initial framework and guidance.



## Project Phases.
The project consists of **three phases**, each introducing new concepts and technologies that build upon the previous phase:hase.

### Phase 1: Console Application.
In this initial phase, we develop a console-based application to read movie data from a local CSV file. The application provides a menu-driven interface, allowing users to search for movies by title, release year, or director. This phase focuses on working with local data storage and basic data processing.

### Phase 2: API integration
In Phase 2, the local CSV data source is replaced with an external API. The app fetches movie data from [The Movie Database (TMDB) API](https://www.themoviedb.org/), handling JSON responses and implementing rate limiting and error handling. This phase introduces core concepts of HTTP requests, JSON parsing, and API interaction, laying the groundwork for understanding web-based data access.

### Phase 3: Cloud Integration.
In the final phase, the project transitions to the cloud using serverless architecture. The application is deployed as an AWS Lambda function with API Gateway, making the API accessible online without dedicated server resources. This phase covers cloud deployment, serverless infrastructure, and AWS services such as IAM for permissions and API Gateway for request handling.

## Technology stacks used.
- **Programming Language**: Python 3.
- **Libraries**: CSV (for file handling in [Phase 1](/phase-1/)), requests (for HTTP requests in the [second phase](/phase-2/))
- **Cloud Services**: AWS Lambda, AWS API Gateway, IAM (for permissions).
- **Version Control**: Git and Github.

## Branch Structure.
```
main
├── phase-1-console
├── phase-2-api
└── phase-3-serverless
```

## Getting started.
1. Clone the Repository.
   ```
   git clone https://github.com/Roy-Kibe/Serverless-Movie-API.git
   ```
2. Chose a phase to start with (I would recommend that you start with Phase 1)
3. Switch to the corresponding branch:
   ```
   git checkout phase-1-console
   ```
4. Follow the README in that branch for specific instructions.

## Contribution.
This is a learning project, but contributions are welcome! Please feel free to submit a Pull Request.
