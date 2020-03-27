# _*_ coding: utf-8 _*_
# !/usr/bin/env python3

"""
Mictlantecuhtli: A Multi-Cloud Global Probe Mesh Creator.

@author: Collisio-Adolebitque
"""


class CommandParser:
    def __init__(self, command_string=''):
        self.command = command_string

    def run(self):
        return self.command


class Terraform:
    def __init__(self):
        pass

    def init(self):
        pass

    def plan(self):
        pass

    def apply(self):
        pass

    def destroy(self):
        pass

    def refresh(self):
        pass

    def taint(self):
        pass

    def untaint(self):
        pass

    def validate(self):
        pass


class AWS:
    def __init__(self):
        pass


class GCP:
    def __init__(self):
        pass


class Azure:
    def __init__(self):
        pass


class Alibaba:
    def __init__(self):
        pass


def main():
    print('Bout ye')


if __name__ == '__main__':
    main()
