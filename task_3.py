class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
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
                    self.flat_result.append(res)
            return self.flat_result
        self.flat_result = []
        flat(self.list_of_list)
        self.count = 0
        return self

    def __next__(self):
        if self.count > len(self.flat_result) - 1:
            raise StopIteration
        item = self.flat_result[self.count]
        self.count += 1
        return item


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()