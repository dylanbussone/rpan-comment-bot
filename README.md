# rpan-comment-bot
Reddit bot to find your newest submission and add comments to it.

## Prerequisites
Install python3 and then install praw:
```
pip3 install praw
```

You will need to [create a reddit app](https://www.reddit.com/prefs/apps) and then add the OAuth2 credentials to these environment variables:
```
REDDIT_BOT_USER_AGENT
REDDIT_BOT_CLIENT_ID
REDDIT_BOT_CLIENT_SECRET
REDDIT_BOT_USERNAME
REDDIT_BOT_PASSWORD
```
## Usage

Edit the messages list and timeout duration in main.py with your desired messages and timeout. The messages will be posted in sequential order on loop.

Run with `python3 main.py`
