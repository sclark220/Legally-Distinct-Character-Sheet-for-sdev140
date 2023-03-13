from math import trunc
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import ImageTk, Image

# Set up the window
root = tk.Tk()
root.title("Legally Distinct Character Sheet")
root.configure(background='dark gray')
root.geometry("750x500")
# Image from OpenGameArt.org created by Flowly
icon = ImageTk.PhotoImage(Image.open("bag.png"))


class CharacterSheetApp:

    def __init__(self):
        # Pycharm made this into nice dictionaries for me, I had them all written out at first
        # These are my frames, like windows within windows to keep things organized
        self.frames = {"statBar": tk.Frame(root, bg='dark gray'),
                       "controls": tk.Frame(root, bg='dark gray'),
                       "topBar": tk.Frame(root, bg='dark gray', pady=25),
                       "topBar2": tk.Frame(root, bg='dark gray', pady=25),
                       "sideBar": tk.Frame(root, bg='dark gray'),
                       "bottomRight": tk.Frame(root, bg='dark gray', pady=25),
                       "center": tk.Frame(root, bg='dark gray')}

        self.frames["statBar"].place(relx=0, rely=0.5, anchor='w')
        self.frames["controls"].place(relx=0.5, rely=1, anchor='s')
        self.frames["topBar"].place(relx=0.5, rely=0, anchor='n')
        self.frames["topBar2"].place(relx=0.225, rely=0.1, anchor='ne')
        self.frames["sideBar"].place(relx=1, rely=0.5, anchor='e')
        self.frames["bottomRight"].place(relx=1, rely=0.85, anchor='se')
        self.frames["center"].place(relx=0.5, rely=0.5, anchor="center")

        # Same thing here for the labels I love dictionaries now, and you can see the labels are sorted to frames
        self.labels = {"name": tk.Label(self.frames["topBar"], text="Name:", bg='dark gray'),
                       "class": tk.Label(self.frames["topBar"], text="Class:", bg='dark gray'),
                       "race": tk.Label(self.frames["topBar"], text="Race:", bg='dark gray'),
                       "characterLevel": tk.Label(self.frames["topBar"], text="Level:", bg='dark gray'),
                       "hitPoints": tk.Label(self.frames["topBar2"], text="HP:", bg='dark gray'),
                       "armorClass": tk.Label(self.frames["topBar2"], text="AC:", bg='dark gray'),
                       "modifier": tk.Label(self.frames["statBar"], text="Modifier", bg='dark gray'),
                       "statLevel": tk.Label(self.frames["statBar"], text="Level", bg='dark gray'),
                       "strength": tk.Label(self.frames["statBar"], text="Strength:", bg='dark gray'),
                       "dexterity": tk.Label(self.frames["statBar"], text="Dexterity:", bg='dark gray'),
                       "constitution": tk.Label(self.frames["statBar"], text="Constitution:", bg='dark gray'),
                       "intelligence": tk.Label(self.frames["statBar"], text="Intelligence:", bg='dark gray'),
                       "wisdom": tk.Label(self.frames["statBar"], text="Wisdom:", bg='dark gray'),
                       "charisma": tk.Label(self.frames["statBar"], text="Charisma:", bg='dark gray'),
                       "money": tk.Label(self.frames["bottomRight"], text="Money", bg='dark gray'),
                       "platinum": tk.Label(self.frames["bottomRight"], text="Platinum:", bg='dark gray'),
                       "gold": tk.Label(self.frames["bottomRight"], text="Gold:", bg='dark gray'),
                       "electrum": tk.Label(self.frames["bottomRight"], text="Electrum:", bg='dark gray'),
                       "silver": tk.Label(self.frames["bottomRight"], text="Silver:", bg='dark gray'),
                       "copper": tk.Label(self.frames["bottomRight"], text="Copper:", bg='dark gray'),
                       "image": tk.Label(self.frames["center"], image=icon, bg='dark gray')}

        self.labels["name"].grid(row=0, column=0)
        self.labels["class"].grid(row=0, column=2)
        self.labels["race"].grid(row=0, column=4)
        self.labels["characterLevel"].grid(row=0, column=6)
        self.labels["hitPoints"].grid(row=0, column=0, padx=(25, 0))
        self.labels["armorClass"].grid(row=0, column=2)
        self.labels["modifier"].grid(row=0, column=2)
        self.labels["statLevel"].grid(row=0, column=1)
        self.labels["strength"].grid(row=1, column=0)
        self.labels["dexterity"].grid(row=2, column=0)
        self.labels["constitution"].grid(row=3, column=0)
        self.labels["intelligence"].grid(row=4, column=0)
        self.labels["wisdom"].grid(row=5, column=0)
        self.labels["charisma"].grid(row=6, column=0)
        self.labels["money"].grid(row=0, column=4, columnspan=2, pady=5)
        self.labels["platinum"].grid(row=1, column=0)
        self.labels["gold"].grid(row=1, column=2)
        self.labels["electrum"].grid(row=1, column=4)
        self.labels["silver"].grid(row=1, column=6)
        self.labels["copper"].grid(row=1, column=8)
        self.labels["image"].grid(row=0, column=0)

        # Same for the entries used to enter stats, it is getting clustered but better than before
        self.entry = {"nameEntry": tk.Entry(self.frames["topBar"], width=20),
                      "classEntry": tk.Entry(self.frames["topBar"], width=20),
                      "raceEntry": tk.Entry(self.frames["topBar"], width=20),
                      "levelEntry": tk.Entry(self.frames["topBar"], width=20),
                      "hitPointEntry": tk.Entry(self.frames["topBar2"], width=5),
                      "armorClassEntry": tk.Entry(self.frames["topBar2"], width=5),
                      "strengthEntry": tk.Entry(self.frames["statBar"], width=3),
                      "dexterityEntry": tk.Entry(self.frames["statBar"], width=3),
                      "constitutionEntry": tk.Entry(self.frames["statBar"], width=3),
                      "intelligenceEntry": tk.Entry(self.frames["statBar"], width=3),
                      "wisdomEntry": tk.Entry(self.frames["statBar"], width=3),
                      "charismaEntry": tk.Entry(self.frames["statBar"], width=3),
                      "platinumEntry": tk.Entry(self.frames["bottomRight"], width=4),
                      "goldEntry": tk.Entry(self.frames["bottomRight"], width=4),
                      "electrumEntry": tk.Entry(self.frames["bottomRight"], width=4),
                      "silverEntry": tk.Entry(self.frames["bottomRight"], width=4),
                      "copperEntry": tk.Entry(self.frames["bottomRight"], width=4)}

        self.entry["nameEntry"].grid(row=0, column=1, padx=(0, 25))
        self.entry["classEntry"].grid(row=0, column=3, padx=(0, 25))
        self.entry["raceEntry"].grid(row=0, column=5, padx=(0, 25))
        self.entry["levelEntry"].grid(row=0, column=7)
        self.entry["hitPointEntry"].grid(row=0, column=1, padx=(0, 10))
        self.entry["armorClassEntry"].grid(row=0, column=3, padx=(0, 25))
        self.entry["strengthEntry"].grid(row=1, column=1)
        self.entry["dexterityEntry"].grid(row=2, column=1)
        self.entry["constitutionEntry"].grid(row=3, column=1)
        self.entry["intelligenceEntry"].grid(row=4, column=1)
        self.entry["wisdomEntry"].grid(row=5, column=1)
        self.entry["charismaEntry"].grid(row=6, column=1)
        self.entry["platinumEntry"].grid(row=1, column=1, padx=(0, 10))
        self.entry["goldEntry"].grid(row=1, column=3, padx=(0, 10))
        self.entry["electrumEntry"].grid(row=1, column=5, padx=(0, 10))
        self.entry["silverEntry"].grid(row=1, column=7, padx=(0, 10))
        self.entry["copperEntry"].grid(row=1, column=9, padx=(0, 10))

        # Buttons!
        self.buttons = {"save_button": tk.Button(self.frames["controls"], text="Save", command=self.save_character),
                        "load_button": tk.Button(self.frames["controls"], text="Load", command=self.load_character),
                        "exit_button": tk.Button(self.frames["controls"], text="Exit", padx=5, command=root.destroy),
                        "modifier_button": tk.Button(self.frames["sideBar"], text="Calculate\nModifiers",
                                                     command=self.modifier)}

        self.buttons["save_button"].grid(row=7, column=0, padx=20, pady=20)
        self.buttons["load_button"].grid(row=7, column=1, padx=20, pady=20)
        self.buttons["exit_button"].grid(row=7, column=2, padx=20, pady=20)
        self.buttons["modifier_button"].grid(padx=10, pady=20)

        self.mod_labels = {"strength_modifier": tk.Label(self.frames["statBar"], bg='dark gray'),
                           "dexterity_modifier": tk.Label(self.frames["statBar"], bg='dark gray'),
                           "constitution_modifier": tk.Label(self.frames["statBar"], bg='dark gray'),
                           "intelligence_modifier": tk.Label(self.frames["statBar"], bg='dark gray'),
                           "wisdom_modifier": tk.Label(self.frames["statBar"], bg='dark gray'),
                           "charisma_modifier": tk.Label(self.frames["statBar"], bg='dark gray')}

        tk.mainloop()

    # calculates modifiers based on stats, grabs them from the entry boxes
    def modifier(self):
        strength = self.entry["strengthEntry"].get()
        dexterity = self.entry["dexterityEntry"].get()
        constitution = self.entry["constitutionEntry"].get()
        intelligence = self.entry["intelligenceEntry"].get()
        wisdom = self.entry["wisdomEntry"].get()
        charisma = self.entry["charismaEntry"].get()

        # I have a lot of error stuff just to try it out, There could be a better way
        try:
            self.mod_labels = {"strength_modifier": tk.Label(self.frames["statBar"], width=2, bg='light gray',
                                                             text=trunc((int(strength) - 10) / 2)),
                               "dexterity_modifier": tk.Label(self.frames["statBar"], width=2, bg='light gray',
                                                              text=trunc((int(dexterity) - 10) / 2)),
                               "constitution_modifier": tk.Label(self.frames["statBar"], width=2, bg='light gray',
                                                                 text=trunc((int(constitution) - 10) / 2)),
                               "intelligence_modifier": tk.Label(self.frames["statBar"], width=2, bg='light gray',
                                                                 text=trunc((int(intelligence) - 10) / 2)),
                               "wisdom_modifier": tk.Label(self.frames["statBar"], width=2, bg='light gray',
                                                           text=trunc((int(wisdom) - 10) / 2)),
                               "charisma_modifier": tk.Label(self.frames["statBar"], width=2, bg='light gray',
                                                             text=trunc((int(charisma) - 10) / 2))}

            self.mod_labels["strength_modifier"].grid(row=1, column=2)
            self.mod_labels["dexterity_modifier"].grid(row=2, column=2)
            self.mod_labels["constitution_modifier"].grid(row=3, column=2)
            self.mod_labels["intelligence_modifier"].grid(row=4, column=2)
            self.mod_labels["wisdom_modifier"].grid(row=5, column=2)
            self.mod_labels["charisma_modifier"].grid(row=6, column=2)

        except ValueError:
            messagebox.showerror("Modifier Error", 'All "level" fields are required and they must be integers!')
            return

    # grabs values from the entry boxes, checks they are ints and writes to file
    def save_character(self):
        name = self.entry["nameEntry"].get()
        character_class = self.entry["classEntry"].get()
        race = self.entry["raceEntry"].get()
        character_level = self.entry["levelEntry"].get()
        hit_points = self.entry["hitPointEntry"].get()
        armor_class = self.entry["armorClassEntry"].get()
        strength = self.entry["strengthEntry"].get()
        dexterity = self.entry["dexterityEntry"].get()
        constitution = self.entry["constitutionEntry"].get()
        intelligence = self.entry["intelligenceEntry"].get()
        wisdom = self.entry["wisdomEntry"].get()
        charisma = self.entry["charismaEntry"].get()
        platinum = self.entry["platinumEntry"].get()
        gold = self.entry["goldEntry"].get()
        electrum = self.entry["electrumEntry"].get()
        silver = self.entry["silverEntry"].get()
        copper = self.entry["copperEntry"].get()

        # makes sure all inputs are filled, this would mess up the order things are checked when loading a file.
        if name == "" or character_class == "" or race == "" or character_level == "" or hit_points == "" \
                or armor_class == "" or strength == "" or dexterity == "" or constitution == "" or intelligence == "" \
                or wisdom == "" or charisma == "" or platinum == "" or gold == "" or electrum == "" or silver == "" \
                or copper == "":
            messagebox.showerror("Save Error", "All fields are required!")
            return

        try:
            character_level = int(character_level)
            hit_points = int(hit_points)
            armor_class = int(armor_class)
            strength = int(strength)
            dexterity = int(dexterity)
            constitution = int(constitution)
            intelligence = int(intelligence)
            wisdom = int(wisdom)
            charisma = int(charisma)
            platinum = int(platinum)
            gold = int(gold)
            electrum = int(electrum)
            silver = int(silver)
            copper = int(copper)

        except ValueError:
            messagebox.showerror("Save Error", 'Invalid input! All input fields must be integers!')
            return
        # lets you pick a custom name for your custom file!
        # also you can open the text file and see exactly what is what. It took so long!

        try:
            filename = tk.simpledialog.askstring("File Name", "Enter the name of the file.")
            if filename is None:
                return
            else:
                filename = filename + ".txt"

            with open(filename, "w") as file:
                file.write(f"Name: {name} \n")
                file.write(f"Class: {character_class} \n")
                file.write(f"Race: {race} \n")
                file.write(f"Level: {character_level} \n")
                file.write(f"HitPoints: {hit_points} \n")
                file.write(f"AC: {armor_class} \n")
                file.write(f"Strength: {strength} \n")
                file.write(f"Dexterity: {dexterity} \n")
                file.write(f"Constitution: {constitution} \n")
                file.write(f"Intelligence: {intelligence} \n")
                file.write(f"Wisdom: {wisdom} \n")
                file.write(f"Charisma: {charisma} \n")
                file.write(f"Platinum: {platinum} \n")
                file.write(f"Gold: {gold} \n")
                file.write(f"Electrum: {electrum} \n")
                file.write(f"Silver: {silver} \n")
                file.write(f"Copper: {copper} \n")

        except IOError:
            messagebox.showerror("Save Error", "Unable to save character to file!")
            return

        messagebox.showinfo("Success", f"Character saved to file {filename}!")

    #   Ask to open a .txt file
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
            hit_points = ""
            armor_class = ""
            strength = ""
            dexterity = ""
            constitution = ""
            intelligence = ""
            wisdom = ""
            charisma = ""
            platinum = ""
            gold = ""
            electrum = ""
            silver = ""
            copper = ""

            # reads through each line and inserts it to the entry boxes. This took way too long just to make the text
            # file have the labels in front of the values, but now I understand .replace and .strip better
            for line in lines:
                if "Name: " in line:
                    name = line.replace("Name: ", "").strip()

                elif "Class: " in line:
                    character_class = line.replace("Class: ", "").strip()

                elif "Race: " in line:
                    race = line.replace("Race: ", "").strip()

                elif "Level: " in line:
                    character_level = line.replace("Level: ", "").strip()

                elif "HitPoints: " in line:
                    hit_points = line.replace("HitPoints: ", "").strip()

                elif "AC: " in line:
                    armor_class = line.replace("AC: ", "").strip()

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

                elif "Platinum: " in line:
                    platinum = line.replace("Platinum: ", "").strip()

                elif "Gold: " in line:
                    gold = line.replace("Gold: ", "").strip()

                elif "Electrum: " in line:
                    electrum = line.replace("Electrum: ", "").strip()

                elif "Silver: " in line:
                    silver = line.replace("Silver: ", "").strip()

                elif "Copper: " in line:
                    copper = line.replace("Copper: ", "").strip()

            # checks to make sure the file is in the right format, with no room for error, or it will not load
            if name == "" or character_class == "" or race == "" or character_level == "" or hit_points == "" \
                    or armor_class == "" or strength == "" or dexterity == "" or constitution == "" \
                    or intelligence == "" or wisdom == "" or charisma == "" or platinum == "" or gold == "" \
                    or electrum == "" or silver == "" or copper == "":

                messagebox.showerror("Error", "Invalid character file!")
                return
            # deletes what was in the entry fields before
            self.entry["nameEntry"].delete(0, tk.END)
            self.entry["classEntry"].delete(0, tk.END)
            self.entry["raceEntry"].delete(0, tk.END)
            self.entry["levelEntry"].delete(0, tk.END)
            self.entry["hitPointEntry"].delete(0, tk.END)
            self.entry["armorClassEntry"].delete(0, tk.END)
            self.entry["strengthEntry"].delete(0, tk.END)
            self.entry["dexterityEntry"].delete(0, tk.END)
            self.entry["constitutionEntry"].delete(0, tk.END)
            self.entry["intelligenceEntry"].delete(0, tk.END)
            self.entry["wisdomEntry"].delete(0, tk.END)
            self.entry["charismaEntry"].delete(0, tk.END)
            self.entry["platinumEntry"].delete(0, tk.END)
            self.entry["goldEntry"].delete(0, tk.END)
            self.entry["electrumEntry"].delete(0, tk.END)
            self.entry["silverEntry"].delete(0, tk.END)
            self.entry["copperEntry"].delete(0, tk.END)

            # inserts new values into entry fields
            self.entry["nameEntry"].insert(0, name)
            self.entry["classEntry"].insert(0, character_class)
            self.entry["raceEntry"].insert(0, race)
            self.entry["levelEntry"].insert(0, character_level)
            self.entry["hitPointEntry"].insert(0, hit_points)
            self.entry["armorClassEntry"].insert(0, armor_class)
            self.entry["strengthEntry"].insert(0, strength)
            self.entry["dexterityEntry"].insert(0, dexterity)
            self.entry["constitutionEntry"].insert(0, constitution)
            self.entry["intelligenceEntry"].insert(0, intelligence)
            self.entry["wisdomEntry"].insert(0, wisdom)
            self.entry["charismaEntry"].insert(0, charisma)
            self.entry["platinumEntry"].insert(0, platinum)
            self.entry["goldEntry"].insert(0, gold)
            self.entry["electrumEntry"].insert(0, electrum)
            self.entry["silverEntry"].insert(0, silver)
            self.entry["copperEntry"].insert(0, copper)

            messagebox.showinfo("Success", f"Character {name} loaded from file!")


# run it
CharacterSheetApp()
root.mainloop()
