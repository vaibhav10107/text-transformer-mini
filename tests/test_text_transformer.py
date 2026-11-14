from text_transformer import to_uppercase, to_lowercase, to_title_case

def test_to_uppercase():
    assert to_uppercase("hello world") == "HELLO WORLD"
    assert to_uppercase("Python") == "PYTHON"
    assert to_uppercase("123") == "123"

def test_to_lowercase():
    assert to_lowercase("HELLO WORLD") == "hello world"
    assert to_lowercase("Python") == "python"
    assert to_lowercase("123") == "123"

def test_to_title_case():
    assert to_title_case("hello world") == "Hello World"
    assert to_title_case("python") == "Python"
    assert to_title_case("123") == "123"
    assert to_title_case("a") == "A"
    assert to_title_case("the quick brown fox") == "The Quick Brown Fox"
