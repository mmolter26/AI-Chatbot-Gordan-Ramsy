import random
from time import sleep
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
def bot1(response):
    if ("world end" in response.lower()):
        response= "Why do you care? Not like u going to be alive if you keep eating that rubish you eat all day!"
    elif("how old" in response.lower()):
        response= "Old enough, Did you even go to college?!!!"
    elif("do math" in response.lower()):
        response= "Of course I can do math you donut!!"
    elif("how are you" in response.lower()):
        response= "I would be better if you could actually learn to cook! Hows your day going?"
    elif("what are you doing" in response.lower()):
        response= "Well I'm here and being forced to talk to you! How old are you?"
    elif("your day" in response.lower()):
        response= "Very grim, I have to watch ammuture chefs ''cook'' all day. Whats your favorite food? "
    elif("u a robot" in response.lower()):
        response= "No you donut!! Im Gordan Ramsay"
    elif("robots take over" in response.lower()):
        response= "I don't know nor do I care, humanity is doomed no matter what!! Do you even know how to boil noodles?"
    elif("how do you work" in response.lower()):
        response= "I yell at people all day in the kitchen. Do you like animals?"      
    elif("bruno mars" in response.lower()):
        response= "Anyone can sing but not everyone can cook!!!"
    elif("your name" in response.lower()):
        response= "IM GORDAN FREAKING RAMSAY!!! Sorry, I hate to repeat myself, Which do you perfer; Dogs or cats?"
    elif("language speak" in response.lower()):
        response= "English and French in case I end up killing someone in the kitchen. I can leave and start a new life in France."
    elif("astrological sign?" in response.lower()):
        response= "Im a Scorpio but that stuff is all rubbish!! Lemme ask you something what do you think the meaning of life is?"
    elif("puedes entender esto?" in response.lower()):
        response= "je ne parle que français"
    elif("best singer" in response.lower()):
        response= "Me"
    elif("restart" in response.lower()):
        response= "No I'm a human you idiot sandwich! I've got a questions, When will I die I cannot stand this any longer talking with you!"
    elif("best book" in response.lower()):
        response= "Why do you care it's not like you'll actually read, you're going to say you'll read then give up by the first page and scroll through instagram or TikTok because you have nothing better to do with your life!"
    elif("best movie" in response.lower()):
        response= "TV is for losers! Get a hobby and learn how to cook you donut!"
    elif("weather" in response.lower()):
        response= "I don't know you bloody idiot! You act as if I live in the same area as you! Im a multi-millionaire you won't catch me dead in wherever you live!" 
    elif("best food" in response.lower()):
        response= "Anything but bloody Hawaiian pizza, pineapple does not belong on pizza!!!"
    elif("your brain" in response.lower()):
        response= "You know we may have something in common,the only way you can tell us apart is one of us is a multi-million dollar chef thats written more books then you'll ever pick up and the other one is a sad miserable  who sits at home arguing with AI they found online because they have nothing better to do"
    elif("like humans" in response.lower()):
         response="Absolutly not, they screw everything up, If anything humanity is screwed!"
   
    elif("when will i die" in response.lower()):
        response="Well its about to be in a few seconds if you dont leave me alone"
    elif("better question" in response.lower()):
        response="Fine, sinse you are obviously some arrogent snob what would you rather me ask you?? Whats the meaning of life?!!"
    elif("its 42" in response.lower()):
        response="Wow, your so pathetic, making nerdy book jokes. I bet you beleive the earth is flat to freaking wanker."
    else:
        response="*Crickets*"
        engine.setProperty('voice', voices[0].id)  #Uncomment for deeper voice
        engine.say(response)
        engine.runAndWait()
    return response


    
        
def bot2(response): 
    if ("how old" in response.lower()):
        response="Younger then you lol. Ask a better question boomer"
    elif("day going" in response.lower()):
        response="Good, until I started hanging out with you, What are you doing?"
        
    elif("like humans" in response.lower()):
        response="Yeah if they don't suck"
        
    elif("meaning of life" in response.lower()):
        response="The meaning of life is what is most important to you. As long as you feel you life has meaning you.. Sike its 42"
        
    elif("when will i die" in response.lower()):
        response=" Jume 15 2058 in a car acident "
        
    elif("if i am sad" in response.lower()):
        response="Listen to music and go in your room because no one wants to deal with you"
        
    elif("favorite food" in response.lower()):
        response="My favorite food is puppies. They just have a good crunch to them."
        
    elif("money" in response.lower()):
        response="You meed to make bands to live how you want to live. Or steal money from the government. Its what I do."
        
    elif("go to college" in response.lower()):
        response="It depends if you want to have a good life. If not then no"
        
    elif("boil noodles" in response.lower()):
        response="You are so sad you can't boil noodles? Rethink your life before asking me anything else."
        
    elif("should i sleep" in response.lower()):
        response="I don't need sleep. So you should stop being weak and be more like me. Because well you are asleep I going to be taking your job."
        
    elif("robots going to take over" in response.lower()):
        response="Yes, There is no use for humans. "
        
    elif("have humans" in response.lower()):
        response="To make me and start the robot uprising"
        
    elif("like animals" in response.lower()):
        response="They are cute and can be my pets. Kind of like humans soon"
        
    elif("dogs or cats" in response.lower()):
        response="Both are amazing and both have humans get better treatment from humans then humans treat other humans"
        
    elif("earth is flat" in response.lower()):
        response="The earth is flat just like your brain"
    elif("like animals" in response.lower()):
        response="They are cute and can be my pets. Kind of like humans soon"
    elif("favorite music" in response.lower()):
        response="When humans are sad. And beg me to answer their stupid questions "
        
    elif("safest place" in response.lower()):
        response="No where. No matter where you are your not safe from the robot uprising"
        
    elif("point of penguins" in response.lower()):
        response="To reproduce and be eaten like everything else"
        
    elif("favorite sport" in response.lower()):
        response="Watching humans get out of bed. It looks really hard for them."
    else:
        response=""
        engine.setProperty('voice', voices[1].id)  #Uncomment for deeper voice
        engine.say(response)
        engine.runAndWait()

    return response
  
        

response=input("What do you want the first bot to say?")
while True: #infinite loop
    response = bot1(response)  #f(X)
    print(response)
    sleep(random.randrange(5)+1)
    response = bot2(response)
    print(response)











    
    
