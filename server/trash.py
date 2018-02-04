from models import *

a = Post.objects.first().to_public_json()
print(a)