import csv
import os

def parsefile(read_obj, output_file_name, writer):
    while True:
        
        a = read_obj.readline()
        if len(a.strip()) == 0:
            break
        
        b = read_obj.readline()
        
        windows = int(read_obj.readline())
        for i in range(0, windows):
            list = []
            list.append(a)
            list.append(b)
            temp = (read_obj.readline().strip()).split()
            list.append(float(temp[6]))
            list.append(float(temp[7]))
            writer.writerow(list)

write_file = open('windows_before_C1_4.0.csv', 'wb')
#write_file_curated = open('curated_parsed.csv', 'wb')
writer = csv.writer(write_file)
#curated_writer = csv.writer(write_file_curated)
for subdir, dirs, files in os.walk("C:\Users\Aadish\Desktop\Flexwin\Data\WINDOW_ORIG\EID_TOMO\T006_T030"):
    for file in files:
        file_name = os.path.join(subdir, file)
        output_file_name = os.path.join(subdir, "".join([file, ".input"]))
        temp = file_name.split('_')
        read_file = open(file_name, "r")
        if temp[-1] == "merge":
            parsefile(read_file, output_file_name, writer)
            print file_name
            #break
        read_file.close()
write_file.close()

