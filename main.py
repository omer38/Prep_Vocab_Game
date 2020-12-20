#vocabulary quiz uygulaması
from kelimeler import dictionary
import random
count_all_questions = 1
count_correct = 0
def new_question(a,b):

    question = random.choice(list(dictionary.keys()))
    print(question)
    correct_answer = (dictionary[question])

    wrong1=random.choice(list(dictionary.values()))
    wrong2=random.choice(list(dictionary.values()))

    if wrong1==wrong2 or wrong1==correct_answer or wrong2==correct_answer:
        while  wrong1==wrong2 or wrong1==correct_answer or wrong2==correct_answer:
            if wrong1==wrong2:
                wrong1 = random.choice(list(dictionary.values()))
            if wrong1==correct_answer:
                wrong1 = random.choice(list(dictionary.values()))
            if wrong2==correct_answer:
                wrong2 = random.choice(list(dictionary.values()))

    list1=[correct_answer,wrong1,wrong2]
    list2=sorted(list1)
    print("a){}\nb){}\nc){}".format(list2[0],list2[1],list2[2]))
    count=0
    for i in list2:
        if i ==correct_answer:
            final_count=count
            break
        else:
            count+=1
    if final_count==0:
        correct_answer="a"
    elif final_count==1:
        correct_answer="b"
    elif final_count==2:
        correct_answer="c"

    answer=input("Type the correct answer: ")
    if answer==correct_answer:
        print("That's correct!!!!")
        a+=1

    else:
        print("Wrong answer:(")

    print(f"Your score is {a}/{b}")
    return a


def new_word_addition():
    x=input("Type new word: ")
    y=input("definition of the word: ")
    dictionary[x]=y

while True:
    print("""
    ****************************************
          Welcome to Omer Tugrul's Vocab Game
          Press:
             1.new word addition
             2.new question 
             3.exit
    ****************************************
             """)
    choice=int(input("Choose the operation: \n"))
    if choice==1:
        new_word_addition()
    elif choice==2:
        count_correct=new_question(count_correct , count_all_questions)
        count_all_questions+=1

    elif choice==3:
        print("game is over")
        break
