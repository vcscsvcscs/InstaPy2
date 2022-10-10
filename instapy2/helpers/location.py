from instagrapi import Client

from typing import Union

class LocationHelper:
    def __init__(self, session: Client):
        self.session = session

    def get_pk(self, query: str) -> Union[int, str]:
        places = self.session.fbsearch_places(query=query)
        place_tuple = [(place.name, place.city, place.zip, place.pk) for place in places]

        for index, place in enumerate(iterable=place_tuple):
            name, city, zip, pk = place
            sel_string = ''
            if name is not None and name != '':
                sel_string += name
            if city is not None and city != '':
                sel_string += f', {city}'
            if zip is not None and zip != '':
                sel_string += f', {zip}'
            print(f'[INFO]: {index + 1}: {sel_string}')


        selection = int(input(f'Enter the index for the correct location (1-{len(place_tuple)}): '))
        if 1 <= selection <= len(places):
            name, city, zip, pk = place_tuple[selection - 1]
            return pk
        else:
            return f'[ERROR]: Selection is invalid. Please choose between 1-{len(places)}.'