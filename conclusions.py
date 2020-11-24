import pandas as pd
from preprocessing import get_subjects_info

dataset = 'test.csv'

def findSiblingsNum(data):

    df = pd.read_csv(data)

    l_names = []
    numSiblings = 0

    # iterate all students with itertuples
    for index, row in enumerate(df.itertuples()):

        # get the student name(row[2]) and specifically the last name (.split()[0])
        try:
            last_name = row[2].split()[0]
        except AttributeError as e:
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


def names_manipulation(data):

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
        except AttributeError as e:
            pass

        # append ALL last names in list
        last_names.append(last_name)

        for index, subject in enumerate(row):
            # if there is a column with a subject that belongs to the subjects(list) then get the grade(in percentage) which is 3 cells right
            if subject in subjects:
                print(subject)
                print(row[index+3])

        # MENEI NA BGAZEIS GIA TON KATHE STUDENT TO MESO ORO KAI NA TO BAZEIS STO GRADE LIST. META THA KANEIS ITERATE LAST_NAME LIST KAI GRADE LIST(ME ZIP?)
        # KAI THA ELEGXEIS AN EINAI ISA TA CONSECUTIVE CELLS STO LAST NAME LIST KAI META THA KOITAS TOUS EKASTOTE GRADE GIA PORISMA

    # print(last_names)


names_manipulation(dataset)
