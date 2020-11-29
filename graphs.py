import collections
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from name_conclusions import figureNameSimilarity
from subject_conclusions import subject_alphanum_grade_manipulation
from subject_conclusions import subject_numeric_grade_manipulation
from preprocessing import dataset


def nameSimilarityGraphs():

    gradeDifs = figureNameSimilarity()

    mostFrequentDifs = dict(collections.Counter(gradeDifs).most_common(35))

    print(mostFrequentDifs)

    keySorted = collections.OrderedDict(sorted(mostFrequentDifs.items()))

    plt.bar(range(len(keySorted)), list(keySorted.values()), align='center')
    plt.xticks(range(len(keySorted)), list(keySorted.keys()))
    plt.xlabel('Grade difference in percentage')
    plt.ylabel('Occurence')
    plt.title('Grade difference between consecutive students with the same lastname (high probability of family ties) ')

    plt.show()

# nameSimilarityGraphs()


def alphanum_grade_subjectGradeGraphs():
    
    subject_grade_lists = subject_alphanum_grade_manipulation(dataset)

    print(subject_grade_lists.keys())

    dict_keys = list(subject_grade_lists)

    for index, subject_grade_list in enumerate(subject_grade_lists.values()):

        # remove nan values
        subject_grade_list = [x for x in subject_grade_list if str(x) != 'nan']

        # print(subject_grade_list)

        keySorted = collections.OrderedDict(sorted(Counter(subject_grade_list).items()))

        print(keySorted)

        plt.bar(range(len(keySorted)), list(keySorted.values()), align='center')
        plt.xticks(range(len(keySorted)), list(keySorted.keys()))
        plt.xlabel('Grade')
        plt.ylabel('Occurence')
        plt.title(f'Grades in subject {dict_keys[index]} in the alphanumerical grading system (A1, A2, B1, B2, C1, C2 ,D1 , D2, E)')
        plt.show()


# alphanum_grade_subjectGradeGraphs()


def arithmetic_grade_subjectGradeGraphs():
    
    subject_grade_lists = subject_numeric_grade_manipulation(dataset)

    dict_keys = list(subject_grade_lists)

    print(subject_grade_lists.keys())

    for index, subject_grade_list in enumerate(subject_grade_lists.values()):

        # print(subject_grade_list)
                
        rounded_grade_list = []
        for str_grade in subject_grade_list:
            try:
                grade = round(int(str_grade)/5)*5
                rounded_grade_list.append(grade)
            except ValueError:
                pass
          
        # print(rounded_grade_list)
       
        # print(Counter(rounded_grade_list))

        keySorted = collections.OrderedDict(sorted(Counter(rounded_grade_list).items()))

        # print(keySorted)

        plt.bar(range(len(keySorted)), list(keySorted.values()), align='center')
        plt.xticks(range(len(keySorted)), list(keySorted.keys()))
        plt.xlabel('Grade')
        plt.ylabel('Occurence')
        plt.title(f'Grades in subject {dict_keys[index]} in 0-100 scale')
        plt.show()


# arithmetic_grade_subjectGradeGraphs()