import glob
import re
import os
import shutil

# VRChat のスクリーンショットのフォルダを指定
user_dir = os.path.expanduser('~')
vrc_screenshot_path = os.path.join(
    user_dir, "Library/Mobile Documents/com~apple~CloudDocs/VRChat")


def check_screenshot_name(file_name):
    pattern = r'VRChat_\d{4}x\d{3,4}_\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}.\d{3}.png'
    result = re.match(pattern, file_name)

    if result:
        return True
    else:
        return False


def get_year_month(file_name):
    pattern = r'VRChat_\d{4}x\d{3,4}_(\d{4}-\d{2})-\d{2}_\d{2}-\d{2}-\d{2}.\d{3}.png'
    result = re.match(pattern, file_name)
    return result.group(1)


files = glob.glob(vrc_screenshot_path + "/*")


for file in files:
    file_name = os.path.basename(file)
    if not check_screenshot_name(file_name):
        continue

    year_month = get_year_month(file_name)

    year_month_dirname = os.path.join(vrc_screenshot_path, year_month)
    os.makedirs(year_month_dirname, exist_ok=True)
    shutil.move(file, year_month_dirname)
