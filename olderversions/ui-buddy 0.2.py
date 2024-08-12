import tkinter as tk
import time
import sys
# tkinter is obviously the library I will be using for
# button widgets and the like, as it's by far the easiest to understand.
# (not that there are many more python libraries that allow you to make buttons)
# Time is needed to make the program not close immediately after it's finished.

print("UI-Buddy v0.2, welcome!")
print("What should the window name be? ")
wndwnm = input()
root= tk.Tk()
root.title(wndwnm)
# basically
# root is just the name I chose for the window,
# and all the choices you can make concerning the window itself are made here. (like the name)
# Sadly, though, you cannot change the window size, as the button size decides the window size.
# At least you can expand the window after running the program, though.
print("Would you like to use a custom icon for the window? ")
iconchoice = input()
if iconchoice == "yes":
   print("Where is the icon located? e.g. myfile.ico if it's in the UI-Buddy folder or OR C:/Users/Someone... if not ")
   iconloc = input()
   root.iconbitmap(iconloc)
elif iconchoice == "no":
   root.iconbitmap("default.ico")
else:
   print("You have entered in unapplicable information, icon has been set to default. ")
   root.iconbitmap("default.ico")

# this above loop endlessly loops until youve entered yes or no.

def button_clicked():
    print("You've clicked the button! ")
# above is just a placeholder. sometime,
# you WILL be able to choose what the button does.
# Very hard, though, so uhh that'll probs be late in dev.

print('How many buttons would you like? ')
numberofbuttons = int(input())
# this. this STUPID variable has caused me more pain than you can imagine.
# Basically, it's a variable that lets the player choose how many buttons will appear.
# It's a pain in the ass, though, as Python keeps seeming to think it's a color variable
# or a fucking integer sometimes. Seriously, FUCK this var.
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
print('Choose the height of the button: ')
hght = input()
print('Choose the width of the button: ')
wdth = input()
print('Choose the alignment of the button (center, n (north), w (west), etc.): ')
anchr = input()
# these are just the general changes you get to make to the buttons.
# MORE TO COME! I PROMISE! edit: they are coming in the
# customization update, coming soon to a dick near you. (either
# 0.3 or 0.3)


if numberofbuttons == 1:
   button = tk.Button(root, 
                   text=txt, 
                   command=button_clicked,
                   activebackground=activebg, 
                   activeforeground=activefg,
                   anchor=anchr,
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

   button.pack(padx=20, pady=20)

   root.mainloop()

elif numberofbuttons == 2:
   button = tk.Button(root, 
                   text=txt, 
                   command=button_clicked,
                   activebackground=activebg, 
                   activeforeground=activefg,
                   anchor=anchr,
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
                   command=button_clicked,
                   activebackground=activebg, 
                   activeforeground=activefg,
                   anchor=anchr,
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
                   command=button_clicked,
                   activebackground=activebg, 
                   activeforeground=activefg,
                   anchor=anchr,
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
                   command=button_clicked,
                   activebackground=activebg, 
                   activeforeground=activefg,
                   anchor=anchr,
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
                   command=button_clicked,
                   activebackground=activebg, 
                   activeforeground=activefg,
                   anchor=anchr,
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
                   command=button_clicked,
                   activebackground=activebg, 
                   activeforeground=activefg,
                   anchor=anchr,
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
                   command=button_clicked,
                   activebackground=activebg, 
                   activeforeground=activefg,
                   anchor=anchr,
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
                   command=button_clicked,
                   activebackground=activebg, 
                   activeforeground=activefg,
                   anchor=anchr,
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
                   command=button_clicked,
                   activebackground=activebg, 
                   activeforeground=activefg,
                   anchor=anchr,
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
else:
    print("You have entered in unapplicable information at some point. The program will now restart after 3 seconds. ")
    exec(open('ui-buddy 0.2.py').read())
    sys.exit()
# i've chosen to put the comment here as to not break this.
# It's very fragile trust me. Anyways, not much to explain here, even,
# as I don't understand much of it tbh. Ya make a button with tk.Button,
# specify some parameters (usually in the code, but this is UI-Buddy, where
# you get to choose your own adventure!! HELL YEAH BROTHER!!!)
# and uhhh, yeah, there's an else statement in case the user enters in bad data.
# DON'T ENTER COLORS IN WHEN IT ASKS YOU FOR A BORDER SIZE, KIDS! THAT'S ALL FOLKS!
print("Would you like to quit or restart from the beginning again? ")
restart = input()
while True:
   if restart == "restart":
      print("The program will restart in 1 second. ")
      time.sleep(1)
      exec(open('ui-buddy 0.2.py').read())
      sys.exit()
   elif restart == "quit":
      print("The program will quit in 3 seconds. ")
      time.sleep(3)
      quit()
   else:
      print("Please enter valid options only. ")
      continue
