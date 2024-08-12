from tkinter import *

questions = [{"question": "What does RAM stand for in computer memory?", 
     "options": ["Random Access Memory", "Readable Application Memory", " Random Application Memory"], "answer": 1},
    {"question": "What type of software is an antivirus program?",
      "options": ["System software", "Utility software", "Application software"], "answer": 2},
    {"question": "Which part of the computer is considered the brain of the computer?", 
     "options": ["CPU", "Hard drive", "RAM"], "answer": 1},
    {"question": "Which file extension is typically associated with Microsoft Word documents?", 
     "options": [" .docx", ".pptx", ".pdf"], "answer": 1},
    {"question": "Which protocol is commonly used for sending emails?", 
     "options": ["HTTP", "DNS", "SMTP"], "answer": 3}]

current_question_index = 0
score = 0

def check_answer():
    global score
    selected_option = option_var.get()
    correct_answer = questions[current_question_index]["answer"]
    if selected_option == correct_answer:
        score += 1

def next_question():
    global current_question_index, score

    check_answer()

    current_question_index += 1

    if current_question_index >= len(questions):
        question_label.config(text="Quiz completed!")
        score_label.config(text=f"Your score: {score}")
        next_button.config(state=DISABLED)
    else:
        question_data = questions[current_question_index]
        question_label.config(text=question_data["question"])
        option1_radio.config(text=question_data["options"][0], value=1)
        option2_radio.config(text=question_data["options"][1], value=2)
        option3_radio.config(text=question_data["options"][2], value=3)

        option_var.set(0)

Win = Tk()
Win.title("Coding Quiz Game")

root = Frame(Win)
root.pack(padx=20, pady=20)

question_label = Label(root, width=80, height=15 ,font=(100), text="Question")
question_label.pack()

option_var = IntVar()

option1_radio = Radiobutton(root, text="Option 1", variable=option_var, value=1)
option1_radio.pack(anchor="w")

option2_radio = Radiobutton(root, text="Option 2", variable=option_var, value=2)
option2_radio.pack(anchor="w")

option3_radio = Radiobutton(root, text="Option 3", variable=option_var, value=3)
option3_radio.pack(anchor="w")

next_button = Button(root, text="Next", command=next_question)
next_button.pack(pady=10)

score_label = Label(root, text="Score: 0")
score_label.pack()

next_question()

Win.mainloop()