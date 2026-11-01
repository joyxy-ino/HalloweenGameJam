# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define yn = Character(_("Me"), color="#ff46b8")
define yn_shout = Character(_("Me"), color="#ff46b8",what_size = 80)
define m_1 = Character("Eveline", color = "#615fed")
define m_2 = Character("Eveline?", color = "#bd0000")
define t = Character("Teacher")
define w = Character("Waitress")
define e = Character(
    None,
    window_background = None,

    what_size=80,
    what_outlines=[( 1, "#f3001c", 0, 0 )],
    what_xalign=0.5,
    what_textalign=0.5,
    what_layout='subtitle')

define fade_out = Fade(0.0,0.0,2.0)

image moth_transform:
    glitch("moth_angry") # reliable slicing
    pause 1.0
    zoom 2.5
    yanchor 0.7
    glitch("moth_monster_angry", offset=100, randomkey=None) # bigger and always-random slicing
    pause 0.2
    yanchor 1.0
    zoom 1.0
    glitch("moth_monster_angry", offset=60, randomkey=None)
    pause 0.1
    glitch("moth_monster_angry", offset=120, randomkey=None)
    pause 0.1
    "moth_monster_angry"

image moth_glitch:
    "moth_monster_angry"
    pause 1.5
    glitch("moth_monster_angry", offset=100, randomkey=None) # bigger and always-random slicing
    pause 0.1
    repeat

image bad_ending:
    Text("BAD END", size = 80, color = "#cf0000")
    "ending_bad"
    Text("BAD END", size = 80, color = "#cf0000")
    pause 1.0
    glitch ("ending_bad")
    Text("BAD END", size = 80, color = "#cf0000")
    pause 0.1 
    repeat

    #image ending text = Text("BAD END", size = 80)
image good_ending:
    Text("HAPPY END", size = 80, color = "#cf0000")
    "ending_good"

image moth_yay:
    glitch("moth_happy") # reliable slicing
    pause 1.0
    glitch("moth_monster_normal", offset=100, randomkey=None) # bigger and always-random slicing
    pause 0.2
    glitch("moth_monster_normal", offset=60, randomkey=None)
    pause 0.1
    "moth_monster_love"
    #pause 0.1
    #"moth_glitter"
# The game starts here.
image moth_glitter:
    "moth_glitter_1"
    pause 0.1
    "moth_glitter_2"
    pause 0.1
    "moth_glitter_3"
    pause 0.1
    "moth_glitter_4"
    pause 0.1
    repeat


label start:

    scene bg_classroom with fade
    play music "audio/class_ending_theme.mp3"

    "{i}It’s my first day at my new school{i}"


    # show player sprite
    show player_normal with dissolve
    yn "Um...! So that's my name. Thank you for welcoming me to your class. I hope we can all get along!"
    t "Thank you for introducing yourself, you may sit down. I think there's a free seat by Eveline"

    scene bg_eveline
    show bg_classroom:
        xanchor 0 yanchor 0
        xpos 0 ypos 0
        linear 1.0 zoom 2.0 xpos -2550 ypos -800
    pause 1.0
    
    scene bg_eveline
    show bg_classroom:
        xanchor 0 yanchor 0
        zoom 2.0
        xpos -2550 ypos -800
    show moth_normal with dissolve:
        xalign 1.0
        yalign 1.0
    "As you look in the direction your teacher is pointing, you notice a girl staring back calmly at you. "
    "Her gaze is cool, and she is undeniably elegant - long strands of hair fall around her pretty face, and they are dyed in a mesmerizing pattern you've never seen before."
    "Even stranger, she seems to be surrounded by a cloud of shimmering powder. It catches light and seems to distort the air."

    show moth_normal at right
    show player_normal:
        xalign 1.0
        yalign 1.0
        linear 2.0 xalign 0.21
    "You are unable to look away as you sit down next to her."

    scene bg_eveline
    show bg_classroom:
        xanchor 0 yanchor 0
        zoom 2.0
        xpos -2550 ypos -800
    show player_normal:
        yalign 1.0
        xalign 0.21
    show moth_smile at right
    m_1 "Hello, new student."

    "Her voice is steady but musical. You are reminded of pollen on the breeze at night."

    hide player_normal
    show player_blush:
        yalign 1.0
        xalign 0.21
    yn "H-hi."

    hide moth_normal
    hide moth_smile with dissolve

    "She turns away and says nothing more. You stumble through the rest of class, barely paying attention to the teacher's ramblings. You are focused entirely on the...presence, of the girl next to you."
    "You cannot explain it, what the mysteriousness about her is, and why you are drawn to it. No one else seems to notice it, the teacher calling on her without even a pause."

    scene bg_classroom_empty with fade
    "When class finally ends, you watch as she stands up and carefully gathers her stuff. Just as she's about to leave, you inexplicably call out to her:"
    show player_yell with moveinright
    yn "Wait!"

    scene bg_classroom_empty
    show moth_normal with dissolve
    m_1 "Yes?"
    show player_blush at left
    show moth_normal at right
    yn "Um."
    yn "..."

    hide player_blush
    show player_uh at left
    yn "Er."

    hide player_uh
    show player_ah at left with vpunch
    yn "WILL YOU GO ON A DATE WITH ME?!"

    hide player_ah
    show player_screwed at left
    "HUH?!?!?!"

    hide moth_normal
    show moth_smile at right
    m_1 "...Yes, why not?"
    show player_screwed at left
    pause 0.5
    hide player_screwed
    show player_yell at left
    with vpunch


    yn "HUHHHHHHH?!?!?!?!"
    yn "{i}HOW DID I END UP IN THIS SITUATION?!?!{i}"

    jump cafe

label cafe:
    scene bg_black
    play music "audio/cafe_theme.mp3"
    yn "{i}So...That's how I ended up in this situation{i}"
    scene bg_cafe with fade_out
    show player_uh at left
    with dissolve
    yn "Ahaha...well this is awkward"
    hide player_uh
    show player_screwed at left
    yn "To be honest with you, I've never actually been on a date. I'm not sure what came over me."
    
    show moth_smile at right
    m_1 "It's alright. I've never gone on a date before either. What do people usually do on dates?"

    hide player_screwed
    show player_normal at left
    yn "I think they start by trying to get to know each other better?"

    hide player_normal
    show player_smile at left
    yn "I can tell you a bit about myself first"

    jump question_1


label question_1:
    scene bg_cafe
    show player_think at left
    show moth_normal at right
    menu:
        "I like taking care of plants":
            jump plant

        "I like baking":
            jump baking

        "I like League of Legends":
            jump lol

label plant:
    scene bg_cafe
    show moth_normal at right

    show player_smile:
        xanchor 0
        yanchor 0
        xalign 0.0
        yalign 1.0

        linear 0.1 yoffset -20
        linear 0.2 yoffset 0
    yn "I enjoy taking care of plants! I have a flower garden in my backyard."

    hide moth_normal
    show moth_happy at right
    m_1 "Oh, how kind of you...Flowers are beautiful, and caring for them is a respectful pursuit."

    hide player_smile
    show player_happy at left
    yn "I'm glad you agree, it's so rewarding to watch them grow from little sprouts!"

    hide player_happy
    jump question_2

label baking:
    scene bg_cafe
    show moth_normal at right

    show player_smile:
        xanchor 0
        yanchor 0
        xalign 0.0
        yalign 1.0

        linear 0.1 yoffset -20
        linear 0.2 yoffset 0
    yn "I like baking in my spare time! I make a mean chiffon cake."

    hide moth_normal
    show moth_smile at right
    m_1 "That sounds delicious. I haven't tried to bake anything before, but I do quite like sweet things"

    hide player_smile
    show player_happy at left
    yn "It's pretty easy to get into! I recommend starting with something simple like cookies."

    hide player_happy
    jump question_2

label lol:
    scene bg_cafe
    show moth_normal at right

    show player_smile:
        xanchor 0
        yanchor 0
        xalign 0.0
        yalign 1.0

        linear 0.1 yoffset -20
        linear 0.2 yoffset 0
    yn "I play League! I got to Master rank last season."

    hide moth_normal
    show moth_serious at right
    m_1 "League...of Legends? I haven't heard the best things about people who play that game..."

    hide player_smile
    show player_uh at left
    yn "Oh um...they're not all that bad...Forget I said anything."

    hide player_uh
    jump question_2


label question_2:
    show player_smile at left
    yn "Oh, you should tell me something about yourself now!"
    show moth_normal at right
    m_1 "I often stargaze at night. Resting upon the grass, and staring up at the constellations in the sky - It's very relaxing"
    
    hide moth_normal
    show moth_smile at right
    m_1 "You can tell a lot about a person based on their favorite constellation. I would like to know yours."

    show player_think at left
    menu:
        "Corvus":
            jump corvus

        "Sirius":
            jump sirius

        "Musca":
            jump musca

label musca:
    scene bg_cafe

    show player_normal at left
    show moth_happy at right
    m_1 "Ah, a fine choice - you are filled with boundless energy, a creature flitting about the world with curiosity. The one I also call my favorite."

    hide player_normal
    show player_smile:
        xanchor 0
        yanchor 0
        xalign 0.0
        yalign 1.0

        linear 0.1 yoffset -20
        linear 0.2 yoffset 0
    yn "Haha, I try my best! Glad we have something in common."

    jump question_3

label corvus:
    scene bg_cafe

    show player_normal at left
    show moth_normal at right
    m_1 "An interesting answer...You are intelligent and loyal to those you are close with. However, this constellation inscribes a bird, which I am not the fondest of."

    hide player_normal
    show player_uh at left
    yn "Ah, I get it. Birds can be kind of scary sometimes, especially when you get close to their nest and they attack you!"

    jump question_3

label sirius:
    scene bg_cafe

    show player_normal at left
    show moth_serious at right
    m_1 "That's a star, not a constellation...I think that also tells me something about you."

    hide player_normal
    show player_screwed at left
    yn "Oh..."

    jump question_3
    

label question_3:
    scene bg_cafe with dissolve
    "The waitress finally walks over, having finished taking the orders of earlier customers."
    w "Hi, sorry for the long wait! What can I get started for you two today?"
    
    show player_smile at left
    with dissolve
    yn "I'll get a spiced chai, please!"
    hide player_smile
    show player_normal at left
    yn "Eveline, did you have enough time to think about what you're going to get?"

    show moth_normal at right
    with dissolve
    m_1 "Hmm, I don't come to such establishments often - I would greatly appreciate a beverage recommendation from you. What should I order?"

    hide player_normal
    show player_think at left
    menu:
        "Honeysuckle-Infused Milk":
            jump milk
        "Roasted Hazelnut Cold Brew":
            jump coffee
        "Jasmine Green Tea":
            jump tea

label milk:
    scene bg_cafe with dissolve
    "The waitress scribbles your orders down and whisks away back into the kitchen. You continue chatting for a few minutes before she returns with your drinks."
    show moth_normal with dissolve:
        xanchor 0
        yanchor 0
        xalign 1.0
        yalign 1.0

        linear 0.4 yoffset 20
        linear 0.4 yoffset 0
    "You thank her and watch in anticipation as Eveline takes a careful sip."

    hide moth_normal
    show moth_happy:
        xanchor 0
        yanchor 0
        xalign 1.0
        yalign 1.0

        linear 0.1 yoffset -20
        linear 0.2 yoffset 0
    m_1 "Ah...This is simply divine - A perfect combination of sweetness and floral flavour, what a delectable nectar you've recommended!"
    show player_happy at left
    yn "I'm glad you like it!"

    jump question_4

label tea:
    scene bg_cafe with dissolve
    "The waitress scribbles your orders down and whisks away back into the kitchen. You continue chatting for a few minutes before she returns with your drinks."
    show moth_normal with dissolve:
        xanchor 0
        yanchor 0
        xalign 1.0
        yalign 1.0

        linear 0.4 yoffset 20
        linear 0.4 yoffset 0
    "You thank her and watch in anticipation as Eveline takes a careful sip."
    
    m_1 "Mmm, thank you for the suggestion. The floral fragrance is so soft and comforting. However, maybe I would’ve preferred something more sweet - the tea itself is a bit bitter."
    
    show player_normal at left
    yn "Understandable - I'll keep that in mind for the future!"

    jump question_4

label coffee:
    scene bg_cafe with dissolve
    "The waitress scribbles your orders down and whisks away back into the kitchen. You continue chatting for a few minutes before she returns with your drinks."
    show moth_normal with dissolve:
        xanchor 0
        yanchor 0
        xalign 1.0
        yalign 1.0

        linear 0.4 yoffset 20
        linear 0.4 yoffset 0
    "You thank her and watch in anticipation as Eveline takes a careful sip."
    
    hide moth_normal
    show moth_serious at right
    m_1 "Oh...It's just so bitter...This much caffeine might make me feel ill..."
    
    show player_ah at left with vpunch
    yn "Ah! I'm so sorry!"

    jump question_4


label question_4:
    "As you two continue sipping on your drinks, suddenly, a large fly lands on the table next to your hand."
    menu:
        "Launch a calculated attack, successfully killing the fly!":
            jump attack
        "Lightly shoo the fly away":
            jump shoo
        "Half-heartedly attempt to hit the fly":
            jump attempt

label shoo:
    scene bg_cafe
    show moth_normal at right
    show player_normal at left

    m_1 "...I'm glad you didn't attempt to harm it."
    yn "Yeah I mean. I didn't want it to get into our drinks, but it wasn't doing anything wrong -"

    hide player_normal
    show player_smile at left
    yn "it was just existing in the world, like you or me."

    hide moth_normal
    show moth_blush at right
    m_1 "Indeed, that is what it's like..."

    jump question_5

label attempt:
    scene bg_cafe
    show moth_serious at right
    show player_uh at left

    m_1 "Do you usually try to exterminate insects like that?"
    yn "...Uh, not really? It's not like I'm ever fast enough to get them, it's mostly just to scare them off."
    
    hide moth_serious
    show moth_normal at right
    m_1 "I see..."

    jump question_5

label attack:
    scene bg_cafe
    show moth_mad at right
    show player_yell:
        xanchor 0
        yanchor 0
        xalign 0.0
        yalign 1.0

        linear 0.1 yoffset -75
        linear 0.1 yoffset 0
        
    pause 0.2
    show player_smile at left with vpunch
    yn "BAM! HA, got it!"

    jump death_1

label death_1:
    play music "angry_mode(purpleeyes).mp3"
    show moth_mad:
        xanchor 0
        yanchor 0
        xalign 1.0
        yalign 1.0
        block:
            linear 0.065 xoffset -5
            linear 0.065 xoffset 0
            repeat

    m_1 "..."

    scene bg_distort
    show player_normal at left
    show moth_mad:
        xanchor 0
        yanchor 0
        xalign 1.0
        yalign 1.0
        block:
            linear 0.060 xoffset -5
            linear 0.060 xoffset 0
            repeat
    "EVELINE suddenly goes quiet. In fact the entire cafe seems to go quiet. There is a strange tension in the air, as if it is about to split open and tear - but held in all at once by an invisible, bulging membrane."
    
    hide player_normal
    show player_screwed:
        xanchor 0
        yanchor 0
        xalign 0.0
        yalign 1.0
        parallel:
            linear 0.060 xoffset 4
            linear 0.060 xoffset 0
            repeat
        parallel:
            linear 0.040  yoffset 5
            linear 0.040  yoffset 0
            repeat
    yn "Eveline? Are you okay?"
    scene bg_distort
    show moth_angry:
        xanchor 0
        yanchor 0
        xalign 0.5
        yalign 1.0
        block:
            linear 0.05 xoffset -10
            linear 0.05 xoffset 0
            repeat
        
    "The membrane tears. Space shattering into incomprehensible shards. There is something wrong. Everything is wrong."
    
    scene bg_distort
    show moth_transform
    pause 1.6
    hide moth_transform

    show moth_glitch
    "An eldritch creature now stands before you, split wings dripping with dark ichor."
    m_2 "How petty and cruel of you. I thought you were different from the others."
    yn_shout "H-huh?! What's happening, Eveline, is that you?!"
    m_2 "I gave you a chance...I wanted you to give me a chance...But it seems that you are as disappointing as those humans who hunt for my head..."

    yn_shout "What— AAAAAAAHHHHH!!!"

    scene ending_bad with fade
    play music "die_music.mp3"
    show bad_ending

    pause 15.0

    scene bg_black with Fade(2.0,0.5,1.5)
    return


label question_5:
    scene bg_cafe
    show player_blush at left
    show moth_normal at right

    yn "Um...You're very pretty by the way. When I saw you in the classroom, this is kind of silly, but it was as if you were sparkling under the light."

    hide moth_normal
    show moth_happy at right
    m_1 "Thank you…But it was most likely a mere trick of the eye…"

    show player_normal at left
    hide player_blush
    yn "Maybe, but it reminded me of—"

    show player_think at left
    hide player_normal
    menu:
        "An iridescent hummingbird":
            jump hummingbird
        "Edward Cullen from Twilight":
            jump twilight
        "A graceful butterfly":
            jump death_2

label twilight:
    scene bg_cafe
    show player_blush at left
    show moth_normal at right


    m_1 "…Is that a vampire?"
    show player_smile at left
    hide player_blush
    yn "Yeah, I don’t mean it in a bad way - he literally sparkles in sunlight, and is beautiful as hell."
    
    show moth_serious at right
    hide moth_normal

    m_1 "But aren’t vampires feared bloodsucking monsters…?"

    show player_happy at left
    hide player_smile

    yn "Not anymore, it’s 2026! Besides, he and his family were supposed to represent exceptions to every rule. And falling in love after not judging someone for who they are. The sparkling helped too. A lot."

    show moth_blush at right
    hide moth_serious

    m_1 "That sounds lovely…perhaps I should watch that film sometime…"

    jump question_6

label hummingbird:
    m_1 "I’m flattered. Although I am still not fond of birds, I must say hummingbirds are quite alright. It would be pleasant dressing like a hummingbird sometime…"

    jump question_6

label death_2:
    hide moth_happy
    show moth_mad:
        xanchor 0
        yanchor 0
        xalign 1.0
        yalign 1.0
        block:
            linear 0.065 xoffset -5
            linear 0.065 xoffset 0
            repeat

    m_1 "..."

    scene bg_distort
    show player_normal at left
    show moth_mad:
        xanchor 0
        yanchor 0
        xalign 1.0
        yalign 1.0
        block:
            linear 0.060 xoffset -5
            linear 0.060 xoffset 0
            repeat
    "EVELINE suddenly goes quiet. In fact the entire cafe seems to go quiet. There is a strange tension in the air, as if it is about to split open and tear - but held in all at once by an invisible, bulging membrane."
    
    hide player_normal
    show player_screwed:
        xanchor 0
        yanchor 0
        xalign 0.0
        yalign 1.0
        parallel:
            linear 0.060 xoffset 4
            linear 0.060 xoffset 0
            repeat
        parallel:
            linear 0.040  yoffset 5
            linear 0.040  yoffset 0
            repeat
    yn "Eveline? Are you okay?"
    scene bg_distort
    show moth_angry:
        xanchor 0
        yanchor 0
        xalign 0.5
        yalign 1.0
        block:
            linear 0.05 xoffset -10
            linear 0.05 xoffset 0
            repeat
        
    "The membrane tears. Space shattering into incomprehensible shards. There is something wrong. Everything is wrong."
    
    scene bg_distort
    show moth_transform
    pause 1.6
    hide moth_transform

    show moth_glitch
    "An eldritch creature now stands before you, split wings dripping with dark ichor."
    m_2 "A butterfly…A BUTTERFLY?! HOW DARE YOU COMPARE ME TO ONE OF THOSE WRETCHED CREATURES! If it wasn’t for them, we wouldn’t have fallen so low in the eyes of the humans, wouldn’t have been banished to these splitten forms…"
    yn_shout "H-huh?! What are you talking about, Eveline, is that you?!"
    m_2 "I gave you a chance...I wanted you to give me a chance...But it seems that you are as disappointing as those humans who hunt for my head..."
    yn_shout "No, listen to me, I— AAAAAAAHHHHH!!!"

    scene ending_bad with fade
    show bad_ending

    pause 15.0


    scene bg_black with Fade(2.0,0.5,1.5)
    return

label question_6:
    scene bg_cafe
    show player_blush at left
    show moth_normal at right

    yn "Getting a bit more personal, I still don’t know where you’re from? You know where I’m from already…"
    m_1 "…I come from a place quite far away. I’m not sure you’d know it, even if I said."

    show player_yell at left
    hide player_blush

    yn "Oh, are you like an international student?"

    hide moth_normal
    show moth_smile at right

    m_1 "…In a way, I suppose."

    hide moth_smile
    show moth_blush at right
    
    m_1 "..."

    hide moth_blush
    show moth_serious at right

    m_1 "Do you believe in monsters, creatures from the space beyond… friend?"

    hide player_yell
    show player_ah at left
    yn "{i}Whoa, she called me a friend?!{i}"

    show player_yell at left
    hide player_ah
    yn "I-"

    menu:
        "Kill them all":
            jump death_3
        "believe it":
            jump believe
        "don't believe it":
            jump nobelieve

label believe:
    yn "-do believe in supernatural monsters from the space beyond."
    yn "Weird things happen in the world all the time. And I don’t think the ones causing them are necessarily monstrous if they’re just from a different place. I mean, it’s not like we’re hearing about anyone but ourselves running around and doing crimes."
    
    hide moth_serious 
    show moth_blush at right
    pause 0.75

    hide moth_blush
    show moth_happy at right
    m_1 "How…compassionate. You continue to surprise me. Hearing you speak as such, it’s almost as if you’ve befriended one yourself..."

    hide player_yell
    show player_happy at left

    yn "HA! Perhaps I have. Which only further proves that maybe they’re not so bad after all."

    jump question_7

label nobelieve:
    yn "-don’t believe in supernatural monsters from the space beyond."
    yn "I think I’m just someone who has to see something to believe it. But that also means my mind can be changed."

    hide moth_serious
    show moth_normal at right
    m_1 "…If you knew for sure they did exist, would you believe they’re all as monstrous as they seem?"

    hide player_yell
    show player_normal at left
    yn "My response’s the same as before! I would only think they were good or evil if I met them myself and got to know them."

    jump question_7

label death_3:
    show player_smile at left
    yn "-kill supernatural monsters from the space beyond, actually."
    yn "It’s my biggest hobby - hahaha, in video games, I mean!"
    
    hide moth_serious
    show moth_mad:
        xanchor 0
        yanchor 0
        xalign 1.0
        yalign 1.0
        block:
            linear 0.065 xoffset -5
            linear 0.065 xoffset 0
            repeat

    m_1 "..."

    scene bg_distort
    show player_normal at left
    show moth_mad:
        xanchor 0
        yanchor 0
        xalign 1.0
        yalign 1.0
        block:
            linear 0.060 xoffset -5
            linear 0.060 xoffset 0
            repeat
    "EVELINE suddenly goes quiet. In fact the entire cafe seems to go quiet. There is a strange tension in the air, as if it is about to split open and tear - but held in all at once by an invisible, bulging membrane."
    
    hide player_normal
    show player_screwed:
        xanchor 0
        yanchor 0
        xalign 0.0
        yalign 1.0
        parallel:
            linear 0.060 xoffset 4
            linear 0.060 xoffset 0
            repeat
        parallel:
            linear 0.040  yoffset 5
            linear 0.040  yoffset 0
            repeat
    yn "Eveline? What's wrong"
    scene bg_distort
    show moth_angry:
        xanchor 0
        yanchor 0
        xalign 0.5
        yalign 1.0
        block:
            linear 0.05 xoffset -10
            linear 0.05 xoffset 0
            repeat
        
    "The membrane tears. Space shattering into incomprehensible shards. There is something wrong. Everything is wrong."
    
    scene bg_distort
    show moth_transform
    pause 1.6
    hide moth_transform

    show moth_glitch
    "An eldritch creature now stands before you, split wings dripping with dark ichor."
    m_2 "That wasn’t funny. I thought you were different from the others."
    yn_shout "H-huh?! What’s happening, Eveline, is that you?!"
    m_2 "I gave you a chance...I wanted you to give me a chance...But it seems that you are as disappointing as those humans who hunt for my head..."
    yn_shout "I’m sorry, it was just a— AAAAAAAHHHHH!!!"

    scene ending_bad with fade
    show bad_ending

    pause 15.0


    scene bg_black with Fade(2.0,0.5,1.5)
    return

label question_7:
    scene bg_cafe
    show player_uh at left
    show moth_happy at right

    yn "…I’m kinda realizing that perhaps neither of us are very subtle."
    
    hide moth_happy
    show moth_blush at right
    m_1 "Ah…perhaps not."

    hide player_uh
    show player_normal at left
    m_1 "Usually, I struggle with comprehending interactions with your kind…"

    hide moth_blush
    show moth_serious at right
    m_1 "The complexity of humans is as winding as the cosmos. The difference being, even the cosmos are willing to yield clarity to those who give chase."

    hide moth_serious
    show moth_blush:
        xalign 1.0
        linear 1.5 xalign 0.6
    m_1 "But with you, it’s been so easy to understand…"


    hide moth_blush
    show moth_blush:
        xalign 0.6
    hide player_normal
    show player_blush at left
    yn "Eveline, why did you agree to my terribly proposed, horribly planned, at first sight date?"

    m_1 "..."
    hide moth_blush
    show moth_happy:
        xalign 0.6
    m_1 "Without even knowing it, perhaps I was hoping for someone who would understand. Who could see me for who I was, and look at me."

    hide player_blush
    show player_normal at left
    yn "You have something to show me, right?"

    hide moth_happy
    show moth_serious:
        xanchor 0
        yanchor 0
        xalign 0.6
        yalign 1.0

        linear 0.4 yoffset 30
        linear 0.4 yoffset 0

    pause 1.0
    show moth_smile with dissolve:
        xalign 0.6
        yalign 1.0
    hide moth_serious
    pause 1.0

    
    jump yes

label yes:

    scene bg_distort with dissolve


    "Everything in the cafe goes quiet. There is a strange tension in the air, as if it is about to split open and tear - but held in all at once by an invisible, silent bubble."

    "The bubble bursts. Space shattering into stardust. There is no longer anything wrong. Everything is right. It is right it is right it is"

    show moth_yay
    pause 1.0
    show moth_glitter:
        xoffset 75
        yoffset -425
    pause 0.4

    play music "audio/class_ending_theme.mp3"
    "An eldritch creature now stands before you, split wings wrapped around itself. Surrounded by a cloud of shimmering scales. Beautiful as she always was."
    m_1 "Here I am, my love. Will you look upon me still?"
    menu:
        "yes":
            scene ending_good with fade
            show good_ending

            pause 15.0

            scene bg_black with Fade(2.0,0.5,1.5)
            return
            

