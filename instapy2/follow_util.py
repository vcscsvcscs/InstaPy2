from instagrapi import Client
from instagrapi.types import Media, UserShort

class FollowUtil:
    def __init__(self, session: Client):
        self.session = session

    def can_follow_user(self, media: Media = None, friends_to_skip: list[str] = []) -> bool:
        return not any(friend in media.user.username for friend in friends_to_skip)

    def follow_user(self, user: UserShort = None) -> bool:
        return self.session.user_follow(user_id=self.session.user_id_from_username(username=user.username))