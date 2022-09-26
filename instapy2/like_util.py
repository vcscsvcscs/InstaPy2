from instagrapi import Client
from instagrapi.types import Media
from .media_type import MediaType

from random import shuffle

import re

class LikeUtil:
    def __init__(self, session: Client):
        self.session = session

    def get_medias_for_tag(self, tag: str = None, amount: int = 50, skip_top_posts: bool = False, randomize: bool = False, media_type: MediaType = None) -> list[Media]:
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

    def check_media(self, media: Media = None, hashtags_and_phrases_to_skip: list[str] = []) -> bool:
        media_dict = self.session.media_info(media_pk=media.pk).dict()
        caption_text = media_dict['caption_text']

        contains_word = False
        for hapict in hashtags_and_phrases_to_skip:
            if re.compile(pattern=hapict).search(string=caption_text) is not None:
                contains_word = True

        return not contains_word


    def verify_is_likeable(self, media: Media = None, min_likes: int = 0, max_likes: int = 1000) -> bool:
        if media.has_liked:
            return False

        return min_likes <= media.like_count <= max_likes

    def like(self, media: Media = None) -> bool:
        return self.session.media_like(media_id=media.id)