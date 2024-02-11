from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter()")
        exit(1)

class Engine(object):
    def __init__(self,scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):
    quips = [
        "You died. You kinda suck at this.",
        "Your Mom would be proud... if she where smarter",
        "Such a luser."
        "I have a small puppy that's better at this"
        "You are worse than your dad's jokes."
    ]
    def enter(self):
        print(Death.quips[randint(0,len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):
    #entire actions are coded into the function
    def enter(self):
        print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship and
            destroyed your entire crew.You are the last surviving
            member and your last mission is to get the neutron destruct
            bomb from the Weapons Armory, put it in the bridge, and
            blow the ship up after getting into an escape pod.
            You're running down the central corridor to the Weapons
            Armory when a Gothon jumps out, red scaly skin, dark grimy
            teeth, and evil clown costume flowing around his hate
            filled body.He's blocking the door to the Armory and
            about to pull a weapon to blast you.
            """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                Quick on the draw you yank out your blaster and fire
                it at the Gothon.
                His clown costume is flowing and
                moving around his body, which throws off your aim.
                Your laser hits his costume but misses him entirely.
                This completely ruins his brand new costume his mother
                bought him, which makes him fly into an insane rage
                and blast you repeatedly in the face until you are
                dead.Then he eats you.
                """))
            return 'death'

        elif action == "dodge!":
            print(dedent("""
                Like a world class boxer you dodge, weave, slip and
                slide right as the Gothon's blaster cranks a laser
                past your head.In the middle of your artful dodge
                your foot slips and you bang your head on the metal
                wall and pass out.
                You wake up shortly after only to
                die as the Gothon stomps on your head and eats you.
                """))
            return 'death'

        elif action == "tell a joke!":
            print(dedent("""
                Lucky for you they made you learn Gothon insults in the academy.
                You tell the one Gothon joke you know:Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,
                fur fvgf nebhaq gur ubhfr.The Gothon stops, tries
                not to laugh, then busts out laughing and can't move.
                While he's laughing you run up and shoot him square in
                the head putting him down, then jump through the
                Weapon Armory door.
                """))
            return 'laser_weapon_armory'
        
        else:
            print("Does not compute!")
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
            You do a dive roll into the Weapon Armory, crouch and scan
            the room for more Gothons that might be hiding.
            It's dead quiet, too quiet.
            You stand up and run to the far side of
            the room and find the neutron bomb in its container.
            There's a keypad lock on the box and you need the code to
            get the bomb out.
            If you get the code wrong 10 times then
            the lock closes forever and you can't get the bomb.
            The code is 3 digits.
            """))
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        print(code)
        guess = input("[Keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZEEDDD")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                The container clicks open and the seal breaks, letting
                gas out. You grab the neutron bomb and run as fast as
                you can to the bridge where you must place it in the
                right spot.
                """))
            return 'the_bridge'

        else:
            print(dedent("""
                The lock buzzes one last time and then you hear 
                sickening melting sound as the mechanism is fused
                together. You decide to sit there, and finally the
                Gothons blow up the ship. 
                """))
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print("You see 5 Gothons trying to control ship")

        action = input("> ")

        if action == "Throw the bomb":
            print("You get killed by the Gothon as they try disarming the bomb")
            return 'death'
        elif action == "Slowly place the bomb":
            print("You place the bomb and fuse the door.")
            return 'escape_pod'
        else:
            print("Doesn't compute")
            return 'the_bridge'


class EscapePod(Scene):

    def enter(self):
        print("You reach the escape pods without interference.")

        good_pod = randint(1,5)
        print(good_pod)
        guess = input("[pod]> ")

        if int(guess) != good_pod:
            print("You implode to death")
            return 'death'

        else:
            print("You escape to planet below")
            return 'finished'

class Finished(Scene):

    def enter(self):
        print("You Won! Good job")
        return 'finished'

class Map(object):
    scenes = {
        'central_corridor' : CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge':TheBridge(),
        'escape_pod':EscapePod(),
        'death':Death(),
        'finished':Finished()
    }
    def __init__(self,start_scene):
        self.start_scene = start_scene

    def next_scene(self,scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()