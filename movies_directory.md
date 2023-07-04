As a person who loves movies,
So I can list all my favourite movies
I want to see a list of movies' titles.

As a person who loves movies,
So I can list all my favourite movies
I want to see a list of movies' genres.

As a person who loves movies,
So I can list all my favourite movies
I want to see a list of movies' release years.


Nouns:
movies, title, genre, release year

Record   |   Properties
Movie    | title, genre, release_year

Columns:
title: text
genre: text
release_year: int


SQL:

file: movie_directory.sql

Create Table movies(
    id SERIAL PRIMARY KEY,
    title text,
    genre text,
    release_year int
)