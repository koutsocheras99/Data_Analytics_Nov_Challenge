import pandas as pd
import itertools
import decimal
from preprocessing import get_subjects_info
from collections import Counter
from itertools import islice 
from preprocessing import dataset


def findSiblingsNum(data):

    df = pd.read_csv(data)

    l_names = []
    numSiblings = 0

    # iterate all students with itertuples
    for index, row in enumerate(df.itertuples()):

        # get the student name(row[2]) and specifically the last name (.split()[0])
        try:
            last_name = row[2].split()[0]
        except AttributeError:
            pass
 
        if last_name not in l_names:
            l_names.append(last_name)
        else:
            # print(last_name)
            numSiblings+=1
        
        # every 5 students clear the list (for memory efficiency reasons)
        if index%5==0:
            l_names.clear()

        
    # siblings number = 41803!
    print(numSiblings)
   
# findSiblingsNum(dataset)


def names_grades_manipulation(data):

    df = pd.read_csv(data)

    # list that contains all the subject names(check preprocessing.py)
    _, subjects = get_subjects_info(data)

    last_names = []
    grades = []
    
    # iterate all students with itertuples
    for row in df.itertuples():

        # get the student name(row[2]) and specifically the last name (.split()[0])
        try:
            last_name = row[2].split()[0]
        except AttributeError:
            pass

        student_overall_grade = 0
        numSubjects = 0

        for index, subject in enumerate(row):
   
            # if there is a column with a subject that belongs to the subjects(list) then get the grade(in percentage) which is 3 cells right
            if subject in subjects:

                # the subject grade is 3 cells right
                subject_grade = row[index+3]
                
                try:
                    student_overall_grade += int(subject_grade)
                    numSubjects += 1
                except ValueError:
                    pass

                # print(subject)
                # print(subject_grade)
        
        try:
            # in the grades list append the cgpa from all courses
            grades.append(student_overall_grade/numSubjects) 
            # append last name in last names list
            last_names.append(last_name) 

        except ZeroDivisionError:
            pass

        # print('\nLast Name: '+last_name)
        # print(f'Student overall grade: {student_overall_grade}')
        # print(f'Student number of subjects: {numSubjects}')
   
    # print(grades)   
    # print(last_names)  

    return last_names, grades


def figureNameSimilarity():

    names, grades = names_grades_manipulation(dataset)
    
    overall_grade_dif = 0
    grade_dif_list = []
    numSiblings = 0

    l_names = []

    for index_name, next_name in zip(enumerate(names),names[1:]):

        # print(index_name)
        # print(next_name)

        if index_name[1] not in l_names:
            l_names.append(index_name[1])
        else:

            # get the differernce of grades between the consecutive students who have the same last name        
            grade_dif = round(abs(grades[index_name[0]]-grades[index_name[0]-1]),1)

            overall_grade_dif += grade_dif
            numSiblings += 1

            # round the grade difference to next 1 (for example 8.8 ~> 9, 8.4 ~> 8)
            grade_dif = decimal.Decimal(grade_dif).quantize(decimal.Decimal('1'),rounding=decimal.ROUND_HALF_UP)

            grade_dif_list.append(grade_dif)

            
        if index_name[0]%5==0:
            l_names.clear()

 
    mean_grade_dif = overall_grade_dif/numSiblings

    # print('The mean-average grade difference(in 100) between all siblings is: {:.2f}'.format(mean_grade_dif))

    # print(Counter(grade_dif_list))

    return Counter(grade_dif_list)

# figureNameSimilarity()
