import datetime

from mongoengine import *


connect("revue")


# class CustomQuerySet(QuerySet):
#     def to_json(self):
#         return "[%s]" % (",".join([doc.to_json() for doc in self]))


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

    # meta = {'queryset_class': CustomQuerySet}

    def to_json(self):
        from bson import json_util
        data = self.to_mongo()
        data["user"] = {"User": {"username": self.user.username, "_id": self.user.id}}
        return json_util.dumps(data)

# lucas = User.objects(username="Lucas").first()
# #
# # post1 = Post(title="Hello", user=lucas, content="Lorem Ipsum", comments=[]).save()
# # post2 = Post(title="Hello Again", user=lucas, content="Lorem Ipsum Dolor", comments=[]).save()
#
# comment = Comment(content="Test", user=lucas)
# post = Post(title="Hello Again", user=lucas, content="Lorem Ipsum Dolor", comments=[comment]).save()