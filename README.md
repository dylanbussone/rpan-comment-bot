# rpan-comment-bot
Reddit bot to find your newest submission and add comments to it.

## Prerequisites
```
pip install praw
```

## Usage
First you will need to create the following environment variables for your Reddit OAuth2 credentials:
```
REDDIT_BOT_USER_AGENT
REDDIT_BOT_CLIENT_ID
REDDIT_BOT_CLIENT_SECRET
REDDIT_BOT_USERNAME
REDDIT_BOT_PASSWORD
```

Then, edit the messages list and timeout duration with your desired messages and time between them. The messages will be posted in sequential order on loop.

Run with `python3 main.py`
