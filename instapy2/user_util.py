from .media_product_type import MediaType, ProductType

from instagrapi import Client
from instagrapi.types import Media

class UserUtil:
    def __init__(self, session: Client):
        self.session = session

    def is_following_user(self, username: str = None) -> bool:
        return len(self.session.search_followers(user_id=self.session.user_id_from_username(username=username))) > 0

    def is_profile_private(self, username: str = None) -> bool:
        return self.session.user_info_by_username(username=username).is_private

    def user_media_count(self, username: str = None) -> int:
        return self.session.user_info_by_username(username=username).media_count

    def user_medias(self, username: str = None, amount: int = 10) -> list[Media]:
        return self.session.user_medias(user_id=self.session.user_id_from_username(username=username), amount=amount)

    def user_medias_filtered(self, username: str = None, amount: int = 10, media: MediaType = None) -> list[Media]:
        medias = []
        while len(medias) < amount:
            posts = self.user_medias(username=username, amount=amount)
            # filter posts to the MediaType and append to medias
            filtered = [post for post in posts if post.media_type == media]
            medias.append(filtered)
        return medias