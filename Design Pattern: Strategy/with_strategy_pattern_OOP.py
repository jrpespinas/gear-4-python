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


class SorterStrategy:
    @abstractmethod
    def sort(self, group: List[Member]) -> List[Member]:
        pass


class NameSorterStrategy(SorterStrategy):
    def sort(self, group: List[Member]) -> List[Member]:
        return sorted(group, key=lambda x: x.name)


class AgeSorterStrategy(SorterStrategy):
    def sort(self, group: List[Member]) -> List[Member]:
        return sorted(group, key=lambda x: x.age, reverse=True)


class Group:
    group: List[Member] = []

    def add_members(self, name: str, age: int):
        self.group.append(Member(name=name, age=age))

    def list_members(self, sorting_strategy: SorterStrategy):
        group = sorting_strategy.sort(self.group)
        for i in group:
            print(vars(i))


def main():
    group = Group()
    sorter = NameSorterStrategy()

    group.add_members(name="Mark Falterson", age=42)
    group.add_members(name="Luke Salzburg", age=26)
    group.add_members(name="Mary Smiths", age=25)

    group.list_members(sorter)


if __name__ == "__main__":
    main()
