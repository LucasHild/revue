import datetime

from mongoengine import *


connect("revue")


class CustomQuerySet(QuerySet):
    def to_public_json(self):
        return [doc.to_public_json() for doc in self]


class User(Document):
    email = EmailField(required=True, unique=True)
    username = StringField(max_length=50, required=True, unique=True)
    password = StringField(required=True)
    created = DateTimeField(required=True, default=datetime.datetime.now())


class Comment(EmbeddedDocument):
    content = StringField(max_length=5000)
    user = ReferenceField(User)
    created = DateTimeField(required=True, default=datetime.datetime.now())


class Post(Document):
    title = StringField(max_length=120, required=True)
    user = ReferenceField(User, reverse_delete_rule=CASCADE)
    content = StringField(max_length=5000)
    comments = ListField(EmbeddedDocumentField(Comment))
    created = DateTimeField(required=True, default=datetime.datetime.now())
    image = StringField()

    meta = {'queryset_class': CustomQuerySet}

    def to_public_json(self):
        data = {
            "id": str(self.id),
            "title": self.title,
            "content": self.content,
            "user": {
                "id": str(self.user.id),
                "username": self.user.username
            },
            "comments": [{
                "content": comment.content,
                "created": comment.created.strftime("%Y-%m-%d %H:%M:%S"),
                "user": {
                    "id": str(comment.user.id),
                    "username": comment.user.username
                }
            } for comment in self.comments][::-1],
            "created": self.created.strftime("%Y-%m-%d %H:%M:%S"),
            "image": self.image
        }

        return data