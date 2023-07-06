from lib.tag import Tag
def test_construct_tag():
    tag = Tag(1, 'Name')
    assert tag.id == 1
    assert tag.name == 'Name'


"""
We can format tags to strings nicely
"""
def test_tags_format_nicely():
    tag = Tag(1, 'Name')
    assert str(tag) == "Tag(1, Name)"

"""
We can compare two identical tags
And have them be equal
"""
def test_tags_are_equal():
    tag1 = Tag(1, 'Name')
    tag2 = Tag(1, 'Name')
    assert tag1 == tag2