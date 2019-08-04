print("Mad Libs Game")
print("Start Below:")

num = input("Number: ")
noun = input("Noun(plural): ")
name = input ("Name: ")
sentence = input("Any sentence: ")
verb = input("Verb: ")

if num =="" or noun =="" or name =="" or sentence =="" or verb =="":
    print("Please fill in all the following inputs.")
else:
    story = "It was " + str(num) + " o\'clock when I heard a nock at the door. \nI opened the door and there was a box full of " + noun + " with a note saying \"From Mr. " + name.title() + "\".\nJust as I closed the door I heard a scream \"" + sentence.upper() + "\".\nI frozein place and all I could do was " + verb +"."
    print(story)


print ("END")
