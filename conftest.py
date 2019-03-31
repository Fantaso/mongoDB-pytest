from pytest import fixture
from datetime import datetime, timedelta

from db import db_init as _db_init


@fixture
def db_init(scope='session'):
    return _db_init('test')


@fixture
def test_data(scope='session'):
    # users
    # post 1
    user1 = dict(
        username='Philippino Phil',
        name='Philippino',
        last_name='Phil',
        email='philippino.phil@test.com'
    )

    # post 2
    user2 = dict(
        username='Ioannis Stavros Golemas',
        name='Ioannis',
        last_name='Stavros Golemas',
        email='Ioannis.stavros@test.com'
    )

    # comments in comment 1 and 2
    user3 = dict(
        username='dionisio',
        name='pedro',
        last_name='picapiedra',
        email='pedro.picapiedra@test.com'
    )

    # comments in comment 1 and 2
    user4 = dict(
        username='morfeo',
        name='robo',
        last_name='tina',
        email='robo.tina@test.com'
    )

# posts
    post1 = dict(
        user=user1,
        text='looking for apartment',
        classification='ok'
    )
    post2 = dict(
        user=user2,
        text='looking for room',
        classification='ok'
    )

# shelter
    # shelter 1
    shelter1 = dict(
        user=user1,
        porpuse='request',
        type='flat',
        price=450.00,
        start=datetime.now(),
        end=(datetime.now() + timedelta(days=10)),
        description_tags=['bright', 'warm neighbor'],
    )
    characteristic1 = dict(
        description='very bewautifull aparmtnet in berlin hearts, 3 rooms etc blahh blahh',
        description_tags=['bright', 'cozy', 'warm'],
        size=98,
        deposit=1500,
        room_quantity=4,
    )
    media1 = dict(
        url_links='',
        url_files='',
        url_videos='',
        url_images='',
    )
    address1 = dict(
        line1='',
        city='',
        district='',
        country='',
        postcode='',
        geolocation='',
        extra='',
    )

    # comments post 1
    comment1_1 = dict(user=user3, text='send you PM')
    comment1_2 = dict(user=user4, text='me too PM')
    comment1_3 = dict(user=user1, text='checking your PM')

    # shelter 2
    shelter2 = dict(
        user=user2,
        porpuse='request',
        type='flat',
        price=450.00,
        start=datetime.now(),
        end=(datetime.now() + timedelta(days=10)),
        description_tags=['bright', 'warm neighbor'],
    )
    characteristic2 = dict(
        description='very bewautifull aparmtnet in berlin hearts, 3 rooms etc blahh blahh',
        description_tags=['bright', 'cozy', 'warm'],
        size=98,
        deposit=1500,
        room_quantity=4,
    )
    media2 = dict(
        url_links='',
        url_files='',
        url_videos='',
        url_images='',
    )
    address2 = dict(
        line1='',
        city='',
        district='',
        country='',
        postcode='',
        geolocation='',
        extra='',
    )
    # comments post 2
    comment2_1 = dict(user=user4, text='me too first PM')
    comment2_2 = dict(user=user4, text='send you PM second')
    comment2_3 = dict(user=user2, text='checking them')

    # return
    all = dict(
        user1=user1,
        user2=user2,
        user3=user3,
        user4=user4,
        post1=post1,
        post2=post2,
        shelter1=shelter1,
        characteristic1=characteristic1,
        media1=media1,
        address1=address1,
        comment1_1=comment1_1,
        comment1_2=comment1_2,
        comment1_3=comment1_3,
        shelter2=shelter2,
        characteristic2=characteristic2,
        media2=media2,
        address2=address2,
        comment2_1=comment2_1,
        comment2_2=comment2_2,
        comment2_3=comment2_3,
    )
    return all


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
