import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()

##assume users were poplulated before
from rango.models import Category, Page, Comment, User

user1_comments = {
    '1' : {'content': 'Hey, wonderful watch !', 'rating':3},
    '2' : {'content': 'I hate it very much !', 'rating':1}
}

user2_comments = {
    '1' : {'content': 'IEJRKJEKRJ !', 'rating':3},
    '3' : {'content': 'Oh no !', 'rating':1},
    '5' : {'content': 'hurra haruier !', 'rating':5}
}

def add_comment(content, rating, category_id, user_id):
    c = Comment.objects.get_or_create(content=content,rating=rating,category_id=category_id,user_id=user_id)[0]
    c.content = content
    c.rating = rating
    c.category_id = category_id
    c.user_id = user_id
    c.save()
    return c

for cat, comment in user1_comments.items():
    add_comment(comment['content'],comment['rating'],int(cat),1)

for cat, comment in user2_comments.items():
    add_comment(comment['content'],comment['rating'],int(cat),2)