from instagrapi import Client
from instagrapi.types import Media, UserShort

from typing import Union

class FollowUtil:
    def __init__(self, session: Client):
        self.session = session

    def can_follow_user(self, media: Union[Media, str] = None, friends_to_skip: list[str] = []) -> bool:
        return not any(friend in (media.user.username if isinstance(media, Media) else media) for friend in friends_to_skip) # does this work?

    def follow_user(self, user: Union[UserShort, str] = None) -> bool:
        return self.session.user_follow(user_id=self.session.user_id_from_username(username=user.username if isinstance(user, UserShort) else user)) # does this work?