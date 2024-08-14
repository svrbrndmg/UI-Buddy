import tkinter as tk
import time
import random
import webbrowser
import os
# tkinter is obviously the library I will be using for
# button widgets and the like, as it's by far the easiest to understand.
# (not that there are many more python libraries that allow you to make buttons)
# Time is needed to make the program not close immediately after it's finished.
# Random is for splash screen text. Webbrowser is for if you want the button to open a link.

ubdir = os.path.dirname(os.path.realpath(__file__))
os.chdir(ubdir)
# this is a check to prevent python from being dumb and
# running the script from system32 or whatever.

splash = ["all your RAM are belong to us", "ya little freak", "ready to make a mediocre game menu at any time", "only 14.99, in stores now", "I love being free and open source! OS 4evar", "insert witty line here", "the worst-programmed software this side of the... galaxy", "stop hitting yourself"]
# pure randomness. Not that hard to understand tbh.

print("Welcome to UI-Buddy v0.3, " + random.choice(splash) + "!")
print("What should the window name be? ")
wndwnm = input()
root= tk.Tk()
root.title(wndwnm)
print("What will the size of the window be? e.g. 640x480 ")
wndwsz = input()
root.geometry(wndwsz)
# basically:
# root is just the name I chose for the window,
# and all the choices you can make concerning the window itself are made here. (like the name)
# Sadly, though, you cannot change the window size, as the button size decides the window size.
# At least you can expand the window after running the program, though.

print("Would you like to use a custom icon for the window? ")
iconchoice = input()
if iconchoice == "yes":
   print("Where is the icon located? e.g. myimage.ico if it's in the UI-Buddy folder or C:/Users/...myimage.ico if not or if it isn't working. ")
   iconloc = input()
   root.iconbitmap(iconloc)
elif iconchoice == "no":
   print("Okay. Icon has been set to default. ")
   root.iconbitmap("default.ico")
else:
   print("You have entered in unapplicable information, icon has been set to default. ")
   root.iconbitmap("default.ico")
# icon choice! If you're a coward or have entered in bad data,
# it's off to the default icon with you.

while True:
   print("Would you like to use a custom background in the window? ")
   cstmbckgchoice = input()
   if cstmbckgchoice == "yes":
      print(r"Okay, paste the file directory here. e.g. myimage.png OR C:\Users\...\myimage.png ")
      imagechoice = input()
      bg = tk.PhotoImage(file = imagechoice)
      label1 = tk.Label(root, image = bg)
      label1.place(x = 0, y = 0, anchor=tk.NW)
      break
   elif cstmbckgchoice == "no":
      break
   else:
      print("Nothing has been due to entering of bad data, proceeding with default... ")
      break
      
print("Would you like the button(s) to open a link or print text? (link/print)")
linkortext = input()
while True:
   if linkortext == "print":
       print("What would you like the button to print? ")
       printtext = input()
       break
   elif linkortext == "link":
       print("Paste your link here. ")
       linkchoice = input()
       break
   else:
       print("invalid") 
def buttonactionchoice():
    if linkortext == "print":
        print(printtext)
    elif linkortext == "link":
        webbrowser.open(linkchoice, new=2, autoraise=True)
    else:
      print("You have entered unapplicable data. ")
# holy crap, it works. We finally have multiple button action choices.
# I never thought I'd see the day. Anyways, you a print guy or a link guy?

print('How many buttons would you like? ')
numberofbuttons = int(input())
# this. this STUPID variable has caused me more pain than you can imagine.
# Basically, it's a variable that lets the player choose how many buttons will appear.
# It's a pain, though, as Python keeps seeming to think it's a color variable
# or an integer sometimes. Seriously, screw this var. (un)Fun fact:
# It's the reason I can't get saving/loading to work.

if numberofbuttons == 1:
   print('What text do you want on the button? ')
   txt = input()
elif numberofbuttons == 2:
   print('What text do you want on the first button? ')
   txt = input()
   print('What text do you want on the second button? ')
   txt2 = input()
elif numberofbuttons == 3:
   print('What text do you want on the first button? ')
   txt = input()
   print('What text do you want on the second button? ')
   txt2 = input()
   print('What text do you want on the third button? ')
   txt3 = input()
elif numberofbuttons == 4:
   print('What text do you want on the first button? ')
   txt = input()
   print('What text do you want on the second button? ')
   txt2 = input()
   print('What text do you want on the third button? ')
   txt3 = input()
   print('What text do you want on the fourth button? ')
   txt4 = input()
elif numberofbuttons == 5:
   print('What text do you want on the first button? ')
   txt = input()
   print('What text do you want on the second button? ')
   txt2 = input()
   print('What text do you want on the third button? ')
   txt3 = input()
   print('What text do you want on the fourth button? ')
   txt4 = input()
   print('What text do you want on the fifth button? ')
   txt5 = input()
print('Choose a font: ')
fnt = input()
print('Choose a font size: ')
fntsz = input()
print('Choose a background color: ')
bckg = input()
print('Choose a foreground color: ')
forg = input()
print('Choose a background color on click: ')
activebg = input()
print('Choose a foreground color on click: ')
activefg = input()
print('Choose a border size (how thick it is, recommend 10): ')
brdr = input()
print('Choose the height of the button (recommended low values, like 5 or 10) ')
hght = input()
print('Choose the width of the button (same thing) ')
wdth = input()
print('Choose the alignment of text inside the button (center, n (north), w (west), etc.): ')
anchr = input()
print("What will the state of the button be? e.g. disabled, active or normal. ")
buttonstate = input()
# these are just the general changes you get to make to the buttons.
# MORE TO COME! I PROMISE! edit: they have been implemented as of 0.3.
# this is quite possibly the simplest thing in the whole file lel

if numberofbuttons == 1:
   button = tk.Button(root, 
                   text=txt,
                   command=buttonactionchoice,
                   activebackground=activebg, 
                   activeforeground=activefg,
                   anchor=anchr,
                   state=buttonstate,
                   bd=brdr,
                   bg=bckg,
                   cursor="hand2",
                   disabledforeground="gray",
                   fg=forg,
                   font=(fnt, fntsz),
                   height=hght,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=wdth,
                   wraplength=100)

   button.pack(side=tk.LEFT, padx=20, pady=20)

   root.mainloop()

elif numberofbuttons == 2:
   button = tk.Button(root, 
                   text=txt, 
                   command=buttonactionchoice,
                   activebackground=activebg, 
                   activeforeground=activefg,
                   anchor=anchr,
                   state=buttonstate,
                   bd=brdr,
                   bg=bckg,
                   cursor="hand2",
                   disabledforeground="gray",
                   fg=forg,
                   font=(fnt, fntsz),
                   height=hght,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=wdth,
                   wraplength=100)

   button.pack(side=tk.LEFT, padx=20, pady=20)
   button2 = tk.Button(root, 
                   text=txt2, 
                   command=buttonactionchoice,
                   activebackground=activebg, 
                   activeforeground=activefg,
                   anchor=anchr,
                   state=buttonstate,
                   bd=brdr,
                   bg=bckg,
                   cursor="hand2",
                   disabledforeground="gray",
                   fg=forg,
                   font=(fnt, fntsz),
                   height=hght,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=wdth,
                   wraplength=100)

   button2.pack(side=tk.LEFT, padx=20, pady=20)

   root.mainloop()

elif numberofbuttons == 3:
   button = tk.Button(root, 
                   text=txt, 
                   command=buttonactionchoice,
                   activebackground=activebg, 
                   activeforeground=activefg,
                   anchor=anchr,
                   state=buttonstate,
                   bd=brdr,
                   bg=bckg,
                   cursor="hand2",
                   disabledforeground="gray",
                   fg=forg,
                   font=(fnt, fntsz),
                   height=hght,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=wdth,
                   wraplength=100)

   button.pack(side=tk.LEFT, padx=20, pady=20)
   button2 = tk.Button(root, 
                   text=txt2, 
                   command=buttonactionchoice,
                   activebackground=activebg, 
                   activeforeground=activefg,
                   anchor=anchr,
                   state=buttonstate,
                   bd=brdr,
                   bg=bckg,
                   cursor="hand2",
                   disabledforeground="gray",
                   fg=forg,
                   font=(fnt, fntsz),
                   height=hght,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=wdth,
                   wraplength=100)

   button2.pack(side=tk.LEFT, padx=20, pady=20)
   button3 = tk.Button(root, 
                   text=txt3, 
                   command=buttonactionchoice,
                   activebackground=activebg, 
                   activeforeground=activefg,
                   anchor=anchr,
                   state=buttonstate,
                   bd=brdr,
                   bg=bckg,
                   cursor="hand2",
                   disabledforeground="gray",
                   fg=forg,
                   font=(fnt, fntsz),
                   height=hght,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=wdth,
                   wraplength=100)

   button3.pack(side=tk.LEFT, padx=20, pady=20)

   root.mainloop()
   
elif numberofbuttons == 4:
   button = tk.Button(root, 
                   text=txt, 
                   command=buttonactionchoice,
                   activebackground=activebg, 
                   activeforeground=activefg,
                   anchor=anchr,
                   state=buttonstate,
                   bd=brdr,
                   bg=bckg,
                   cursor="hand2",
                   disabledforeground="gray",
                   fg=forg,
                   font=(fnt, fntsz),
                   height=hght,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=wdth,
                   wraplength=100)

   button.pack(side=tk.LEFT, padx=20, pady=20)
   button2 = tk.Button(root, 
                   text=txt2, 
                   command=buttonactionchoice,
                   activebackground=activebg, 
                   activeforeground=activefg,
                   anchor=anchr,
                   state=buttonstate,
                   bd=brdr,
                   bg=bckg,
                   cursor="hand2",
                   disabledforeground="gray",
                   fg=forg,
                   font=(fnt, fntsz),
                   height=hght,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=wdth,
                   wraplength=100)

   button2.pack(side=tk.LEFT, padx=20, pady=20)
   button3 = tk.Button(root, 
                   text=txt3, 
                   command=buttonactionchoice,
                   activebackground=activebg, 
                   activeforeground=activefg,
                   anchor=anchr,
                   state=buttonstate,
                   bd=brdr,
                   bg=bckg,
                   cursor="hand2",
                   disabledforeground="gray",
                   fg=forg,
                   font=(fnt, fntsz),
                   height=hght,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=wdth,
                   wraplength=100)

   button3.pack(side=tk.LEFT, padx=20, pady=20)
   button4 = tk.Button(root, 
                   text=txt4, 
                   command=buttonactionchoice,
                   activebackground=activebg, 
                   activeforeground=activefg,
                   anchor=anchr,
                   state=buttonstate,
                   bd=brdr,
                   bg=bckg,
                   cursor="hand2",
                   disabledforeground="gray",
                   fg=forg,
                   font=(fnt, fntsz),
                   height=hght,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=wdth,
                   wraplength=100)

   button4.pack(side=tk.LEFT, padx=20, pady=20)
   
   root.mainloop()

elif numberofbuttons == 5:
   button = tk.Button(root, 
                   text=txt, 
                   command=buttonactionchoice,
                   activebackground=activebg, 
                   activeforeground=activefg,
                   anchor=anchr,
                   state=buttonstate,
                   bd=brdr,
                   bg=bckg,
                   cursor="hand2",
                   disabledforeground="gray",
                   fg=forg,
                   font=(fnt, fntsz),
                   height=hght,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=wdth,
                   wraplength=100)

   button.pack(side=tk.LEFT, padx=20, pady=20)
   button2 = tk.Button(root, 
                   text=txt2, 
                   command=buttonactionchoice,
                   activebackground=activebg, 
                   activeforeground=activefg,
                   anchor=anchr,
                   state=buttonstate,
                   bd=brdr,
                   bg=bckg,
                   cursor="hand2",
                   disabledforeground="gray",
                   fg=forg,
                   font=(fnt, fntsz),
                   height=hght,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=wdth,
                   wraplength=100)

   button2.pack(side=tk.LEFT, padx=20, pady=20)
   button3 = tk.Button(root, 
                   text=txt3, 
                   command=buttonactionchoice,
                   activebackground=activebg, 
                   activeforeground=activefg,
                   anchor=anchr,
                   state=buttonstate,
                   bd=brdr,
                   bg=bckg,
                   cursor="hand2",
                   disabledforeground="gray",
                   fg=forg,
                   font=(fnt, fntsz),
                   height=hght,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=wdth,
                   wraplength=100)

   button3.pack(side=tk.LEFT, padx=20, pady=20)
   button4 = tk.Button(root, 
                   text=txt4, 
                   command=buttonactionchoice,
                   activebackground=activebg, 
                   activeforeground=activefg,
                   anchor=anchr,
                   state=buttonstate,
                   bd=brdr,
                   bg=bckg,
                   cursor="hand2",
                   disabledforeground="gray",
                   fg=forg,
                   font=(fnt, fntsz),
                   height=hght,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=wdth,
                   wraplength=100)

   button4.pack(side=tk.LEFT, padx=20, pady=20)
   button5 = tk.Button(root, 
                   text=txt5, 
                   command=buttonactionchoice,
                   activebackground=activebg, 
                   activeforeground=activefg,
                   anchor=anchr,
                   state=buttonstate,
                   bd=brdr,
                   bg=bckg,
                   cursor="hand2",
                   disabledforeground="gray",
                   fg=forg,
                   font=(fnt, fntsz),
                   height=hght,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=wdth,
                   wraplength=100)

   button5.pack(side=tk.LEFT, padx=20, pady=20)
   
   root.mainloop()

else:
    print("You have entered in unapplicable information at some point. The program will now quit after 3 seconds. ")
    time.sleep(3)
    quit()
# i've chosen to put the comment here as to not break this.
# It's very fragile trust me. Anyways, not much to explain here, even,
# as I don't understand much of it tbh. Ya make a button with tk.Button,
# specify some parameters (usually in the code, but this is UI-Buddy, where
# you get to choose your own adventure!! HELL YEAH BROTHER!!!)
# and uhhh, yeah, there's an else statement in case the user enters in bad data.
# DON'T ENTER COLORS IN WHEN IT ASKS YOU FOR A BORDER SIZE, KIDS!
# THAT'S ALL FOLKS!
