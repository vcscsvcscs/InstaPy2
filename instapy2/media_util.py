from .comment_util import CommentUtil
from .like_util import LikeUtil

from instagrapi.types import Media

class MediaUtil:
    def __init__(self, usernames: str = None, mandatory_hashtags_or_phrases: str = None, hashtags_or_phrases_to_skip: str = None):
        self.usernames = usernames
        self.mandatory_hashtags_or_phrases = mandatory_hashtags_or_phrases
        self.hashtags_or_phrases_to_skip = hashtags_or_phrases_to_skip

    def media_passes_all_checks(self, media: Media = None, comment_util: CommentUtil = None, like_util: LikeUtil = None) -> tuple[bool, str]:
        if media is None or comment_util is None or like_util is None:
            return False, '[ERROR]: MediaUtil.media_passes_all_checks: media, comment_util or like_util is None'

        if like_util.media_contains_friend(media=media, usernames=self.usernames):
            return False, '[ERROR]: MediaUtil.media_passes_all_checks: Media contains a friend from the provided list'
        else:
            if like_util.media_contains_mandatory_hashtags_or_phrases(media=media, hashtags_or_phrases=self.mandatory_hashtags_or_phrases):
                if like_util.media_contains_hashtags_or_phrases_to_skip(media=media, hashtags_or_phrases=self.hashtags_or_phrases_to_skip):
                    return False, '[ERROR]: MediaUtil.media_passes_all_checks: Media contains a hashtag or phrase in the skippable list.'
                else:
                    return True, '[INFO]: MediaUtil.media_passes_all_checks: Media passed all checks.'
            else:
                return False, '[ERROR]: MediaUtil.media_passes_all_checks: Media does not contain all hashtags or phrases from the mandatory list.'