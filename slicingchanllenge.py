#!/usr/bin/env python3

easy= ["science", "turbo", ["goggles", "eyes"], "nothing"]


medium= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


hard= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

e1 = easy[2][1]
g1 = easy[2][0]
n1 = easy[3]


e2 = medium[2]["goggles"]
g2 = medium[2]["eyes"]
n2 = medium[3]


e3 = hard[0]["user"]["name"]["first"]
g3 = hard[0]["kumquat"]
n3 = hard[0]["d"]


def slicing(e, g, n):
    print(f"My {e}! The {g} do {n}!")

slicing(e1, g1, n1)
slicing(e2, g2, n2)
slicing(e3, g3, n3)
