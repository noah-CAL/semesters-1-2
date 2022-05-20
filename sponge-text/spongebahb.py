import pyperclip   # python code that lets me easily copy stuff to clipboard

while True:  # do this forever
    text = input('sugondese >>> ')   # get the input from the user

    # sponge_text = ''    # create an empty variable that will hold the spongified text
    # i = 1               # keeps track of which character we are looking at (e.g. 1st character, 2nd character, 3rd character, etc.)

    # ## Repeat everything "inside" this loop ##
    # while i <= len(text):   # i will start at 1st character and repeat the code until it has reached the end of the text

    #     if i % 2 == 0:                          # if you're on an even character...
    #         sponge_text += text[i-1].upper()    # make the character upper case
    #     else:                                   # otherwise...
    #         sponge_text += text[i-1].lower()    # make the character lower case

    #     i = i + 1           # add 1 to i so it looks at the next character on the next "loop cycle"
    ## End repeat block ##

    # This expression I wrote is equivalent to lines 6-17 and is preferred because it is "syntatically efficient" 
    #
    sponge_text = ''.join([char.lower() if i % 2 == 0 else char.upper() for char, i in zip(text, range(len(text)))])
    #
    # (it accomplishes the job in 1 line instead of 12 lines). However, 
    # it is hard to understand if you're not as experienced at programming

    print(sponge_text)              # display the spongified word to the screen
    pyperclip.copy(sponge_text)     # copy the word to the clipboard for maximum argumentative power
    print('\n')                     # same as pressing "Enter" on the keyboard (spaces out the command line so it's easier on the eyes)
