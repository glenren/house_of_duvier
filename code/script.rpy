# The script of the game goes in this file.

define uma = Character("Unknown Voice 1", color="#3048D8")
define ume = Character("Unknown Voice 2", color="#BD1F29")
define ue = Character("Unknown Voice 3", color="#9017B5")
define bg = Character("Blue Girl", color="#3048D8")
define rl = Character("Red Lady", color="#BD1F29")
define ld = Character("Lord Duvier", color="#9017B5")
define e = Character("Endrei", color="#9017B5")
define ma = Character("Marion", color="#3048D8")
define me = Character("Medea", color="#BD1F29")
define you = Character ("You", color="#ffffff")

define flash = Fade(0.2, 0.0, 0.8, color="#ffffff")
define slowdissolve = Dissolve(1.0)
define slowfade = Fade(0.5, 0.2, 1.0)

transform center:
    xalign 0.5
    yalign 1.0
transform ecenter:
    xalign 0.635
    yalign 1.0
transform left:
    xalign -0.1
    yalign 1.0
transform right:
    xalign 1.1
    yalign 1.0
transform leftish:
    xalign 0.1
    yalign 1.0
transform rightish:
    xalign 0.9
    yalign 1.0

# Let's do this :)

label start:

    scene modern room

    "You sit down at your sofa and release a contented sigh, feeling your muscles relax as you sink deeper into the soft cushions."
    "After a long day of work, this was exactly what you needed. Maybe you'll turn on the TV or fix yourself a meal later, but for now you plan on enjoying the freedom to do nothing."
    "As you relax, you close your eyes. Maybe a nap wouldn't hurt..."

    show black
    with dissolve

    show black
    with flash

    uma "Something went wrong!"
    ume "Why is there a rift here?"
    uma "I don't know! This wasn't supposed to happen!"

    show black
    with flash

    show black
    with flash

    uma "There's something approaching!"
    ume "What? Is it a daemon?"
    uma "I don't know! It looks human, though it's too early to tell."

    show black
    with flash

    show black
    with flash

    show black
    with flash

    uma "Woah! It came through the rift!"
    ume "That's not a daemon. It's not giving off any energy at all."
    ue "An anomoly... How peculiar."

    scene windows blurry
    with slowdissolve

    "You slowly open your eyes."
    "Your head is killing you, and it doesn't look like you're in any room in your house, despite your vision still being blurry."
    "What happened last night? All you can remember is working late, and falling asleep on your sofa..."
    "Nothing to warrant this headache."

    show windows blurry
    with slowfade

    show windows blurry
    with slowfade

    show windows
    with slowdissolve

    "This is definitely not your house."
    "You look around at your surroundings. You seem to be on a large, fancy bed in a room that looks straight out of the 1800s. Turning to your right, you startle."
    "There's a girl sitting on an armchair, reading a book that looks to be in a language you've never seen before. She hasn't seem to have noticed that you're awake and staring at her, so you take the time to observe her."
    "The first thing you notice is the blue. She has blue hair, and her clothes are blue too. She seems to be wearing a dress, though it's not any type of dress you've ever seen before."
    "The second thing you notice is that she looks young, younger than you at least. You wonder who she is, and if this is her room."
    "Speaking of which, maybe it's time to get some answers."

    you "Who are you? And where am I?"

    "The girl startles, staring at you, before getting out of the chair and moving closer."

    show marion oh

    bg "Oh! You're awake!"

    show marion

    bg "Hold on, let me go get Lord Duvier. Stay here!"

    hide marion smile

    "And she's gone."
    "You ponder over her words, thinking about whether to listen and stay in bed or not."

    menu:

        "Stay in bed.":
            jump c1stay

        "Get out of bed.":
            jump c1go

    label c1stay:

        "Being in an unfamiliar place, you decide that it's best to stay put as you don't know your surroundings well. Plus, that headache from earlier is still there."
        "You decide to wait for the blue girl to come back, with whoever that \"Lord Duvier\" she mentioned is."

        jump c1done

    label c1go:

        "You decide that following orders is for chumps, and you better find out more about your surroundings while no one's watching you."
        "You sit up and attempt to leave the bed."

        you "Woah!"

        show windows
        with fade
        show windows
        with fade

        "You collapse back onto the bed, dizzy. Maybe that wasn't such a good idea after all."

        jump c1done

    label c1done:

        "A couple of minutes pass."
        "Or so you guess, since there aren't any clocks in the room."

        show marion smile at right
        "Suddenly, the door opens and three people come in, one of them being the girl from earlier."

        show endrei smile
        "Then there's a brunet with a purple streak in his hair, wearing fancy white and purple clothes. You assume that he's the lord that the girl was talking about earlier."

        show medea neutral at left
        "The last one is a red haired lady with a red and white coat. You wonder why they're all colour coded."

        show endrei at ecenter
        ld "I see you're awake, then. How are you feeling?"

    return
