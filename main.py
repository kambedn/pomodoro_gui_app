from tkinter import *
# ---------------------------- CONSTANTS -------------------------------
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ''


# ---------------------------- TIMER RESET -------------------------------
def reset_timer():
    window_tk.after_cancel(timer)  # cancelling the current timer
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    check_m_text.config(text='')
    up_text.config(text="Timer", fg=GREEN)


# ---------------------------- TIMER MECHANISM -------------------------------
def start_timer():
    global reps
    reps += 1

    # These lines make the app window pop up on the screen on the top of other windows
    window_tk.attributes('-topmost', True)
    window_tk.update()
    window_tk.attributes('-topmost', False)

    if reps % 2:  # work
        countdown(WORK_MIN * 60)
        up_text.config(text="Work")
    elif reps == 8:  # long break
        countdown(LONG_BREAK_MIN * 60)
        up_text.config(text="Break", fg=RED)
    else:  # short breaks
        countdown(SHORT_BREAK_MIN * 60)
        up_text.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM -------------------------------
def countdown(count):
    canvas.itemconfig(timer_text, text=f"{count//60:02d}:{count%60:02d}")  # displaying time in format MM:SS
    if count > 0:  # while the time is positive
        global timer
        timer = window_tk.after(1000, countdown, count-1)  # count-1 is passed as an argument to the countdown function
    else:  # if count is equal to 0
        if reps % 2:  # if a work stage is ended, a check mark is added below the tomato image
            check_m_text.config(text=(reps//2+1)*'✔')
        start_timer()  # starting another timer

    # has to be executed after creating the canvas variable


# ---------------------------- UI SETUP -------------------------------
# App window
window_tk = Tk()
window_tk.title("Pomodoro")
window_tk.config(padx=100, pady=50, bg=YELLOW)

# Canvas - image and timer text
canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=photo)
timer_text = canvas.create_text(103, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# Title label
up_text = Label(text="Timer", padx=10, pady=5, font=(FONT_NAME, 42, 'bold'), fg=GREEN, bg=YELLOW)
up_text.grid(column=1, row=0)

# Check marks
check_m_text = Label(text='', font=(FONT_NAME, 20, 'bold'), padx=5, pady=5, fg=GREEN, bg=YELLOW)
check_m_text.grid(column=1, row=3)

# Start button
start_btn = Button(text="Start", command=start_timer, font=(FONT_NAME, 12, 'bold'), highlightthickness=0)
start_btn.grid(column=0, row=2)

# Reset button
reset_btn = Button(text="Reset", command=reset_timer, font=(FONT_NAME, 12, 'bold'), highlightthickness=0)
reset_btn.grid(column=2, row=2)


window_tk.mainloop()
