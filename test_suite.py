from assertions import *

from assertpy import assert_that


def test_something():
    assert_that(1+2).is_equal_to(3)
    assert_that('foobar').is_length(6).starts_with('foo').ends_with('bar')
    assert_that(['a', 'b', 'c']).contains('a').does_not_contain('x')


def test_values():
    test_something()
    assert_greater(5, 3)
    assert_smaller(2, 5)
    assert_equal(4, 4)
    assert_in_list(2, [1, 2, 3])
    assert_in_list(3, [1, [2, [3, 4]]])
    assert_key_in_dict('key', {'key': 'value'})
    assert_key_in_dict('nested', {'outer': {'nested': 'value'}})
    assert_value_in_dict('value', {'key': 'value'})
    assert_value_in_dict('nested_value', {'outer': {'nested': 'nested_value'}})

    print("All tests passed!")


if __name__ == "__main__":
    test_values()
