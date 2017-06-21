import re

_digits = re.compile('\d')
def contains_digits(d):
    return bool(_digits.search(d))


def is_audio(file_name):
    if " " in file_name :
        return False
    
    file = file_name.split(".")
    audio = ['.mp3', '.flac', '.alac',  '.aac']
    if "."+file[1] in audio and "-" not in file[0] and "_" not in file[0]:
        return True
    return False

def is_img(file_name):
    if " " in file_name or contains_digits(file_name):
        return False
    file = file_name.split(".")
    image = ['.jpg', '.jpeg', '.png',  '.bmp', '.gif']
    if "."+file[1] in image and "-" not in file[0] and "_" not in file[0]:
        return True
    return False