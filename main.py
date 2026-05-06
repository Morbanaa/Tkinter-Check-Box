from tkinter import *

class MyGui():
    def __init__(self):
        self.window = Tk()
        self.x = IntVar()

        self.photo = PhotoImage(file="M.png")

        self.check_button    = Checkbutton(self.window,
                                           text="I Agree to",
                                           variable=self.x,
                                           onvalue=1,
                                           offvalue=0,
                                           command=self.display,
                                           font=("Arial",20),
                                           fg="red",
                                           bg="black",
                                           activeforeground="red",
                                           activebackground="black",
                                           padx=25,
                                           pady=20,
                                           image=self.photo,
                                           compound='right')   
        self.check_button.pack()

        self.window.mainloop()

    def display(self):
        if(self.x.get()==1):
            print("You Agree")
        else:
            print("You don't agree")


def main():  
    my_gui = MyGui() 
    
if __name__ == "__main__":
    main()
     
