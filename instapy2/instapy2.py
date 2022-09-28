from .comment_util import CommentUtil
from .database import InstaPy2DB
from .like_util import LikeUtil
from .media_type import MediaType
from .media_util import MediaUtil

from instagrapi.types import Media
from random import shuffle

import instagrapi, os

class InstaPy2:
    def  __init__(self, username: str = None, password: str = None):
        working_directory = os.getcwd()

        self.client = instagrapi.Client()
        if os.path.isfile(path=f'{working_directory}/settings.json'):
            self.client.load_settings(path=f'{working_directory}/settings.json')
        else:
            self.client.login(username=username, password=password)
            self.client.dump_settings(path=f'{working_directory}/settings.json')

        # utilities
        self.comment_util = CommentUtil(session=self.client, username=username)
        self.database = InstaPy2DB(database='database.db')
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

        self.commenting_mandatory_words = []
        self.friends_to_skip = []
        self.hashtags_or_phrases_to_skip = []
        self.mandatory_hashtags_or_phrases = []


    def like_by_tags(self, tags: list[str] = [], use_random_tags: bool = False, amount: int = 50, skip_top_posts: bool = True, interact: bool = False, randomize: bool = False, media_type: MediaType = None):
        if tags is None:
            return

        tags = [tag.strip() for tag in tags]
        tags = tags or []

        if use_random_tags:
            shuffle(x=tags)

            for index, tag in enumerate(iterable=tags):
                print(f'Tag list randomized: [{index + 1}/{len(tags)}/{tag}]')
        
        for index, tag in enumerate(iterable=tags):
            print(f'Tag [{index + 1}/{len(tags)}]')
            print(f'--> {tag}')

            medias = self.like_util.get_medias_for_tag(tag=tag, amount=amount, skip_top_posts=skip_top_posts, randomize=randomize, media_type=media_type)
            total = 'media' if len(medias) == 1 else 'medias'
            print(f'Found: {len(medias)} {total} for {tag}')

            for index, media in enumerate(iterable=medias):
                passes_all_checks, log = MediaUtil(usernames=self.friends_to_skip, mandatory_hashtags_or_phrases=self.mandatory_hashtags_or_phrases, hashtags_or_phrases_to_skip=self.hashtags_or_phrases_to_skip).media_passes_all_checks(media=media, comment_util=self.comment_util, like_util=self.like_util)
                print(log)
                if passes_all_checks:
                    did_like = self.like_util.like_media(media=media)

                    print(f'[INFO]: Successfully liked media: {media.code}' if did_like else f'[ERROR]: Failed to like media: {media.code}')

                    if did_like or self.can_comment_on_liked_media:
                        if not self.comment_util.has_commented_on_media(media=media) and self.can_comment:
                            if self.comment_util.media_contains_mandatory_words(media=media, words=self.commenting_mandatory_words):
                                comment = self.comment_util.get_comment_from_comments(comments=self.comments).format(media.user.username)
                                print(f'[INFO]: Successfully commented on media: {media.code}' if self.comment_util.comment_on_media(media=media, comment=comment) else f'[ERROR]: Failed to comment on media: {media.code}')
                        else:
                            print('[ERROR]: Media has already been commented on.')
                
    
    
    # start configurations
    def set_friends_to_skip(self, usernames: list[str] = []):
        self.friends_to_skip = usernames

    def set_limit_for_liking(self, enabled: bool = False, min_likes: int = 0, max_likes: int = 1000):
        self.limit_liking = enabled
        self.min_likes = min_likes
        self.max_likes = max_likes

    def set_hashtags_or_phrases_to_skip(self, tags: list[str] = []):
        self.hashtags_or_phrases_to_skip = tags

    def set_mandatory_hashtags_or_phrases(self, tags: list[str] = []):
        self.mandatory_hashtags_or_phrases = tags


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