import os
import os.path

def przegladanie(root, files_dict):
    file_list = os.listdir(root)
    dir_list = []
    for item in file_list:
        if os.path.isfile(os.path.join(root, item)):
            full_name = os.path.join(root, item)
            file_size = os.path.getsize(full_name)
            if file_size not in files_dict:
                files_dict[file_size] = [full_name]
            else:
                files_dict[file_size].append(full_name)

        if os.path.isdir(os.path.join(root, item)):
            dir_list.append(item)
    for dirname in dir_list:
        przegladanie(os.path.join(root, dirname), files_dict)
    return files_dict

for key in sorted(przegladanie('.', {}).keys()):
    print("{0}:  {1}".format(key, przegladanie('.', {})[key]))

#przegladanie('.', {})