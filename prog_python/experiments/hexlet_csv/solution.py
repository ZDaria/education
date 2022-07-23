from validators import get_validator

# Такие штуки правильно делать через фикстуры.
# В следущих уроках мы разберём это подробнее.
make_validator = get_validator()


def test_validator():
    add_check, is_valid = make_validator()
    assert is_valid("value")

# BEGIN (write your solution here)


# END
