import pandas as pd
import itertools
from preprocessing import get_top_subjects
from preprocessing import dataset


def subject_manipulation(data):

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


# subject_manipulation(dataset)