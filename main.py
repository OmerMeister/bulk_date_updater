import os
import piexif
from datetime import datetime
from colorama import Fore, Back, Style

# auxilary functions

# the function gets date and time parameters and create from them a datetime object
# than, it replaces the value of 3 exif date related properties with the newly created object
def exif_date_changer(filename, year, month, day,hour,minute,second):
    exif_dict = piexif.load(filename)
    new_date = datetime(year, month, day, hour, minute,
                        second).strftime("%Y:%m:%d %H:%M:%S")
    exif_dict['0th'][piexif.ImageIFD.DateTime] = new_date
    exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_date
    exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = new_date
    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, filename)


# auxilary variables
total_files = 0
total_converted = 0
total_skipped = 0

# main function

print(Fore.GREEN + "--BULK DATE UPDATER--" + Style.RESET_ALL)
print('''the program gets a batch of whatsapp images and set their
date taken exif attribute by their filename. time taken being
arbitrary set to 13:00\n''')
# the folder path
confirm = 'n'
while (confirm != 'y' and confirm != 'Y'):
    print(Fore.GREEN + "paste the folder path which contains images: " + Style.RESET_ALL)
    dir_path = input()
    print(Style.RESET_ALL +
          "insert 'y' to confirm selected path, anything else to reenter: " + Fore.GREEN, end="")
    confirm = input()
    print()

# get a list of all files and folders inside that folder
try:
    files_list = os.listdir(dir_path)
# raise an IOError if file cannot be found,or the image cannot be opened.
except IOError:
    print()
    print(Fore.RED, Back.WHITE +
          "#-#-#-#-#-#- folder path was not found -#-#-#-#-#-#" + Style.RESET_ALL)
    print()

# iterate over the list
for filename in files_list:
    # skips all the folders and files which are not jpg or jpeg
    # counts the total amount of image files
    total_files += 1
    fullpath = dir_path+'\\'+filename
    if filename[0:4] != "IMG-":
        total_skipped += 1
        print(Fore.RED + f"skipped file {fullpath}" + Style.RESET_ALL)
        continue 
    year = int(filename[4:8])
    month = int(filename[8:10])
    day = int(filename[10:12])
    try:
        exif_date_changer(fullpath,year,month,day,13,0,0)
        total_converted+=1
    except Exception as e:
        total_skipped+=1
        print(Fore.RED + f"skipped file {fullpath}" + Style.RESET_ALL)
        print("exif change error\n")
        print(e)

print()
print(Fore.GREEN + "DONE!" + Style.RESET_ALL)
print(f"{total_converted} out of {total_files} files were converted in total")
print(
    f"{total_skipped} were skipped because incorrect filename/other error")
print(Fore.GREEN + "**created by meister - 21/8/2023**" + Style.RESET_ALL)
print()
print()

# data which used for tests:
# C:\Users\Omer\Desktop\test2
# IMG-20130611-WA0003
# IMG-20220610-WA0002
