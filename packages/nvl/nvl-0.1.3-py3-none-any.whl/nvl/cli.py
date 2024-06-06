#!/usr/bin/env python3

import os
import yaml
import argparse
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), 'ProjectStructure.yaml')
    print(f"Looking for config at: {config_path}")  # Debugging print

    if not os.path.exists(config_path):
        print(f"Config file not found: {config_path}")
        raise FileNotFoundError(f"Config file not found: {config_path}")
    
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def init_command():
    config = load_config()
    
    for directory_config in config['directories']:
        directory = directory_config['name']
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"{Fore.GREEN}Created directory: {directory}")
            
            # Create subdirectories
            for subdir in directory_config['subdirectories']:
                subdir_path = os.path.join(directory, subdir)
                os.makedirs(subdir_path)
                print(f"{Fore.GREEN}Created subdirectory: {subdir_path}")

            # Create files with simple text
            for filename, content in directory_config['files'].items():
                file_path = os.path.join(directory, filename)
                with open(file_path, 'w') as f:
                    f.write(content)
                print(f"{Fore.GREEN}Created file: {file_path} with content: '{content}'")
        else:
            print(f"{Fore.YELLOW}Directory already exists: {directory}")

def debug_command():
    print(f"{Fore.CYAN}Debugging Information:")
    print(f"Current Working Directory: {os.getcwd()}")
    print(f"List of Files: {os.listdir()}")
    # Add more debug information as needed

def main():
    parser = argparse.ArgumentParser(description='NVL CLI Tool')
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Init command
    init_parser = subparsers.add_parser('init', help='Initialize directories from YAML configuration')

    # Debug command
    debug_parser = subparsers.add_parser('debug', help='Print debugging information')
    
    args = parser.parse_args()

    if args.command == 'init':
        init_command()
    elif args.command == 'debug':
        debug_command()

if __name__ == '__main__':
    main()
