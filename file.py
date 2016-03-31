import sys
import os

file_handler = open('./t2.txt', 'r')
line = file_handler.readline()

student_type_dict = {}

while line:
    tmp_list = line.split()
    if len(tmp_list) ~= 2:
        print line
        continue

    #print "student_id is :" + tmp_list[0] + "\n"
    #print  "type: " + tmp_list[1] + "\n"
    student_type_dict[tmp_list[0]] = tmp_list[1]
    print line

    line = file_handler.readline()

print student_type_dict

file_handler.close()

result_dict = {}

file_handler = open("./t1.txt", "r")
line = file_handler.readline()

while line:
    print line
    tmp_list = line.split()
    if len(tmp_list) ~= 3:
        print line 
        continue
    student_id = tmp_list[0]
    date = tmp_list[1]
    times = tmp_list[2]
    if date not in result_dict:
        result_dict[date] = {}
    student_type = student_type_dict[student_id]
    if student_type not in result_dict[date]:
        result_dict[date][student_type] = 0

    result_dict[date][student_type] += int(times)

    line = file_handler.readline()
    

print result_dict
