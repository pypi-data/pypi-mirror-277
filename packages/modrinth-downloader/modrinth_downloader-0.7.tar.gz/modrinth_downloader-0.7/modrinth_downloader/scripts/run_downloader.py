from modrinth_downloader.downloader import *
from modrinth_downloader.utils import *
import argparse
import toml
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, 'config.toml')
with open(config_path, 'r') as config_file:
    config = toml.load(config_file)

config_list_path = config['paths']['lists']
config_download_path = config['paths']['downloads']
config_backup_path = config['paths']['backups']

list_path = os.path.expanduser(config_list_path)
download_path = os.path.expanduser(config_download_path)
backup_path = os.path.expanduser(config_backup_path)

def main():
    parser = argparse.ArgumentParser(description="Parse Arguments for "
                                                 "Modrinth Downloader")

    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Increase output verbosity')
    parser.add_argument('--list', type=str, help='The list name',
                        required=True)
    parser.add_argument('-m', '--game_version', type=str,
                        required=True, help='The game version')
    parser.add_argument('-l', '--loader', type=str, required=True,
                        help='The loader you want to use')

    args = parser.parse_args()

    list_file_path = os.path.join(list_path, args.list)
    list_name = args.list

    if args.verbose:
        print(f"Verbose mode is on")
        print(f"List Path: {list_file_path}")
        print("File content:")
        with open(list_file_path, 'r') as file:
            content = file.read()
        print(content)

    if not os.path.exists(download_path):
        os.makedirs(download_path)
    if not os.path.exists(os.path.join(download_path, list_name)):
        os.makedirs(os.path.join(download_path, list_name))

    rotate_backups(list_name, download_path, backup_path)

    try:
        with open(list_file_path, 'r') as f:
            for line in f:
                project_id = line.strip()
                game_version = args.game_version
                loader = args.loader
                download_project(project_id, game_version, loader,
                                 download_path, list_name)

    except FileNotFoundError:
        print(f'The list file {list_file_path} was not found.')
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
