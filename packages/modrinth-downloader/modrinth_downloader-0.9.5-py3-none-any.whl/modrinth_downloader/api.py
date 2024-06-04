import requests
import os

BASE_URL = "https://api.modrinth.com/v2"

def get_project_info(project_id):
    response = requests.get(f"{BASE_URL}/project/{project_id}")
    return response.json()

def download_project_file(project_id, game_version, loader, output_file,
                          download_path):
    try:
        versions_url = f"{BASE_URL}/project/{project_id}/version"
        response = requests.get(versions_url)
        response.raise_for_status()
        versions = response.json()

        matching_versions = [
            version for version in versions
            if game_version in version["game_versions"] and loader in version[
                "loaders"]
        ]
        if not matching_versions:
            print(
                f"No versions found for' {project_id}' on '{game_version}' "
                f"and loader '{loader}'.")
            return

        matching_versions.sort(key=lambda v: v["date_published"], reverse=True)
        latest_version = matching_versions[0]

        file_url = latest_version["files"][0]["url"]

        file_response = requests.get(file_url)
        file_response.raise_for_status()

        full_output_path = os.path.join(download_path, output_file)

        if not os.path.exists(download_path):
            os.makedirs(download_path)

        with open(full_output_path, 'wb') as f:
            f.write(file_response.content)

        print(f"Downloaded {latest_version['name']} to {full_output_path}")

    except Exception as e:
            print(e)
