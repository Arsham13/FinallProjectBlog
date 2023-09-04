from weblog import app, db
from weblog import User, Post, Tag, post_tag
from faker import Faker
import random

fake = Faker()
with app.app_context():
    db.drop_all()
    db.create_all()

roles = ['Author', 'Admin', 'Editor']

tag_names = ['politics', 'sport', 'technology',
             'finance', 'entertainment']
tag_count = [1,2,3]
users = []
tags = []
posts = []
post_tag = []

for _ in range(10):
    user = User(name=fake.name(), username=fake.name(), password=fake.password(), role=random.choice(roles))
    users.append(user)

for t_name in tag_names:
    tag = Tag(name=t_name)
    tags.append(tag)

for _ in range(30):
    post = Post(title=fake.sentence(),
                content=fake.text(),
                author=random.choice(users))
    posts.append(post)

for post in posts:
    tag_counts = random.choice(tag_count)
    current_tags = random.sample(tags, tag_counts)
    post.labels = current_tags

with app.app_context():
    db.session.add_all(users)
    db.session.add_all(tags)
    db.session.add_all(posts)
    db.session.commit()