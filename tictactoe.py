from tkinter import *
import tkinter.messagebox as mb
Beclick = True
flag = 0



def ButtonClick(btm):
    global Beclick, flag, player1Name, player2Name
    if Beclick == True and btm["text"] == " ":
        btm["text"] = "X"
        Beclick = False
        flag = flag+1
        checkForWin()
    elif Beclick == False and btm["text"] == " ":
        btm["text"] = "O"
        flag += 1
        Beclick = True
        checkForWin()
    else:
        mb.showinfo("Error", "This button has already been clicked")


def checkForWin():
    if(button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
       button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
       button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" or
       button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
       button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
       button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
       button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
       button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X"):
        disableAllButtons()
        playerA = p1.get()+" "+"Wins"
        mb.showinfo("Yippey", playerA)
    elif(button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
         button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
         button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" or
         button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
         button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
         button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
         button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
         button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O"):
        disableAllButtons()
        playerB = p2.get()+" "+ "Wins"
        mb.showinfo("yippey", playerB)
    elif flag==9:
        disableAllButtons()
        mb.showinfo("Draw","Its A Tie")

def disableAllButtons():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)


tk = Tk()
tk.title("Tic Tac Toe")
playerA = StringVar()
playerB = StringVar()
p1 = StringVar()
p2 = StringVar()
player1Name = Entry(tk, textvariable=p1, bd=5)
player1Name.grid(row=1, column=1, columnspan=10)
player2Name = Entry(tk, textvariable=p2, bd=5)
player2Name.grid(row=2, column=1, columnspan=10)
buttons = StringVar()
label = Label(tk, text="Player 1", font="Times 20 bold",
              bg="white", fg="black", height=1, width=8)
label.grid(row=1, column=0)
label = Label(tk, text="Player 2", font="Times 20 bold",
              bg="white", fg="black", height=1, width=8)
label.grid(row=2, column=0)
button1 = Button(tk, text=" ", font="Times 20 bold", bg="grey",
                 fg="white", height=4, width=8, command=lambda: ButtonClick(button1))
button1.grid(row=3, column=0)
button2 = Button(tk, text=" ", font="Times 20 bold", bg="grey",
                 fg="white", height=4, width=8, command=lambda: ButtonClick(button2))
button2.grid(row=3, column=1)
button3 = Button(tk, text=" ", font="Times 20 bold", bg="grey",
                 fg="white", height=4, width=8, command=lambda: ButtonClick(button3))
button3.grid(row=3, column=2)
button4 = Button(tk, text=" ", font="Times 20 bold", bg="grey",
                 fg="white", height=4, width=8, command=lambda: ButtonClick(button4))
button4.grid(row=4, column=0)
button5 = Button(tk, text=" ", font="Times 20 bold", bg="grey",
                 fg="white", height=4, width=8, command=lambda: ButtonClick(button5))
button5.grid(row=4, column=1)
button6 = Button(tk, text=" ", font="Times 20 bold", bg="grey",
                 fg="white", height=4, width=8, command=lambda: ButtonClick(button6))
button6.grid(row=4, column=2)
button7 = Button(tk, text=" ", font="Times 20 bold", bg="grey",
                 fg="white", height=4, width=8, command=lambda: ButtonClick(button7))
button7.grid(row=5, column=0)
button8 = Button(tk, text=" ", font="Times 20 bold", bg="grey",
                 fg="white", height=4, width=8, command=lambda: ButtonClick(button8))
button8.grid(row=5, column=1)
button9 = Button(tk, text=" ", font="Times 20 bold", bg="grey",
                 fg="white", height=4, width=8, command=lambda: ButtonClick(button9))
button9.grid(row=5, column=2)
tk.mainloop()
