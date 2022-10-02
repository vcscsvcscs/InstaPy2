from instagrapi import Client
from instagrapi.types import Media

from emoji import demojize, emojize
from random import choice
from typing import Union

class CommentUtil:
    def __init__(self, session: Client, username: str):
        self.session = session
        self.username = username

    def has_commented_on_media(self, media: Media = None) -> bool:
        all_comments = self.session.media_comments(media_id=media.id, amount=0)
        return any(self.username in comment.user.username for comment in all_comments)

    def get_comment_from_comments(self, comments: list[str] = []) -> Union[None, str]:
        if len(comments) == 0:
            return None

        comment = choice(seq=comments)

        demoji_comment = demojize(string=comment)
        emoji_comment = emojize(string=demoji_comment)
        return emoji_comment

    def comment_on_media(self, media: Media = None, comment: str = None) -> bool:
        return self.session.media_comment(media_id=media.id, text=comment) is not None

    def media_contains_mandatory_words(self, media: Media = None, words: list[str] = []) -> bool:
        return True if len(words) == 0 else all(word in media.caption_text for word in words)