from .instapy2_base import InstaPy2Base
from .media_type import MediaType
from .media_util import MediaUtil

from instagrapi.types import Media
from random import randint, shuffle

class InstaPy2(InstaPy2Base):
    def like_by_tags(self, tags: list[str] = [], use_random_tags: bool = False, amount: int = 50, skip_top_posts: bool = True, interact: bool = False, randomize: bool = False, media_type: MediaType = None):
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

            medias = self.like_util.get_medias_for_tag(tag=tag, amount=amount, skip_top_posts=skip_top_posts, randomize=randomize, media_type=media_type)
            total = 'media' if len(medias) == 1 else 'medias'
            print(f'Found: {len(medias)} {total} for {tag}')

            for index, media in enumerate(iterable=medias):
                passes_all_checks, log = MediaUtil(usernames=self.friends_to_skip, mandatory_hashtags_or_phrases=self.mandatory_hashtags_or_phrases, hashtags_or_phrases_to_skip=self.hashtags_or_phrases_to_skip).media_passes_all_checks(media=media, comment_util=self.comment_util, like_util=self.like_util)
                if passes_all_checks:
                    # like
                    did_like = self.like_util.like_media(media=media)

                    print(f'[INFO]: Successfully liked media: {media.code}' if did_like else f'[ERROR]: InstaPy2.like_by_tags: Failed to like media: {media.code}')

                    # comment
                    commenting = (randint(0, 100) <= self.comment_percentage)
                    if (did_like or self.can_comment_on_liked_media) and commenting:
                        if not self.comment_util.has_commented_on_media(media=media) and self.can_comment:
                            if self.comment_util.media_contains_mandatory_words(media=media, words=self.commenting_mandatory_words):
                                comment = self.comment_util.get_comment_from_comments(comments=self.comments).format(media.user.username)
                                print(f'[INFO]: Successfully commented on media: {media.code}' if self.comment_util.comment_on_media(media=media, comment=comment) else f'[ERROR]: InstaPy2.like_by_tags: Failed to comment on media: {media.code}')
                        else:
                            print('[ERROR]: InstaPy2.like_by_tags: Media has already been commented on or comment_percentage does not fall within the commenting range.')
                
                    # follow
                    following = (randint(0, 100) <= self.follow_percentage)
                    if (following or self.can_follow) and self.follow_util.can_follow_user(media=media, friends_to_skip=self.friends_to_skip):
                        print(f'[INFO]: Successfully followed user: @{media.user.username}' if self.follow_util.follow_user(user=media.user) else f'[ERROR]: Failed to follow user: @{media.user.username}')
                    else:
                        print('[ERROR]: InstaPy2.like_by_tags: follow_percentage does not fall within the following range.')

                    # interactions
                    # incomplete