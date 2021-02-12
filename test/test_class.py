from typing import Optional
import pytest


class Person:
    def __init__(self, _id: int, first_name: str, last_name: str):
        self.id = _id
        self.first_name = first_name
        self.last_name = last_name

    def __eq__(self, other):
        if other is None or type(self) != type(other):
            return False
        return self.__dict__ == other.__dict__

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def say(self):
        return "Hello World!"


class PersonCache:
    cache = {}

    @classmethod
    def add(cls, person: Person):
        if person.id not in cls.cache:
            cls.cache[person.id] = person

    @classmethod
    def remove(cls, key: int):
        if key in cls.cache:
            cls.cache.pop(key)

    @classmethod
    def get(cls, key: int) -> Optional[Person]:
        if key in cls.cache:
            return cls.cache[key]
        return None


def test_say_hello():
    p = Person(1, 'hoge', 'fuga')
    assert 'Hello World!' == p.say()


@pytest.mark.parametrize("_id, first, last, expected", [
    (1, 'hoge', 'fuga', 'hoge fuga'),
    (2, 'fuga', 'hoge', 'fuga hoge'),
])
def test_full_name(_id, first, last, expected):
    p = Person(_id, first, last)
    assert expected == p.full_name


def test_add_person():
    p = Person(1, 'hoge', 'fuga')
    PersonCache.add(p)
    assert len(PersonCache.cache.keys()) == 1


def test_remove_person():
    p = Person(1, 'hoge', 'fuga')
    PersonCache.add(p)
    assert len(PersonCache.cache.keys()) == 1
    PersonCache.remove(p.id)
    assert len(PersonCache.cache.keys()) == 0


def test_not_remove_person():
    p = Person(1, 'hoge', 'fuga')
    PersonCache.add(p)
    PersonCache.remove(2)
    assert len(PersonCache.cache.keys()) == 1


def test_get_person():
    p = Person(1, 'hoge', 'fuga')
    PersonCache.add(p)
    c = PersonCache.get(1)
    assert p == c


def test_not_get_person():
    p = Person(1, 'hoge', 'fuga')
    PersonCache.add(p)
    assert PersonCache.get(2) == None

