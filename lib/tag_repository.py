from lib.tag import *

class TagRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_by_post(self, tag_id):
        rows = self._connection.execute(
            'select tags.* from posts join posts_tags on posts.id = posts_tags.post_id join tags on posts_tags.tag_id = tags.id where posts.id = %s', [tag_id]
        )
        tags = []

        for row in rows:
            tag = Tag(row["id"], row["name"])
            tags.append(tag)
        
        return tags