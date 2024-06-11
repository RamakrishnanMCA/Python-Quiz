import requests   #pip install requests
import json
import html
import random



url = "https://opentdb.com/api.php?amount=1&category=18&type=multiple"   #get api url from https://opentdb.com/api_config.php this website tailor made your quiz
gameend=""
score=0
question_no = 0

while gameend != "quit":

    req = requests.get(url)
    if req.status_code == 200:
        data_valid = False
        options=1
        api_data = json.loads(req.text)
        question = api_data["results"][0]["question"]
        correct_answer = api_data["results"][0]["correct_answer"]
        incorrect_answers = api_data["results"][0]["incorrect_answers"]
        incorrect_answers.append(correct_answer)
        random.shuffle(incorrect_answers)

        print(str(question_no+1)+"." + html.unescape(question)+"\n")
        question_no+=1

        for answer in incorrect_answers:
            print(str(options)+" "+html.unescape(answer))
            options+=1

        while data_valid == False:
            user_answer = input("\n Choose the correct option number: ")
            try:
                user_answer = int(user_answer)
                if user_answer > len(incorrect_answers) or user_answer<=0:
                    print("Please type the Valid Number")
                else:
                    data_valid=True
            except:
                print("Please enter Valid Number")

        if incorrect_answers[(user_answer)-1]== correct_answer:
            print("Congratulations, you are Correct, " + html.unescape(correct_answer))
            score+=1
        else:
            print("Sorry, " + html.unescape(incorrect_answers[(user_answer)-1])+" is incorrect, the correct answer is " + html.unescape(correct_answer))

        print("\n-------------------------")
        print("Score: " +str(score)+" / " + str(question_no))

        print("-------------------------")

        gameend=input("\n Continue - Press Enter , Exit - Type 'quit': ").lower()
        print("\n")
        
    else:
        gameend=input("Sorry, something wrong in my side. Press enter to continue or Type 'quit' to exit ").lower()


if score>(question_no)/2:
    print("\nTotal Score: " +str(score)+" / " + str(question_no))
    print("You Done a Good job, Keep it up\n")
else:
    print("Total Score: " +str(score)+" / " + str(question_no))
    print("Don't Worry, You learned a lot Today\n")
print("\nThank you, Have a nice day")
        
        
        
