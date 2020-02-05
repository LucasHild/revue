import datetime
import hashlib

from mongoengine import (
    connect, Document, EmailField, StringField, ListField, ReferenceField, DateTimeField, EmbeddedDocument,
    EmbeddedDocumentField, CASCADE
)


connect("revue")


class User(Document):
    email = EmailField(required=True, unique=True)
    username = StringField(max_length=50, required=True, unique=True)
    password = StringField(required=True)
    subscribed = ListField(ReferenceField("Subvue"))
    created = DateTimeField(required=True, default=datetime.datetime.now())

    def to_public_json(self):
        hashed_email = hashlib.md5(self.email.encode("utf-8")).hexdigest()

        data = {
            "id": str(self.id),
            "username": self.username,
            "hashedEmail": hashed_email,
            "subscribed": [subvue.to_public_json() for subvue in self.subscribed],
            "created": self.created,
        }

        return data


class Comment(EmbeddedDocument):
    content = StringField(max_length=5000)
    user = ReferenceField(User)
    created = DateTimeField(required=True, default=datetime.datetime.now())

    def to_public_json(self):
        data = {
            "content": self.content,
            "created": self.created,
            "user": {
                "id": str(self.user.id),
                "username": self.user.username
            }
        }

        return data


class Subvue(Document):
    name = StringField(max_length=120, required=True)
    permalink = StringField(max_length=120, required=True)
    description = StringField(max_length=500, required=True)
    created = DateTimeField(required=True, default=datetime.datetime.now())
    moderators = ListField(ReferenceField(User))

    def to_public_json(self):
        data = {
            "id": str(self.id),
            "name": self.name,
            "permalink": self.permalink,
            "description": self.description,
            "moderators": [{
                "id": str(moderator.id),
                "username": moderator.username
            } for moderator in self.moderators],
        }

        return data


class Post(Document):
    title = StringField(max_length=120, required=True)
    subvue = ReferenceField(Subvue, required=True, reverse_delete_rule=CASCADE)
    user = ReferenceField(User, reverse_delete_rule=CASCADE)
    content = StringField(max_length=5000)
    comments = ListField(EmbeddedDocumentField(Comment))
    created = DateTimeField(required=True, default=datetime.datetime.now())
    image = StringField()
    upvotes = ListField(ReferenceField(User, reverse_delete_rule=CASCADE))
    downvotes = ListField(ReferenceField(User, reverse_delete_rule=CASCADE))

    def to_public_json(self):
        data = {
            "id": str(self.id),
            "title": self.title,
            "subvue": self.subvue.to_public_json(),
            "content": self.content,
            "user": {
                "id": str(self.user.id),
                "username": self.user.username
            },
            "comments": [comment.to_public_json() for comment in self.comments][::-1],
            "created": self.created,
            "image": self.image,
            "upvotes": [{
                "id": str(upvote.id),
                "username": upvote.username
            } for upvote in self.upvotes],
            "downvotes": [{
                "id": str(downvote.id),
                "username": downvote.username
            } for downvote in self.downvotes],
        }

        return data
