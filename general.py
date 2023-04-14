def format_team_name_for_tweet(name: str) -> str:
    formated_name = ''.join(e for e in name if e.isalnum())
    return formated_name
