"""
File: entity.py
Define the entity in program
Date: 2025-02-18
"""


class Item:
    def __init__(self, label, weight, unit_price, price):
        self.label = label
        self.weight = weight
        self.unit_price = unit_price
        self.price = price
