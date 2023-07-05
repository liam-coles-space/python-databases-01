As a blogger
So I can write interesting stuff
I want to write posts having a title.

As a blogger
So I can write interesting stuff
I want to write posts having a content.

As a blogger
So I can let people comment on interesting stuff
I want to allow comments on my posts.

As a blogger
So I can let people comment on interesting stuff
I want the comments to have a content.

As a blogger
So I can let people comment on interesting stuff
I want the author to include their name in comments.

Nouns: 
title, contents, comments, name, posts

Record  |   Properties
Post        title, content
Comment     name, contents

Table: posts
ID: SERIAL
title: text
content: text

Table: comments
id: SERIAL
content: text
name: text

1. Can one post have many comments? YES
2. Can one comment have many posts? NO

-> Therefore,
-> A post HAS MANY comments
-> An comment BELONGS TO a post

-> Therefore, the foreign key is on the comments table.

CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  conetent text
);

CREATE TABLE comments(
    id SERIAL PRIMARY KEY,
    content text,
    name text,
    post_id int,
    constraint fk_post foreign key(post_id) references posts(id) on delete cascade
);
