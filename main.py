import tweepy
import secrets
from general import format_team_name_for_tweet


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
    selected_team = 'São Paulo'
    media = api.media_upload(filename=f'logos/{selected_team}.png')
    media_id = media.media_id

    formated_name = format_team_name_for_tweet(
        name=selected_team
    )
    client.create_tweet(text=f'Love for #{formated_name}', media_ids=[media_id, ])


def tweet(api: tweepy.API, message: str, image_path: str):
    api.update_status_with_media(message, image_path)


twitter_auth()
