from lib.post import *

#when created object has correct properties
def test_construct_post():
    post = Post(1, 'title')
    assert post.title == 'title'
    assert post.id == 1

"""
We can format posts to strings nicely
"""
def test_posts_format_nicely():
    post = Post(1, 'title')
    assert str(post) == "Post(1, title)"

"""
We can compare two identical posts
And have them be equal
"""
def test_posts_are_equal():
    post1 = Post(1, 'title')
    post2 = Post(1, 'title')
    assert post1 == post2
    