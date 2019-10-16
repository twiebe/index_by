from index_by import index_by_attr, index_by_attr_as_list, index_by_attrs, index_by_attrs_as_list
import unittest


class AttributeObject:
    def __init__(self, key):
        self.key = key


class AttributesObject:
    def __init__(self, compound_key_one, compound_key_two):
        self.compound_key_one = compound_key_one
        self.compound_key_two = compound_key_two


class TestIndexByAttribute(unittest.TestCase):
    def test_attr_found(self):
        obj_list = [AttributeObject(0), AttributeObject(1), AttributeObject(2), AttributeObject(3)]
        index = index_by_attr(obj_list, 'key')
        for i, obj in index.items():
            self.assertIs(obj, obj_list[i])

    def test_attr_latest_persists(self):
        obj_list = [AttributeObject(0), AttributeObject(0), AttributeObject(0)]
        index = index_by_attr(obj_list, 'key')
        self.assertIs(index[0], obj_list[-1])

    def test_attr_not_found(self):
        obj_list = [AttributeObject(0)]
        with self.assertRaises(AttributeError):
            index_by_attr(obj_list, 'non_existing_key')


class TestIndexByAttributeAsList(unittest.TestCase):
    def test_attr_found(self):
        obj_list = [AttributeObject(0), AttributeObject(0), AttributeObject(1), AttributeObject(1)]
        index = index_by_attr_as_list(obj_list, 'key')
        self.assertEqual(index[0], obj_list[0:2])
        self.assertEqual(index[1], obj_list[2:])


class TestIndexByAttributes(unittest.TestCase):
    def test_attr_found(self):
        obj_list = [AttributesObject(0, 0), AttributesObject(0, 1), AttributesObject(1, 0), AttributesObject(1, 1)]
        index = index_by_attrs(obj_list, ('compound_key_one', 'compound_key_two'))
        self.assertIs(index[(0, 0)], obj_list[0])
        self.assertIs(index[(0, 1)], obj_list[1])
        self.assertIs(index[(1, 0)], obj_list[2])
        self.assertIs(index[(1, 1)], obj_list[3])

    def test_attr_latest_persists(self):
        obj_list = [AttributesObject(0, 0), AttributesObject(0, 0), AttributesObject(0, 0)]
        index = index_by_attrs(obj_list, ('compound_key_one', 'compound_key_two'))
        self.assertIs(index[(0, 0)], obj_list[-1])

    def test_attr_not_found_full(self):
        obj_list = [AttributesObject(0, 0)]
        with self.assertRaises(AttributeError):
            index_by_attrs(obj_list, ('non_existing_key_one', 'non_existing_key_two'))

    def test_attr_not_found_partial(self):
        obj_list = [AttributesObject(0, 0)]
        with self.assertRaises(AttributeError):
            index_by_attrs(obj_list, ('compound_key_one', 'non_existing_key_two'))


class TestIndexByAttributesAsList(unittest.TestCase):
    def test_attr_found(self):
        obj_list = [AttributesObject(0, 0), AttributesObject(0, 0), AttributesObject(1, 0), AttributesObject(1, 0)]
        index = index_by_attrs_as_list(obj_list, ('compound_key_one', 'compound_key_two'))
        self.assertEqual(index[(0, 0)], obj_list[0:2])
        self.assertEqual(index[(1, 0)], obj_list[2:])


if __name__ == '__main__':
    unittest.main()
