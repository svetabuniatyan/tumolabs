import random as rd 

a = rd.randint(1,3)
print(a)

if a==1:

    proper_noun = input("enter pn: ")
    adjective=input("enter a: ")
    color=input("enter color: ")
    Animal=input("enter animal: ")
    Place=input("enter place: ")

    text1=f"""Dear {proper_noun}, I am writing to you from a {adjective} castle in an enchanted forest. 
    I found myself here one day after going for a ride on a {color} {Animal} in {Place}."""


    print(text1)
elif a==2:
    Number1 = input("enter number: ")
    mot = input("enter mot: ")
    Transportation = input("enter Transportation: ")
    Adjective = input("enter Adjective: ")
    Adjective2 = input("enter Adjective2: ")
    Noun = input("enter Noun: ")
    Color = input("enter color: ")
    potb = input("enter Part of the Body: ")

    
    text2=f"""It was about {Number1} {mot} ago when I arrived at the hospital in a{mot}. 
    The hospital is a/an {Adjective} place, there are a lot of {Adjective2} {Noun} here. There are nurses here who have {Color} {potb}."""
    print(text1)
else:
    Proper_Noun=input("enter pn:")
    Noun=input("enter noun:")
    adj_f=input("enter Adjective (Feeling):")
    Verb=input("enter Verb:")
    adj_f2=input("enter adj2:")
    Animal=input("enter Animal:")
    Verb2=input("enter Verb2:")

    text3=f"""This weekend I am going camping with {Proper_Noun}. I packed my lantern, sleeping bag, and {Noun}. I am so {adj_f} to {Verb} in a tent. 
    I am {adj_f2} we might see a(n) {Animal}, I hear they're kind of dangerous. While we're camping, we are going to hike, fish, and {Verb2}. """
