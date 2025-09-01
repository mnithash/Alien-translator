import csv
import os

DICTIONARY_FILE = "dictionary.csv"

def load_dictionary():
    eng_to_alien = {}
    alien_to_eng = {}
    with open(DICTIONARY_FILE, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=" ")
        for row in reader:
            if len(row) == 2:
                eng, alien = row
                eng_to_alien[eng.lower()] = alien.lower()
                alien_to_eng[alien.lower()] = eng.lower()
    return eng_to_alien, alien_to_eng

def add_word(eng, alien):
    with open(DICTIONARY_FILE, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=" ")
        writer.writerow([eng.lower(), alien.lower()])
    print(f"Added '{eng}' ↔ '{alien}' to dictionary.")

def translate_file(input_file, output_file, direction="eng_to_alien"):
    eng_to_alien, alien_to_eng = load_dictionary()
    
    with open(input_file, "r", encoding="utf-8") as f:
        words = f.read().split()
    
    translated_words = []
    for word in words:
        w = word.lower()
        if direction == "eng_to_alien":
            translated_words.append(eng_to_alien.get(w, f"[{w}]"))  # mark missing
        else:
            translated_words.append(alien_to_eng.get(w, f"[{w}]"))

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(" ".join(translated_words))
    print(f"Translation saved to {output_file}")

# ---------------- Example Usage ----------------
if __name__ == "__main__":
    while True:
        print("\nAlien-Human Interpreter")
        print("1. Translate English → Aliench")
        print("2. Translate Aliench → English")
        print("3. Add new word to dictionary")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            inp = input("Enter input text file: ")
            outp = input("Enter output text file: ")
            translate_file(inp, outp, "eng_to_alien")
        elif choice == "2":
            inp = input("Enter input text file: ")
            outp = input("Enter output text file: ")
            translate_file(inp, outp, "alien_to_eng")
        elif choice == "3":
            eng = input("Enter English word: ")
            alien = input("Enter Aliench word: ")
            add_word(eng, alien)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")
