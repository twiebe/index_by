from index_by import index_by_key, index_by_key_as_list, index_by_keys, index_by_keys_as_list
import unittest


class TestIndexByKey(unittest.TestCase):
    def test_key_found(self):
        obj_list = [dict(key=0), dict(key=1), dict(key=2), dict(key=3)]
        index = index_by_key(obj_list, 'key')
        for i, obj in index.items():
            self.assertIs(obj, obj_list[i])

    def test_key_latest_persists(self):
        obj_list = [dict(key=0), dict(key=0), dict(key=0)]
        index = index_by_key(obj_list, 'key')
        self.assertIs(index[0], obj_list[-1])

    def test_key_not_found(self):
        obj_list = [dict(key=0)]
        with self.assertRaises(KeyError):
            index_by_key(obj_list, 'non_existing_key')


class TestIndexByKeyAsList(unittest.TestCase):
    def test_key_found(self):
        obj_list = [dict(key=0), dict(key=0), dict(key=1), dict(key=1)]
        index = index_by_key_as_list(obj_list, 'key')
        self.assertEqual(index[0], obj_list[0:2])
        self.assertEqual(index[1], obj_list[2:])


class TestIndexByKeys(unittest.TestCase):
    def test_key_found(self):
        obj_list = [
            dict(compound_key_one=0, compound_key_two=0),
            dict(compound_key_one=0, compound_key_two=1),
            dict(compound_key_one=1, compound_key_two=0),
            dict(compound_key_one=1, compound_key_two=1)]
        index = index_by_keys(obj_list, ('compound_key_one', 'compound_key_two'))
        self.assertIs(index[(0, 0)], obj_list[0])
        self.assertIs(index[(0, 1)], obj_list[1])
        self.assertIs(index[(1, 0)], obj_list[2])
        self.assertIs(index[(1, 1)], obj_list[3])

    def test_key_latest_persists(self):
        obj_list = [
            dict(compound_key_one=0, compound_key_two=0),
            dict(compound_key_one=0, compound_key_two=0),
            dict(compound_key_one=0, compound_key_two=0)]
        index = index_by_keys(obj_list, ('compound_key_one', 'compound_key_two'))
        self.assertIs(index[(0, 0)], obj_list[-1])

    def test_key_not_found_full(self):
        obj_list = [dict(compound_key_one=0, compound_key_two=0)]
        with self.assertRaises(KeyError):
            index_by_keys(obj_list, ('non_existing_key_one', 'non_existing_key_two'))

    def test_key_not_found_partial(self):
        obj_list = [dict(compound_key_one=0, compound_key_two=0)]
        with self.assertRaises(KeyError):
            index_by_keys(obj_list, ('compound_key_one', 'non_existing_key_two'))


class TestIndexByKeysAsList(unittest.TestCase):
    def test_key_found(self):
        obj_list = [
            dict(compound_key_one=0, compound_key_two=0),
            dict(compound_key_one=0, compound_key_two=0),
            dict(compound_key_one=1, compound_key_two=0),
            dict(compound_key_one=1, compound_key_two=0)
        ]
        index = index_by_keys_as_list(obj_list, ('compound_key_one', 'compound_key_two'))
        self.assertEqual(index[(0, 0)], obj_list[0:2])
        self.assertEqual(index[(1, 0)], obj_list[2:])


if __name__ == '__main__':
    unittest.main()
