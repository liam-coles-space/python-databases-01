CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text
);

CREATE TABLE comments(
    id SERIAL PRIMARY KEY,
    content text,
    name text,
    post_id int,
    constraint fk_post foreign key(post_id) references posts(id) on delete cascade
);