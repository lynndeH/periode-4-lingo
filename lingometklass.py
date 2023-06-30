# all mijn imports
import random
import tkinter as tk
import time

#all mijn variabelen
wordlist = ["lynn", "jelle", "max", "jorick", "thomas"]
word = random.choice(wordlist)
guesses = 0
game_started = False
start_time = 0

#hier start de game dit doet die wanneer op de knop start geklikt wordt
def start_game():
    #global zorgt ervoor dat de variabelen ook buiten de functie gebruikt kunnen worden
    global game_started, start_time
    start_time = time.time() 
    #hij roept de functie update_timer aan  
    update_timer()
    game_started = True
    #zodra er op de knop start geklikt wordt dan verdwijnt de knop start zichzelf
    start_button.pack_forget() 
    #en dan nadat de knop weg is komen de packs van de andere widgets tevoorschijn
    label.pack()
    entry.pack()
    button.pack()
    result_label.pack()
    timer_label.pack()
    reset_button.pack()
    tk.Label(window, textvariable=guesses_label).pack()
    highscore_label.pack()  
    highscore_listbox.pack() 
    
#hier reset die de game dit doet die wanneer op de knop reset geklikt wordt
def reset_game():
    global word, guesses, game_started, start_time
    word = random.choice(wordlist)
    guesses = 0
    game_started = True
    start_time = time.time()
    result.set("")  
    guesses_label.set("Aantal pogingen: 0")  
    label.config(text=f"Jouw woord heeft {len(word)} letters")  
    entry.delete(0, tk.END)  
    
#de timer functie
def update_timer():
    timer_label.config(text="Timer: " + get_elapsed_time())
    window.after(1000, update_timer)

#hier valideert die de input van de gebruiker en wordt gekeken welke letters goed zijn en welke niet
def validate_input():
    global guesses  
    if not game_started:
        return
    
    #eerst zetten we de letters allemaal gelijk naar lowercase
    guess = entry.get().lower()
    
    #als de gebruiker meer dan 4 keer fout heeft gegokt dan krijgt die een melding dat die verloren heeft
    if guesses >= 4:
        result.set("Helaas, je hebt verloren!")
        return
    
    #als de gebruiker een woord invoert dat niet even lang is als het woord dat geraden moet worden dan krijgt die een melding dat die een woord moet invoeren met het aantal letters dat het woord heeft
    if len(guess) != len(word):
        result.set(f"Typ een woord met {len(word)} letters.")
        return
    
    #als de gebruiker het woord goed heeft geraden dan krijgt die een melding dat die gewonnen heeft en hoeveel tijd die erover heeft gedaan en hoeveel pogingen die heeft gedaan
    if guess == word:
        result.set("Gefeliciteerd, goed gegokt! Jouw score is: " + str(get_elapsed_ms()) + " ms in " + str(guesses) + " pogingen.")
        add_entry(guess, get_elapsed_ms())
        return
    
    feedback = ""
    #hier wordt gekeken welke letters goed zijn en welke niet
    for position, letter in enumerate(guess):
        if letter == word[position]:
            feedback += letter
        elif letter in word:
            feedback += "?"
        else:
            feedback += "-"
    
    result.set(feedback)
    guesses += 1  # voeg een poging toe aan het einde van de functie
    guesses_label.set(f"Aantal pogingen: {guesses}")  #tabel update


#hier wordt de ms berekend
def get_elapsed_ms():
    #alleen als game op true staat
    if game_started:
        elapsed_time = time.time() - start_time
        return int(elapsed_time * 1000)
    else:
        return 0

#hier wordt de tijd berekend
def get_elapsed_time():
    if game_started:
        elapsed_time = time.time() - start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        #hier wordt de tijd in een mooi formaat gezet dus 2 cijfers en dan : en dan weer 2 cijfers
        return "{:02d}:{:02d}".format(minutes, seconds)
    else:
        return "00:00"
    
    #hier wordt de highscore toegevoegd aan de listbox
def add_entry(guess, elapsed_time):
    #mooi formaat tekstje
    entry = f"Gokwoord: {guess}, Tijd: {elapsed_time} ms, Kansen: {guesses}"
    highscore_listbox.insert(tk.END, entry)


window = tk.Tk()
window.title("Lingo")

# Maak widgets aan
result = tk.StringVar()
guesses_label = tk.StringVar()
result_label = tk.Label(window, textvariable=result)
guesses_label.set("Aantal pogingen: 0")  
start_button = tk.Button(window, text="Start", command=start_game)
label = tk.Label(window, text=f"Jouw woord heeft {len(word)} letters")
entry = tk.Entry(window)
button = tk.Button(window, text="Gok", command=validate_input)
start_button = tk.Button(window, text="Start", command=start_game)
timer_label = tk.Label(window, text="Timer: 00:00")
reset_button = tk.Button(window, text="Reset", command=reset_game)
highscore_label = tk.Label(window, text="Highscores")
highscore_listbox = tk.Listbox(window)




start_button.pack()  #en de startknop wordt gepackt
window.mainloop()
