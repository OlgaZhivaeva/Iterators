import types


def flat_generator(list_of_list):
    def flat(some_list):
        result = iter(some_list)
        while True:
            try:
                res = next(result)
            except StopIteration:
                break
            if isinstance(res, list):
                flat(res)
            else:
                flat_result.append(res)
        return flat_result

    flat_result = []
    for item in flat(list_of_list):
        yield item



def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()

