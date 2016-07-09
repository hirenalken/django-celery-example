#!venv/bin/python2
import random
import sys

import os


if __name__ == '__main__' and __package__ is None:
    os.sys.path.append(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celery_demo.settings")

import django
django.setup()

from api.models import User, Post, Comment


def main():
    users = User.objects.all()
    posts = Post.objects.all()
    for post in posts:
        for i in range(random.randint(3, 6)):
            Comment.objects.create(
                text='This is Comment.',
                post_id=post.id,
                user_id=random.randint(1, 504)
            )
    # for user in users:
    #     for i in range(15):
    #         Post.objects.create(
    #             title='Title %s' % i,
    #             text='text for post. Any text can go here',
    #             user_id=user.id
    #         )


if __name__ == '__main__':
    main()
