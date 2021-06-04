import pandas as pd
import numpy as np
import os
import time 
import datetime
import random as rand


#registrator class begin

data = [["Jan 15 2021", 999, 10, "Basketball", 7, True]] # put demo data
data1 = [[999, 0, 1 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, -1]]
data2 = [[0, "Jan 15 2021", "Jan 15 2021", "Yoga" , 1, 0, 1]]
data3 = [[999, 0, 1 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0]]

master_log = pd.DataFrame(data, columns = ['Date', 'Student ID', 'Class ID', 'Class Name', 'Class Type', 'Registered']) # 
        
student_log = pd.DataFrame(data1, columns = ['Student ID', 'Cat1', 'Cat2'
                                                , 'Cat3', 'Cat4', 'Cat5', 'Cat6'
                                                , 'Cat7', 'Cat8', 'Cat9', 'Cat10', 'Cat11', 'Cat12'
                                                ,'Num This Month', 'Tab'])
        
class_log = pd.DataFrame(data2, columns = ['Class ID', 'Start Date', 'End Date', 
                                                'Class Name', 'Quota', 'Enrollment', 'Fil0led'])

weekly_log = pd.DataFrame(data, columns = ['Date', 'Student ID', 'Class ID', 'Class Name', 'Class Type', 'Registered']) # 

def write_to_log(path, log_type):
    if (log_type == 'm'):
        master_log.to_csv(path, index = False, header = True)
        print("Master Log Written to Successfully")
    elif (log_type == 'c'):
        class_log.to_csv(path, index = False, header = True)
        print("Class Log Written to Successfully")
    elif (log_type == 's'):
        student_log.to_csv(path, index = False, header = True)
        print("Student Log Written to Successfully")
    elif (log_type == 'n'):
        weekly_log.to_csv(path, index = False, header = True)
        print("Weekly Log Written to Successfully")
    else:
        print("Invalid Log Type. Valid inputs are \'m\', \'c\', \'m\', \'n\' \n")

def read_in_log(path, log_type):
    if (log_type == 'm'):
        master_log = pd.read_csv(path)
        print("Master Log Read In Successfully")
        return master_log
    elif (log_type == 'c'):
        class_log = pd.read_csv(path)
        print("Class Log Read In Successfully")
        return class_log
    elif (log_type == 's'):
        student_log = pd.read_csv(path)
        print("Student Log Read In Successfully")
        return student_log
    elif (log_type == 'n'):
        weekly_log = pd.read_csv(path)
        print("Weekly Log Read In Successfully")
        return weekly_log
    else:
        print("Invalid Log Type. Valid inputs are \'m\', \'c\', \'m\', \'n\' \n")
    
def no_ml_bf():
    for j in range(len(weekly_log)):
        i_log = pd.DataFrame(data3, columns = ['Student ID', 'Cat1', 'Cat2'
                                                , 'Cat3', 'Cat4', 'Cat5', 'Cat6'
                                                , 'Cat7', 'Cat8', 'Cat9', 'Cat10', 'Cat11', 'Cat12'
                                                , 'Num This Month'])
        d2 = weekly_log.iat[j,0].split('/')
        for i in range(len(weekly_log)):
            #print(student_log.iat[int(weekly_log.iat[i,1]), (len(student_log.columns) - 1)])
            if (student_log.iat[int(weekly_log.iat[i,1]), (len(student_log.columns) - 1)] == -1): # if current registrant has not been tabulated
                if ((int(weekly_log.iat[i,1]) == int(weekly_log.iat[j,1]))): #same student id, and was successful 
                    num = str(weekly_log.iat[i,4])
                    nums = num.split('.')
                    category = 'Cat' + nums[0]
                    i_log.at[0,category] += 1
                    #check if date is same month
                    d1 = weekly_log.iat[i,0].split('/')
                    if (d1[2] == d2[2]):
                        if (d1[1] == d2[1]): # same month same year
                            i_log.at[0,'Num This Month'] += 1
        #copy i_log values to student_log
        copy_tabs(i_log)
        del i_log

def brute_force_count_points(): #only works if master_log had entries prior
    for j in range(len(weekly_log)):
        i_log = pd.DataFrame(data3, columns = ['Student ID', 'Cat1', 'Cat2'
                                                , 'Cat3', 'Cat4', 'Cat5', 'Cat6'
                                                , 'Cat7', 'Cat8', 'Cat9', 'Cat10', 'Cat11', 'Cat12'
                                                , 'Num This Month'])
        d2 = weekly_log.iat[j,0].split('/')
        for i in range(len(master_log)):
            if (student_log.iat[master_log.iat[i,1], (len(student_log.columns) - 1)] == -1): # if current registrant has not been tabulated
                if ((master_log.iat[i,1] == weekly_log.iat[j,1]) and (master_log.iat[i,1] == 1)): #same student id, and was successful 
                    num = str(master_log.iat[i,4])
                    nums = num.split('.')
                    category = 'Cat' + nums[0]
                    i_log.at[0,category] += 1
                    #check if date is same month
                    d1 = master_log.iat[i,0].split('/')
                    if (d1[2] == d2[2]):
                        if (d1[1] == d2[1]): # same month same year
                            i_log.at[0,'Num This Month'] += 1
        #copy i_log values to student_log
        copy_tabs(i_log)
        del i_log

def copy_tabs(i_log):
    id = i_log.iat[0,0]
    for i in range(1, len(i_log.columns) - 1):
        category = 'Cat' + str(i)
        student_log.at[id, category] = i_log.at[0, category]
    student_log.at[id, 'Tab'] = 1

def assign_class(class_dict):
    
    for i in range(len(weekly_log)):
        student_id = weekly_log.iat[i,1]
        num_instances_this_year = student_log.iat[student_id, weekly_log.iat[i, 4]]
        if (student_log.iat[student_id, (len(student_log.columns) - 1)] == 0):
            val = 3
        else:
            val = 0
        points = val - num_instances_this_year 
        if (class_dict.get((weekly_log.iat[i, 2]), -1) == -1): # class not found
            class_dict[weekly_log.iat[i, 2]] = [(student_id, points, i)]
        else: # class found, add new student
            search_list = [index for (index, a_tuple) in enumerate(class_dict[weekly_log.iat[i, 2]]) if a_tuple[0]== student_id]
            if (len(search_list) == 0):
                class_dict[weekly_log.iat[i, 2]].append((student_id, points, i)) 
      
    #for
    # count number of people at each priority
    # if total <= spaces left just write to txt
    # if total > spaces left, take all people of same priority and shuffle in place
    # write to txt till filled
    # repeat with new priority

    for index, class_list in enumerate(class_dict):
        class_dict[class_list].sort(key = lambda x: x[1]) #sorts list of tuples by second element, ascending
        f = open(str(class_list) + ".txt", "w+")

        index1 = 0
        quota = class_log.iat[class_list, 5]
        while (index1 < quota):
            prior_val = class_dict[class_list][index1][1]
            index2 = index1
            while(class_dict[class_list][index2][1] == prior_val):
                index2 += 1
                if(index2 >= len(class_dict[class_list])):
                    break;
            if(index2 - index1 > quota - index1):
                short_list = class_dict[class_list][index1:index2]
                rand.shuffle(short_list)
                list_swap(short_list,  class_dict[class_list], index1, index2)
            index1 = index2
        
        for i in range(len(class_dict[class_list])):
            if (i == class_log.iat[class_list, 5]):
                f.write("Cut Off. All Below Did Not Successfully Register.\n")
                weekly_log.iat[class_dict[class_list][i][2], 5] = 0
                #weekly_log.at[class_dict[class_list][i][2], 'Registered'] = 0
                f.write(str(class_dict[class_list][i][0]) + " " + str(class_dict[class_list][i][1]) + "\n")
            else:
                weekly_log.iat[class_dict[class_list][i][2], 5] = 1
                #weekly_log.at[class_dict[class_list][i][2], 'Registered'] = 1
                f.write(str(class_dict[class_list][i][0]) + " " + str(class_dict[class_list][i][1]) + "\n")

        f.close()

def delete_duplicates(weekly_log):
    dupli = weekly_log.duplicated()
    count = 0
    index = 0
    while(index < len(weekly_log)):
        if (dupli[count]):
            weekly_log = weekly_log.drop(labels = index, axis = 0)
            index -= 1
        count += 1
        index += 1
    return weekly_log

def list_swap(src, dst, idx1, idx2):
    for i in range(idx2-idx1):
        dst[idx1+i] = src[i]

# main driver
print("Welcome to Love 21 Registrator." 
      "Please make sure the files are labeled according to the specifications \nin the READ.ME file.")

master_log = read_in_log("master_log.csv", 'm')
class_log = read_in_log("class_log.csv", 'c')
student_log = read_in_log("student_log.csv", 's')
weekly_log = read_in_log("weekly_log.csv", 'n')

weekly_log = delete_duplicates(weekly_log)

while(True):
    is_first = input("\nHas a Master Log Been Created Before(Y/N): ")
    if (is_first == 'N'): # No Master Log existed before
        no_ml_bf()
        first = True
        break;
    elif(is_first == 'Y'):
        brute_force_count_points(weekly_log, student_log, master_log)
        first = False
        break;
    else:
        print("----------------------------------------------------------")
        print("\nInvalid Option. Please choose between \'Y\' or \'N\'. \n")
        print("----------------------------------------------------------")


class_dict = {}
assign_class(class_dict)


master_log.append(weekly_log)

#print(master_log)
if (first):
    master_log = weekly_log

#print(master_log)
write_to_log("master_log.csv", 'm') #should just overwrite it
write_to_log("class_log.csv", 'c')
write_to_log("student_log.csv", 's')
write_to_log("weekly_log.csv", 'n') #not essential


print("Done")

