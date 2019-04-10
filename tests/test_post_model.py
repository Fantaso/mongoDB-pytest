from pprint import pprint

from db_models import Characteristic, Comment, Post, Shelter, User
from pytest import mark


@mark.smoke
@mark.post
class MongoPostModelTests:
    def test_user_post(self, db_init):
        assert True


'''
user1 = User(*user1).save()
user2 = User(*user2).save()
user3 = User(*user3).save()
user4 = User(*user4).save()


post1 = Post(*post1)

characteristic1 = Characteristic(characteristic1)
media1 = Media(*media1)
address1 = Address(*address1)

shelter1 = Shelter(*shelter1)
shelter1.characteristic = characteristic1
shelter1.address = address1
shelter1.media = media1

shelter1.save()
post1.shelter_id(shelter1.id).save()

comment1_1 = Comment(*comment1_1)
comment1_2 = Comment(*comment1_2)
comment1_3 = Comment(*comment1_3)

post1.comments.extend([comment1_1, comment1_2, comment1_3]).save()


post2 = Post(*post2)
characteristic2 = Characteristic(characteristic2)
media2 = Media(*meadia2)
address2 = Address(*address2)

shelter2.characteristic = characteristic2
shelter2.address = address2
shelter2.media = media2

shelter2.save()
post2.shelter_id(shelter2.id).save()

comment2_1 = Comment(*comment2_1)
comment2_2 = Comment(*comment2_2)
comment2_3 = Comment(*comment2_3)


post2.comments.extend([comment2_1, comment2_2, comment2_3]).save()
'''
