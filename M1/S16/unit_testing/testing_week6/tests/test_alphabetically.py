import pytest
from my_modules.alphabetically import sort_string

def test_sort_string_return_sorted_string_with_many_words():
    # Arrage
    string_100_words = (
    "Lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-sed-do-eiusmod-tempor-incididunt-ut-labore-et-dolore-magna-aliqua-"
    "Ut-enim-ad-minim-veniam-quis-nostrud-exercitation-ullamco-laboris-nisi-ut-aliquip-ex-ea-commodo-consequat-Duis-aute-irure-"
    "dolor-in-reprehenderit-in-voluptate-velit-esse-cillum-dolore-eu-fugiat-nulla-pariatur-Excepteur-sint-occaecat-cupidatat-non-"
    "proident-sunt-in-culpa-qui-officia-deserunt-mollit-anim-id-est-laborum"
)
    excepted_sort_string = (
    "ad adipiscing aliqua aliquip amet anim aute cillum commodo consectetur consequat culpa cupidatat deserunt do dolor dolor dolore dolore "
    "Duis ea eiusmod elit enim esse est et eu ex Excepteur exercitation fugiat id in in in incididunt ipsum irure labore laboris laborum Lorem magna " 
    "minim mollit nisi non nostrud nulla occaecat officia pariatur proident qui quis reprehenderit sed sint sit sunt tempor ullamco ut Ut ut velit " 
    "veniam voluptate"
)

    # Act
    sorted_string = sort_string(string_100_words)

    # Assert
    assert sorted_string == excepted_sort_string


def test_sort_string_return_sorted_string_with_few_words():
    # Arrage
    short_string = "house-dog-cat-tree-sun-moon-flower-river-sky-sea"
    excepted_sort_string = "cat dog flower house moon river sea sky sun tree"
   
    # Act
    sorted_string = sort_string(short_string)

    # Assert
    assert sorted_string == excepted_sort_string


def test_sort_string_return_None_with_empty_string():
    # Arrage
    string = ""

    # Act
    result = sort_string(string)
    # Assert
    assert result == ""