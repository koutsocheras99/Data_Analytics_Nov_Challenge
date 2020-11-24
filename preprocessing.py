import numpy as np
import re
import csv
import itertools
from itertools import islice 


dataset = 'test.csv'


def get_subjects_info(data):

    # open dataset using csv reader function
    data = csv.reader(open(dataset))

    # initializing the list that will contain the subjects names
    subject_list = []

    # dictionary containing the subject name and the occurrence-how many students took it
    subject_occurrence = dict()
        
    # iterating all students a.k.a all rows
    for student in data:

        # print(student)

        # keep only uppercase strings with len>=3
        r = re.compile('[A-Z][A-Z][A-Z]')

        # format every line/row in a list applying(filtering) the regex filter above
        student_list = list(filter(r.match, student))

        # print(student_list)
        
        # iterating each student list (first item is the name and is irrelevant with the subject name)
        for subject in student_list[1:]:
        
            # if subject not already in the subject list add it
            if subject not in subject_list:
                subject_list.append(subject)
                

            # if subject already in the subject occurrence dictionary +=1 occurrency of that particular subject
            if subject in subject_occurrence:
                subject_occurrence[subject] += 1
            # if subject not already in the subject occurrence dictionary set occurrency to 1(that means that it is the first time we iterate it)
            elif subject not in subject_occurrence:
                subject_occurrence[subject] = 1
        

    # sort subject occurrency dictionary based on value (item[1])
    subject_occurrence = dict(sorted(subject_occurrence.items(), key=lambda item: item[1], reverse=True))

    # print subject names with their occurrence(sorted)
    # print(subject_occurrence)

    # number of subjects = 172!
    # print(len(subject_occurrence))

    # print only the subject names
    # print(subject_list)

    return subject_occurrence, subject_list


# get_subjects_info(dataset)


def get_top_subjects(numSubjects):

    # get all subjects in dictionary form from the function above
    all_subjects, _ = get_subjects_info(dataset)

    # get the top N (most appeared) subjects
    topSubjects = dict(itertools.islice(all_subjects.items(), numSubjects))

    # print(topSubjects)

    # only the most frequent subject names
    # print(list(topSubjects.keys()))

    return list(topSubjects.keys())


get_top_subjects(20)
