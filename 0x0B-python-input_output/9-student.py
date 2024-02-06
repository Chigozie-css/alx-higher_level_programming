#!/usr/bin/python3
"""Defines a Student class and its to_json method."""

class Student:
    """Represents a student with first name, last name, and age."""
    def __init__(self, first_name, last_name, age):
        """Initializes a student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of the student instance"""
        return {'first_name': self.first_name, 'last_name': self.last_name, 'age': self.age}
