import csv
import os

def parsefile(read_obj, write_obj):
    samples = int(read_obj.readline())
    for i in range(0, samples):
        data = (read_obj.readline())
        syn = (read_obj.readline())
        for j in range(0, int(read_obj.readline())):
            temp = read_obj.readline().split()
            write_obj.writerow([data, syn, temp[0], temp[1]])    

write_file = open('origin_parsed.csv', 'wb')
write_file_curated = open('curated_parsed.csv', 'wb')
writer = csv.writer(write_file)
curated_writer = csv.writer(write_file_curated)
for subdir, dirs, files in os.walk("C:\Users\Aadish\Desktop\Flexwin\Data\WINDOW_ORIG\EID_TOMO"):
    for file in files:
        file_name = os.path.join(subdir, file)
        temp = file_name.split('_')
        read_file = open(file_name, "r")
        if temp[-1] == "orig":
            parsefile(read_file, writer)
        read_file.close()

for subdir, dirs, files in os.walk("C:\Users\Aadish\Desktop\Flexwin\Data\WINDOW\EID_TOMO"):
    for file in files:
        file_name = os.path.join(subdir, file)
        temp = file_name.split('\\')
        read_file = open(file_name, "r")
        parsefile(read_file, curated_writer)
        read_file.close()
write_file.close()
write_file_curated.close()





