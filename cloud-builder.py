# _*_ coding: utf-8 _*_
# !/usr/bin/env python3

"""
Mictlantecuhtli: A Multi-Cloud Global Probe Mesh Creator.

@author: Collisio-Adolebitque
"""

import mictl


def main():
    """
    <PYTHON> <SCRIPT_NAME> <FUNCTION> <CSP> <LOCATION> <TYPE> <TARGET>
    python3 cloud-builder.py serverless aws us-east-2a http get www.amazon.com
    python3 cloud-builder.py serverless aws -all-eu https post www.test.com
    python3 cloud-builder.py serverless aws ireland dns www.google.com
    python3 cloud-builder.py serverless gcp http get www.google.com
    python3 cloud-builder.py serverless azure westeurope http get www.microsoft.com
    :return: None
    """
    command = 'python3 cloud-builder.py serverless aws http get www.google.com'
    build_cloud = mictl.CommandParser(command)
    print(build_cloud.run())


if __name__ == '__main__':
    main()
