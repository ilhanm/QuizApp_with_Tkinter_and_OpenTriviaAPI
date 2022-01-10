from tkinter import *
from quiz_brain import QuizBrain
from time import sleep

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quizbrain :QuizBrain) -> None:
        self.quiz=quizbrain
        self.window=Tk()
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
                
        self.scoreBoard=Label(text="Score: 0",bg=THEME_COLOR,fg="white")
        self.scoreBoard.config(font=("Arial",15))
        self.scoreBoard.grid(row=0,column=1)
        self.canvas=Canvas(width=300,height=250,bg="gold")
        self.question_text=self.canvas.create_text(150,125,text="Questions here",font=("Arial",20,"italic"),width=250)
        self.canvas.grid(row=2,column=1, columnspan=2, pady=50)
        true_image=PhotoImage(file="images/true.png")
        false_image=PhotoImage(file="images/false.png")
        self.trueButton=Button(image=true_image).grid(row=3,column=1)
        self.falseButton=Button(image=false_image).grid(row=3,column=2)
        self.get_next_question()
        
        self.window.mainloop()

    def get_next_question(self):
        q_text= self.quiz.next_question()
        self.canvas.itemconfig(self.question_text,text=q_text)
