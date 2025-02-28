import random
import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()
engine.setProperty('rate',150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Questions and Options
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

Option1 = ["A> Cauvery",
"B> Ganga",
"C> Narmada",
"D> Godavari \n"]

Option2 = ["A> 45","B> 65","C> 35","D> 25 \n"]

Option3 = ["A> North of Tropic of Cancer",
"B> North of the Equator",
"C> South of the Capricorn",
"D> South of the Equator \n"]

Option4 = ["A> The Palghat gap",
"B> The Bhorghat pass",
"C> The Thalgat pass",
"D> The Bolan pass \n"]
Option5 = ["A> Hazaribag and Singbhum of Bihar",
"B> Khetri and Daribo areas of Rajasthan",
"C> Anantapur in Andhra Pradesh",
"D> Siwaliks in Uttar Pradesh and in Karnataka \n"]
Option6 = ["A> 3:5","B> 3:2","C> 2:4","D> 3:4"]

Option7 = ["A> Only the first stanza",
"B> The whole song",
"C> Third and Fourth stanza",
"D> First and Second stanza \n"]
Option8 = ["A> Punjab",
"B> Gujarat",
"C> Tamil Nadu",
"D> Maharashtra \n"]
Option9 = ["A> 1936",
"B> 1913",
"C> 1911",
"D> 1935 \n"]

# Question dictionary
dic = {
    Que1: [Option1, "D"],
    Que2: [Option2, "C"],
    Que3: [Option3, "B"],
    Que4: [Option4, "A"],
    Que5: [Option5, "A"],
    Que6: [Option6, "B"],
    Que7: [Option7, "A"],
    Que8: [Option8, "B"],
    Que9: [Option9, "C"]
}

prize = 1000
lis = list(dic.keys())

for j in range(len(lis)):
    ran = random.choice(lis)
    
    # Print and speak question
    print(f"\n{j+1}{ran}")
    speak(ran)
    
    # Print and speak options
    for option in dic[ran][0]:
        print(option)
        speak(option)
    
    # Prompt user for input
    mes = "Enter your option in alphabet form and press 'Q' to quit the game"
    print(mes)
        
    speak(mes)
    ans = input()
    ans = ans.capitalize()
    speak(f"you enter the option {ans}")
    if not (("A" <= ans <= "D") or (ans == "Q")):
        raise ValueError("The value is not between 'A' and 'D', or 'Q'.")
    
    if ans == "Q":
        quit = "You quit the game."
        thank_you_message = "Thank you for playing the game."
        prize_message = f"Your winning prize is {prize}"
        
        print(quit)
        speak(quit)

        print(thank_you_message)
        speak(thank_you_message)

        print(prize_message.upper())
        speak(prize_message)
        break
    
    if ans == dic[ran][1]:
        correct_message = "Your answer is correct"
        prize *= 2
        total_prize_message = f"Your total prize now is {prize}"
        
        print(correct_message.upper())
        speak(correct_message)
        
        print(total_prize_message.upper())
        speak(total_prize_message)
        dic.pop(ran)
        lis = list(dic.keys())  # Update keys list after popping the question
    else:
        lose_message = "Your answer is incorrect\nYou lose the game"
        prize_message = f"Your winning prize is {prize}"
        
        print(lose_message.upper())
        speak(lose_message)
        print(prize_message.upper())
        speak(prize_message)
        break