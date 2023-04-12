import tweepy
import secrets


def twitter_auth():
    client = tweepy.Client(
        consumer_key=secrets.APIKEY,
        consumer_secret=secrets.APIKEY_SECERET,
        access_token=secrets.ACCESS_TOKEN,
        access_token_secret=secrets.ACCESS_TOKEN_SECRET
    )

    auth = tweepy.OAuthHandler(
        consumer_key=secrets.APIKEY,
        consumer_secret=secrets.APIKEY_SECERET
    )
    auth.set_access_token(
        key=secrets.ACCESS_TOKEN,
        secret=secrets.ACCESS_TOKEN_SECRET
    )
    api = tweepy.API(auth)
    media = api.media_upload(filename='logos/Santos.jpg')

    media_id = media.media_id
    client.create_tweet(text='Love for #Santos', media_ids=[media_id, ])


def tweet(api: tweepy.API, message: str, image_path: str):
    api.update_status_with_media(message, image_path)


twitter_auth()
