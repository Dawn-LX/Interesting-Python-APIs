import os
import shutil

def copy_py_files(source_dir, dest_dir):
    """
    Copy all python scripts from source_dir to dest_dir, while preserving directory structure.
    """
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.py'):# or file.endswith('.log') or file.endswith('.md'):
                source_path = os.path.join(root, file)
                dest_path = source_path.replace(source_dir, dest_dir, 1)
                dest_folder = os.path.dirname(dest_path)
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder,exist_ok=True)
                shutil.copy(source_path, dest_path)

if __name__ == "__main__":
    copy_py_files("/home/gaokaifeng/project/DiffuSeq","/home/gaokaifeng/project/DiffuSeq/_All_py_files")