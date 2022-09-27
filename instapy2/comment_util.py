from instagrapi import Client
from instagrapi.types import Media

class CommentUtil:
    def __init__(self, session: Client, username: str):
        self.session = session
        self.username = username

    def has_commented_on_media(self, media: Media = None) -> bool:
        all_comments = self.session.media_comments(media_id=media.id, amount=0)
        return any(self.username in comment.user.username for comment in all_comments)

    def media_contains_mandatory_words(self, media: Media = None, words: list[str] = []) -> bool:
        return True if len(words) == 0 else any(word in media.caption_text for word in words)