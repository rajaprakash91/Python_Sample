import os;
from datetime import datetime as date;
from shutil import move as mv;

image_type = ['jpg', 'gif', 'jpeg', 'ing']
audio_type = ['m4a', 'mp3', 'wma', 'webm']
video_type = ['mp4', 'avi', 'flv', 'mkv', 'wmv']
doc_type = ['doc', 'ppt', 'pdf', 'txt', 'xlx', 'xlsx']

img_path = 'D:\\Entertainment\\Pictures\\'
audio_path = 'D:\\Entertainment\\Music\\'
vdo_path = r"D:\Entertainment\Videos"
doc_path = r"D:\\Learning\\"
mve_path = 'D:\\Entertainment\\Movies\\'


def bytes_to(byte, to, bsize=1024):
    """convert bytes to megabytes, etc.
       sample code:
           print_this('mb= ' + str(bytes_to(314575262000000, 'm')))
       sample output:
           mb= 300002347.946
    """

    a = {'k': 1, 'm': 2, 'g': 3, 't': 4, 'p': 5, 'e': 6}
    r = float(byte)
    for i in range(a[to]):
        r = r / bsize

    return r


def mov(source, dest, flag):
    if flag == 1:
        mv(source, dest)
        return True
    else:
        return False


def print_this(text, file):
    print(text, file=file)
    print(text)


# for Files in path
def process_dir(path, log_file, flag):
    """ This function is process the each directory files """
    if flag == 1:
        msg = " has been moved to "
    else:
        msg = " will be moved to "
    print_this("\n Processing directory : " + path, file=log_file)
    if len(os.listdir(path)) != 0:
        for file in os.listdir(path):
            if os.path.isdir(os.path.join(path, file)):
                print_this("\n Found Directory : " + file, file=log_file)
                process_dir(os.path.join(path, file), log_file, flag)
            elif file.lower().endswith(tuple(image_type)):
                print_this("\n" + file.capitalize() + " is a image type.", file=log_file)
                mov(os.path.join(path, file), os.path.join(img_path, file), flag)
                print_this(file.capitalize() + msg + img_path, file=log_file)
            elif file.lower().endswith(tuple(video_type)):
                if bytes_to(os.path.getsize(os.path.join(path, file)), 'm') > 120:
                    print_this("\n" + file.capitalize() + " is a Movie type.", file=log_file)
                    mov(os.path.join(path, file), os.path.join(mve_path, file), flag)
                    print_this(file.capitalize() + msg + mve_path, file=log_file)
                else:
                    print_this("\n" + file.capitalize() + " is a video type.", file=log_file)
                    mov(os.path.join(path, file), os.path.join(vdo_path, file), flag)
                    print_this(file.capitalize() + msg + vdo_path, file=log_file)
                    # os.rename(os.path.join(path,file), os.path.join(vdo_path,file))
            elif file.lower().endswith(tuple(doc_type)):
                if file != 'File_mov.txt':
                    print_this("\n" + file.capitalize() + " is a document type.", file=log_file)
                    mov(os.path.join(path, file), os.path.join(doc_path, file), flag)
                    print_this(file.capitalize() + msg + doc_path, file=log_file)

            elif file.lower().endswith(tuple(audio_type)):
                print_this("\n" + file.capitalize() + " is a Audio type.", file=log_file)
                mov(os.path.join(path, file), os.path.join(audio_path, file), flag)
                print_this(file.capitalize() + msg + audio_path, file=log_file)

            else:
                print_this("\n" + file.capitalize() + " is other type, so ignoring it", file=log_file)
    else:
        print_this("\n" + path + " contains no files.", file=log_file)


ip = input("Enter any directory  path : ")
while not os.path.isdir(ip):
    ip = input("\n Enter Directory path saala, Don't you know what Directory is : ")

test_run = input("you want to see Test run it, yes or no ?")
log = open(os.path.join(ip, 'File_mov.txt'), 'w')
print_this(" Script started at: " + str(date.now()), file=log)
print_this("\n The input Directory is " + ip, file=log)
if test_run.upper() in ('YES', 'Y', '1', 'YEA', 'YEAH', 'TRUE', 'YEP'):
    test_run = 0
    print_this("\n This will be a Test Run :) ! ", file=log)
else:
    test_run = 1
process_dir(ip, log, test_run)
print_this("\n Script Ended at: " + str(date.now()), file=log)
log.close()
