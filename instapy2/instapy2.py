from .like_util import LikeUtil
from .media_type import MediaType

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

        self.like_util = LikeUtil(session=self.client)
        self.limit_liking = False
        self.min_likes = 0
        self.max_likes = 1000

        self.hashtags_or_phrases_to_skip = []

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
            print(f'Found: {len(medias)} medias for {tag}')

            for index, media in enumerate(iterable=medias):
                is_valid = self.like_util.check_media(media=media, hashtags_and_phrases_to_skip=self.hashtags_or_phrases_to_skip) # check if caption ro comment contains any user set hashtags or phrases
                is_likeable = self.like_util.verify_is_likeable(media=media, min_likes=self.min_likes, max_likes=self.max_likes) # current like count is between user set limit

                if is_likeable and is_valid:
                    code = media.dict()['code']
                    print(f'Liked {code}: {self.like_util.like(media=media)}')
                else:
                    print(f'[ERROR]: InstaPy2.like_by_tags: Post could not be liked: [Likeable: {is_likeable}/Valid: {is_valid}]')

    def set_limit_for_liking(self, enabled: bool = False, min_likes: int = 0, max_likes: int = 1000):
        self.limit_liking = enabled
        self.min_likes = min_likes
        self.max_likes = max_likes

    def set_hashtags_or_phrases_to_skip(self, tags: list[str] = []):
        self.hashtags_or_phrases_to_skip = tags