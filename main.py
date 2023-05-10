import tweepy
import secrets
from general import format_team_name_for_tweet, random_team
from constants import NUMBER_OF_POSTS


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

    return client, auth


def tweet(twitter_client: tweepy.Client, twitter_authorization: tweepy.OAuthHandler):
    api = tweepy.API(twitter_authorization)
    tweeted_teams = []
    posts = 0

    while posts < NUMBER_OF_POSTS:
        selected_team = random_team(teams_file='teams.txt')
        if selected_team not in tweeted_teams:
            print(f'Tweeting about {selected_team}')

            # Upload team logo
            media = api.media_upload(filename=f'logos/{selected_team}.png')
            media_id = media.media_id

            # Format team name for hashtag
            formated_name = format_team_name_for_tweet(
                name=selected_team
            )

            # Create tweet
            try:
                twitter_client.create_tweet(text=f'Love for #{formated_name}', media_ids=[media_id, ])

                # Handle tweets control to not tweet a team twice
                tweeted_teams.append(selected_team)
                posts += 1
            except FileNotFoundError:
                # In case of an error, the number of posts is not increased
                pass


if __name__ == "__main__":
    my_client, my_auth = twitter_auth()
    tweet(
        twitter_client=my_client,
        twitter_authorization=my_auth
    )
