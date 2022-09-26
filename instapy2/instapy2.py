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

    def like_by_tags(self, tags: list[str] = None, use_random_tags: bool = False, amount: int = 50, skip_top_posts: bool = True, interact: bool = False, randomize: bool = False, media_type: MediaType = None):
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

            links = LikeUtil(session=self.client).get_medias_for_tag(tag=tag, amount=amount, skip_top_posts=skip_top_posts, randomize=randomize, media_type=media_type)
            print(f'Found: {len(links)} links for {tag}')