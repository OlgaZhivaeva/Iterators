import types


def flat_generator(list_of_lists):
    count_a = 0
    count_b = 0
    while True:
        if count_a > len(list_of_lists) - 1:
            break
        item = list_of_lists[count_a][count_b]
        if count_b < len(list_of_lists[count_a]) - 1:
            count_b += 1
        else:
            count_a += 1
            count_b = 0
        yield item





def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
