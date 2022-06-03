import tweepy

api_key = 'YOBqmX4Zj2L6kpZuqrJ7b2kZc'
api_key_secret = 'hORcrDHdf0LI7LE2Oy1qGmTR7cZOFdz3ZbU1ec6A2assoKBYze'
access_token = '1532676880645636096-t4sNJ5iTVyaAjIUyuJkrmnCydyuyC5'
access_token_secret = 'maM0GCCGxZMt8o1lv0jXaeoslYzgF82QM0yL2LGyrPJab'


def setup():
    authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
    authenticator.set_access_token(access_token, access_token_secret)
    api = tweepy.API(authenticator, wait_on_rate_limit=True)
    return api