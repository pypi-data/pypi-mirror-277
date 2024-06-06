#!/usr/bin/env python3

import os
import argparse

def init_command(directories):
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")
        else:
            print(f"Directory already exists: {directory}")

def main():
    parser = argparse.ArgumentParser(description='NVL CLI Tool')
    subparsers = parser.add_subparsers(dest='command')

    init_parser = subparsers.add_parser('init', help='Initialize directories')
    init_parser.add_argument('directories', nargs='+', help='Directories to create')

    args = parser.parse_args()

    if args.command == 'init':
        init_command(args.directories)

if __name__ == '__main__':
    main()
