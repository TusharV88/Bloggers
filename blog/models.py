from mongoengine import Document, StringField, DateTimeField
from datetime import datetime

class BlogPost(Document):
    title = StringField(max_length=100, required=True)
    description = StringField(required=True)
    timestamp = DateTimeField(default=datetime.now)