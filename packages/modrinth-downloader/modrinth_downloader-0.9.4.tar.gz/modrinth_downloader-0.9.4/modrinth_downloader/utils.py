import os
import shutil
import toml
def rotate_backups(list_name, download_path, backup_path, max_backups=5):
    specific_backup_path = os.path.join(backup_path, list_name)

    if not os.path.exists(backup_path):
        os.makedirs(backup_path)

    # Rotate existing backups
    for i in range(max_backups - 1, 0, -1):
        old_backup = os.path.join(str(specific_backup_path), f"backup_{i}")
        new_backup = os.path.join(str(specific_backup_path), f"backup_{i + 1}")
        if os.path.exists(old_backup):
            shutil.move(old_backup, new_backup)

    # Move the current backup to backup_1
    current_backup = os.path.join(str(specific_backup_path), "backup_0")
    if os.path.exists(current_backup):
        shutil.move(current_backup,
                    os.path.join(str(specific_backup_path), "backup_1"))

    # Create a new current backup
    if not os.path.exists(specific_backup_path):
        os.makedirs(specific_backup_path)
    shutil.move(os.path.join(str(download_path), list_name), current_backup)

def setup_dirs(list_path, download_path, backup_path):
    if not os.path.exists(list_path):
        os.makedirs(list_path)
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    if not os.path.exists(backup_path):
        os.makedirs(backup_path)
