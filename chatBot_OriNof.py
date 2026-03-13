#=====================
#SMART CHATBOT PROJECT
#=====================

#student name = ori nof
#bot name = snoopy
#bot purpose = have fun!

import random
import time

bot_name = "snoopy the bot"


# =============================================================================
# STEP 1: BOT PERSONALITY DATA
# =============================================================================

greetings = [
    "hello", "hi", "hey", "hi there", "hello there", "hey there",
    "good day",
    "nice to meet you", "pleasure to meet you", "welcome"
    ]

goodbyes = [
    "goodbye", "bye", "bye-bye",
    "see you", "see you later", "see you soon", "see you tomorrow", "see you next time",
    "take care", "take it easy",
    "farewell", "good night",
    "have a good night", "have a nice day", "have a great day",
    "be seeing you", "keep in touch", "stay safe", "bye for now",
    "adios", "cheers",
     "see you around", "have a good evening", "until we meet again" 
    ]

jokes = [
    "Why did the computer go to the doctor? Because it caught a virus.",
    "Why don't programmers like nature? Too many bugs.",
    "Why did the math book look sad? Because it had too many problems.",
    "Why did the student eat his homework? Because the teacher said it was a piece of cake.",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "What do you call a bear with no teeth? A gummy bear.",
    "Why did the bicycle fall over? Because it was two-tired.",
    "What do you call fake spaghetti? An impasta.",
    "Why can't your nose be 12 inches long? Because then it would be a foot.",
    "What do you call cheese that isn't yours? Nacho cheese.",
    "Why did the cookie go to the hospital? Because it felt crummy.",
    "What do you call a sleeping bull? A bulldozer.",
    "Why did the tomato turn red? Because it saw the salad dressing.",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
    "Why did the computer show up at work late? It had a hard drive."
    ]

shower_thoughts = [
    "If tomatoes are fruit, ketchup is technically a smoothie.",
    "Your age is just the number of times you've gone around the sun.",
    "Someone invented the word 'word'.",
    "The brain named itself.",
    "You will never see your own face except in a reflection.",
    "At some point, your parents put you down and never picked you up again.",
    "Every word in the dictionary is defined using other words.",
    "The first person who discovered milk probably had strange priorities.",
    "Your future self is watching you through memories.",
    "Most of the time elevators are just standing still waiting."
]

facts = [
    "Octopuses have three hearts.",
    "Honey never spoils and can last thousands of years.",
    "Bananas are technically berries.",
    "Sharks existed before trees.",
    "The human body has 206 bones.",
    "A day on Venus is longer than a year on Venus.",
    "Butterflies taste with their feet.",
        "The Eiffel Tower can grow taller in summer because of heat expansion.",
    "Water can boil and freeze at the same time under special conditions.",
    "Your brain uses about 20% of your body's energy."
]

compliments = [
    "You have a great sense of curiosity.",
    "You explain things really clearly.",
    "You seem like a thoughtful person.",
    "You ask smart questions.",
    "You have good ideas.",
    "You are good at learning new things.",
    "You seem very determined.",
    "You have a creative mind.",
    "You notice interesting details.",
    "You bring positive energy."
]

tips = [
    "Break big tasks into small steps.",
    "Take short breaks when studying.",
    "Drink enough water during the day.",
    "Write things down so you remember them better.",
    "Practice a little every day instead of a lot once.",
    "Sleep well before important tasks.",
    "Ask questions when you don't understand something.",
    "Keep your workspace organized.",
    "Review what you learned at the end of the day.",
    "Try to learn something new every day."
]

book_recommendations = [
    "The Hobbit",
    "Harry Potter and the Sorcerer's Stone",
    "Percy Jackson and the Lightning Thief",
    "The Hunger Games",
    "Ender's Game",
    "The Maze Runner",
    "The Giver",
    "The Chronicles of Narnia",
    "Artemis Fowl",
    "Eragon",
    "The Lord of the Rings (3 books)"
]

movie_recommendations = [
    "Inception",
    "Interstellar",
    "The Matrix",
    "Spider-Man: Into the Spider-Verse",
    "Jurassic Park",
    "Back to the Future",
    "The Lord of the Rings: The Fellowship of the Ring",
    "Avatar",
    "Guardians of the Galaxy",
    "The Dark Knight"
]

worry_fear_words = [
    "worried","anxious","afraid","scared","fearful","nervous","tense","uneasy","stressed",
    "panicked","alarmed","frightened","terrified","concerned","troubled","disturbed","shaken",
    "overwhelmed","paranoid","restless","dreadful","apprehensive","insecure","uncertain","uneasy","worried_sick",
    "petrified","startled","shocked","panicky"
 ]

supportive_responses = [
    "It's okay to feel worried sometimes, you're not alone.",
    "Take a deep breath, things will get better.",
    "I'm here to listen if you want to talk about it.",
    "You’re stronger than you think.",
    "It’s normal to feel this way sometimes.",
    "Try to take things one step at a time.",
    "Remember that tough moments don’t last forever.",
    "You’ve handled difficult things before, you can do it again.",
     "Sometimes a small break can help clear your mind.","Everything will be okay, just give it some time."
 ]

board_games = [
    "Chess","Checkers","Monopoly","Scrabble","Risk","Catan",
    "Ticket to Ride","Carcassonne","Pandemic","Clue","Battleship","The Game of Life",
    "Connect Four","Backgammon","Sorry!","Uno","Dominion","Azul","7 Wonders","Splendor",
    "Dixit","Codenames","Terraforming Mars","Wingspan","Root"
 ]

outdoor_activities = [
    "hiking","cycling","running","jogging","walking","birdwatching",
    "picnicking","fishing","swimming","surfing","kayaking","canoeing",
    "rock_climbing","camping","backpacking","mountain_biking","skiing",
    "snowboarding","sledding","skating","playing_soccer","playing_basketball",
    "playing_volleyball","frisbee",
    "gardening","photography","observing_stars","kite_flying","trail_running",
    "beach_volleyball","trail_biking",
    "nature_walks","geocaching","orienteering"
]

indoor_activities = [
"read a book","write a story","draw or sketch","paint","build origami",
"solve a puzzle","play a board game","cook a new recipe","bake cookies","listen to music",
"watch a movie","learn a new word","practice coding","organize your room",
"do a workout","stretch or do yoga","play a video game","write in a journal","build something with LEGO","learn a magic trick"
]

breakfast_ideas = [
    "oatmeal with fruits","pancakes","waffles","smoothie bowl",
    "yogurt with granola","scrambled eggs","omelette with vegetables",
    "toast with avocado","peanut butter toast","cereal with milk",
    "bagel with cream cheese",
    "fruit salad","breakfast burrito","muffins","croissant with jam","chia pudding",
    "french toast","breakfast sandwich","quiche","banana pancakes"
]

video_games = [
    "Minecraft","Fortnite","The Legend of Zelda: Breath of the Wild",
    "Among Us","Roblox","Animal Crossing: New Horizons","Call of Duty: Modern Warfare",
    "Cyberpunk 2077","Grand Theft Auto V","The Sims 4","Overwatch","League of Legends",
    "Valorant","Stardew Valley","Hollow Knight",
    "Super Mario Odyssey","FIFA 23","Rocket League","Dead by Daylight","God of War",
    "Elden Ring","Assassin's Creed Valhalla","Fall Guys","Terraria","Hades","city skylines"
]

happy_responses = [
    "That's awesome!","I'm so happy for you!","Yay!","That's fantastic!","Amazing news!",
    "That makes me smile!","Wow, that's great!","I'm thrilled to hear that!","Awesome job!","That's wonderful!"
]

sympathetic_responses = [
    "I'm sorry you're going through that.","I understand how you feel.","That sounds really tough.",
    "I'm here for you.","I can imagine that must be hard.","Sending you positive thoughts.",
    "I hope things get better soon.","Take your time, it's okay to feel that way.",
    "You're not alone in this.","I wish I could make it easier for you."
]

thanks_responses = [
    "You're welcome!","No problem!","Anytime!","Glad I could help!","My pleasure!",
    "Happy to help!","Always happy to help!","It was nothing!",
    "That's what I'm here for!","You're very welcome!"
]

neutral_responses = [
    "Okay.","I see.","Alright.","Hmm, interesting.","Got it.","Thanks for sharing.",
    "I understand.","Noted.","Alright then.","That's something to think about."
]

generic_responses = [
    "Can you tell me more about that?","I'm not sure I understand.",
    "Could you explain that differently?",
    "Hmm, I'm not sure how to respond to that.",
    "Interesting, tell me more.","I didn't quite get that.",
    "Let's talk about something else.","Sorry, I don't understand.",
    "Can you clarify what you mean?","I'm still learning, can you help me understand?"
]

riddles = [
{"riddle":"I speak without a mouth and hear without ears. What am I?","answer":"an echo"},
{"riddle":"What has keys but can't open locks?","answer":"A piano"},
{"riddle":"I’m tall when I’m young, and I’m short when I’m old. What am I?","answer":"a candle"},
{"riddle":"What has hands but can’t clap?","answer":"A clock"},
{"riddle":"What has to be broken before you can use it?","answer":"An egg"},
{"riddle":"I have cities but no houses, forests but no trees, and water but no fish. What am I?","answer":"a map"},
{"riddle":"What can travel around the world while staying in a corner?","answer":"a stamp"},
{"riddle":"The more of this you take, the more you leave behind. What is it?","answer":"Footsteps"},
{"riddle":"What has one eye but can’t see?","answer":"a needle"},
{"riddle":"What gets wetter the more it dries?","answer":"a towel"},
{"riddle":"What comes once in a minute, twice in a moment, but never in a thousand years?","answer":"The letter m"},
{"riddle":"What begins with T, ends with T, and has T in it?","answer":"a teapot"},
{"riddle":"I’m light as a feather, yet the strongest person can’t hold me for more than 5 minutes. What am I?","answer":"Breath"},
{"riddle":"What has a head, a tail, is brown, and has no legs?","answer":"a penny"},
{"riddle":"What runs all around a backyard, yet never moves?","answer":"a fence"}
]

true_false_questions = [
{"question": "Octopuses have three hearts.", "answer": "true"},
{"question": "Bananas grow on trees.", "answer": "false"},
{"question": "The Earth revolves around the Sun.", "answer": "true"},
{"question": "Sharks are mammals.", "answer": "false"},
{"question": "Honey can last for thousands of years without spoiling.", "answer": "true"},
{"question": "The human body has 300 bones.", "answer": "false"},
{"question": "Lightning never strikes the same place twice.", "answer": "false"},
{"question": "Bats are blind.", "answer": "false"},
{"question": "Water boils at 100 degrees Celsius at sea level.", "answer": "true"},
{"question": "Penguins can fly.", "answer": "false"},
{"question": "The Great Wall of China is visible from space with the naked eye.", "answer": "false"},
{"question": "The Pacific Ocean is the largest ocean on Earth.", "answer": "true"},
{"question": "Spiders are insects.", "answer": "false"},
{"question": "Humans and dinosaurs lived at the same time.", "answer": "false"},
{"question": "Sound travels faster in water than in air.", "answer": "true"}
]

trivia_questions = [
{"question": "What is the capital of France?", "answer": "paris"},
{"question": "How many continents are there on Earth?", "answer": "7"},
{"question": "What planet is known as the Red Planet?", "answer": "mars"},
{"question": "Who wrote 'Romeo and Juliet'?", "answer": "william shakespeare"},
{"question": "What is the largest ocean on Earth?", "answer": "pacific ocean"},
{"question": "How many sides does a hexagon have?", "answer": "6"},
{"question": "What gas do plants absorb from the air?", "answer": "carbon dioxide"},
{"question": "Who painted the Mona Lisa?", "answer": "leonardo da vinci"},
{"question": "What is the hardest natural substance on Earth?", "answer": "diamond"},
{"question": "Which country invented paper?", "answer": "china"},
{"question": "What is the smallest prime number?", "answer": "2"},
{"question": "How many players are there on a soccer team on the field?", "answer": "11"},
{"question": "What is the capital of Japan?", "answer": "Tokyo"},
{"question": "Which planet is the largest in the solar system?", "answer": "jupiter"},
{"question": "What language has the most native speakers in the world?", "answer": "mandarin chinese"}
]

angry_responses = [
    "Hey! That's not nice.",
    "Please be respectful.",
    "I don't like rude language.",
    "Let's keep the conversation polite."
]

bad_words = [
    "idiot","stupid","dumb","moron","loser","jerk","shut up",
    "nonsense","trash","ugly","annoying","hate you","pathetic","lame","ridiculous",
     "fuck","fucking","shit","bitch","asshole","bastard",
    "dick","piss off","bullshit","damn you","motherfucker",
    "son of a bitch", "wtf","stfu"
]

rps_choices = ["rock", "paper", "scissors"]
# =============================================================================
# STEP 2: HELPER FUNCTIONS
# =============================================================================

def print_separator():
    print("==========================================")


def print_bot(message):
    print(f"🤖 {bot_name}:", end=' ', flush=True)

    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def show_help():
    print_bot("That's what I can do:")
    print()
    print_bot("I can tell jokes or shower thoughts")
    print()
    print_bot("I can recommend books, movies, board games and video games to you")
    print()
    print_bot("I can tell you tips or facts")
    print()
    print_bot("I can give you a variety of riddles or solve math problems(I can solve quadratic equations and simple math expressions with +, -, * operators)")
    print()
    print_bot("I can play a variety of games or just talk!, you can feel free to ask me anything you want! ")
    print()
    

# =============================================================================
# STEP 3: GREETING FUNCTION
# =============================================================================s

def greet_user():
    greeting = random.choice(greetings)
    print_bot(greeting)
    print()
    print_bot("What's your name?")
    print()
    user_name = input("your name: ")
    print()
    print_bot("how old are you? ")
    print()
    user_age = input("your age: ")
    print()
    print_bot("Are you a male or a female? ")
    print()
    user_gender = input("you gender: ")
    print()
    print_bot(f"{random.choice(greetings)} {user_name}, i'm here to have fun with you! ")
    print()
    print_bot("you have a great name! ")
    print()
    return user_name

# =============================================================================
# STEP 4: RESPONSE FUNCTIONS
# =============================================================================

def tell_joke():
    joke = random.choice(jokes)
    return joke

def tell_shower_thoughts():
    shower_thought = random.choice(shower_thoughts)
    return shower_thought

def recommend_books():
    book_recommendation = random.choice(book_recommendations)
    return book_recommendation

def recommend_movie():
    movie_recommendation = random.choice(movie_recommendations)
    return movie_recommendation

def tell_tips():
    tip = random.choice(tips)
    return tip

def tell_fact():
    fact = random.choice(facts)
    return fact
    
def play_guess_game():
    random_number = random.randint(1, 20)
    attempts = 0
    while True:
        user_guess = int(input("choose a number between 1 to 20; let's see if you can guess it! "))
        print()
        if user_guess != random_number:
            if user_guess > 20 or user_guess < 1:
                print_bot("invalid number, try again")
                print()
            elif user_guess > random_number:
                print_bot("too high!")
                print()
                attempts += 1
            elif user_guess < random_number:
                print_bot("too low!")
                print()
                attempts += 1
        elif user_guess == random_number:
            break
    return f"congratulations!!!, you did it in {attempts} tries!!"

def play_rps_game():
    bot_wins = 0
    user_wins = 0
    while True:
        user_choose = input("choose: rock, paper, scissors: ")
        print()
        bot_choose = random.choice(rps_choices)
        print_bot(f"bot choose: {bot_choose}")
        print()
        print_bot(f"user choose: {user_choose}")
        print()
        if user_choose == "rock" and bot_choose == "scissors":
            user_wins  += 1
            print_bot("user win")
            print()
        elif user_choose == "paper" and bot_choose == "rock":
            user_wins  += 1
            print_bot("user win")
            print()
        elif user_choose == "scissors" and bot_choose == "paper":
            user_wins  += 1
            print_bot("user win")
            print()
        elif user_choose == bot_choose :
            print_bot("A tie!")
            print()
        else:
            bot_wins += 1
            print_bot("bot win")
            print()
        print_bot(f"bot has: {bot_wins} points")
        print()
        print_bot(f"user has: {user_wins} points")
        print()
        if bot_wins == 3:
            return "bot win the game!"
        elif user_wins == 3:
            return "user win the game!"
            

def analyze_mood(message):
    happy_words = [
                "happy","joyful", "cheerful", "delighted", "excited", "content", "pleased", "glad", "thrilled",
                "blissful", "grateful", "optimistic", "hopeful", "proud", "satisfied", "amused", "bright",
                "lively", "jolly", "merry", "playful", "energetic",
                "radiant", "sunny", "sparkling", "smiling", "uplifted",
                "inspired", "motivated", "peaceful", "relaxed", "thankful", "lucky", "fortunate",
                "fantastic", "wonderful", "amazing", "great", "excellent", "brilliant", "super", "awesome",
                "cool", "nice", "kind", "friendly", "lovely", "charming", "warm", "fun", "funny", "lol", "hilarious", "ha", "haha",
                "lmao", "rofl", "lmfao", "funniest", "hilarious", "humorous", "comical", "witty",]

    sad_words = [
                "sad", "unhappy", "miserable", "depressed", "gloomy", "melancholy", "down", "heartbroken", "lonely",
                "hopeless", "tired", "upset", "hurt", "disappointed", "regretful", "sorrowful", "tearful", "crying",
                "broken", "empty", "lost", "afraid", "worried", "anxious", "nervous", "stressed", "weak", "cold", "dark", "dull",
                "boring", "bitter", "angry", "frustrated", "tired", "exhausted", "painful", "tragic", "pathetic", "sorry", "ashamed",
                "guilty", "isolated", "ignored", "abandoned", "forgotten", "troubled", "disturbed", "confused", "bad"
                ]
    
    for word in happy_words:
        if word in message:
            return "happy"

    for word in sad_words:
        if word in message:
            return "sad"
    
    return "neutral"

def play_riddle():
    riddle_choose = random.choice(riddles)
    return riddle_choose

def true_false_game():
    question_choose = random.choice(true_false_questions)
    return question_choose

def trivia_game():
    selected_trivia_question = random.choice(trivia_questions)
    return selected_trivia_question
    
def quadratic(a, b, c):
    eqation = b**2 - 4*a*c
    
    if eqation < 0:
        return "No real solutions"
    
    sqrt_equation = eqation ** 0.5
    
    x_1 = (-b + sqrt_equation) / (2*a)
    x_2 = (-b - sqrt_equation) / (2*a)
    
    return x_1, x_2 
    
# =============================================================================
# STEP 5: MAIN RESPONSE FUNCTION
# =============================================================================

def get_response(message, user_name):
    message_lower = message.lower()
    
    for greet in greetings:
        if greet in message_lower:
            greeting =  random.choice(greetings)
            return f"{greeting}, {user_name}!"
        
    for bad_word in bad_words:
        if bad_word in message_lower:
            return random.choice(angry_responses)

    if "how are you" in message_lower:
        return "I'm great! How are you?"
    
    if "your name" in message_lower or "who are you" in message_lower:
        return f"I'm {bot_name}, nice to meet you!"
    
    if "teach" in message_lower:
        return "good to know!"
    
    if "favorite" in message_lower or "prefer" in message_lower:
        return "I'm a bot, I don't have favorites."

    if "talk" in message_lower:
        return "I love to talk! What would you like to discuss?, you can ask me questions, ask for recommendations, ask for jokes or shower thoughts, play games and more! if you want to know what I can do, type: 'help' or 'commands'"

    if "thanks" in message_lower or "thank" in message_lower:
        respon = random.choice(thanks_responses)
        return respon

    if "feel" in message_lower:
        return "I feel great! how do you feel?"

    if "joke" in message_lower or "funny" in message_lower or "jokes" in message_lower:
        joke = tell_joke()
        return f"{joke}, if you want to hear another joke, type: 'joke' or 'funny' again!"
    
    if "shower thought" in message_lower or "shower thoughts" in message_lower:
        shower_thought = tell_shower_thoughts()
        return f"{shower_thought}, if you want to hear another shower thought, type: 'shower thought' again!"

    if "book" in message_lower or "books" in message_lower:
        book_recommendation = recommend_books()
        return f"{book_recommendation}, if you already read it, type: 'book' and I will reccomend you another one!"

    if "movie" in message_lower or "movies" in message_lower:
        movie_recommendation = recommend_movie()
        return f"{movie_recommendation}, if you already watched it, type: 'movie' and I will reccomend you another one!"
    
    if "tip" in message_lower or "tips" in message_lower:
        tip = tell_tips()
        return f"{tip}, if you want to hear another tip, type: 'tip' again!"
    
    if "fact" in message_lower or "facts" in message_lower:
        fact = tell_fact()
        return f"{fact}, if you want to hear another fact, type: 'fact' again!"

    if "game" in message_lower or "play" in message_lower:
        return "game_menu"
    
    if "help" in message_lower or "commands" in message_lower:
        show_help()
        return "What else can I help with?"
    
    if "quadratic" in message_lower:
            a = float(input("enter a: "))
            b = float(input("enter b: "))
            c = float(input("enter c: "))
            result = quadratic(a, b, c)
            return f"The solutions are: {result}"
        
    
    if "+" in message_lower or "-" in message_lower or "*" in message_lower:
        try:
            result = eval(message_lower)
            return str(result)
        except:
            return "invalid math expression"
        
    
    for word in worry_fear_words:
        if word in message_lower:
            respon = random.choice(supportive_responses)
            return respon

    if "board game" in message_lower:
        game = random.choice(board_games)
        return f"You should try playing {game}, it's really fun! if you want another suggestion, type: 'board game' again!"
    
    if "bored" in message_lower or "indoor activity" in message_lower or "outdoor activity" in message_lower:
        activity = input("do you want an idea for an indoor or outdoor activity?").strip().lower()
        if activity == "indoor":
            activity_choice = random.choice(indoor_activities)
            return f"you will really enjoy {activity_choice}"
        elif activity == "outdoor":
            activity_choice = random.choice(outdoor_activities)
            return f"you will really enjoy {activity_choice}"
        else:
            return "please type bored again and then type 'indoor' or 'outdoor' so I can suggest something."
    
    if "breakfast" in message_lower or "food" in message_lower:
        idea = random.choice(breakfast_ideas)
        return f"make a {idea}, it's delicious!"
    
    if "computer games" in message_lower or "vidio games" in message_lower:
        game = random.choice(video_games)
        return f"you will really enjoy playing {game}"
    
    if "riddle" in message_lower or "question" in message_lower:
        choice = int(input("which game do you want to play? (1 - riddles,2 -  true false questions,3 -  trivia): "))
        if choice == 1:
            riddle_choose = play_riddle()
            print_separator()
            print_bot(f"riddle: {riddle_choose['riddle']}")
            print_separator()
            user_answer = input("your answer: ")
            if  user_answer == riddle_choose['answer']:
                return "congratulations, you did it!, if you want another riddle type: 'riddle' or 'question' again!"
            else:
                return f"you are wrong, the answer is {riddle_choose['answer']}, if you want another riddle type: 'riddle' or 'question' again!"
    
        elif choice == 2:
            question_choose = true_false_game()
            print_separator()
            print_bot(f"question: {question_choose['question']}")
            print_separator()
            user_answer = input("your answer: ")
            if  user_answer == question_choose['answer']:
                return "congratulations, you did it!, if you want another riddle type: 'riddle' or 'question' again!"
            else:
                return f"you are wrong, the answer is {question_choose['answer']}, if you want another riddle type: 'riddle' or 'question' again!"
        elif choice == 3:
            selected_trivia_question = trivia_game()
            print_separator()
            print_bot(f"trivia question is: {selected_trivia_question['question']}")
            print_separator()
            user_answer = input("your answer: ")
            if  user_answer == selected_trivia_question['answer']:
                return "congratulations, you did it!, if you want another riddle type: 'riddle' or 'question' again!"
            else:
                return f"you are wrong, the answer is {selected_trivia_question['answer']}, if you want another riddle type: 'riddle' or 'question' again!"
        else:
            return "please type 'riddles' or 'true false questions' or 'trivia'so I can suggest something."
    
    mood = analyze_mood(message_lower)
    if mood == "happy":
        answer = random.choice(happy_responses)
        return answer
    elif mood == "sad":
        answer = random.choice(sympathetic_responses)
        return answer
    
    default_respone = random.choice(generic_responses)
    return f"{default_respone}, I'm just a simple bot and I'm still learning, but I hope we can have fun together! " 


# =============================================================================
# STEP 6: MAIN CHAT LOOP
# =============================================================================

def chat():
    print_separator()
    print("               SNOOPI CHAT")
    print_separator()

    user_name = greet_user()
    if user_name.lower() == "alon":
        print_bot("wow! that's the best name ever, you are so lucky to have it!")

    show_help()

    while True:
        user_message = input(f"{user_name}: ").strip() 
        print()
        
        if not user_message:
            continue
        
        if "bye" in user_message.lower() or "goodbye" in user_message.lower() or "quit" in user_message.lower() or "exit" in user_message.lower():
            good_bye_greet = random.choice(goodbyes)
            print_separator()
            print(good_bye_greet, user_name)
            print_separator()
            break
        
        respone = get_response(user_message, user_name)

        if respone == "game_menu":
            print_bot("What would you like to play?" )
            print()
            print_bot("1-Number Guessing Game")
            print()
            print_bot("2-rps_game")
            print()
            print_bot("3-never mind")
            print()
            user_choice = int(input("which game do you want to play? "))
            print()
            if user_choice == 1:
                result = play_guess_game()
                print_separator()
                print_bot(result)
                print_separator()
                print_bot("if you want to play another game, type: 'game'")
            elif user_choice == 2:
               result = play_rps_game()
               print_separator()
               print_bot(result)
               print_separator()
               print_bot("if you want to play another game, type: 'game'")
               print()
        elif respone in generic_responses:
            print_bot(respone)
            print()
            show_help()
        else:
            print_bot(respone)
            print()


# =============================================================================
# STEP 7: RUN THE CHATBOT
# =============================================================================

if __name__ == "__main__":
    chat()