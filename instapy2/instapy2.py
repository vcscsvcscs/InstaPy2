from .instapy2_base import InstaPy2Base

from typing import List

import random

class InstaPy2(InstaPy2Base):
    # MARK: follow users by locations
    def follow_locations(self, amount: int = 50, locations: List[int] = [], randomize_media: bool = False, skip_top: bool = True):
        followed_count = 0
        for index, location in enumerate(iterable=locations):
            print(f'[INFO]: Location [{index + 1}/{len(locations)}]')
            print(f'[INFO]: {location}')

            location_info = self.session.location_info(location_pk=location)
            location_name = location_info.name if location_info.name is not None else 'Unavailable'

            medias = self.medias_location(amount=amount, location=location_info.pk, randomize_media=randomize_media, skip_top=skip_top)
            print(f'[INFO]: Found {len(medias)} media from {location_name}.')

            for index, media in enumerate(iterable=medias):
                if self.configuration.media.validated_for_interaction(media=media):
                    user_id = self.session.user_id_from_username(username=media.user.username)
                    relationship_status = self.session.user_friendship_v1(user_id=user_id)
                    if not relationship_status.following:
                        followed = self.session.user_follow(user_id=self.session.user_id_from_username(username=media.user.username))
                        print(f'[INFO]: Successfully followed: {media.user.username}' if followed else f'[ERROR]: Failed to follow user.')

                        if followed:
                            followed_count += 1

        print(f'[INFO]: Followed {followed_count} of {len(medias)} users.')

    def follow_tags(self, amount: int = 50, tags: List[str] = [], randomize_media: bool = False, randomize_tags: bool = False, skip_top: bool = True):
        followed_count = 0
        tags = [tag.strip() for tag in tags] or []
        
        if randomize_tags:
            random.shuffle(x=tags)

        for index, tag in enumerate(iterable=tags):
            print(f'[INFO]: Tag [{index + 1}/{len(tags)}]')
            print(f'[INFO]: {tag}')

            medias = self.medias_tag(amount=amount, tag=tag, randomize_media=randomize_media, skip_top=skip_top)
            print(f'[INFO]: Found {len(medias)} media from {[media.user.username for media in medias]}.')

            for index, media in enumerate(iterable=medias):
                if self.configuration.media.validated_for_interaction(media=media):
                    user_id = self.session.user_id_from_username(username=media.user.username)
                    relationship_status = self.session.user_friendship_v1(user_id=user_id)

                    if (random.randint(0, 100) <= self.configuration.follows.percentage) and not relationship_status.following:
                        followed = self.session.user_follow(user_id=self.session.user_id_from_username(username=media.user.username))
                        print(f'[INFO]: Successfully followed: {media.user.username}' if followed else f'[ERROR]: Failed to follow user.')

                        if followed:
                            followed_count += 1

        print(f'[INFO]: Followed {followed_count} of {len(medias)} users.')

    # MARK: follow users by usernames
    def follow_usernames(self, usernames: List[str] = []):
        followed_count = 0
        for index, username in enumerate(iterable=usernames):
            print(f'[INFO]: Username [{index + 1}/{len(usernames)}]')
            print(f'[INFO]: {username}')

            user_id = self.session.user_id_from_username(username=username)
            relationship_status = self.session.user_friendship_v1(user_id=user_id)
            if not relationship_status.following:
                followed = self.session.user_follow(user_id=user_id)
                print(f'[INFO]: Successfully followed user: {username}' if followed else f'[ERROR]: Failed to follow user: {username}.')
                if followed:
                    followed_count += 1
            else:
                print('[INFO]: Already following.')

        print(f'[INFO]: Followed {followed_count} of {len(usernames)} users.')

    def unfollow_usernames(self, amount: int = 10, usernames: List[str] = [], only_nonfollowers: bool = False, randomize_usernames: bool = False):
        user_ids = []
        [user_ids.append(user_id) for user_id in self.session.user_following(user_id=self.session.user_id, amount=amount)] if len(usernames) == 0 else [user_ids.append(self.session.user_id_from_username(username=username)) for username in usernames]

        if randomize_usernames:
            random.shuffle(x=user_ids)

        for index, user_id in enumerate(iterable=user_ids):
            print(f'[INFO]: Username [{index + 1}/{len(user_ids)}]')
            print(f'[INFO]: {self.session.username_from_user_id(user_id=user_id)}')

            if only_nonfollowers:
                if not self.session.user_friendship_v1(user_id=user_id).followed_by:
                    self.session.user_unfollow(user_id=user_id)
            else:
                self.session.user_unfollow(user_id=user_id)

    # MARK: Like media by hashtag
    def like_tags(self, amount: int = 50, tags: List[str] = [], randomize_media: bool = False, randomize_tags: bool = False, skip_top: bool = True):
        tags = [tag.strip() for tag in tags] or []
        
        if randomize_tags:
            random.shuffle(x=tags)

        for index, tag in enumerate(iterable=tags):
            print(f'[INFO]: Tag [{index + 1}/{len(tags)}]')
            print(f'[INFO]: {tag}')

            medias = self.medias_tag(amount=amount, tag=tag, randomize_media=randomize_media, skip_top=skip_top)
            print(f'[INFO]: Found {len(medias)} media from {[media.user.username for media in medias]}.')

            for index, media in enumerate(iterable=medias):
                if self.configuration.media.validated_for_interaction(media=media):
                    liked = self.session.media_like(media_id=media.id)
                    print(f'[INFO]: Successfully liked media: {media.code}' if liked else f'[ERROR]: Failed to like media.')

                    if liked or self.configuration.comments.enabled_for_liked_media:
                        if (self.configuration.follows.enabled and random.randint(0, 100) <= self.configuration.comments.percentage):
                            if (media.user.username not in self.configuration.people.friends_to_skip):
                                commented = self.session.media_comment(media_id=media.id, text=random.choice(seq=self.configuration.comments.comments))
                                print(f'[INFO]: Successfully commented on media: {media.code}' if commented is not None else f'[ERROR]: Failed to comment on media.')

                        user_id = self.session.user_id_from_username(username=media.user.username)
                        relationship_status = self.session.user_friendship_v1(user_id=user_id)
                        if (self.configuration.follows.enabled and random.randint(0, 100) <= self.configuration.follows.percentage) and not relationship_status.following:
                            if (media.user.username not in self.configuration.people.friends_to_skip):
                                followed = self.session.user_follow(user_id=self.session.user_id_from_username(username=media.user.username))
                                print(f'[INFO]: Successfully followed: {media.user.username}' if followed else f'[ERROR]: Failed to follow user.')