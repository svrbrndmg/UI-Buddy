import tkinter as tk

root= tk.Tk()
root.title("Hello, Wonderful World!")
root.geometry=('675x400')

def button_clicked():
    print("Button clicked!")

print('How many buttons? ')
numberofbuttons = int(input())
print('What text do you want on the button? ')
txt = input()
print('Choose a font: ')
fnt = input()
print('Choose a font size: ')
fnt2 = input()
print('Choose a background: ')
bckg = input()
print('Choose a foreground: ')
forg = input()
print('Choose an orientation (center, n, w, etc.: ')
anchr = input()
print('Choose a border size: ')
brdr = input()
print('Choose a background on hover: ')
activebg = input()
print('Choose a foreground on hover: ')
activefg = input()
print('Choose a height: ')
hght = input()
print('Choose a width: ')
wdth = input()

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
                   font=(fnt, fnt2),
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

if numberofbuttons > 1:
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
                   font=(fnt, fnt2),
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

else:
    root.mainloop()
