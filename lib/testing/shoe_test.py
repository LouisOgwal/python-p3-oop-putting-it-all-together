import pytest
from shoe import Shoe

def test_requires_int_size():
    '''raises ValueError if size is not an integer.'''
    shoe = Shoe("Adidas", 9)
    with pytest.raises(ValueError, match="size must be an integer"):
        shoe.size = "not an integer"