import csv
orig_parse_csvfile = open('origin_parsed.csv', 'rb')
curated_parse_csvfile = open('curated_parsed.csv', 'rb')
origreader = csv.reader(orig_parse_csvfile)
curatedreader = csv.reader(curated_parse_csvfile)

stats_csvfile = open('stats_grouped.csv', 'wb')
writer = csv.writer(stats_csvfile)
orig_dic = {}
curated_dic = {}
for row in origreader:
    #print row
    if (row[0], row[1]) in orig_dic:
        orig_dic[(row[0], row[1])].append([float(row[2]), float(row[3])])
    else:
        orig_dic[(row[0], row[1])] = [[float(row[2]), float(row[3])]]

for row in curatedreader:
    #print row
    if (row[0], row[1]) in curated_dic:
        curated_dic[(row[0], row[1])].append([float(row[2]), float(row[3])])
    else:
        curated_dic[(row[0], row[1])] = [[float(row[2]), float(row[3])]]

print len(orig_dic)
print len(curated_dic)

# True Positives
true_positives_dic = {}

# True Negatives
true_negatives_dic = {}

# False Positives
false_positives_dic = {}

# False Negatives
false_negatives_dic = {}

# Calculating True Positives and False Positives
for key in orig_dic:
    x = key[0].split("/")[-1].split(".")[0]
    y = key[0].split("/")[-1].split(".")[-1]
    true_positives_dic[(x, y)] = 0
    false_positives_dic[(x, y)] = 0

for key in orig_dic:
    x = key[0].split("/")[-1].split(".")[0]
    y = key[0].split("/")[-1].split(".")[-1]
    #true_postives_dic[(x, y)] = 0
    #false_positives_dic[(x, y)] = 0
    for item in orig_dic[key]:
        if key in curated_dic:
            if item in curated_dic[key]:
                true_positives_dic[(x, y)] += 1
            else:
                false_positives_dic[(x, y)] += 1
        else:
            false_positives_dic[(x, y)] += 1
    #true_positives_dic[key] = true_positives
    #false_positives_dic[key] = false_positives
    #writer.writerow([key[0], key[1], true_positives, false_positives])

for key in true_positives_dic:
    writer.writerow([key[0], key[1], true_positives_dic[key], false_positives_dic[key]])
stats_csvfile.close()




