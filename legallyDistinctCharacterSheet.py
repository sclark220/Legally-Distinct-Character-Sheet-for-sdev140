import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

root = tk.Tk()
root.title("Legally Distinct Character Sheet")
root.configure(background='dark gray')
root.geometry("750x500")


class CharacterSheetApp:

    def __init__(self):

        self.frames = {"statBar": tk.Frame(root, bg='dark gray'),
                       "controls": tk.Frame(root, bg='dark gray'),
                       "topBar": tk.Frame(root, bg='dark gray', pady=25),
                       "sideBar": tk.Frame(root, bg='dark gray'),
                       "center": tk.Frame(root, bg='dark gray')}

        self.frames["statBar"].place(relx=0, rely=0.5, anchor='w')
        self.frames["controls"].place(relx=0.5, rely=1, anchor='s')
        self.frames["topBar"].place(relx=0.5, rely=0, anchor='n')
        self.frames["sideBar"].place(relx=1, rely=0.5, anchor='e')
        self.frames["center"].place(relx=0.5, rely=0.5, anchor="center")

        self.labels = {"name": tk.Label(self.frames["topBar"], text="Name:", bg='dark gray'),
                       "class": tk.Label(self.frames["topBar"], text="Class:", bg='dark gray'),
                       "race": tk.Label(self.frames["topBar"], text="Race:", bg='dark gray'),
                       "characterLevel": tk.Label(self.frames["topBar"], text="Level:", bg='dark gray'),
                       "modifier": tk.Label(self.frames["statBar"], text="Modifier", bg='dark gray'),
                       "statLevel": tk.Label(self.frames["statBar"], padx=10, text="Level", bg='dark gray'),
                       "strength": tk.Label(self.frames["statBar"], text="Strength:", bg='dark gray'),
                       "dexterity": tk.Label(self.frames["statBar"], text="Dexterity:", bg='dark gray'),
                       "constitution": tk.Label(self.frames["statBar"], text="Constitution:", bg='dark gray'),
                       "intelligence": tk.Label(self.frames["statBar"], text="Intelligence:", bg='dark gray'),
                       "wisdom": tk.Label(self.frames["statBar"], text="Wisdom:", bg='dark gray'),
                       "charisma": tk.Label(self.frames["statBar"], text="Charisma:", bg='dark gray'),
                       "image": tk.Label(self.frames["center"], text="IMAGE HERE MAYBE IDK", bg='dark gray')}

        self.labels["name"].grid(row=0, column=0)
        self.labels["class"].grid(row=0, column=2)
        self.labels["race"].grid(row=0, column=4)
        self.labels["characterLevel"].grid(row=0, column=6)
        self.labels["modifier"].grid(row=0, column=2)
        self.labels["statLevel"].grid(row=0, column=1)
        self.labels["strength"].grid(row=1, column=0)
        self.labels["dexterity"].grid(row=2, column=0)
        self.labels["constitution"].grid(row=3, column=0)
        self.labels["intelligence"].grid(row=4, column=0)
        self.labels["wisdom"].grid(row=5, column=0)
        self.labels["charisma"].grid(row=6, column=0)
        self.labels["image"].grid(row=0, column=0)

        self.entry = {"nameEntry": tk.Entry(self.frames["topBar"], width=20),
                      "classEntry": tk.Entry(self.frames["topBar"], width=20),
                      "raceEntry": tk.Entry(self.frames["topBar"], width=20),
                      "levelEntry": tk.Entry(self.frames["topBar"], width=20),
                      "strengthEntry": tk.Entry(self.frames["statBar"], width=3),
                      "dexterityEntry": tk.Entry(self.frames["statBar"], width=3),
                      "constitutionEntry": tk.Entry(self.frames["statBar"], width=3),
                      "intelligenceEntry": tk.Entry(self.frames["statBar"], width=3),
                      "wisdomEntry": tk.Entry(self.frames["statBar"], width=3),
                      "charismaEntry": tk.Entry(self.frames["statBar"], width=3)}

        self.entry["nameEntry"].grid(row=0, column=1, padx=(0, 25))
        self.entry["classEntry"].grid(row=0, column=3, padx=(0, 25))
        self.entry["raceEntry"].grid(row=0, column=5, padx=(0, 25))
        self.entry["levelEntry"].grid(row=0, column=7)
        self.entry["strengthEntry"].grid(row=1, column=1)
        self.entry["dexterityEntry"].grid(row=2, column=1)
        self.entry["constitutionEntry"].grid(row=3, column=1)
        self.entry["intelligenceEntry"].grid(row=4, column=1)
        self.entry["wisdomEntry"].grid(row=5, column=1)
        self.entry["charismaEntry"].grid(row=6, column=1)

        self.buttons = {"save_button": tk.Button(self.frames["controls"], text="Save", command=self.save_character),
                        "load_button": tk.Button(self.frames["controls"], text="Load", command=self.load_character),
                        "exit_button": tk.Button(self.frames["controls"], text="Exit", padx=5, command=root.destroy),
                        "modifier_button": tk.Button(self.frames["sideBar"], text="Calculate\nModifiers",
                                                     command=self.modifier)}

        self.buttons["save_button"].grid(row=7, column=0, padx=20, pady=20)
        self.buttons["load_button"].grid(row=7, column=1, padx=10, pady=20)
        self.buttons["exit_button"].grid(row=7, column=2, padx=10, pady=20)
        self.buttons["modifier_button"].grid(row=3, column=4, padx=10, pady=20)

        self.mod_labels = {"strength_modifier": tk.Label(self.frames["statBar"], bg='dark gray'),
                           "dexterity_modifier": tk.Label(self.frames["statBar"], bg='dark gray'),
                           "constitution_modifier": tk.Label(self.frames["statBar"], bg='dark gray'),
                           "intelligence_modifier": tk.Label(self.frames["statBar"], bg='dark gray'),
                           "wisdom_modifier": tk.Label(self.frames["statBar"], bg='dark gray'),
                           "charisma_modifier": tk.Label(self.frames["statBar"], bg='dark gray')}

        tk.mainloop()

    def modifier(self):
        strength = self.entry["strengthEntry"].get()
        dexterity = self.entry["dexterityEntry"].get()
        constitution = self.entry["constitutionEntry"].get()
        intelligence = self.entry["intelligenceEntry"].get()
        wisdom = self.entry["wisdomEntry"].get()
        charisma = self.entry["charismaEntry"].get()

        try:
            self.mod_labels = {"strength_modifier": tk.Label(self.frames["statBar"], width=2, bg='light gray',
                                                             text=round((int(strength) - 10) / 2)),
                               "dexterity_modifier": tk.Label(self.frames["statBar"], width=2, bg='light gray',
                                                              text=round((int(dexterity) - 10) / 2)),
                               "constitution_modifier": tk.Label(self.frames["statBar"], width=2, bg='light gray',
                                                                 text=round((int(constitution) - 10) / 2)),
                               "intelligence_modifier": tk.Label(self.frames["statBar"], width=2, bg='light gray',
                                                                 text=round((int(intelligence) - 10) / 2)),
                               "wisdom_modifier": tk.Label(self.frames["statBar"], width=2, bg='light gray',
                                                           text=round((int(wisdom) - 10) / 2)),
                               "charisma_modifier": tk.Label(self.frames["statBar"], width=2, bg='light gray',
                                                             text=round((int(charisma) - 10) / 2))}

            self.mod_labels["strength_modifier"].grid(row=1, column=2)
            self.mod_labels["dexterity_modifier"].grid(row=2, column=2)
            self.mod_labels["constitution_modifier"].grid(row=3, column=2)
            self.mod_labels["intelligence_modifier"].grid(row=4, column=2)
            self.mod_labels["wisdom_modifier"].grid(row=5, column=2)
            self.mod_labels["charisma_modifier"].grid(row=6, column=2)

        except ValueError:
            messagebox.showerror("Modifier Error", 'All "level" fields are required and they must be integers!')
            return

    def save_character(self):
        name = self.entry["nameEntry"].get()
        character_class = self.entry["classEntry"].get()
        race = self.entry["raceEntry"].get()
        character_level = self.entry["levelEntry"].get()
        strength = self.entry["strengthEntry"].get()
        dexterity = self.entry["dexterityEntry"].get()
        constitution = self.entry["constitutionEntry"].get()
        intelligence = self.entry["intelligenceEntry"].get()
        wisdom = self.entry["wisdomEntry"].get()
        charisma = self.entry["charismaEntry"].get()

        if name == "" or character_class == "" or race == "" or character_level == "" or strength == "" \
                or dexterity == "" or constitution == "" or intelligence == "" or wisdom == "" or charisma == "":
            messagebox.showerror("Save Error", "All fields are required!")
            return

        try:
            character_level = int(character_level)
            strength = int(strength)
            dexterity = int(dexterity)
            constitution = int(constitution)
            intelligence = int(intelligence)
            wisdom = int(wisdom)
            charisma = int(charisma)

        except ValueError:
            messagebox.showerror("Save Error", 'Invalid input! All "level" fields must be integers!')
            return

        filename = tk.simpledialog.askstring("File Name", "Enter the name of the file.") + ".txt"
        try:
            with open(filename, "w") as file:
                file.write(f"Name: {name} \n")
                file.write(f"Class: {character_class} \n")
                file.write(f"Race: {race} \n")
                file.write(f"Level: {character_level} \n")
                file.write(f"Strength: {strength} \n")
                file.write(f"Dexterity: {dexterity} \n")
                file.write(f"Constitution: {constitution} \n")
                file.write(f"Intelligence: {intelligence} \n")
                file.write(f"Wisdom: {wisdom} \n")
                file.write(f"Charisma: {charisma} \n")

        except IOError:
            messagebox.showerror("Save Error", "Unable to save character to file!")
            return

        messagebox.showinfo("Success", f"Character saved to file {filename}!")

    def load_character(self):
        file = filedialog.askopenfilename(title="Select a character file",
                                          filetypes=[("text file", "*.txt")])
        if file == "":
            return

        with open(file, "r") as f:
            lines = f.readlines()
            name = ""
            character_class = ""
            race = ""
            character_level = ""
            strength = ""
            dexterity = ""
            constitution = ""
            intelligence = ""
            wisdom = ""
            charisma = ""

            for line in lines:
                if "Name: " in line:
                    name = line.replace("Name: ", "").strip()

                elif "Class: " in line:
                    character_class = line.replace("Class: ", "").strip()

                elif "Race: " in line:
                    race = line.replace("Race: ", "").strip()

                elif "Level: " in line:
                    character_level = line.replace("Level: ", "").strip()

                elif "Strength: " in line:
                    strength = line.replace("Strength: ", "").strip()

                elif "Dexterity: " in line:
                    dexterity = line.replace("Dexterity: ", "").strip()

                elif "Constitution: " in line:
                    constitution = line.replace("Constitution: ", "").strip()

                elif "Intelligence: " in line:
                    intelligence = line.replace("Intelligence: ", "").strip()

                elif "Wisdom: " in line:
                    wisdom = line.replace("Wisdom: ", "").strip()

                elif "Charisma: " in line:
                    charisma = line.replace("Charisma: ", "").strip()

            if name == "" or character_class == "" or race == "" or character_level == "" or strength == "" \
                    or dexterity == "" or constitution == "" or intelligence == "" or wisdom == "" or charisma == "":
                messagebox.showerror("Error", "Invalid character file!")
                return

            self.entry["nameEntry"].delete(0, tk.END)
            self.entry["classEntry"].delete(0, tk.END)
            self.entry["raceEntry"].delete(0, tk.END)
            self.entry["levelEntry"].delete(0, tk.END)
            self.entry["strengthEntry"].delete(0, tk.END)
            self.entry["dexterityEntry"].delete(0, tk.END)
            self.entry["constitutionEntry"].delete(0, tk.END)
            self.entry["intelligenceEntry"].delete(0, tk.END)
            self.entry["wisdomEntry"].delete(0, tk.END)
            self.entry["charismaEntry"].delete(0, tk.END)

            self.entry["nameEntry"].insert(0, name)
            self.entry["classEntry"].insert(0, character_class)
            self.entry["raceEntry"].insert(0, race)
            self.entry["levelEntry"].insert(0, character_level)
            self.entry["strengthEntry"].insert(0, strength)
            self.entry["dexterityEntry"].insert(0, dexterity)
            self.entry["constitutionEntry"].insert(0, constitution)
            self.entry["intelligenceEntry"].insert(0, intelligence)
            self.entry["wisdomEntry"].insert(0, wisdom)
            self.entry["charismaEntry"].insert(0, charisma)

            messagebox.showinfo("Success", f"Character {name} loaded from file!")


CharacterSheetApp()
root.mainloop()
