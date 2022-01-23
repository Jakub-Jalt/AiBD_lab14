import pytest
from BubbleSort import bubble_sort

list1 = [3, 1, 5, 2, 9, 12, 4, 8, 14, 10]
ans1 = [1, 2, 3, 4, 5, 8, 9, 10, 12, 14]
test_data = [(list1, ans1)]


@pytest.mark.parametrize('list, ans', test_data)
def test_sorting(list, ans):
    got = bubble_sort(list)
    want = ans
    assert got == want




