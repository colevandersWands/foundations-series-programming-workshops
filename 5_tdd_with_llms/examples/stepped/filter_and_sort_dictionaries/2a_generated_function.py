import unittest


def f(lst, key):
    if not isinstance(lst, list):
        raise AssertionError("Input should be a list")

    if not isinstance(key, str):
        raise AssertionError("Key should be a string")

    filtered_list = [d for d in lst if isinstance(d, dict) and key in d]
    sorted_list = sorted(filtered_list, key=lambda x: x[key])

    return sorted_list


class TestFilterAndSort(unittest.TestCase):
    """A test suite for filtering and sorting a list of dicts"""

    def test_emtpy_list(self):
        """Test case 1: Empty list"""
        lst = []
        result = f(lst, "a")
        expected = []
        self.assertEqual(result, expected)

    def test_list_with_one_dictionary(self):
        """Test case 2: List with one dictionary"""
        lst = [{"a": "z"}]
        result = f(lst, "a")
        expected = [{"a": "z"}]
        self.assertEqual(result, expected)

    def test_many_dicts_same_key(self):
        """Test case 3: List with multiple dictionaries, all having the same key"""
        lst = [{"a": "z"}, {"a": "y"}, {"a": "x"}]
        result = f(lst, "a")
        expected = [{"a": "x"}, {"a": "y"}, {"a": "z"}]
        self.assertEqual(result, expected)

    def test_many_dicts_some_shared_keys(self):
        """Test case 4: List with multiple dictionaries, some missing the key"""
        lst = [{"a": "z"}, {"b": "y"}, {"a": "x"}]
        result = f(lst, "a")
        expected = [{"a": "x"}, {"a": "z"}]
        self.assertEqual(result, expected)

    def test_many_dicts_no_shared_keys(self):
        """Test case 5: List with dictionaries having different keys"""
        lst = [{"a": "z"}, {"b": "y"}, {"c": "x"}]
        result = f(lst, "a")
        expected = [{"a": "z"}]
        self.assertEqual(result, expected)

    def test_dicts_with_non_string_keys(self):
        """Test case 6: List with dictionaries having non-string values for the key"""
        lst = [{"a": 1}, {"a": True}, {"a": "x"}]
        with self.assertRaises(AssertionError):
            f(lst, "a")

    def test_dicts_with_other_non_string_keys(self):
        """Test case 7: List with dictionaries having non-string values for other keys"""
        lst = [{"a": "z"}, {"b": 1}, {"c": True}]
        with self.assertRaises(AssertionError):
            f(lst, "a")

    def test_list_with_non_dict_elements(self):
        """Test case 8: List with dictionaries having non-dict elements"""
        lst = [{"a": "z"}, "b", {"a": "x"}]
        with self.assertRaises(AssertionError):
            f(lst, "a")

    def test_dicts_with_all_different_keys(self):
        """Test case 9: List with dictionaries having different keys and values"""
        lst = [{"a": "z"}, {"b": "y"}, {"c": "x"}, {"a": "w"}, {"b": "v"}, {"c": "u"}]
        result = f(lst, "b")
        expected = [{"b": "v"}, {"b": "y"}]
        self.assertEqual(result, expected)

    def test_dicts_with_same_keys(self):
        """Test case 10: List with dictionaries having duplicate values for the key"""
        lst = [{"a": "z"}, {"a": "y"}, {"a": "y"}, {"a": "x"}]
        result = f(lst, "a")
        expected = [{"a": "x"}, {"a": "y"}, {"a": "y"}, {"a": "z"}]
        self.assertEqual(result, expected)

    def test_dicts_with_many_keys(self):
        """Test case 11: List with dictionaries having duplicate values for the key"""
        lst = [
            {"a": "z", "b": "hi"},
            {"a": "y", "c": "bonjour"},
            {"a": "y"},
            {"a": "x", "b": "hallo"},
        ]
        result = f(lst, "b")
        expected = [
            {"a": "x", "b": "hallo"},
            {"a": "z", "b": "hi"},
        ]
        self.assertEqual(result, expected)

    def test_dicts_with_many_long_keys(self):
        """Test case 12: List with dictionaries having duplicate values for the key"""
        lst = [
            {"alphabet": "z", "bodega": "hi"},
            {"alphabet": "y", "Calliope": "bonjour"},
            {"alphabet": "y", "Calliope": "goede dag"},
            {"alphabet": "x", "bodega": "hallo"},
        ]
        result = f(lst, "Calliope")
        expected = [
            {"alphabet": "y", "Calliope": "bonjour"},
            {"alphabet": "y", "Calliope": "goede dag"},
        ]
        self.assertEqual(result, expected)

    def test_empty_dictionaries(self):
        """Test case 13: A list with some empty dictionaries"""
        lst = [
            {"a": "z"},
            {},
            {"a": "y"},
            {
                "a": "x",
            },
            {},
        ]
        result = f(lst, "a")
        expected = [{"a": "x"}, {"a": "y"}, {"a": "z"}]
        self.assertEqual(result, expected)

    def test_does_not_modify_argument_list(self):
        """Test case 14: Function does not modify the list argument"""
        lst = [{"a": "x"}, {"a": "y"}, {"a": "z"}]
        f(lst, "a")
        self.assertEqual(lst, [{"a": "x"}, {"a": "y"}, {"a": "z"}])``


if __name__ == "__main__":
    unittest.main()
