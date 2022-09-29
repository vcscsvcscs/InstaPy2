from instagrapi import Client

from .comment_util import CommentUtil
from .database import InstaPy2DB
from .follow_util import FollowUtil
from .like_util import LikeUtil

import os

class InstaPy2Base:
    def  __init__(self, username: str = None, password: str = None):
        working_directory = os.getcwd()

        self.client = Client()
        if os.path.isfile(path=f'{working_directory}/settings.json'):
            self.client.load_settings(path=f'{working_directory}/settings.json')
        else:
            self.client.login(username=username, password=password)
            self.client.dump_settings(path=f'{working_directory}/settings.json')

        # utilities
        self.comment_util = CommentUtil(session=self.client, username=username)
        self.database = InstaPy2DB(database='database.db')
        self.follow_util = FollowUtil(session=self.client)
        self.like_util = LikeUtil(session=self.client)

        self.limit_liking = False
        self.min_likes = 0
        self.max_likes = 1000

        self.comments = []
        self.can_comment = False
        self.can_comment_on_liked_media = False
        self.comment_percentage = 0
        self.limit_commenting = False
        self.min_comments = 0
        self.max_comments = 35

        self.follow_times = 1
        self.can_follow = False
        self.follow_percentage = 0

        self.commenting_mandatory_words = []
        self.friends_to_skip = []
        self.hashtags_or_phrases_to_skip = []
        self.mandatory_hashtags_or_phrases = []

    # configuration options
    # main
    def set_limit_for_liking(self, enabled: bool = False, min_likes: int = 0, max_likes: int = 1000):
        self.limit_liking = enabled
        self.min_likes = min_likes
        self.max_likes = max_likes

    def set_hashtags_or_phrases_to_skip(self, tags: list[str] = []):
        self.hashtags_or_phrases_to_skip = tags

    def set_mandatory_hashtags_or_phrases(self, tags: list[str] = []):
        self.mandatory_hashtags_or_phrases = tags

    # commenting
    def set_limit_for_commenting(self, enabled: bool = False, min_comments: int = 0, max_comments: int = 35, commenting_mandatory_words: list[str] = []):
        self.limit_commenting = enabled
        self.min_comments = min_comments
        self.max_comments = max_comments
        self.commenting_mandatory_words = commenting_mandatory_words

    def set_can_comment(self, enabled: bool = False, comment_on_liked_media: bool = False, percentage: int = 0):
        self.can_comment = enabled
        self.can_comment_on_liked_media = comment_on_liked_media
        self.comment_percentage = percentage

    def set_comments(self, comments: list[str] = []):
        self.comments = comments

    # following
    def set_can_follow(self, enabled: bool = False, percentage: int = 0, times: int = 1):
        self.can_follow = enabled
        self.follow_percentage = percentage
        self.follow_times = times

    def set_friends_to_skip(self, usernames: list[str] = []):
        self.friends_to_skip = usernames