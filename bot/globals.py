import os

def get_globals():
    global token
    global prefix

    info = {}

    info['props'] = {
        "token": os.environ.get("BOT_TOKEN"),
        "prefix": os.environ.get("BOT_PREFIX")
    }

    return info
