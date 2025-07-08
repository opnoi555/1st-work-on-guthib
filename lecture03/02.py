score01 = float(input("Enter the score for test 1 : "))
score02 = float(input("Enter the score for test 2 : "))
score03 = float(input("Enter the score for test 3 : "))

average_score = float((score01 + score02 + score03)/3)
if float(average_score) > 95 :
    print("Your average score is :", format(average_score, "0.2f"))
    print("Congratulation!")
    print("That is a great average!")
else:
    print("Your average score is :", format(average_score, "0.2f"))