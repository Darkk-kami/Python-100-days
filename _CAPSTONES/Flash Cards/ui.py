from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"


class Ui:
    def __init__(self, cards):
        self.card_deck = cards
        self.score = -1
        self.total = len(self.card_deck)
        self.current_card = ""
        self.window = Tk()
        self.title = self.window.title("Flash Cards")
        self.window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

        self.timer = self.window.after(5000, func=self.flip_card)

        self.card_back = PhotoImage(file="images/card_back.png")
        self.card_front = PhotoImage(file="images/card_front.png")

        self.canvas = Canvas(self.window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.image_bg = self.canvas.create_image(400, 263, image=self.card_front)
        self.head = self.canvas.create_text(400, 150, text="Japanese", font=("Arial", 52, "bold"))
        self.body = self.canvas.create_text(400, 253, text="English", font=("Arial", 24, "normal"))
        self.canvas.grid(column=0, row=0, columnspan=2)

        yes_img = PhotoImage(file="images/right.png")
        no_img = PhotoImage(file="images/wrong.png")

        self.yes_button = Button(image=yes_img, highlightthickness=0, command=lambda: self.next_card('1'))
        self.no_button = Button(image=no_img, highlightthickness=0, command=lambda: self.next_card('0'))
        self.yes_button.grid(column=0, row=1)
        self.no_button.grid(column=1, row=1)

        self.window.mainloop()

    def next_card(self, button_id):
        self.window.after_cancel(self.timer)

        if button_id == '1':
            self.score += 1

        if len(self.card_deck) == 1:
            self.canvas.itemconfig(self.head, text="--End--")
            self.canvas.itemconfig(self.body, text=f"Total Score:{self.score/len(self.total)}")
            self.yes_button.configure()
            self.no_button.configure()

        else:
            if self.current_card in self.card_deck:
                self.card_deck.remove(self.current_card)

            self.current_card = random.choice(self.card_deck)

            self.canvas.itemconfig(self.image_bg, image=self.card_front)
            self.canvas.itemconfig(self.head, text="Japanese")
            self.canvas.itemconfig(self.body, text=f"{self.current_card[0]}\n{self.current_card[1]}")

            self.timer = self.window.after(5000, func=self.flip_card)

    def flip_card(self):
        self.canvas.itemconfig(self.image_bg, image=self.card_back)
        self.canvas.itemconfig(self.head, text="English")
        self.canvas.itemconfig(self.body, text=f"{self.current_card[2]}")
