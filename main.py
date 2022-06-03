from bing_image_downloader import downloader
import tweepy
import random
import shutil
import os
import time
import wikipedia

pictureAmount = 10

api_key = 'YOBqmX4Zj2L6kpZuqrJ7b2kZc'
api_key_secret = 'hORcrDHdf0LI7LE2Oy1qGmTR7cZOFdz3ZbU1ec6A2assoKBYze'
access_token = '1532676880645636096-t4sNJ5iTVyaAjIUyuJkrmnCydyuyC5'
access_token_secret = 'maM0GCCGxZMt8o1lv0jXaeoslYzgF82QM0yL2LGyrPJab'

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)
api = tweepy.API(authenticator, wait_on_rate_limit=True)

def randomWord():
    with open("words.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
        picture_object = random.choice(words)
        return picture_object

def randomPicture(picture_object, random_from_amount):

    downloader.download(f'{picture_object}', limit=random_from_amount, output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=10)

    if pictureAmount != 1:
        randPictureNumber = random.randrange(1, random_from_amount, 1)
    
    path = f'C:\\twtbot\\dataset\\{picture_object}'
    random_filename = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
    ])

    media = api.media_upload(f'dataset/{picture_object}/{random_filename}')

    api.update_status(status=f'This is a picture of "{picture_object}".', media_ids=[media.media_id_string])
    
    #print(wikipedia.summary({picture_object}))

    try:
        shutil.rmtree(f'C:\\twtbot\\dataset\\{picture_object}')
    except OSError as e:
        print("Error: %s : %s" % (f'C:\\twtbot\\dataset\\{picture_object}', e.strerror))


# while True:
#     time.sleep(5)
#     randomPicture(randomWord(), pictureAmount)
#     time.sleep(15)

randomPicture(randomWord(), pictureAmount)