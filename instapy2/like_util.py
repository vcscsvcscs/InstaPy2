from instagrapi import Client
from instagrapi.types import Media
from .media_type import MediaType

from random import shuffle

class LikeUtil:
    def __init__(self, session: Client):
        self.session = session

    def get_medias_for_tag(self, tag: str, amount: int, skip_top_posts: bool, randomize: bool, media_type: MediaType) -> list[Media]:
        # media_type is unused currently
        if media_type is None:
            media_type = [MediaType.Carousel, MediaType.Clip, MediaType.IGTV, MediaType.Photo, MediaType.Video]
        elif media_type is MediaType.Photo:
            media_type = [MediaType.Carousel, MediaType.Carousel]
        else:
            media_type = [media_type]

        tag = tag[1:] if tag[:1] == '#' else tag
        links = []

        links += self.session.hashtag_medias_top(name=tag)
        links += self.session.hashtag_medias_recent(name=tag, amount=amount)

        if skip_top_posts:
            del links[0:9]

        if randomize:
            shuffle(links)

        return links[:amount]