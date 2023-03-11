import uuid
from typing import List


class Member:
    id: str
    name: str
    age: int

    def __init__(self, name: str, age: int):
        self.id = uuid.uuid4()
        self.name = name
        self.age = age

    def __repr__(self):
        return """"""


class Group:
    group: List[Member] = []

    def add_members(self, name: str, age: int):
        self.group.append(Member(name=name, age=age))

    def list_members(self, sorting_attribute: str = "name"):
        if sorting_attribute == "name":
            self.group.sort(key=lambda x: x.name)
            for i in self.group:
                print(vars(i))

        if sorting_attribute == "age":
            self.group.sort(key=lambda x: x.age, reverse=True)
            for i in self.group:
                print(vars(i))


def main():
    group = Group()

    group.add_members(name="Mark Falterson", age=42)
    group.add_members(name="Luke Salzburg", age=26)
    group.add_members(name="Mary Smiths", age=25)

    group.list_members("age")


if __name__ == "__main__":
    main()
