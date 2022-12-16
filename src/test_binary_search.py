from binary_search_list import binary_search

def test_binary_search_list():
    foo = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]
    assert binary_search(foo, 69) == True
    assert binary_search(foo, 1336) == False
    assert binary_search(foo, 69420) == True
    assert binary_search(foo, 69421) == False
    assert binary_search(foo, 0) == True
    assert binary_search(foo, 1) == False
