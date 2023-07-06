from lib.post import *
from lib.post_repository import *

def test_find_by_tag(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = PostRepository(db_connection)
    posts = repository.find_by_tag('coding')
    assert posts == [
        Post(1, 'How to use Git'),
        Post(2, 'Python classes'),
        Post(3, 'Using a REPL'),
        Post(7, 'SQL basics'),
    ]

