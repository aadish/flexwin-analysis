import csv
import os

def parsefile(read_obj, output_file_name):
    #print output_file_name
    f = open(output_file_name, "w")
    samples = read_obj.readline()
    f.write(samples)
    for i in range(0, int(samples)):
        data = read_obj.readline()
        syn = read_obj.readline()
        temp = data.split("/")
        f.write("".join(["/media/sf_Flexwin/Data/DATA/EID_TOMO/", (temp[-1].split("."))[0], "/", (temp[-1].split(".")[-1]).strip(), "/", temp[-1]]))
        f.write("".join(["/media/sf_Flexwin/Data/SYN/EID_TOMO/", (temp[-1].split("."))[0], "/", (temp[-1].split(".")[-1]).strip(), "/", syn.split("/")[-1]]))
        f.write("".join(["MEASURE/", (temp[-1].split("."))[0], "_", (syn.split("/")[-1]).strip(), "_", (temp[-1].split(".")[-1])]))
        #print data , syn
        for j in range(0, int(read_obj.readline())):
            temp = read_obj.readline()
            #write_obj.writerow([data, syn, temp[0], temp[1]])
    f.close()

write_file = open('origin_parsed.csv', 'wb')
write_file_curated = open('curated_parsed.csv', 'wb')
writer = csv.writer(write_file)
curated_writer = csv.writer(write_file_curated)
for subdir, dirs, files in os.walk("C:\Users\Aadish\Desktop\Flexwin\Data\WINDOW_ORIG\EID_TOMO"):
    for file in files:
        file_name = os.path.join(subdir, file)
        output_file_name = os.path.join(subdir, "".join([file, ".input"]))
        temp = file_name.split('_')
        read_file = open(file_name, "r")
        if temp[-1] == "orig":
            parsefile(read_file, output_file_name)
            print file_name
            #break
        read_file.close()

