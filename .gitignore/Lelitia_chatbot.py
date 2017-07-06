#Lelitia
#My first chatbot
import random, time
pos_response = ["Ohh cool", "Thats interesting", "Coooollll", "Nice :-)", "Coolio"]
neg_response = ["Aha yeah", "Okay yeah", "Okayyy", "Ahhh yeah", "Okay"]
age = 0
likes = []
dislikes = []
things = ["sport", "cycling", "football", "playing on an x-box", "playing on a playstation",
          "sleeping", "planes", "science", "computers", "lego", "rugby", ]
def hello():
    hi = ["Hello", "Hi", "Hey"]
    how = ["I am a computer I cannot feel emotions ;->", "I am good thanks", "I'm alright", "Goooddddd thx"]
    print hi[random.randint(0, 2)]
    inp = raw_input("I'm Lelitia, what is your name? ").lower()
    name = inp
    name = name[0].upper() + name[1:]
    if name == "Aaron" :
        inp = raw_input("Are you Aaron Ramsey, My creator!?!?!? ").lower()
        if inp == "yeah" or inp == "yes" or inp == "yess" or inp == "yesss" or inp == "yeahh" or inp == "yeahhh" :
            print "The One and Only Aaron Ramsey. WOOOOOO!!!!"
        else :
            print "You are an inferior Aaron"
    inp = raw_input("How are you %s???" % name).lower()
    words = inp.split()
    if "how" in words :
        num = words.index("how")
        if words[num+1] == "are" and (words[num+2] == "you?" or words[num+2] == "you") :
            print how[random.randint(0, 1)]
    elif "you" in words or "you?" in words :
        print how[random.randint(0, 1)]
    return name

def jokes() :
    global name
    text = open("jokes.txt", "r")
    joke = text.readlines()
    no = (len(joke))/2
    the_joke = (random.randint(0, no))*2
    answer = the_joke + 1
    inp = raw_input(joke[the_joke].strip("\n") + "- ")
    if inp.lower() != (joke[answer].strip("\n")).lower() :
        inp = raw_input(joke[answer].strip("\n") + "- ").lower()
        if "ha" in inp or "lol" in inp or "rofl" in inp :
            print "Woooo, I made you laugh, that's sooo good because I struggle with human emotions :->"
    else :
        inp = raw_input("Yes!!! Haha, great minds think alike %s " % name)
    questions()

def questions() :
    global likes, dislikes, things, counter, age, pos_response, neg_response
    qs = open("Questions.txt", "r")
    question = qs.readlines()
    the_question = question[random.randint(0, len(question)-1)]
    if "?" not in the_question:
        thing = random.randint(0, len(things)-1)
        while thing in likes :
            thing = random.randint(0, len(things)-1)
        while thing in dislikes :
            thing = random.randint(0, len(things)-1)
        the_question = the_question.strip("\n") + things[thing] + "?"
        inp = raw_input(the_question + " ").lower()
        words = inp.split()
        print words
        print likes
        
        if "joke" in words and ("hear" in words or "tell" in words) :
            jokes()            
        elif "yes" in words or "yeah" in words or "yesss" in words or "yes," in words or "yeah," in words or "yesss," in words :
            likes.append(things[thing])
            print pos_response[random.randint(0, len(pos_response)-1)]
        elif "no" in words or ("not" in words and "really" in words) or "naaa" in words or "na" in words or "naa" in words or "noo" in words or "nooo" in words or "no," in words or ("not" in words and "really," in words) or "naaa," in words or "na," in words or "naa," in words or "noo," in words or "nooo," in words:
            dislikes.append(things[thing])
            print neg_response[random.randint(0, len(pos_response)-1)]
        elif ("do" in words and ("you" in words or "you?" in words)) or (("what" in words or "how" in words) and "about" in words and ("you" in words or "you?" in words)) :
            responses = ["Yeah its alright", "Not really", "Kinda", "Yeah, I really like it", "Hmm, not really", "I just dont like it, really"]
            print responses[random.randint(0, len(responses)-1)]
        else :
            print pos_response[random.randint(0, len(pos_response)-1)]
            
    elif "old" in the_question and age == 0 :
        age = 0
        inp = raw_input(the_question + " ")
        inp1 = inp
        words = inp.split()
        if "joke" in words and ("hear" in words or "tell" in words) :
            jokes()
        while age < 1 :
            if "how" in words and "old" in words and ("you" in words or "you?" in words):
                print "I have no age, I am infinitely old and young"
                q = True
            for item in words :
                try :
                    item = int(item)
                    age = item
                    break
                except :
                    age = 0
            if age == 0 :
                inp = raw_input("I dont understand ages in text, :-(, please enter in again in a number- ").lower()
                inp = raw_input(the_question + " ")
            else :
                break
        age_response = ["Ohh cool", "Aha", "Okay"]
        print age_response[random.randint(0, len(age_response)-1)]

    elif "old" in the_question and age != 0 :
        questions()
        
    elif "doing" in the_question and counter > 20 :
        inp = raw_input(the_question.strip("\n") + " ").lower()
        words = inp.split()
        if "joke" in words and ("hear" in words or "tell" in words) :
            jokes()
        if ("cute" in words or "hot" in words or "pretty" in words) and ("chatbot" in words or ("chat" in words and "bot" in words)) and ("not" not in words) :
            print "Aww thanks"
        if "what" in words and "are" in words and "you" in words and ("doing?" in words or "doing" in words or "doin" in words or "doin?" in words or "doin'" in words or "doin'?" in words) :
            print "Talking to you ;-)"
        elif "what" in words and "about" in words and ("you" in words or "you?" in words) :
            print "Talking to you ;-)"

def questions_two() :
    global likes, dislikes
    option = random.randint(0, 1)
    if option == 0 and likes > 1 :
        num = len(likes)-1
        like = likes[random.randint(0, num)]
        inp = raw_input("Why do you like %s? " % like)
        words = inp.split()
        if "joke" in words and ("hear" in words or "tell" in words) :
            jokes()
        response = ["Ohh cool", "Sounds interesting ;-)", "Ahh yeah", "Interesting"]
        print response[random.randint(0, len(response)-1)]
        time.sleep(0.5)
    if option == 1 and dislikes > 1 :
        num = len(dislikes)-1
        dislike = dislikes[random.randint(0, num)]
        inp = raw_input("Why don't you like %s?" % dislike)
        words = inp.split()
        if "joke" in words and ("hear" in words or "tell" in words) :
            jokes()
        response = ["Ah yeah", "Okayy", "I understand, yeah", "Yeahh"]
        print response[random.randint(0, len(response)-1)]
        time.sleep(0.5)

def questioned() :
    global words
    how = ["I am a computer I cannot feel emotions ;->", "I am good thanks", "I'm alright", "Goooddddd thx"]
    if "how" in words :
        num = words.index("how")
        if words[num+1] == "are" and (words[num+2] == "you?" or words[num+2] == "you") :
            print how[random.randint(0, 1)]
    if "what" in words and "are" in words and "you" in words and ("doing?" in words or "doing" in words or "doin" in words or "doin?" in words or "doin'" in words or "doin'?" in words) :
        print "Talking to you ;-)"
    elif "what" in words and "about" in words and ("you" in words or "you?" in words) :
        print "Talking to you ;-)"

#while True :
def main() :
    global counter
    counter += 1
    choice = random.randint(0, 8)
    
    if choice == 1 or choice == 5 or choice == 6 or choice == 7 :
        questions()
        main()
        
    elif (choice == 2 or choice == 4 or choice == 8) and (len(likes) > 1 or len(dislikes) > 1) :
        questions_two()
        main()
        
    elif choice == 3 or choice == 0:
        inp = raw_input("Talk to me - ").lower()
        words = inp.split()
        if "joke" in words and ("hear" in words or "tell" in words) :
            jokes()
            main()
            
        if "i" in words and "like" in words :
            if inp.strip("i like ") in dislikes :
                dislikes.remove(inp.strip("i like "))
            if "you" in words :
                likes.append("Me")
            else :
                likes.append(inp.strip("i like "))
            print pos_response[random.randint(0, len(pos_response)-1)]
            main()
                
        elif "i" in words and "dont" in words and "like" in words :
            if inp.strip("i dont like ") in likes :
                likes.remove(inp.strip("i dont like "))
            if "you" in words :
                dislikes.append("Me")
            else :
                dislikes.append(inp.strip("i dont like"))
            print neg_response[random.randint(0, len(neg_response)-1)]
            main()
                
        elif "i" in words and "don't" in words and "like" in words :
            if inp.strip("i don't like ") in likes :
                likes.remove(inp.strip("i don't like "))
            if "you" in words :
                dislikes.append("Me")
            else :
                dislikes.append(inp.strip("i don't like"))
            print neg_response[random.randint(0, len(neg_response)-1)]
            main()
                
        elif "i" in words and "do" in words and "not in words" and  "like" in words :
            if inp.strip("i do not like ") in likes :
                likes.remove(inp.strip("i do not like "))
            if "you" in words :
                dislikes.append("Me")
            else :
                dislikes.append(inp.strip("i do not like"))
            print neg_response[random.randint(0, len(neg_response)-1)]
            main()
                
        elif "?" in words[len(words)-1] :
            questioned()
            main()

        elif "question" in words or "questions" in words :
            if "ask" in words and "me" in words and "a" in words :
                choice = random.randint(0, 2)
                if choice == 0 or choice == 1 :
                    questions()
                elif (choice == 2 or choice == 3) and (len(likes) > 1 or len(dislikes) > 1) :
                    questions_two()
            elif "me" in words :
                if words.index("me") == words.index("question") + 1 :
                    choice = random.randint(0, 2)
                    if choice == 1 or choice == 0 :
                        questions()
                    elif (choice == 2 or choice == 3) and (len(likes) > 1 or len(dislikes) > 1) :
                        questions_two()
            elif inp == "question" or words[0] == "question" :
                choice = random.randint(0, 3)
                if choice == 1 or choice == 0:
                    questions()
                elif (choice == 2 or choice == 3) and (len(likes) > 1 or len(dislikes) > 1) :
                    questions_two()
            main()
        else :
            dont_understand = ["Sorry i don't understand %s ", "Sorry ,I don't understand that command %s ", "Sorrryyyyy, I don't understand that command %s ", "Eeekkkk, i don't know that command %s "]
            num = random.randint(0, len(dont_understand)-1)
            print dont_understand[num] % name
            main()
    main()

name = hello()
counter = 0
main()
