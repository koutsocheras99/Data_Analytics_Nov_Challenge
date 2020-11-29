import pandas as pd
import itertools
import statistics
from preprocessing import get_top_subjects
from preprocessing import get_arithmetic_grade_subjects
from preprocessing import dataset


def subject_alphanum_grade_manipulation(data):

    df = pd.read_csv(data)

    topSubjects = get_top_subjects(10)

    # initializing lists with the subject name in a dictionary form
    subject_grade_lists = {i: [] for i in topSubjects}

    # print(subject_grade_lists)

    # iterate all rows with itertuples
    for row in df.itertuples():
        # print(row)

        # iterating all cells of each row-student
        for index, cell in enumerate(row):
            if cell in topSubjects:
                
                # subject grade is 4 cells right
                subject_grade = row[index+4]

                # in the dictonary(subject_lists) that contains all the top subjects lists append in the specific subject list the corresponding grade
                subject_grade_lists[cell].append(subject_grade)

                # print(cell)
                # print(subject_grade)

    # print(subject_grade_lists)

    return subject_grade_lists


# subject_alphanum_grade_manipulation(dataset)


def subject_numeric_grade_manipulation(data):

    df = pd.read_csv(data)

    topSubjects = get_arithmetic_grade_subjects()

    # initializing lists with the subject name in a dictionary form
    subject_grade_lists = {i: [] for i in topSubjects}

    # print(subject_grade_lists)

    # iterate all rows with itertuples
    for row in df.itertuples():
        # print(row)

        # iterating all cells of each row-student
        for index, cell in enumerate(row):
            if cell in topSubjects:
                
                # subject grade is 3 cells right
                subject_grade = row[index+3]

                # dont add empty grades
                if subject_grade != '    ':

                    # in the dictonary(subject_lists) that contains all the top subjects lists append in the specific subject list the corresponding grade
                    subject_grade_lists[cell].append(subject_grade)

                # print(cell)
                # print(subject_grade)

    # print(subject_grade_lists)

    return subject_grade_lists

# subject_numeric_grade_manipulation(dataset)


def generalGradeFacts():

    subject_grade_lists = subject_numeric_grade_manipulation(dataset)

    dict_keys = list(subject_grade_lists)

    for index, subject_str_grade_list in enumerate(subject_grade_lists.values()):

        subject_int_grade_list = []

        # print(subject_str_grade_list)

        for str_grade in subject_str_grade_list:
            try:
                subject_int_grade_list.append(int(str_grade))
            except ValueError:
                pass

        # print(subject_int_grade_list)
        
        standard_deviaton = statistics.stdev(subject_int_grade_list)
        mean = statistics.mean(subject_int_grade_list)

        print('The standard deviaton for subject ', dict_keys[index], ' is {:.2f}'.format(standard_deviaton))
        print('The mean for subject ', dict_keys[index], ' is {:.2f}'.format(mean))


# generalGradeFacts()
