from name_func import get_formatted_name

def test_first_last_name():
    formatted_name = get_formatted_name('John', 'dummy','Wall')
    assert formatted_name == 'John dummy Wall'