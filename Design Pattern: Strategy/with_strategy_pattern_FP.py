import uuid
from typing import List
from abc import ABC, abstractmethod


class Member:
    id: str
    name: str
    age: int

    def __init__(self, name: str, age: int):
        self.id = uuid.uuid4()
        self.name = name
        self.age = age


def NameSorterStrategy(group: List[Member]) -> List[Member]:
    return sorted(group, key=lambda x: x.name)


def AgeSorterStrategy(group: List[Member]) -> List[Member]:
    return sorted(group, key=lambda x: x.age, reverse=True)


class Group:
    group: List[Member] = []

    def add_members(self, name: str, age: int):
        self.group.append(Member(name=name, age=age))

    def list_members(self, sorting_strategy_function):
        group = sorting_strategy_function(self.group)
        for i in group:
            print(vars(i))


def main():
    group = Group()

    group.add_members(name="Mark Falterson", age=42)
    group.add_members(name="Luke Salzburg", age=26)
    group.add_members(name="Mary Smiths", age=25)

    group.list_members(NameSorterStrategy)


if __name__ == "__main__":
    main()
