#!/usr/bin/env python3


class SchoolMember:
    """
    Parent class
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(SchoolMember):
    """
    Child class with salary
    """
    def __init__(self, *args, **kwargs):
        if args:
            salary = args[-1]
        else:
            salary = kwargs['salary']
        super().__init__(*args[:-1], **kwargs)
        self.salary = salary

    def show(self):
        print(f'Имя:{self.name} Возраст:{self.age} Зарплата:{self.salary}')


class Student(SchoolMember):
    """
    Child class with marks
    """
    def __init__(self, *args, **kwargs):
        if args:
            marks = args[-1]
        else:
            marks = kwargs['marks']
        super().__init__(*args[:-1], **kwargs)
        self.marks = marks

    def show(self):
        print(f'Имя:{self.name} Возраст:{self.age} Оценки:{self.marks}')
