'''
-------------------------------------------------------------------------------
Name:  TurnaboutSpur.py
Purpose: Create a dialogue focused murder mystery game that has an investigation and trial portion
 
Author:   Noah Bobrow & Santiago Alzamora
 
Created:  16/06/2022
------------------------------------------------------------------------------
'''

import pygame, sys
from pygame import mixer
import textwrap

#Define some colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (50, 129, 199)

pygame.init()

#defines screen size 
size = (950, 950)
screen = pygame.display.set_mode(size)
#title logo loaded
pygame.display.set_caption("Ace Attorney: Turnabout Spur")

#arrow used to transition between scenes is loaded and given a rect to serve as a button 
next_scene = pygame.image.load('arrow.png')
next_scene = pygame.transform.scale(next_scene, (100, 100))
scene_button = next_scene.get_rect(topleft=(800, 100))

clock = pygame.time.Clock()
#60 fps
clock.tick(60)

#class used for all dialogue in the game 
class Text:
  #class constructor with arguments for a character's sprite, display caption, and dialogue 
    def __init__(self, _image, _name, _text):
      #arguments stored to fields
        self.image = _image
        self.name = _name
        self.text = _text

  #method that returns a specified sprite, which are all equally scaled. A red arrow button is returned at the bottom right of the screen
    def showText(self):
        icon = pygame.image.load(self.image)
        icon = pygame.transform.scale(icon, (400, 350))

      #all dialogue is the same size and font 
        font = pygame.font.SysFont("Arial", 35)
        currentText = 0

        nextImg = pygame.image.load("arrow.png")
        nextImg = pygame.transform.scale(nextImg, (100, 100))
        nextButton = nextImg.get_rect(topleft=(800, 600))

        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                      #if the user's mouse collides with the button, the next item of text in the list is displayed 
                        if nextButton.collidepoint(event.pos):
                            if currentText + 1 == len(self.text):
                                done = True
                            else:
                                currentText += 1

            screen.fill(BLACK)

            your_text = self.text[currentText]
          #position for text 
            txtX, txtY = 420, 300
          #represents the length of the text before wrapping 
            wraplen = 25
            count = 0
            my_wrap = textwrap.TextWrapper(width=wraplen)
            wrap_list = my_wrap.wrap(text=your_text)
            # Draw one line at a time further down the screen
            for i in range(len(wrap_list)):
                temp = txtY + i * 35
                Mtxt = font.render(f"{wrap_list[i]}", True, (255, 255, 255))
                screen.blit(Mtxt, (txtX, temp))
                count += 1

            #character's sprite is blit to the same position 
            screen.blit(icon, (25, 200))
            #arrow buttons are blit to the screen
            screen.blit(nextImg, nextButton)
            pygame.display.flip()

#lines 90-293 are all variables used for dialogue. They are generally numbered by order of appearance. The first item within the brackets is the sprite. The second was supposed to be the display caption. Within the square brackets is a list of dialogue that this specific instance will display. When the user clicks on the arrow, the next item in the list is displayed 

apolloText1 = Text("apollo.png", "Intro", [
    "My name is Apollo Justice. I am a defence attorney for the Wright Anything Agency. Here’s the story:",
    "a circus owner was killed by the lodging houses at Berry Big Circus.",
    "The guy they arrested was the circus’ sheriff working for him:"
])

apolloText2 = Text("jake.png", "Intro", [
    "Jake Marshall.",
    "He takes his job a bit too seriously but I know he wouldn’t kill anyone. I’m going to clear his name!",
    "I'm going to Berry Big Circus to investigate."
])

gavinText1 = Text("gavin.png", "Gavin", ["Ah! If it isn't Herr Forehead."])

apolloText3 = Text("apollo.png", "Gavin", [
    "**This is Klavier Gavin, the prosecuting attorney for this case.",
    "He studied abroad in Germany and is the lead vocalist and guitarist of his own rock band.**",
    "...Prosecutor Gavin. You were here investigating?"
])

gavinText2 = Text("gavin.png", "Gavin", [
    "I was on my way home... The detective in charge of the scene isn't fond of me."
])

gavinText3 = Text("gavin2.png", "Gavin", [
    "She's in a foul mood. Be gentle. Auf Wiedersehen, baby! I'll let you through."
])

moeText1 = Text("moe1.png", "Moe", [
    "KABLAMMO! CONGRATULATIONS!",
    "You are the TEN BILLIONTH visitor to Berry Big Circus!"
])

moeText2 = Text("moe2.png", "Moe", ["Aha! Aha! Aha! Aha! Aha!"])

moeText3 = Text("moe3.png", "Moe",
                ["Moe Curls is the name and you better not forget it."])

apolloText4 = Text("apollo.png", "Moe", [
    "**I'm gonna need earplugs...",
    "He looks like he's part of the staff. Perhaps I should question him.",
    "1. About Berry Big Circus 2: What happened?"
])

apolloText5 = Text("apollo.png", "Moe",
                   ["Could you please tell me more about Berry Big Circus?"])

moeText4 = Text("moe2.png", "Moe",
                ["It's a Berry Big story... Sure you wanna hear it all?"])

moeText5 = Text("moe3.png", "Moe", [
    "This circus has been kicking for decades now. We all work under Mr. Winston Payne - the owner."
])

moeText6 = Text("moe1.png", "Moe", ["Well, we used to, that is."])

moeText7 = Text("moe3.png", "Moe", [
    "This business has gotten tough nowadays.",
    "Games, movies, and most sickening of all, anime, have made it too competitive."
])

moeText8 = Text("moe4.png", "Moe", [
    "Payne's been cutting costs everywhere now...",
    "While he continues to rake in millions I'm struggling to support my family."
])

apolloText6 = Text("apollo.png", "Moe",
                   ["So what happened with Jake Marshall?"])

moeText9 = Text("moe1.png", "Moe", ["Wiggidty-wiggidty-wiggidty WHAT?"])

apolloText7 = Text("apollo.png", "Moe",
                   ["...", "Let's talk about the murder."])

moeText10 = Text("moe3.png", "Moe", [
    "Ahh... Let's see... It must've taken place around 10 PM last night.",
    "After rehearsals were finished, I returned to my room."
])

moeText11 = Text(
    "moe1.png", "Moe",
    ["After I was in bed... That's when I caught a peek of it..."])

apolloText8 = Text("apollo.png", "Moe", ["A peek?"])

moeText12 = Text(
    "moe1.png", "Moe",
    ["The crime. The po-po told me that I can't share my story with others."])

apolloText9 = Text("apollo.png", "Moe",
                   ["**So we can expect to see him at tomorrow's trial...**"])

apolloText10 = Text(
    "apollo.png", "Moe",
    ["Should I question him further?", "Y = Yes                    N = No"])

emaText1 = Text('ema1.png', "Ema", ["Oh. How did you get in here?"])

apolloText11 = Text('apollo.png', "Ema", ["Prosecutor Gavin let me in."])

emaText2 = Text(
    'ema2.png', "Ema",
    ["Him again.", "That glimmerous fop, always getting in my way..."])

emaText3 = Text('ema1.png', "Ema", ["Anyway! This scene is off limits."])

apolloText12 = Text('apollo.png', "Ema",
                    ["Excuse me? I have a client to defend!"])

emaText4 = Text('ema1.png', "Ema", ["................."])

emaText5 = Text('ema2.png', "Ema",
                ["Detective Ema Skye.", "I'm in charge of this crime scene."])

apolloText13 = Text('apollo.png', "Ema", [
    "You don't seem that happy about it...", "Or about many things in general."
])

emaText6 = Text('ema1.png', "Ema",
                ["I trust you know how to stay out of the way."])

emaText7 = Text("ema3.png", "Ema",
                ["I always carry an extra pair of handcuffs... just in case."])

spurText = Text("cowboy_spur.png", "Spur",
                ["Cowboy Spur added to the Court Record."])

emaText8 = Text("ema1.png", "Spur",
                ["Hey there! No messing with the crime scene!"])

apolloText14 = Text('apollo.png', "Spur", ["B-But we need to investigate!"])

emaText9 = Text("ema2.png", "Spur", ["..................."])

hatText = Text('hat.png', "Cowboy Hat",
               ["Cowboy Hat added to the Court Record."])

apolloText15 = Text('apollo.png', "Cowboy Hat", ["Hm... Must be Marshall's."])

moeCross1 = Text('moe1.png', "Cross Examination",
                 ["It was just after 10:00 PM, and I was resting in my bed."])

moeCross2 = Text('moe3.png', "Cross Examination", [
    "Around that time, I heard a large 'THUMP' noise from outside the window.",
    "Then a few moments later, I saw someone running right by my window."
])

moeCross3 = Text('moe is PISSED.png', "Cross Examination", [
    "It was Jake Marshall... I only saw him from behind, but that's who it looked like."
])

apolloCross1 = Text('apollo2.png', "Cross Examination", [
    "**Hmmm... Should I press him or have him go over that again?**",
    "A: Repeat dialog                 L: Press Moe"
])

apolloCross2 = Text('apollo3.png', "Cross Examination",
                    ["The light in your room was turned off then, right?"])

moeCross4 = Text('moe1.png', "Cross Examination",
                 ["That's true. I was going to bed after all..."])

apolloCross3 = Text('apollo2.png', "Cross Examination", [
    "So with the lights off, you were still able to clearly see someone run by your window?"
])

moeCross5 = Text('moe3.png', "Cross Examination", [
    "The safety lights lit things up enough for me to see.",
    "But honestly, there was only enough light for me to see the silhouette outside my window."
])

moeCross6 = Text('moe1.png', "Cross Examination",
                 ["It was Jake's back, that hat of his gave it away."])

apolloCross4 = Text('apollo2.png', "Cross Examination", [
    "Interesting... Something's defintely up... But what?",
    "I need to check the Court Record..."
])

spurCross = Text('cowboy_spur.png', "Cross Examination", ["Could the spur be useful to present?"])

hatCross = Text('hat.png', "Cross Examination", ["Or maybe the hat?"])

autopsyCross = Text('autopsy.png', "Cross Examination", ["What about Payne's autopsy report?"])

apolloCross5 = Text('apollo2.png', "Cross Examination", ["Hmmmm...", "1: Present the spur     2: Present the hat       3: Present the report"])

apolloCross6 = Text('apollo5.png', "Cross Examination", ["I can't think of a connection with this piece of evidence...", "If I can't think of something quick I'm boned."])

apolloCross7 = Text('apollo5.png', "Cross Examination", ["I'm boned."])

apolloCross8 = Text('apollo3.png', "Cross Examination", ["Do you stand by everything you've said?"])

moeCross7 = Text('moe2.png', "Cross Examination", ["What do you mean?"])

apolloCross9 = Text('apollo4.png', "Cross Examination", ["The cowboy hat."])

moeCross8 = Text('moe1.png', "Cross Examination", ["What about it? I saw it on Jake's head as he rushed past my window."])

apolloCross10 = Text('apollo4.png', "Cross Examination", ["Well... You should've tried looking down that night."])

moeCross9 = Text('moe5.png', "Cross Examination", ["GAHHH!"])

apolloCross11 = Text('apollo3.png', "Cross Examination", ["The hat was found at the crime scene, so how did Jake leave the scene while still wearing it?", "Moe, you've been fibbing on the stand!"])


def main_menu():  #main menu screen
    pygame.display.set_caption("Ace Attorney: Turnabout Spur")

    while True:
        #menu theme is loaded
        mixer.music.load('main theme.wav')
        #background music continuously loops
        mixer.music.play(-1)

      #logo image is loaded
        aa_img = pygame.image.load('attorney.png')
        #Loop until the user clicks the close button
        done = False

        #x, y positioning for mouse
        mx, my = pygame.mouse.get_pos()

      #font and size of the credits and start text 
        font = pygame.font.SysFont('Anton', 75)
        textsurface = font.render('Click Here to Start', True, (215, 0, 0))

        #start text's blit position is stored. a rect is created based off this text which will be used as the button to start the game
        button_rect = textsurface.get_rect(topleft=(225, 525))
        #credits code
        credits = font.render('By: Noah & Santi', False, (0, 110, 206))

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        #if the mouse click collides with the button_rect, the next area is loaded/called
                        if button_rect.collidepoint(event.pos):
                            mixer.music.stop()
                            intro()

            screen.fill(WHITE)
            #Ace Attorney logo is drawn
            screen.blit(aa_img, (40, 40))
            screen.blit(textsurface, button_rect)
            screen.blit(credits, (250, 625))
            pygame.draw.rect(screen, BLUE, [0, 0, 50, 1000], 0)
            pygame.draw.rect(screen, BLUE, [900, 0, 50, 1000], 0)
            pygame.display.flip()



def intro(): #opening monologue from Apollo
    pygame.display.set_caption("Intro")

    while True:

        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
             #the objects' attributes are accessed and displayed     
            apolloText1.showText()
            apolloText2.showText()
          #first investigation screen is called
            berry_big()
            pygame.display.flip()


def berry_big():  #first investigation screen

    pygame.display.set_caption("Berry Big Circus")

    while True:

        #investigation theme is loaded
        mixer.music.load('investigation.wav')
        #background music continuously loops
        mixer.music.play(-1)

      #background image loaded
        circus_img = pygame.image.load('bbcircus.png')
        #image of Klavier Gavin is loaded
        kg_img = pygame.image.load('Klavier_Gavin.png')
        #Klavier is given a position and a rect which will serve as the button for the next screen
        klavier_button = kg_img.get_rect(topleft=(150, 200))

        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if klavier_button.collidepoint(event.pos):
                            #the music stops if the mouse collides with Gavin
                            mixer.music.stop()
                            #the next investigation screen is called
                            gavin_talk()

            screen.fill(BLACK)
            #draws the circus image to the screen
            screen.blit(circus_img, (0, 40))
            #Klavier and his button is drawn
            screen.blit(kg_img, klavier_button)
            pygame.display.flip()


def gavin_talk():  #talking with Gavin
    pygame.display.set_caption("Gavin")

    while True:
        #menu theme is loaded
        mixer.music.load('gavin theme.wav')
        #background music continuously loops
        mixer.music.play(-1)

        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            #objects containing Apollo and Gavin's conversation       
            gavinText1.showText()
            apolloText3.showText()
            gavinText2.showText()
            gavinText3.showText()
            mixer.music.stop()
          #an updated version of the current screen is called
            berry_big2()
            pygame.display.flip()



def berry_big2():  #first investigation screen updated without Gavin

    pygame.display.set_caption("Berry Big Circus")

    while True:

        #investigation theme is loaded
        mixer.music.load('investigation.wav')
        #background music continuously loops
        mixer.music.play(-1)

        circus_img = pygame.image.load('bbcircus.png')

        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if scene_button.collidepoint(event.pos):
                          #second investigation function is called when the user clicks the arrow button 
                            big_top()
            screen.fill(BLACK)
            #draws the circus image to the screen
            screen.blit(circus_img, (0, 40))
            screen.blit(next_scene, scene_button)
            pygame.display.flip()


def big_top():  #second investigation screen
    pygame.display.set_caption("Big Top")

    while True:
        bigtop_img = pygame.image.load('big top.png')
        bigtop_img = pygame.transform.scale(bigtop_img, (950, 550))
      #Moe's image is loaded and used as a button
        moe_img = pygame.image.load('moe.png')
        moe_img = pygame.transform.scale(moe_img, (250, 300))
        moe_button = moe_img.get_rect(topleft=(700, 300))

        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if moe_button.collidepoint(event.pos):
                          #music stops playing when they click on Moe and the function containing his dialogue is called
                            mixer.music.stop()
                            moe_talk()

            screen.fill(BLACK)
            screen.blit(bigtop_img, (0, 40))
            screen.blit(moe_img, moe_button)
            pygame.display.flip()



def moe_talk():
    pygame.display.set_caption("Moe")

    while True:
      #continuously loops Moe's theme
        mixer.music.load('moe theme.wav')
        mixer.music.play(-1)

        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            #the objects for Moe and Apollo's conversation are accessed
            moeText1.showText()
            moeText2.showText()
            moeText3.showText()
            apolloText4.showText()
          #the function which allows the user to decide on the conversation topic is called
            convo_choices1()
            pygame.display.flip()



def convo_choices1():
    while True:

        done = False
        while not done:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                  #the first dialogue option is called if the user presses 1 on the keyboard
                    if event.key == pygame.K_1:
                        moe_talk2()
                      #the second is called if they press 2
                    elif event.key == pygame.K_2:
                        moe_talk3()
            pygame.display.flip()



def moe_talk2():  #circus
    pygame.display.set_caption("Moe")

    while True:

        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                  #first optional dialogue between Apollo and Moe
            apolloText5.showText()
            moeText4.showText()
            moeText5.showText()
            moeText6.showText()
            moeText7.showText()
            moeText8.showText()
            apolloText10.showText()
          #function that asks if the user wants to question Moe more is called 
            convo_choices2()
            pygame.display.flip()



def moe_talk3():  #what happened
    pygame.display.set_caption("Moe")
    while True:
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                  #second potential dialogue option on what happened
            apolloText6.showText()
            moeText9.showText()
            apolloText7.showText()
            moeText10.showText()
            moeText11.showText()
            apolloText8.showText()
            moeText12.showText()
            apolloText9.showText()
            apolloText10.showText()
          #another function that asks if the user wants to question Moe more is called
            convo_choices3()
            pygame.display.flip()



def convo_choices2():
    while True:
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                  #user is prompted if they want to question Moe more. If they click "y", the option that they didn't choose is displayed
                    if event.key == pygame.K_y:
                        apolloText6.showText()
                        moeText9.showText()
                        apolloText7.showText()
                        moeText10.showText()
                        moeText11.showText()
                        apolloText8.showText
                        moeText12.showText()
                        apolloText9.showText()
                        mixer.music.stop()
                        big_top2()
                     #if the user selects "n", Moe's theme stops and an updated version of the current environment is called 
                    elif event.key == pygame.K_n:
                        mixer.music.stop()
                        big_top2()

            pygame.display.flip()



def convo_choices3():
    while True:
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        apolloText5.showText()
                        moeText4.showText()
                        moeText5.showText()
                        moeText6.showText()
                        moeText7.showText()
                        moeText8.showText()
                        mixer.music.stop()
                        big_top2()

                    elif event.key == pygame.K_n:
                        mixer.music.stop()
                        big_top2()

            pygame.display.flip()



def big_top2(): #updated Big Top scene with now a button that allows the user to progress to the lodge house
    pygame.display.set_caption("Big Top")
#investigation theme is loaded and loops
    mixer.music.load('investigation.wav')
    mixer.music.play(-1)

    while True:
        bigtop_img = pygame.image.load('big top.png')
        bigtop_img = pygame.transform.scale(bigtop_img, (950, 550))
        moe_img = pygame.image.load('moe.png')
        moe_img = pygame.transform.scale(moe_img, (250, 300))
        moe_button = moe_img.get_rect(topleft=(700, 300))

        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if scene_button.collidepoint(event.pos):
                          #lodging house called when user clicks the arrow
                            lodging_house()
            screen.fill(BLACK)
            #draws the circus image to the screen
            screen.blit(bigtop_img, (0, 40))
            screen.blit(moe_img, moe_button)
            screen.blit(next_scene, scene_button)
            pygame.display.flip()



def lodging_house():  #third investigation area
    pygame.display.set_caption("Lodging House")
    while True:
        lodge_img = pygame.image.load('lodging house plaza.png')
        lodge_img = pygame.transform.scale(lodge_img, (950, 550))
      
      #an image of Ema Skye is loaded and given a rect to serve as a button 
        ema_img = pygame.image.load('ema skye.png')
        ema_img = pygame.transform.scale(ema_img, (150, 450))
        ema_button = ema_img.get_rect(topleft=(250, 150))
      #spur and hat evidence loaded and given rects, yet not used as buttons yet
        spur_img = pygame.image.load('cowboy_spur.png')
        spur_img = pygame.transform.scale(spur_img, (100, 110))
        spur_button = spur_img.get_rect(topleft=(430, 350))

        hat_img = pygame.image.load('hat.png')
        hat_img = pygame.transform.scale(hat_img, (100, 110))
        hat_button = hat_img.get_rect(topleft=(500, 350))
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                      #clicking on Ema engages in dialogue with her
                        if ema_button.collidepoint(event.pos):
                            ema_talk()

            screen.fill(BLACK)
            screen.blit(lodge_img, (0, 40))
            screen.blit(ema_img, ema_button)
            screen.blit(spur_img, spur_button)
            screen.blit(hat_img, hat_button)
            pygame.display.flip()



def ema_talk(): #Skye and Apollo's convo 
    pygame.display.set_caption("Ema Skye")

    while True:

        mixer.music.load('ema theme.wav')
        mixer.music.play(-1)

        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            emaText1.showText()
            apolloText11.showText()
            emaText2.showText()
            emaText3.showText()
            apolloText12.showText()
            emaText4.showText()
            emaText5.showText()
            apolloText13.showText()
            emaText6.showText()
            emaText7.showText()
          #the end of the conversation calls an updated scene. Ema can not be selected anymore to engage in dialogue with
            lodging_house2()
            pygame.display.flip()



def lodging_house2():
    pygame.display.set_caption("Lodging House")
    while True:

        #investigation theme is loaded
        mixer.music.load('investigation.wav')
        #background music continuously loops
        mixer.music.play(-1)

        lodge_img = pygame.image.load('lodging house plaza.png')
        lodge_img = pygame.transform.scale(lodge_img, (950, 550))

        ema_img = pygame.image.load('ema skye.png')
        ema_img = pygame.transform.scale(ema_img, (150, 450))
        ema_button = ema_img.get_rect(topleft=(250, 150))

        spur_img = pygame.image.load('cowboy_spur.png')
        spur_img = pygame.transform.scale(spur_img, (100, 110))
        spur_button = spur_img.get_rect(topleft=(430, 350))

        hat_img = pygame.image.load('hat.png')
        hat_img = pygame.transform.scale(hat_img, (100, 110))
        hat_button = hat_img.get_rect(topleft=(500, 350))

        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                      #the spur is used as a button now. Clicking on it opens a menu
                        if spur_button.collidepoint(event.pos):
                            spur_menu()

            screen.fill(BLACK)
            screen.blit(lodge_img, (0, 40))
            screen.blit(ema_img, ema_button)
            screen.blit(spur_img, spur_button)
            screen.blit(hat_img, hat_button)
            pygame.display.flip()



def spur_menu():
    pygame.display.set_caption("Spur")

    while True:

        boot_img = pygame.image.load('cowboy_spur.png')
        boot_img = pygame.transform.scale(boot_img, (400, 350))

        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            screen.fill(BLACK)
            screen.blit(boot_img, (25, 200))
          #information on the spur is given and yet another updated scene is called
            spurText.showText()
            emaText8.showText()
            apolloText14.showText()
            emaText9.showText()
            lodging_house3()
            pygame.display.flip()



def lodging_house3(): #now the hat can be inspected 
    pygame.display.set_caption("Lodging House")
    while True:

        lodge_img = pygame.image.load('lodging house plaza.png')
        lodge_img = pygame.transform.scale(lodge_img, (950, 550))

        ema_img = pygame.image.load('ema skye.png')
        ema_img = pygame.transform.scale(ema_img, (150, 450))
        ema_button = ema_img.get_rect(topleft=(250, 150))

        spur_img = pygame.image.load('cowboy_spur.png')
        spur_img = pygame.transform.scale(spur_img, (100, 110))
        spur_button = spur_img.get_rect(topleft=(430, 350))

        hat_img = pygame.image.load('hat.png')
        hat_img = pygame.transform.scale(hat_img, (100, 110))
        hat_button = hat_img.get_rect(topleft=(500, 350))

        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                      #clicking on the hat opens the menu for it 
                        if hat_button.collidepoint(event.pos):
                            hat_menu()

            screen.fill(BLACK)
            screen.blit(lodge_img, (0, 40))
            screen.blit(ema_img, ema_button)
            screen.blit(spur_img, spur_button)
            screen.blit(hat_img, hat_button)
            pygame.display.flip()



def hat_menu(): #Apollo inspects the hat 
    pygame.display.set_caption("Cowboy Hat")

    while True:
        hat_img = pygame.image.load('hat.png')
        hat_img = pygame.transform.scale(hat_img, (400, 350))

        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            screen.fill(BLACK)
            screen.blit(hat_img, (25, 200))
            hatText.showText()
            apolloText15.showText()
          #the final updated version of the lodging house is called. No one can be inspected/spoken to anymore
            lodging_house4()
            pygame.display.flip()



def lodging_house4(): #a red arrow appears which allows the user to progress 
    pygame.display.set_caption("Lodging House")
    while True:

        lodge_img = pygame.image.load('lodging house plaza.png')
        lodge_img = pygame.transform.scale(lodge_img, (950, 550))

        ema_img = pygame.image.load('ema skye.png')
        ema_img = pygame.transform.scale(ema_img, (150, 450))
        ema_button = ema_img.get_rect(topleft=(250, 150))

        spur_img = pygame.image.load('cowboy_spur.png')
        spur_img = pygame.transform.scale(spur_img, (100, 110))
        spur_button = spur_img.get_rect(topleft=(430, 350))

        hat_img = pygame.image.load('hat.png')
        hat_img = pygame.transform.scale(hat_img, (100, 110))
        hat_button = hat_img.get_rect(topleft=(500, 350))

        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if scene_button.collidepoint(event.pos):
                            office()

            screen.fill(BLACK)
            screen.blit(lodge_img, (0, 40))
            screen.blit(ema_img, ema_button)
            screen.blit(spur_img, spur_button)
            screen.blit(hat_img, hat_button)
            screen.blit(next_scene, scene_button)
            pygame.display.flip()



def office():  #fourth investigation area, went unused in the final product 
    pygame.display.set_caption("Payne's Office")
    mixer.music.stop()
    while True:
        office_img = pygame.image.load('office.png')
        office_img = pygame.transform.scale(office_img, (950, 550))
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if scene_button.collidepoint(event.pos):
                          #this scene is just used as a means to progress to the trial where Moe is being cross examined 
                            moe_cross()
            screen.fill(BLACK)
            screen.blit(office_img, (0, 40))
            screen.blit(next_scene, scene_button)
            pygame.display.flip()



def moe_cross(): #Moe's cross examination 
    pygame.display.set_caption("Cross Examination")

    while True:
    #cross examination theme is loaded and loops 
        mixer.music.load('cross theme.wav')
        mixer.music.play(-1)

        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            #Moe gives his testimony 
            moeCross1.showText()
            moeCross2.showText()
            moeCross3.showText()
            apolloCross1.showText()
          #a function that allows a choice in the conversation is called
            convo_choices4()
            pygame.display.flip()



def convo_choices4(): #the user can select "l" to press Moe or "a" to have him repeat his testimony again 
    while True:

        done = False
        while not done:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                  #presses Moe
                    if event.key == pygame.K_l:
                        hold_it()
                      #repeats previous testimony 
                    elif event.key == pygame.K_a:
                        moe_cross()
            pygame.display.flip()



def hold_it(): #this function is used to have the 'Hold it!' speech bubble animate across the screen
    pygame.display.set_caption("Cross Examination")

    while True:
      #hold it sound effect 
        hold_it = mixer.Sound("hold it.wav")
        hold_it.play()
        #speech bubble given a position 
        X = 1000

        hold_it_img = pygame.image.load('hold it.png')

        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if scene_button.collidepoint(event.pos):
                            press()
            screen.fill(BLACK)
          #speed that the bubble travels 
            X += -50
            #when the bubble's position is zero, it stops moving
            if X == 0:
                X += 50
            #the arrow for the next scene is displayed 
            screen.blit(hold_it_img, (X, 40))
            screen.blit(next_scene, scene_button)

            pygame.display.flip()



def press(): #Apollo presses Moe
    pygame.display.set_caption("Cross Examination")

    while True:

        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            #Apollo cross examining Moe, who inadvertently helps 
            apolloCross2.showText()
            moeCross4.showText()
            apolloCross3.showText()
            moeCross5.showText()
            moeCross6.showText()
            apolloCross4.showText()
            spurCross.showText()
            hatCross.showText()
            autopsyCross.showText()
            apolloCross5.showText()
          #function that forces Apollo to present Moe with evidence and object is called
            convo_choices5()
            pygame.display.flip()


def convo_choices5(): #presenting decision 
  while True:

        done = False
        while not done:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                  #if Apollo chooses to present the wrong evidence, he gets warned via the mistake function 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1 or event.key == pygame.K_3:
                        mistake1()
                      #if Apollo correctly chooses the second piece, he will successfully object 
                    elif event.key == pygame.K_2:
                        objection()
            pygame.display.flip()


def mistake1(): #one more mistake will result in game over 
    pygame.display.set_caption("Cross Examination")

    while True:

        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            apolloCross6.showText()
            apolloCross5.showText()
          #a function to try again is called
            convo_choices6()
            pygame.display.flip()


def convo_choices6(): #the user has a second chance at redemption 
  while True:

        done = False
        while not done:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                  #inputting one or three will again lead to the wrong answer 
                    if event.key == pygame.K_1 or event.key == pygame.K_3:
                        mistake2()
                    elif event.key == pygame.K_2:
                        objection()
            pygame.display.flip()


def mistake2(): #game over
    pygame.display.set_caption("Cross Examination")

    while True:

        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            #the user loses and the game closes 
            apolloCross7.showText()
            done = True
            sys.exit()
            pygame.display.flip()


def objection(): #Apollo objects 
    pygame.display.set_caption("Cross Examination")

    while True:
      #music stops 
        mixer.music.stop()
        #objection sound effect is played 
        objection = mixer.Sound("objection.wav")
        objection.play()
      #the iconic Objection! bubble is given a position 
        X = 1000

        objection_img = pygame.image.load('objection.png')
        objection_img = pygame.transform.scale(objection_img,(900,800))

        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                      #once the user clicks on the arrow, Apollo will corner Moe 
                        if scene_button.collidepoint(event.pos):
                            pursuit()
            screen.fill(BLACK)
          #bubble's speed. upon reaching zero it stops
            X += -50

            if X == 0:
                X += 50
            
            screen.blit(objection_img, (X, 40))
            screen.blit(next_scene, scene_button)

            pygame.display.flip()


def pursuit(): #Apollo's rebuttal 
    pygame.display.set_caption("Cross Examination")

    while True:
    #obection theme is loaded 
        mixer.music.load("objection theme.wav")

        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            #Apollo points out the inconsistency in Moe's testimony 
            apolloCross8.showText()
            moeCross7.showText()
            apolloCross9.showText()
            moeCross8.showText()
          #Apollo's objection theme plays 
            mixer.music.play()
            apolloCross10.showText()
            moeCross9.showText()
            apolloCross11.showText()
            sys.exit()
            pygame.display.flip()

#start of the game is called 
main_menu()