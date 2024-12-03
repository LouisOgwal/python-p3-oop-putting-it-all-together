import pytest
from book import Book

def test_requires_int_page_count():
    '''raises ValueError if page_count is not an integer.'''
    book = Book("And Then There Were None", 272)
    with pytest.raises(ValueError, match="page_count must be an integer"):
        book.page_count = "not an integer"