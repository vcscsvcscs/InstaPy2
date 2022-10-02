from enum import Enum

class MediaType(Enum):
    Album = 8,
    IGTV = 2,
    Photo = 1
    Reel = 2
    Video = 2

class ProductType(Enum):
    IGTV = 'igtv'
    Reel = 'clips'
    Video = 'feed'