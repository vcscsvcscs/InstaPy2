from .instapy2_base import InstaPy2Base

from typing import List

import random

class InstaPy2(InstaPy2Base):
    def like(self, amount: int = 50, tags: List[str] = [], randomize_media: bool = False, randomize_tags: bool = False, skip_top: bool = True):
        tags = [tag.strip() for tag in tags] or []
        
        if randomize_tags:
            random.shuffle(x=tags)

        for index, tag in enumerate(iterable=tags):
            print(f'[INFO]: Tag [{index + 1}/{len(tags)}]')
            print(f'[INFO]: {tag}')

            medias = self.medias(amount=amount, tag=tag, randomize_media=randomize_media, skip_top=skip_top)
            print(f'[INFO]: Found {len(medias)} media from {[media.user.username for media in medias]}.')

            for index, media in enumerate(iterable=medias):
                if self.configuration.media.validated_for_interaction(media=media):
                    liked = self.session.media_like(media_id=media.id)
                    print(f'[INFO]: Successfully liked media: {media.code}' if liked else f'[ERROR]: Failed to like media.')

                    if liked or self.configuration.comments.enabled_for_liked_media:
                        if (self.configuration.follows.enabled and random.randint(0, 100) <= self.configuration.comments.percentage):
                            if (media.user.username not in self.configuration.people.friends_to_skip):
                                # we can comment, wow
                                commented = self.session.media_comment(media_id=media.id, text=random.choice(seq=self.configuration.comments.comments))
                                print(f'[INFO]: Successfully commented on media: {media.code}' if commented is not None else f'[ERROR]: Failed to comment on media.')

                        user_followers = self.session.user_followers(user_id=self.session.user_id_from_username(username=media.user.username)) # used to check if we already follow
                        if (self.configuration.follows.enabled and random.randint(0, 100) <= self.configuration.follows.percentage) and self.session.user_id not in user_followers.keys():
                            if (media.user.username not in self.configuration.people.friends_to_skip):
                                followed = self.session.user_follow(user_id=self.session.user_id_from_username(username=media.user.username))
                                print(f'[INFO]: Successfully followed: {media.user.username}' if followed else f'[ERROR]: Failed to follow user.')