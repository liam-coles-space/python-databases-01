from lib.post import *

class PostRepository:
    def __init__(self,connection):
        self._connection = connection

    def find_by_tag(self, tag_name):
        rows = self._connection.execute(
            'select posts.* from posts join posts_tags on posts.id = posts_tags.post_id join tags on posts_tags.tag_id = tags.id where name = %s', [tag_name]
        )
        posts = []

        for row in rows:
            post = Post(row["id"], row["title"])
            posts.append(post)

        return posts 