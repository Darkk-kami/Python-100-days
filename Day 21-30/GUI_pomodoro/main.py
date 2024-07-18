from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
HEIGHT = 400
WIDTH = 500
reps = 0
time_remaining = 0
timer_id = None


def stop_timer():
    global timer_id

    if timer_id is None:
        reset()

    if timer_id:
        window.after_cancel(timer_id)
        timer_id = None


def reset():
    global timer_id, time_remaining, reps
    reps = 0
    time_remaining = 0
    timer_id = 0
    canvas.itemconfig(timer, text=f"00:00")
    canvas.itemconfig(heading, text="TIMER")
    canvas.itemconfig(check_mark, text="")


def start_timer():
    global reps, timer_id
    if timer_id is None:
        if time_remaining > 0:
            count_down(time_remaining)
        else:
            continue_time()
    else:
        continue_time()


def continue_time():
    global reps
    reps += 1
    if reps % 8 == 0:
        canvas.itemconfig(check_mark, text="✔" * (reps//2))
        count_down(LONG_BREAK_MIN * 60)
        canvas.itemconfig(heading, text="LONG BREAK", fill=RED)
    elif reps % 2 == 0:
        canvas.itemconfig(check_mark, text="✔" * (reps//2))
        canvas.itemconfig(heading, text="SHORT BREAK", fill=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        canvas.itemconfig(heading, text="WORK", fill=GREEN)
        count_down(WORK_MIN * 60)


def count_down(count):
    global time_remaining, timer_id
    time_remaining = count

    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f'0{count_sec}'

    if count >= 0:
        timer_id = window.after(1000, count_down, count - 1)
        canvas.itemconfig(timer, text=f'{count_min}:{count_sec}')
    else:
        start_timer()


window = Tk()
window.title("pomodoro")
window.minsize(width=WIDTH, height=HEIGHT)
window.maxsize(width=WIDTH, height=HEIGHT)
window.config(bg=YELLOW)

canvas = Canvas(width=WIDTH, height=HEIGHT, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file='tomato.png')
canvas.create_image(WIDTH/2, HEIGHT/2, image=img)
timer = canvas.create_text(WIDTH/2, HEIGHT/2 + 20, text="00:00", fill="white", font=(FONT_NAME, 38, "bold"))
heading = canvas.create_text(WIDTH/2, 40, text="TIMER", fill=GREEN, font=(FONT_NAME, 34, "bold"))
check_mark = canvas.create_text(WIDTH/2, HEIGHT - 40, text="", fill=GREEN, font=(FONT_NAME, 20, "bold"))
canvas.pack()

start_button = Button(text="START", command=start_timer)
start_button.place(x=20, y=260)

stop_button = Button(text="STOP", command=stop_timer)
stop_button.place(x=WIDTH - 60, y=260)

window.mainloop()
