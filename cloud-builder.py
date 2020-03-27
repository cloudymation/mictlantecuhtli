# _*_ coding: utf-8 _*_
# !/usr/bin/env python3

"""
Mictlantecuhtli: A Multi-Cloud Global Probe Mesh Creator.

@author: Collisio-Adolebitque
"""

from mictl import *


def main():
    """
    python3 cloud-builder.py aws serverless http get www.google.com
    python3 cloud-builder.py aws serverless https post www.test.com
    python3 cloud-builder.py aws serverless dns www.google.com
    :return: None
    """
    build_cloud = __main__.CommandParser()
    print(build_cloud.run('python3 cloud-builder.py aws serverless http www.google.com'))


if __name__ == '__main__':
    main()
