import random


def format_team_name_for_tweet(name: str) -> str:
    formated_name = ''.join(e for e in name if e.isalnum())
    return formated_name


def random_team(teams_file: str) -> str:
    teams = open(teams_file).read().splitlines()
    team = random.choice(teams)
    return team
