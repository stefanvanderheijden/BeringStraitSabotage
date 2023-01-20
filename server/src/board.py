import json


class Field:
    def __init__(self, special_action: str = None):
        self._special_action = special_action
        self._occupancy = False

    def is_occupied(self):
        return self._occupancy

    def occupy(self):
        if self.is_occupied():
            print("Field already occupied")

        self._occupancy = True


class Board:
    def __init__(self, fields: json):
