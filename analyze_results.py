results = "/Users/kristen/Documents/Data-Mining-Project/results.txt"
classification = "/Users/kristen/Documents/Data-Mining-Project/train_classification.txt"



image_output = open(results,"r")
correct_classification = open(classification,"r")

results = ""
cc = ""
for line in image_output:
    results += line
list_results = results.split("???")


for line in correct_classification:
    cc += line
cc  = cc.split("\n")


correct = 0
incorrect = 0
for i in range(0,len(cc)):
    sublist = list_results[i].split("\n")

    if sublist[0] == "":
        if cc[i] in sublist[1]:
            correct += 1
        else:
            print sublist[1]
            print cc[i]
            incorrect +=1
    else:
        if cc[i] in sublist[0]:
            correct += 1
        else:
            print sublist[0]
            print cc[i]
            incorrect +=1
    i+=1


print correct
print incorrect
