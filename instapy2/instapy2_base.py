from .configuration import Configuration

from instagrapi import Client
from instagrapi.types import Media

from typing import List

import random, os

class InstaPy2Base:
    def __init__(self, username: str = None, password: str = None):
        if username is None:
            print('[ERROR]: Username has not been set.')
            return

        if password is None:
            print('[ERROR]: Password has not been set.')
            return

        self.session = Client()
        if os.path.exists(path=os.getcwd() + '/instapy2/files/settings.json'):
            self.session.load_settings(path=os.getcwd() + '/instapy2/files/settings.json')
            logged_in = self.session.login(username=username, password=password)
        else:
            logged_in = self.session.login(username=username, password=password)
            self.session.dump_settings(path=os.getcwd() + '/instapy2/files/settings.json')

        print(f'[INFO]: Successfully logged in as: {self.session.username}.' if logged_in else f'[ERROR]: Failed to log in.')
        self.configuration = Configuration()


    def medias(self, amount: int, tag: str, randomize_media: bool, skip_top: bool) -> List[Media]:
        medias = []
        if skip_top:
            while len(medias) < amount:
                medias += [media for media in self.session.hashtag_medias_recent(name=tag, amount=amount) if not any(username in media.user.username for username in self.configuration.people.users_to_skip)]
        else:
            medias += [media for media in self.session.hashtag_medias_top(name=tag) if not any(username in media.user.username for username in self.configuration.people.users_to_skip)]
            while len(medias) < amount:
                medias += [media for media in self.session.hashtag_medias_recent(name=tag, amount=amount - len(medias)) if not any(username in media.user.username for username in self.configuration.people.users_to_skip)]

        if randomize_media:
            random.shuffle(x=medias)

        return medias[:amount]