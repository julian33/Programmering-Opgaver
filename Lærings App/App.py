import tkinter as tk
import random
#import gradio



# Klasse til at oprette knapper
class MathButtons:
    def __init__(self, root, text, command):
        self.button = tk.Button(root, text=text, command=command)
        self.button.pack(pady=10)

    def destroy(self):
        self.button.destroy()

# Klasse til at generere spørgsmål
class QuestionFactory:
    def generate_question(self):
        num1, num2 = self.generate_numbers()
        question, answer = self.create_question(num1, num2)
        return question, answer

    def generate_numbers(self):
        return random.randint(-10, 10), random.randint(-10, 10)

    def create_question(self, num1, num2):
        raise NotImplementedError("Subclasses must implement create_question method")

# Underklasse til addition
class AdditionFactory(QuestionFactory):
    def create_question(self, num1, num2):
        question = f"What is {num1} + {num2}?"
        answer = num1 + num2
        return question, answer

# Underklasse til subtraktion  
class SubtractionFactory(QuestionFactory):
    def create_question(self, num1, num2):
        num1, num2 = max(num1, num2), min(num1, num2)
        question = f"What is {num1} - {num2}?"
        answer = num1 - num2
        return question, answer

# Underklasser til multiplikation
class MultiplicationFactory(QuestionFactory):
    def create_question(self, num1, num2):
        question = f"What is {num1} * {num2}?"
        answer = num1 * num2
        return question, answer

# Underklasser til division
class DivisionFactory(QuestionFactory):
    def create_question(self, num1, num2):
        if num2 == 0:
            num1, num2 = self.generate_numbers()
        result = num1 // num2
        question = f"What is {num1} / {num2}?"
        answer = result
        return question, answer

# Funktioner til at fjerne eksisterende knapper
def destroy_choices():
    for math_button in math_choice_buttons:
        math_button.destroy()

# Funktion til at fjerne svarknapper
def destroy_answers():
    for math_button in math_answer_buttons:
        math_button.destroy()

# Funktion til at håndtere valg af matematisk operation 
def on_choice_chosen(factory):
    destroy_choices()
    destroy_answers()

    # Genererer et nyt spørgsmål baseret på den valgte matematiske operation
    question, correct_answer = factory.generate_question()
    label.config(text=question)

    # Genererer tre forkerte svar
    incorrect_answers = [correct_answer + random.randint(-5, 5) for _ in range(3)]
    answers = [correct_answer] + incorrect_answers
    random.shuffle(answers)

    # Opretter knapper til svarmuligheder
    for answer in answers:
        math_answer_buttons.append(MathButtons(root, str(answer), lambda a=answer: check_answer(a, correct_answer, factory)))

# Funktion til at kontrollere det valgte svar
def check_answer(selected_answer, correct_answer, factory):
    if selected_answer == correct_answer:
        label.config(text="Rigtigt!")
    else:
        label.config(text=f"Forkert! Det rigtige svar var {correct_answer}")
    root.after(3000, lambda: reset_question(factory))

# Funktion til at gå til næste spørgsmål
def reset_question(factory):
    destroy_choices()
    destroy_answers()
    on_choice_chosen(factory)

# Oprettelse af skærmen
root = tk.Tk()
root.title("Matematik Træneren")

# Størrelse på vinduet
root.geometry("960x540")  # Width x Height

# Oprettelse af et label til tekstvisning
label = tk.Label(root, text="Vælg matematik emne!")
label.pack(pady=10)

# Oprettelse af knapper til valg af matematiske emne
math_choice_buttons = [
    MathButtons(root, "Addering", lambda: on_choice_chosen(AdditionFactory())),
    MathButtons(root, "Substrahering", lambda: on_choice_chosen(SubtractionFactory())),
    MathButtons(root, "Multiplicering", lambda: on_choice_chosen(MultiplicationFactory())),
    MathButtons(root, "Dividering", lambda: on_choice_chosen(DivisionFactory())),
]

# Liste til at gemme knapper til svarmuligheder
math_answer_buttons = []

# Kører Tkinter event loop
root.mainloop()