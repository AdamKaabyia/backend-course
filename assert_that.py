class FluentAssert:
    def __init__(self, value):
        self.value = value

    def is_equal_to(self, other):
        assert self.value == other, f"Expected {self.value} to be equal to {other}"
        return self

    def is_length(self, length):
        assert len(self.value) == length, f"Expected length of {self.value} to be {length}"
        return self

    def starts_with(self, prefix):
        assert self.value.startswith(prefix), f"Expected {self.value} to start with {prefix}"
        return self

    def ends_with(self, suffix):
        assert self.value.endswith(suffix), f"Expected {self.value} to end with {suffix}"
        return self

    def contains(self, item):
        assert item in self.value, f"Expected {self.value} to contain {item}"
        return self

    def does_not_contain(self, item):
        assert item not in self.value, f"Expected {self.value} not to contain {item}"
        return self

    def evaluates_to(self, expression):
        try:
            environment = {"__builtins__": None, "value": self.value}
            result = eval(expression, environment)
        except Exception as e:
            raise AssertionError(f"Failed to evaluate expression '{expression}': {e}")
        assert result, f"Expected expression '{expression}' to be True, got {result} instead"
        return self
