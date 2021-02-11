import pytest


class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def say(self):
        return "Hello World!"


def test_say_hello():
    p = Person('hoge', 'fuga')
    assert 'Hello World!' == p.say()


@pytest.mark.parametrize("first, last, expected", [
    ('hoge', 'fuga', 'hoge fuga'),
    ('fuga', 'hoge', 'fuga hoge'),
])
def test_full_name(first, last, expected):
    p = Person(first, last)
    assert expected == p.full_name
