import os
import shutil


class DkFolderManager:
    def create_folder(self, path):
        """Create a folder and its parent directories if they don't exist."""
        if os.path.exists(path):
            print(f"The folder '{path}' already exists.")
        else:
            os.makedirs(path)
            print(f"The folder '{path}' has been created.")

    def rename_folder(self, old_path, new_path):
        """Rename a folder."""
        if not os.path.exists(old_path):
            print(f"The folder '{old_path}' does not exist.")
        else:
            os.rename(old_path, new_path)
            print(f"The folder '{old_path}' has been renamed to '{new_path}'.")

    def move_folder(self, src_path, dest_path):
        """Move a folder to a new location."""
        if not os.path.exists(src_path):
            print(f"The folder '{src_path}' does not exist.")
        else:
            shutil.move(src_path, dest_path)
            print(f"The folder '{src_path}' has been moved to '{dest_path}'.")

    def delete_folder(self, path, force=False):
        """Delete a folder.

        If force is False, only delete the folder if it is empty.
        If force is True, delete the folder and all its contents.
        """
        if not os.path.exists(path):
            print(f"The folder '{path}' does not exist.")
        else:
            if force:
                shutil.rmtree(path)
                print(f"The folder '{path}' and all its contents have been deleted.")
            else:
                try:
                    os.rmdir(path)
                    print(f"The empty folder '{path}' has been deleted.")
                except OSError:
                    print(f"The folder '{path}' is not empty and cannot be deleted.")
