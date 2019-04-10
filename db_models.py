from datetime import datetime

from mongoengine import (CASCADE, DateTimeField, DecimalField, DictField,
                         Document, EmailField,
                         EmbeddedDocument, EmbeddedDocumentField,
                         EmbeddedDocumentListField, IntField, ListField,
                         ObjectIdField, PointField, ReferenceField,
                         StringField, URLField)

from db_setup import db_init


db_init('prod')


# user
class User(Document):
    post_ids = ListField(ObjectIdField(required=True))
    username = StringField(max_length=50, required=True, unique=True)
    name = StringField(max_length=50, required=True)
    last_name = StringField(max_length=50, required=True)
    email = EmailField(max_length=100, required=True)
    joined_at = DateTimeField(default=datetime.now)
    # more fields with data provided from user source
    # depending of what its accessable from facebook

    meta = {
        'db_alias': 'main',
        'collection': 'users',
        'indexes': ['email', 'name', 'last_name', 'username', 'joined_at', 'post_ids'],
        'ordering': ['-email'],
    }

    def __str__(self):
        return f'{self.email}'


# post
class Comment(EmbeddedDocument):
    user = ReferenceField(User, required=True)
    text = StringField(required=True)
    created_at = DateTimeField()

    meta = {
        'db_alias': 'main',
        'collection': 'comments',
        'indexes': ['user', 'text'],
        'ordering': ['-created_at'],
    }

    def __str__(self):
        return f'{self.text}'


CLASSIFICATION_CHOICES = ('spam', 'ok')


class Post(Document):
    user = ReferenceField(User, required=True, reverse_delete_rule=CASCADE)
    shelter_id = ObjectIdField(required=True)
    text = StringField(required=True)
    comments = EmbeddedDocumentListField(Comment)
    classification = StringField(required=True, choices=CLASSIFICATION_CHOICES)
    created_at = DateTimeField()

    meta = {
        'db_alias': 'main',
        'collection': 'posts',
        'indexes': ['user', 'shelter_id', 'classification', 'text', 'comments'],
        'ordering': ['-created_at'],
    }

    def __str__(self):
        return f'{self.id}'


# shelter
class Characteristic(EmbeddedDocument):
    description = StringField(required=True, max_length=1500)
    description_tags = ListField(StringField(max_length=30))
    room_quantity = IntField(min_value=1)
    size = DecimalField(min_value=1, precision=2, rounding='ROUND_HALF_UP')
    deposit = DecimalField(min_value=1, precision=2, rounding='ROUND_HALF_UP')
    additional_information = StringField(max_length=500)
    contact_information = ReferenceField(User)
    extra = DictField()

    meta = {
        'db_alias': 'main',
        'collection': 'characteristics',
        'indexes': ['description', 'description_tags', 'room_quantity', 'size',
                    'deposit', 'additional_information', 'contact_information', 'extra'],
    }

    def __str__(self):
        return f'{self.id}'


class Media(EmbeddedDocument):
    url_links = ListField(URLField())
    url_files = ListField(URLField())
    url_videos = ListField(URLField())
    url_images = ListField(URLField())
    url_events = ListField(URLField())
    extra = DictField()

    meta = {
        'db_alias': 'main',
        'collection': 'medias',
        'indexes': ['url_images', 'url_videos', 'url_files',
                    'url_links', 'url_events', 'url_events', 'extra'],
    }

    def __str__(self):
        return f'{self.id}'


class Address(EmbeddedDocument):
    line1 = StringField(required=True, max_length=80)
    line2 = StringField(max_length=80)
    line3 = StringField(max_length=80)

    city = StringField(required=True, max_length=40)
    district = StringField(max_length=40)
    country = StringField(required=True, max_length=40)
    postcode = StringField(required=True, max_length=10)

    geolocation = PointField(required=True, auto_index=True)  # geojson object
    extra = DictField()

    meta = {
        'db_alias': 'main',
        'collection': 'addresses',
        'indexes': ['line1', 'line2', 'line3', 'postcode', 'district',
                    'city', 'country', 'geolocation', 'extra'],
    }

    def __str__(self):
        return f'{self.geolocation}'


PORPUSE_CHOICES = ('offer',  'request')
TYPE_CHOICES = ('room', 'flat', 'house')


class Shelter(Document):
    post = ReferenceField(Post, required=True, reverse_delete_rule=CASCADE)

    porpuse = StringField(required=True, choices=PORPUSE_CHOICES)  # Suche or Gesuch
    type = StringField(required=True, choices=TYPE_CHOICES)
    price = DecimalField(required=True, min_value=1, precision=2, rounding='ROUND_HALF_UP')
    start = DateTimeField(required=True)
    end = DateTimeField()
    address = EmbeddedDocumentField(Address)
    characteristic = EmbeddedDocumentField(Characteristic)
    media = EmbeddedDocumentField(Media)
    description_tags = ListField(StringField(max_length=30))
    created_at = DateTimeField()
    updated_at = DateTimeField()  # with signal
    extra = DictField()

    meta = {
        'db_alias': 'main',
        'collection': 'shelters',
        'indexes': ['post', 'description_tags', 'porpuse', 'type',
                    'price', 'start', 'end', 'address', 'characteristic',
                    'media', 'created_at', 'extra', ],
        'ordering': ['-start'],
    }

    def __str__(self):
        return f'{self.geolocation}'
