from insertion_sort_list import insertion_sort

def test_insertion_sort():
    arr = [9, 3, 7, 4, 69, 420, 42]
    insertion_sort(arr)

    assert arr == [3, 4, 7, 9, 42, 69, 420]
