from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# Create a list of indexes to be learned
# with open(file="data/to_learn.txt", mode="w") as file:
#     to_write_in_file = ""
#     for i in range(0,101):
#         to_write_in_file += str(i)+"\n"
#     print(to_write_in_file)
#     file.write(to_write_in_file)

# Reading data
data = pd.read_csv("data/french_words.csv")
# print(data.iloc[100])

# Generate random French words


def random_french():
    ri = random.randint(0, 100)
    return ri, data.iloc[ri]["French"]


def flip_card(index):
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=data.iloc[index]["English"], fill="white")


def right_command():
    global flip_timer
    if flip_timer != 0:
        window.after_cancel(flip_timer)
    index, french_word = random_french()
    with open(file="data/to_learn.txt", mode="r") as file:
        indexes = file.readlines()
    if index in indexes:
        right_command()
    else:
        canvas.itemconfig(title, text="French", fill="black")
        canvas.itemconfig(word, text=french_word, fill="black")
        canvas.itemconfig(canvas_image, image=card_front_img)
        with open(file="data/to_learn.txt", mode="a") as file:
            file.write(str(index))
            file.write("\n")
        flip_timer = window.after(3000, flip_card, index)

    # window.after_cancel(after_id)


def left_command():
    global flip_timer
    if flip_timer != 0:
        window.after_cancel(flip_timer)
    canvas.itemconfig(title, text="French", fill="black")
    index, french_word = random_french()
    canvas.itemconfig(word, text=french_word, fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    flip_timer = window.after(3000, flip_card, index)
    # window.after_cancel(after_id)

# Creating the UI

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = 0

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526)
canvas_image = canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=right_command)
right_button.grid(column=1, row=1)

left_image = PhotoImage(file="images/wrong.png")
left_button = Button(image=left_image, highlightthickness=0, command=left_command)
left_button.grid(column=0, row=1)

left_command()

window.mainloop()
