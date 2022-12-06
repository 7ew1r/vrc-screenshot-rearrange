import glob
import re
import os
import sys

if(len(sys.argv) < 2):
     print("not enough args")
     sys.exit(1)

vrc_screenshot_path = os.path.abspath(sys.argv[1])

if not (os.path.isdir(sys.argv[1])):
    print(f'{sys.argv[1]} is not directory')
    sys.exit(1)


def check_screenshot_name(file_name, pattern):
    # pattern = r'VRChat_\d{4}x\d{3,4}_\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}.\d{3}.png'
    result = re.match(pattern, file_name)

    if result:
        return True
    else:
        return False


def get_file_data(file_name):
     pattern = r'VRChat_(\d{4}x\d{3,4})_(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}.\d{3}).(png)'
     result = re.match(pattern, file_name)
     return result.group(1), result.group(2), result.group(3)


# VRChat_2022-12-06_01-53-30.150_3840x2160.png
def create_new_file_name(resolution, datetime, extension):
    return f'VRChat_{datetime}_{resolution}.{extension}'


items = os.listdir(vrc_screenshot_path)
year_month_dirs =[f for f in items if os.path.isdir(os.path.join(vrc_screenshot_path, f))]

for dir in year_month_dirs:
    dir_path = os.path.join(vrc_screenshot_path, dir)
    files = glob.glob(dir_path + "/*.png")

    for file in files:
        file_name = os.path.basename(file)

        # VRChat_1920x1080_2019-12-01_03-18-48.414.png
        old_file_name_pattern = r'VRChat_\d{4}x\d{3,4}_\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}.\d{3}.png'
        if not check_screenshot_name(file_name, old_file_name_pattern):
            print(f'not change: {file_name}')
            continue

        resolution, datetime, extension = get_file_data(file_name)
        new_file_name = create_new_file_name(resolution, datetime, extension)

        old_file_path = os.path.join(dir_path, file_name)
        new_file_path = os.path.join(dir_path, new_file_name)
        print(f'rename: {file_name} => {new_file_name}')
        os.rename(old_file_path, new_file_path)

