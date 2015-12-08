import csv
windows_file = open('windows_before.csv', 'rb')
curated_parse_csvfile = open('curated_parsed.csv', 'rb')
original_parse_csvfile = open('origin_parsed.csv', 'rb')
windowreader = csv.reader(windows_file)
curatedreader = csv.reader(curated_parse_csvfile)
originalreader = csv.reader(original_parse_csvfile)

curated_dic = {}
original_dic = {}

for row in curatedreader:
    #print row
    if (row[0], row[1]) in curated_dic:
        curated_dic[(row[0], row[1])].append((float(row[2]), float(row[3])))
    else:
        curated_dic[(row[0], row[1])] = [(float(row[2]), float(row[3]))]

for row in originalreader:
    #print row
    if (row[0], row[1]) in original_dic:
        original_dic[(row[0], row[1])].append((float(row[2]), float(row[3])))
    else:
        original_dic[(row[0], row[1])] = [(float(row[2]), float(row[3]))]

true_positive = 0
false_positive = 0
true_negative = 0
false_negative = 0
unknown = 0
counter = 0
classified_window_dictionary = {}
for row in windowreader:
    counter += 1
    if (row[0], row[1]) in original_dic:
        if (row[0], row[1]) in curated_dic:
            if (float(row[2]), float(row[3])) in original_dic[(row[0], row[1])] and (float(row[2]), float(row[3])) in curated_dic[(row[0], row[1])] :
                true_positive += 1
                classified_window_dictionary[(row[0], row[1], float(row[2]), float(row[3]))] = "True Positive"
            elif (float(row[2]), float(row[3])) in original_dic[(row[0], row[1])] and (float(row[2]), float(row[3])) not in curated_dic[(row[0], row[1])]:
                false_positive += 1
                classified_window_dictionary[(row[0], row[1], float(row[2]), float(row[3]))] = "False Positive"
            else:
                unknown += 1
                
                classified_window_dictionary[(row[0], row[1], float(row[2]), float(row[3]))] = "Unknown"
        elif (float(row[2]), float(row[3])) in original_dic[(row[0], row[1])]:
            false_positive += 1
            classified_window_dictionary[(row[0], row[1], float(row[2]), float(row[3]))] = "False Positive"
        else:
            unknown += 1
            classified_window_dictionary[(row[0], row[1], float(row[2]), float(row[3]))] = "Unknown"
    else:
        print "Here"
        unknown += 1

print true_positive
print false_positive
print unknown
print counter
print true_positive + false_positive + unknown

# True Analysis Start
file = open('windows_before_C2_1.0.csv', 'rb')
reader = csv.reader(file)
true_positive = 0
false_positive = 0
true_negative = 0
false_negative = 0
unknown = 0
counter = 0
window_analysis_dictionary = {}
for row in reader:
    if (row[0], row[1], float(row[2]), float(row[3])) in classified_window_dictionary:
        if classified_window_dictionary[(row[0], row[1], float(row[2]), float(row[3]))] == 'True Positive':
            window_analysis_dictionary[(row[0], row[1], float(row[2]), float(row[3]))] = "True Positive"
            true_positive += 1;
        if classified_window_dictionary[(row[0], row[1], float(row[2]), float(row[3]))] == 'False Positive':
            window_analysis_dictionary[(row[0], row[1], float(row[2]), float(row[3]))] = "False Positive"
            false_positive += 1;
        if classified_window_dictionary[(row[0], row[1], float(row[2]), float(row[3]))] == 'Unknown':
            window_analysis_dictionary[(row[0], row[1], float(row[2]), float(row[3]))] = "Unknown"
            unknown += 1;
    else:
        unknown += 1

for key in classified_window_dictionary:
    if classified_window_dictionary[key] == "True Positive":
        if key not in window_analysis_dictionary:
            false_negative += 1
    if classified_window_dictionary[key] == "False Positive":
        if key not in window_analysis_dictionary:
            true_negative += 1
print "Analysis"
print true_positive
print false_positive
print true_negative
print false_negative
print unknown