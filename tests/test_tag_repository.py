from lib.tag import *
from lib.tag_repository import *

def test_find_by_tag(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = TagRepository(db_connection)
    tags = repository.find_by_post(6)
    assert tags == [
        Tag(2, 'travel'),
        Tag(3, 'cooking')
    ]