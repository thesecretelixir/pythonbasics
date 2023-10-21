
print("Welcome to the poetry collection by the_secret_elixir")

print("Before we proceed further, We eager to know, What is your take on Poetry?\n"+ "Describe Poetry in One word: " )

Your_Word = str(input("Your word here:"))

print("Woah! That's quite an unique take on Poetry! ")

Poet_name= str(input("Well, What is the name of your favourite Poet?: "))

print(f"Ah, hardcore agree {Poet_name} is worth reading, Commendable Choice!")

Poetry_Genre = ["love", "death", "agony", "joy"]

print("What poetry genre are you interested to read today?")
for genre in (Poetry_Genre):
    print(genre)

To_Read= (str(input("Choose from the list above : "))).lower()


if To_Read == str(Poetry_Genre[0]):
      print( '"Well, Love is the most powerful feeling in the world, No wonder you choose Love over everything"')
      print('"Here you go!!!\n"+ "Happy Reading"')
      print("                 ")
      print(" How do I love thee? Let me count the ways\n" + "This famous line is the opening of Elizabeth Barrett Browning\'s sonnet Sonnet 43 which beautifully expresses the depth and breadth of love, suggesting that love is immeasurable and boundless")
      print("-------------------------------------------")
      print ('"Love is an endless act of forgiveness. Forgiveness is the key to action and freedom.\n"'+ "This thought-provoking line is from Maya Angelou, known for her insightful poetry. It reflects the idea that love and forgiveness are interconnected, and forgiveness is essential for love to flourish.")
      print("-------------------------------------------")
      print('"Love itself describes its own perfection. Be speechless and listen.\n"'+ "Rumi, a renowned Persian poet and mystic, penned this profound line, emphasizing that love is a force that defies verbal description and can only be truly understood through silence and listening")
elif To_Read == str(Poetry_Genre[1]):
      print('"Well, Everyone wonders about the pinnacle of life, i.e Death , No wonder you choose to read about Death"')
      print("Here you go!!!\n"+ "Happy Reading")
      print("                 ")
      print('"Because I could not stop for Death, He kindly stopped for me.\n"'+" This line is the opening of Emily Dickinson\'s poem \"Because I could not stop for Death.\" It presents Death as a courteous and inevitable companion on life\'s journey, emphasizing its inescapable nature.")
      print("-------------------------------------------")
      print ('"Do not go gentle into that good night, Old age should burn and rave at close of day.\n"'+ "Dylan Thomas\'s \"Do Not Go Gentle into That Good Night\" is a passionate plea against submission to death, urging people to resist its approach with vigor and determination..")
      print("-------------------------------------------")
      print('"Nothing gold can stay.\n"'+ "Robert Frost\'s succinct line, from the poem \"Nothing Gold Can Stay,\" reflects the fleeting nature of beauty and the impermanence of life\'s most precious moments")
elif To_Read == str(Poetry_Genre[2]):
      print('"Well, Agony is destructing emotion, we are wondering what desrtucted you that you chose agony"')
      print("Here you go!!!\n"+ "Happy Reading")
      print("                 ")
      print("I am the master of my fate: I am the captain of my soul\n"+"From the poem \"Invictus\" by William Ernest Henley, this line encapsulates the theme of resilience in the face of agony and adversity, emphasizing the power of the human spirit to endure and overcome.")
      print("-------------------------------------------")
      print ("I am waiting for something to make me feel nothing.\n"+ "From Charles Bukowski's poem \"Style\" this line touches on the existential and emotional agony experienced by individuals waiting for a catalyst to numb their feelings or bring relief from inner turmoil.")
      print("-------------------------------------------")
      print("Hurt, is hurt, is hurt is hurt is hurt is hurt is hurt is hurt\n"+ "This repetition of \"is hurt\" is from the poem \"The History of One Tough Motherf***er\" by Charles Bukowski. It starkly conveys the unrelenting nature of agony and suffering in life")
elif To_Read == str(Poetry_Genre[3]):
      print( "Well, Who doesn't want to feel joyous , No wonder you choose to Joy!")
      print("Here you go!!!\n"+ "Happy Reading")
      print("                 ")
      print(" Joy is the sweet voice, joy the luminous cloud—we in ourselves rejoice!\n"+"This line is from William Wordsworth's poem \"Lines Written in Early Spring.\" It celebrates the joy found in the natural world and how it can awaken a sense of happiness within us.")
      print("-------------------------------------------")
      print ("And then my heart with pleasure fills, and dances with the daffodils.\n"+ "Also from Wordsworth, this line is from his famous poem \"I Wandered Lonely as a Cloud\" and describes the profound joy and inspiration he felt while observing a field of daffodils.")
      print("-------------------------------------------")
      print("There are moments when everything goes well; don't be frightened, it won't last.\n"+ "This line from Jules Supervielle\'s poem \"Joy\" hints at the fleeting nature of joy, reminding us to savor and appreciate those moments when everything seems to be going right")
else:
      print("We are constantly working to add up more poetries to our database. Till that time choose from the options above")


   