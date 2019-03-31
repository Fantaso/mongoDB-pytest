from pytest import mark
from db_models import User, Post, Comment, Shelter, Characteristic
from pprint import pprint


@mark.smoke
@mark.user
class MongoUserModelTests:
    def test_user_model(self, db_init, test_data):
        user1 = test_data.get('user1')

        # pprint(*user1)
        # pprint(test_data1)
        assert True


@mark.smoke
@mark.post
class MongoPostModelTests:
    def test_user_post(self, db_init):
        assert True


@mark.smoke
@mark.shelter
class MongoShelterModelTests:
    def test_user_shelter(self, db_init):
        assert True
