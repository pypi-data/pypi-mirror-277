# Import each module within the TiRank package
from .degpe import *
from .faq import *
from .homepage import *
from .others import *
from .preprocess import *
from .tirank import *
from .tutorial import *
from .upload import *

# Define an __all__ list that specifies all the modules you want to be imported when 'from TiRank import *' is used
__all__ = [
    'degpe', 
    'faq', 
    'homepage', 
    'others', 
    'preprocess', 
    'preprocess', 
    'tirank', 
    'tutorial', 
    'upload',
]
