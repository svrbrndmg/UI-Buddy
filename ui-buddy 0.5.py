import tkinter as tk
import time
import random
import webbrowser
import os

ubdir = os.path.dirname(os.path.realpath(__file__))
os.chdir(ubdir)

splash = [
   "all your RAM are belong to us", "ya little freak", "ready to make a mediocre game menu at any time", "only 14.99, in stores now",
   "I love being free and open source! OS 4evar", "insert witty line here", "the worst-programmed software this side of the... galaxy",
   "stop hitting yourself", "you know I had to do it do 'em", "over and out", "schtupid", "buuurpp", "something about Minecraft", "ding, ding ding..."]

print("Welcome to UI-Buddy v0.5, " + random.choice(splash) + "!")
print("v0.5 is the... PROCRASTINATOR'S UPDATE!!")
print("")
print("What should the window name be? ")
wndwnm = input()
root = tk.Tk()
root.withdraw()
root.title("No! You aren't supposed to see this! ")
print("What will the size of the window be? e.g. 640x480 ")
wndwsz = input()
root.geometry('100x100')

main = tk.Toplevel(root)
main.title(wndwnm)
main.geometry(wndwsz)

print("Would you like to use a custom icon for the window? ")
iconchoice = input()
if iconchoice == "yes":
   print("Where is the icon located? e.g. myimage.ico if it's in the UI-Buddy folder or C:/Users/...myimage.ico if not or if it isn't working. ")
   iconloc = input()
   main.iconbitmap(iconloc)
elif iconchoice == "no":
   print("Okay. Icon has been set to default. ")
   main.iconbitmap("default.ico")
else:
   print("You have entered in unapplicable information, icon has been set to default. ")
   main.iconbitmap("default.ico")

while True:
   print("Would you like to use a custom background in the window? ")
   cstmbckgchoice = input()
   if cstmbckgchoice == "yes":
      print(r"Okay, paste the file directory here. e.g. myimage.png OR C:\Users\...\myimage.png ")
      imagechoice = input()
      bg = tk.PhotoImage(file = imagechoice)
      label1 = tk.Label(main, image = bg)
      label1.place(x = 0, y = 0, anchor=tk.NW)
      break
   elif cstmbckgchoice == "no":
      break
   else:
      print("Nothing has been due to entering of bad data, proceeding with default... ")
      break
      
print("Would you like the button(s) to open a link, open a file on your computer or print text? (please type link, print or file)")
buttonactionchoice = input()
while True:
   if buttonactionchoice == "print":
       print("What would you like the button to print? ")
       printtext = input()
       break
   elif buttonactionchoice == "link":
       print("Paste your link here. ")
       linkchoice = input()
       break
   elif buttonactionchoice == "file":
       filechoice = input(r'Paste the file directory here. ')
       break
   else:
       print("You have entered in new info")
       
def buttonaction():
    if buttonactionchoice == "print":
        print(printtext)
    elif buttonactionchoice == "link":
        webbrowser.open(linkchoice, new=2, autoraise=True)
    if buttonactionchoice == "file":
        os.startfile(filechoice)
    else:
      print("You have entered unapplicable data. ")

print('How many buttons would you like? ')
numberofbuttons = int(input())

if numberofbuttons >= 1:
   print('What text do you want on the (first) button? ')
   txt = input()
if numberofbuttons >= 2:
   print('What text do you want on the second button? ')
   txt2 = input()
if numberofbuttons >= 3:
   print('What text do you want on the third button? ')
   txt3 = input()
if numberofbuttons >= 4:
   print('What text do you want on the fourth button? ')
   txt4 = input()
if numberofbuttons >= 5:
   print('What text do you want on the fifth button? ')
   txt5 = input()
if numberofbuttons >= 6:
   print('What text do you want on the sixth button? ')
   txt6 = input()
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

done = True

while done:
   if numberofbuttons >= 1:
      button = tk.Button(main, 
                   text=txt,
                   command=buttonaction,
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

      button.pack(side=tk.TOP, padx=20, pady=20)

   

   if numberofbuttons >= 2:
      button2 = tk.Button(main, 
                   text=txt2, 
                   command=buttonaction,
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

      button2.pack(side=tk.TOP, padx=20, pady=20)

   

   if numberofbuttons >= 3:
      button3 = tk.Button(main, 
                   text=txt3, 
                   command=buttonaction,
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

      button3.pack(side=tk.TOP, padx=20, pady=20)

   
   
   if numberofbuttons >= 4:
      button4 = tk.Button(main, 
                   text=txt4, 
                   command=buttonaction,
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

      button4.pack(side=tk.TOP, padx=20, pady=20)
   
   

   if numberofbuttons >= 5:
      button5 = tk.Button(main, 
                   text=txt5, 
                   command=buttonaction,
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

      button5.pack(side=tk.TOP, padx=20, pady=20)
      
   if numberofbuttons >= 6:
      button6 = tk.Button(main, 
                   text=txt6, 
                   command=buttonaction,
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

      button6.pack(side=tk.TOP, padx=20, pady=20)
   
   main.mainloop()
   done = False
    
quit()
