from datetime import datetime

from mongoengine import (DateTimeField, Document, DynamicEmbeddedDocument,
                         EmailField, EmbeddedDocument, EmbeddedDocumentField,
                         EmbeddedDocumentListField, FloatField, ListField,
                         ObjectIdField, StringField)

from mongo_setup import database_init

database_init()


class Location(DynamicEmbeddedDocument):
    """Lat & Lon | City | District | Street | Apartment Num | ..."""

    meta = {
        'db_alias': 'main',
        'collection': 'locations',
    }


class Availability(DynamicEmbeddedDocument):
    """Start date | End date | Time quantity | ..."""

    meta = {
        'db_alias': 'main',
        'collection': 'availability',
    }


class Characteristics(DynamicEmbeddedDocument):
    """Anmeldung (False | True) | Floor Num | Balcony | Basement ..."""

    meta = {
        'db_alias': 'main',
        'collection': 'characteristics',
    }


class Media(DynamicEmbeddedDocument):
    """Videos urls | Photos | File Documents | Links | ..."""

    meta = {
        'db_alias': 'main',
        'collection': 'medias',
    }


class Tag(DynamicEmbeddedDocument):
    """Preferences such as: bright | altbau | near transport | ..."""
    meta = {
        'db_alias': 'main',
        'collection': 'tags',
    }


PORPUSE_CHOICES = (('Suche', 'Suche'), ('Gesuch', 'Gesuch'))


class Apartment(DynamicEmbeddedDocument):
    post_id = ObjectIdField()
    porpuse = StringField(required=True, choices=PORPUSE_CHOICES)  # Suche or Gesuch
    budget = ListField(FloatField(default=[]))  # Rent price|Budget range

    location = EmbeddedDocumentListField(Location)
    availability = EmbeddedDocumentListField(Availability)
    characteristics = EmbeddedDocumentListField(Characteristics)
    media = EmbeddedDocumentListField(Media)
    tags = EmbeddedDocumentListField(Tag)

    meta = {
        'db_alias': 'main',
        'collection': 'apartments',
        'indexes': ['porpuse',
                    'budget',
                    'location',
                    'availability',
                    'characteristics',
                    'media',
                    'tags',
                    'created_at',
                    ],
        'ordering': ['-created_at'],
    }

    def __str__(self):
        return f'{self.post}'


class Comment(EmbeddedDocument):
    user_id = ObjectIdField()
    post_id = ObjectIdField()

    comment = StringField(required=True)
    created_at = DateTimeField(default=datetime.now)

    meta = {
        'db_alias': 'main',
        'collection': 'comments',
        'indexes': ['comment', 'created_at'],
        'ordering': ['-created_at'],
    }

    def __str__(self):
        return f'{self.comments}'


class Post(DynamicEmbeddedDocument):
    user_id = ObjectIdField()
    post = StringField(required=True)

    comments = EmbeddedDocumentListField(Comment)
    apartment = EmbeddedDocumentListField(Apartment)

    created_at = DateTimeField(default=datetime.now)

    meta = {
        'db_alias': 'main',
        'collection': 'posts',
        'indexes': ['post', 'apartment', 'comments', 'created_at'],
        'ordering': ['-created_at'],
    }

    def __str__(self):
        return f'{self.post}'


class FacebookUser(Document):
    username = StringField(max_length=50, required=True, verbose_name='Facebook Username')
    name = StringField(max_length=50, required=True)
    last_name = StringField(max_length=50, required=True)
    email = EmailField(max_length=100, required=True)
    join_group_at = DateTimeField(default=datetime.now)

    meta = {
        'db_alias': 'main',
        'collection': 'facebookusers',
        'indexes': ['email', 'name', 'last_name', 'username', 'join_group_at'],
        'ordering': ['-email'],
    }

    def __str__(self):
        return f'{self.username}'
