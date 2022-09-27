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
        # if media_type is None:
        #     media_type = [MediaType.Carousel, MediaType.Clip, MediaType.IGTV, MediaType.Photo, MediaType.Video]
        # elif media_type is MediaType.Photo:
        #     media_type = [MediaType.Carousel, MediaType.Carousel]
        # else:
        #     media_type = [media_type]

        tag = tag[1:] if tag[:1] == '#' else tag
        links = []

        links += self.session.hashtag_medias_top(name=tag)
        links += self.session.hashtag_medias_recent(name=tag, amount=amount)

        if skip_top_posts:
            del links[0:9]

        if randomize:
            shuffle(links)

        return links[:amount]

    # check if media is viable for interaction
    def has_already_liked_media(self, media: Media = None) -> bool:
        return media.has_liked

    def media_contains_friend(self, media: Media = None, usernames: list[str] = []) -> bool:
        username = media.user.username
        return any(friend in username for friend in usernames)

    def media_contains_mandatory_hashtags_or_phrases(self, media: Media = None, hashtags_or_phrases: list[str] = []) -> bool:
        return True if len(hashtags_or_phrases) == 0 else any(hashtag_or_phrase in media.caption_text for hashtag_or_phrase in hashtags_or_phrases)

    def media_contains_hashtags_or_phrases_to_skip(self, media: Media = None, hashtags_or_phrases: list[str] = []) -> bool:
        return False if len(hashtags_or_phrases) == 0 else any(hashtag_or_phrase in media.caption_text for hashtag_or_phrase in hashtags_or_phrases)