from modrinth_downloader.api import *

def show_project_info(project_id):
    info = get_project_info(project_id)
    print(info)

def download_project(project_id, game_version, loader, download_path,
                     list_name):
    project_id=str(project_id)
    game_version=str(game_version)
    loader=str(loader)
    download_path = os.path.join(download_path, list_name)
    output_file_name=project_id + '_' + game_version + '_' + loader + '.jar'

    download_project_file(project_id, game_version, loader, output_file_name,
                          download_path)
