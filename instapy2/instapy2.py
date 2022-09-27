from .comment_util import CommentUtil
from .database import InstaPy2DB
from .like_util import LikeUtil
from .media_type import MediaType

from emoji import demojize, emojize
from instagrapi.types import Media
from random import choice, randint, random, shuffle

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
                if self.like_util.media_contains_friend(media=media, usernames=self.friends_to_skip):
                    print('[ERROR]: Media does contain a friend from the provided list. Skipping.')
                    pass
                else:
                    if self.like_util.media_contains_mandatory_hashtags_or_phrases(media=media, hashtags_or_phrases=self.mandatory_hashtags_or_phrases):
                        if self.like_util.media_contains_hashtags_or_phrases_to_skip(media=media, hashtags_or_phrases=self.hashtags_or_phrases_to_skip):
                            print('[ERROR]: Media does contain a hashtag or phrase to skip. Skipping.')
                            pass
                        else:
                            print(f'[INFO]: Succesfully liked {media.code}' if self.client.media_like(media_id=media.id) else f'[ERROR]: Failed to like {media.code}')

                            if self.can_comment:
                                should_comment_on_media = (randint(0, 100) <= self.comment_percentage)
                                print(should_comment_on_media)

                                if should_comment_on_media:
                                    if not self.comment_util.has_commented_on_media(media=media):
                                        if self.comment_util.media_contains_mandatory_words(media=media, words=self.commenting_mandatory_words):
                                            random_comment = choice(seq=self.comments).format(media.user.username)
                                            random_comment = demojize(string=random_comment)
                                            random_comment = emojize(string=random_comment)

                                            print(f'[ERROR]: Failed to comment on {media.code}' if self.client.media_comment(media_id=media.id, text=random_comment) is None else f'[INFO]: Successfully commented on {media.code}')
                                    else:
                                        print('[ERROR]: Media has already been commented on by user. Skipping.')
                    else:
                        print('[ERROR]: Media does not contain a mandatory hashtag or phrase. Skipping.')
                        pass
    
    
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