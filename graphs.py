import collections
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from name_conclusions import figureNameSimilarity
from subject_conclusions import subject_manipulation
from preprocessing import dataset


def nameSimilarityGraphs():

    gradeDifs = figureNameSimilarity()

    mostFrequentDifs = dict(collections.Counter(gradeDifs).most_common(45))

    # print(mostFrequentDifs)

    keySorted = collections.OrderedDict(sorted(mostFrequentDifs.items()))

    plt.bar(range(len(keySorted)), list(keySorted.values()), align='center')
    plt.xticks(range(len(keySorted)), list(keySorted.keys()))

    # vale kai onoma sto grafhma opws kai legend mporei kai color!!!

    plt.show()

# nameSimilarityGraphs()



def subjectGradeGraphs():
    
    subject_grade_lists = subject_manipulation(dataset)


    print(subject_grade_lists.keys())

    for subject_grade_list in subject_grade_lists.values():

        # remove nan values
        subject_grade_list = [x for x in subject_grade_list if str(x) != 'nan']

        # print(subject_grade_list)

        '''
        rounded_grade_list = []
        for grade in subject_grade_list:

            try:
                grade = round(grade/5)*5
                rounded_grade_list.append(grade)
            except TypeError:
                pass
        print(rounded_grade_list)

        print(Counter(rounded_grade_list))
        '''

        keySorted = collections.OrderedDict(sorted(Counter(subject_grade_list).items()))

        # print(keySorted)

        plt.bar(range(len(keySorted)), list(keySorted.values()), align='center')
        plt.xticks(range(len(keySorted)), list(keySorted.keys()))
        plt.show()


subjectGradeGraphs()