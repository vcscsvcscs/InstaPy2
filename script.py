from dotenv import load_dotenv
from instapy2 import InstaPy2

import os

load_dotenv()

session = InstaPy2(username=os.getenv(key='insta_username'), password=os.getenv(key='insta_password'))

# skips people you add to the list, perfect for skipping friends or less than desirable people (#fuckthem).
# session.set_friends_to_skip(usernames=[''])

# enable commenting on media
# session.set_can_comment(enabled=True, comment_on_liked_media=True, percentage=10)

# sets the comments to use, InstaPy2 will choose a random comment from the list, more comments means more variety.
# session.set_comments(comments=['']) # use @{} to tag the user of the post

# hashtags or phrases to skip, perfect for nsfw, sex, fuck, etc.
# session.set_hashtags_or_phrases_to_skip(tags=['ai', 'btech', 'fullstackdev'])

# NEW (as of v0.0.14)
# enable following of a user (times is unused currently).
session.set_can_follow(enabled=True, percentage=25, times=0)

# set with tags InstaPy2 will go through with the above configuration.
session.like_by_tags(tags=['python3'], amount=5, skip_top_posts=False)