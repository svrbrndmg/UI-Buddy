import tkinter as tk
# tkinter is obviously the library I will be using for
# button widgets and the like, as it's by far the easiest to understand.

print("What'll the window name be? ")
wndwnm = input()
root= tk.Tk()
root.title(wndwnm)
root.geometry=('100x100')
# basically
# root is just the name I chose for the window,
# and all the choices you can make concerning the window itself are made here. (like the name)
# Sadly, though, you cannot change the window size, as I cannot get it to work as of right now.

def button_clicked():
    print("Button clicked!")
# above is just a placeholder. sometime,
# you WILL be able to choose what the button does.
# Very hard, though, so uhh that'll probs be late in dev.

print('How many buttons? ')
numberofbuttons = int(input())
# this. this FUCKING variable has caused me more pain than you can imagine.
# Basically, it's a variable that lets the player choose how many buttons will appear.
# It's a pain in the ass, though, as Python keeps seeming to think it's a color variable
# sometimes. Seriously, FUCK this var.
print('What text do you want on the button? ')
txt = input()
print('Choose a font: ')
fnt = input()
print('Choose a font size: ')
fntsz = input()
print('Choose a background: ')
bckg = input()
print('Choose a foreground: ')
forg = input()
print('Choose a background on hover: ')
activebg = input()
print('Choose a foreground on hover: ')
activefg = input()
print('Choose a border size: ')
brdr = input()
print('Choose a height: ')
hght = input()
print('Choose a width: ')
wdth = input()
print('Choose an orientation (center, n, w, etc.): ')
anchr = input()
# these are just the general changes you get to make to the buttons.
# MORE TO COME! I PROMISE!


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

   button.pack(padx=20, pady=20)
   button2 = tk.Button(root, 
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

   button2.pack(padx=20, pady=20)

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

   button.pack(padx=20, pady=20)
   button2 = tk.Button(root, 
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

   button2.pack(padx=20, pady=20)
   button3 = tk.Button(root, 
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

   button3.pack(padx=20, pady=20)

   root.mainloop()

else:
    print("You have entered in unapplicable information. Try again. ")


# i've chosen to put the comment here as to not break this.
# It's very fragile trust me. Anyways, not much to explain here, even,
# as I don't understand much of it tbh. Ya make a button with tk.Button,
# specify some parameters (usually in the code, but this is UI-Buddy, where
# you get to choose your own adventure!! HELL YEAH BROTHER!!!)
# and uhhh, yeah, there's an else statement in case the user enters in bad data.
# DON'T ENTER COLORS IN WHEN IT ASKS YOU FOR A BORDER SIZE, KIDS! THAT'S ALL FOLKS!
