#!/usr/bin/env python3
import sys
import time
import os
import praw

messages = [
    'You should totally follow this guy on [Spotify](https://open.spotify.com/artist/1Op9vSnBgavICOjzdFpM3X) 💃',
    'Whoa! I\'m on [youtube](https://www.youtube.com/channel/UCkkAYSOwxBFpTaQc4_Y7WnA)',
    'Is [soundcloud](https://soundcloud.com/dylanbussone) still cool?',
    '🏄 Radical! Free downloads on [bandcamp](https://dylonious.bandcamp.com/)',
]
timeout = 3 * 60

reddit = praw.Reddit(
    user_agent=os.environ['REDDIT_BOT_USER_AGENT'],
    client_id=os.environ['REDDIT_BOT_CLIENT_ID'],
    client_secret=os.environ['REDDIT_BOT_CLIENT_SECRET'],
    username=os.environ['REDDIT_BOT_USERNAME'],
    password=os.environ['REDDIT_BOT_PASSWORD'],
)

new_posts = reddit.redditor(os.environ['REDDIT_BOT_USERNAME']).submissions.new()
for post in new_posts:
    if not post.pinned:
        print(f'Found post: {post.title}\n{post.url}\n')
        message_index = 0
        while True:
            print('Posting message')
            post.reply(messages[message_index % len(messages)])
            message_index += 1
            time.sleep(timeout)
