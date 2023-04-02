import os


def print_directory_structure(path, print_files=False,linewidth=160,statistic_func=None):
    """
    Recursively prints the directory structure for the given path.
    :param path: The path to the directory.
    :param print_files: Whether or not to print files in the directory structure.
    """
    def func(dirs, files):
        num_folders = len(dirs)
        num_files = len(files)
        statistic_info = f"(num_folders:{num_folders}, num_files={num_files})"
        return statistic_info

    stat_func = func if statistic_func is None else statistic_func

    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        # indent = ' ' * 4 * level
        indent = '|   ' * level

        structure_info = f"{indent}{os.path.basename(root)}/"
        statistic_info = stat_func(dirs, files)
        dash_len = max(0,linewidth-len(structure_info)-len(statistic_info))
        info = structure_info + '-'*dash_len + statistic_info
        print(info)
        if print_files:
            sub_indent = ' ' * 4 * (level + 1)
            for file in files:
                print(f"{sub_indent}{file}")


def func2(dirs, files):
    num_folders = len(dirs)
    num_files = len(files)
    video_names = set()
    for file in files:
        if file.startswith("ILSVRC"):
            video_names.add(
                file.split('-')[0]
            )
    num_videos = len(video_names)

    statistic_info = f"(num_folders:{num_folders}, num_files={num_files}),num_videos={num_videos}"
    return statistic_info

print_directory_structure("data0",statistic_func=func2)
