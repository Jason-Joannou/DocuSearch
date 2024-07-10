import os
from .config import extentions, excluded_direcotries, search_directory

def crawl_directory(directory, excluded_dir_names=excluded_direcotries, included_extensions=extentions):
    if excluded_dir_names is None:
        excluded_dir_names = []
    if included_extensions is None:
        included_extensions = []

    file_paths = []
    for root, dirs, files in os.walk(directory):
        # Exclude directories by name
        dirs[:] = [d for d in dirs if d not in excluded_dir_names]
        for file in files:
            # Include only files with the specified extensions
            if any(file.endswith(ext) for ext in included_extensions):
                file_paths.append(os.path.join(root, file))
    return file_paths


documents = crawl_directory(directory=search_directory)
for doc in documents:
    print(doc)


