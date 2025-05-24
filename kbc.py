import random

Que1 = "Que>> The Paithan (Jayakwadi) Hydro-electric project, completed with the help of Japan, is on the river \n"
Que2 = "Que>> The percentage of irrigated land in India is about \n"
Que3 = "Que>> The southernmost point of peninsular India, that is, Kanyakumari, is \n"
Que4 = "Que>> The pass located at the southern end of the Nilgiri Hills in south India is called \n"
Que5 = "Que>> The principal copper deposits of India lie in which of the following places? \n"
Que6 = "Que>> The ratio of width of our National flag to its length is :\n"
Que7 = "Que>> Rabindranath Tagore's 'Jana Gana Mana' has been adopted as India's National Anthem. How many stanzas of the said song were adopted?\n"
Que8 = "Que>> Dandia' is a popular dance of :\n"
Que9 = "Que>> The National Anthem was first sung in the year:\n"
# Que = [Que1,Que2,Que3,Que4,Que5]

Option1 = ["1> Cauvery",
"2> Ganga",
"3> Narmada",
"4> Godavari \n"]

Option2 = ["1> 45","2> 65","3> 35","4> 25 \n"]

Option3 = ["1> North of Tropic of Cancer",
"2> North of the Equator",
"3> South of the Capricorn",
"4> South of the Equator \n"]

Option4 = ["1> The Palghat gap",
"2> The Bhorghat pass",
"3> The Thalgat pass",
"4> The Bolan pass \n"]
Option5 = ["1> Hazaribag and Singbhum of Bihar",
"2> Khetri and Daribo areas of Rajasthan",
"3> Anantapur in Andhra Pradesh",
"4> Siwaliks in Uttar Pradesh and in Karnataka \n"]
Option6 = ["1> 3:5","2> 3:2","3> 2:4","4> 3:4"]

Option7 = ["1> Only the first stanza",
"2> The whole song",
"3> Third and Fourth stanza",
"4> First and Second stanza \n"]
Option8 = ["1> Punjab",
"2> Gujarat",
"3> Tamil Nadu",
"4> Maharashtra \n"]
Option9 = ["1> 1936",
"2> 1913",
"3> 1911",
"4> 1935 \n"]

dic = {
    Que1:[Option1,"D"],
    Que2:[Option2,"C"],
    Que3:[Option3,"B"],
    Que4:[Option4,"A"],
    Que5:[Option5,"A"],
    Que6:[Option6,"B"],
    Que7:[Option7,"A"],
    Que8:[Option8,"B"],
    Que9:[Option9,"C"]
}

prize =1000
lis =list(dic.keys())
for j in range(0,len(lis)):
    ran= random.choice(lis)
    print(f"\n{j+1}{ran}") #print question 
    print(*dic[ran][0],sep="\n") #print option of question
    ans = input("Enter your option in alphabate form and press 'Q' for quit the game : ")
    ans= ans.capitalize()
    if not (("A" <= ans <= "D") or (ans == "Q")):
        raise ValueError("The value is not between 'A' and 'D' ,or 'Q'.")
    if ans == "Q":
        print ("you quit the game ")
        print("Thank you for playing the game")
        print("your wining prize is ".upper(),prize)
        break
    for i in range(0,len(dic)):
        if (ran == lis[i]) and (ans==dic[ran][1]):
            print("your answer is correct".upper()) 
            prize=prize*2
            print("your total prize now is ".upper(),prize)
    if (ans!=dic[ran][1] ):
        print("you lose the game ".upper())
        print("your wining prize is ".upper(),prize)
        break
    dic.pop(ran)   
    lis =list(dic.keys()) #it make the update keys list after the pop of the question

















