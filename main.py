#from bing_image_downloader import downloader
import random
import shutil
import os
import time
import wikipedia
import re
import config
import gidl

api = config.setup()

pictureAmount = 3



def randomWord():
    with open("words.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
        random_word = random.choice(words)
        return random_word

def make_random_friendship():
    for user in api.search_users(q=randomWord(), count=20):
        api.create_friendship(user_id=user.id_str)
        print(f'Made friendship with user id: {user.id_str}')
        time.sleep(0.1)

def randomPicture(picture_object):

    picture_object = re.sub('\W+',' ', picture_object)
    print(f'Looking for: {picture_object}')

    #downloader.download(f'{picture_object}', limit=random_from_amount, output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=10)
    gidl.downloadimages(f'{picture_object}')
    
    path = f'C:\\twtbot\\downloads\\img'
    random_filename = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
    ])

    media = api.media_upload(f'downloads/img/{random_filename}')

    try:
        summary = wikipedia.summary(picture_object, sentences=2)
    except wikipedia.exceptions.PageError:
        summary = "Couldn't find info on wiki for this one!"
    except wikipedia.exceptions.DisambiguationError as e:
        sub_search = e.options[0]
        summary = wikipedia.summary(sub_search, sentences=2)

    if len(summary) > 267 - len(picture_object):
        summary = wikipedia.summary(picture_object, sentences=1)
        if len(summary) > 267 - len(picture_object):
            summary = ""

    api.update_status(status=f'This is: "{picture_object}." '+ f'{summary}', media_ids=[media.media_id_string])

    try:
        shutil.rmtree(f'C:\\twtbot\\downloads\\img')
    except OSError as e:
        print("Error: %s : %s" % (f'C:\\twtbot\\downloads\\img', e.strerror))


    print(f'Picture object: {picture_object}')
    print(f'Tweet posted succesfully!')



while True:
    try:
        randomPicture(wikipedia.random(pages=1))
        # try:
        #     make_random_friendship()
        # except:
        #     pass
        time.sleep(300)
    except KeyboardInterrupt:
        break
    except:
        pass

