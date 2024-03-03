def assert_greater(tested_value, compare_to):
    assert tested_value > compare_to, f"{tested_value} is not greater than {compare_to}"


def assert_smaller(tested_value, compare_to):
    assert tested_value < compare_to, f"{tested_value} is not smaller than {compare_to}"


def assert_equal(tested_value, compare_to):
    assert tested_value == compare_to, f"{tested_value} is not equal to {compare_to}"


def assert_in_list(value, list_or_nested):
    if isinstance(list_or_nested, list):
        if value in list_or_nested or any(
                assert_in_list(value, item) for item in list_or_nested if isinstance(item, list)):
            return True
    raise AssertionError(f"{value} is not in {list_or_nested}")


def assert_key_in_dict(key, dict_or_nested):
    if key in dict_or_nested or any(
            assert_key_in_dict(key, v) for k, v in dict_or_nested.items() if isinstance(v, dict)):
        return True
    raise AssertionError(f"{key} is not in {dict_or_nested}")


def assert_value_in_dict(value, dict_or_nested):
    if value in dict_or_nested.values() or any(
            assert_value_in_dict(value, v) for k, v in dict_or_nested.items() if isinstance(v, dict)):
        return True
    raise AssertionError(f"{value} is not in {dict_or_nested}")
