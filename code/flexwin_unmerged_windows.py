import os
def generate_output(window_file):
	#window_file = '/media/sf_Flexwin/Data/WINDOW_ORIG/EID_TOMO/T006_T030/MEASUREMENT_WINDOWS_3321426_T006_T030_m16_orig'
	output_file = window_file+ '_before_merge'
	window_file_obj = open(window_file, 'r')
	samples = window_file_obj.readline()
	count = 0
	output_file_obj = open(output_file, 'w')
	for i in range(0, int(samples)):
		input_file = "/home/aadish/Desktop/flexwin/test_data/input.test"
		f = open(input_file, "w")
		data = window_file_obj.readline()
		syn = window_file_obj.readline()
		output_file_obj.write(data)
		output_file_obj.write(syn)
		temp = data.split("/")
		f.write("1\n")
		f.write("".join(["/media/sf_Flexwin/Data/DATA/EID_TOMO/", (temp[-1].split("."))[0], "/", (temp[-1].split(".")[-1]).strip(), "/", temp[-1]]))
		f.write("".join(["/media/sf_Flexwin/Data/SYN/EID_TOMO/", (temp[-1].split("."))[0], "/", (temp[-1].split(".")[-1]).strip(), "/", syn.split("/")[-1]]))
		f.write("".join(["MEASURE/", (temp[-1].split("."))[0], "_", (syn.split("/")[-1]).strip(), "_", (temp[-1].split(".")[-1])]))
		for j in range(0, int(window_file_obj.readline())):
		    temp = window_file_obj.readline()
		    #write_obj.writerow([data, syn, temp[0], temp[1]])
	    	f.close()

		a = os.popen("cd /home/aadish/Desktop/flexwin/test_data; /home/aadish/Desktop/flexwin/test_data/flexwin < /home/aadish/Desktop/flexwin/test_data/input.test")
		list = a.read().split('\n') 
		for i in range(0, len(list)):
			if "duplicate rejection retained" in list[i]:
				output_file_obj.write(list[i].split()[-3]+'\n')
				for j in range (0, int(list[i].split()[-3])):
					output_file_obj.write(list[i+j+2].strip()+'\n')
				break
	output_file_obj.close()


for subdir, dirs, files in os.walk('/media/sf_Flexwin/Data/WINDOW_ORIG/EID_TOMO/T006_T030'):
    for file in files:
        file_name = os.path.join(subdir, file)
        temp = file_name.split('_')
        if temp[-1] == "orig":
            generate_output(file_name)
            print file_name
            #break
