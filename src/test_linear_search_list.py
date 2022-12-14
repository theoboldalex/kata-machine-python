from linear_search_list import linear_search

def test_linear_search_list():
    foo = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]
    assert linear_search(foo, 69) == True
    assert linear_search(foo, 1336) == False
    assert linear_search(foo, 69420) == True
    assert linear_search(foo, 69421) == False
    assert linear_search(foo, 1) == True
    assert linear_search(foo, 0) == False
