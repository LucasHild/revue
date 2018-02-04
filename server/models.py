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


class Subvue(Document):
    name = StringField(max_length=120, required=True)
    permalink = StringField(max_length=120, required=True)
    description = StringField(max_length=500, required=True)
    created = DateTimeField(required=True, default=datetime.datetime.now())
    moderators = ListField(ReferenceField(User))

    meta = {'queryset_class': CustomQuerySet}

    def to_public_json(self):
        data = {
            "id": str(self.id),
            "name": self.name,
            "description": self.description,
            "moderators": [{
                "id": str(moderator.id),
                "username": moderator.username
            } for moderator in self.moderators],
        }

        return data


class Post(Document):
    title = StringField(max_length=120, required=True)
    subvue = ReferenceField(Subvue, required=True, default=Subvue.objects(permalink="default").first(), reverse_delete_rule=CASCADE)
    user = ReferenceField(User, reverse_delete_rule=CASCADE)
    content = StringField(max_length=5000)
    comments = ListField(EmbeddedDocumentField(Comment))
    created = DateTimeField(required=True, default=datetime.datetime.now())
    image = StringField()
    upvotes = ListField(ReferenceField(User, reverse_delete_rule=CASCADE))
    downvotes = ListField(ReferenceField(User, reverse_delete_rule=CASCADE))

    meta = {'queryset_class': CustomQuerySet}

    def to_public_json(self):
        data = {
            "id": str(self.id),
            "title": self.title,
            "subvue": {
                "name": self.subvue.name,
                "permalink": self.subvue.permalink,
                "description": self.subvue.description,
                "created": self.subvue.created.strftime("%Y-%m-%d %H:%M:%S"),
                "moderators": [{
                    "id": str(moderator.id),
                    "username": moderator.username
                } for moderator in self.subvue.moderators],
            },
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