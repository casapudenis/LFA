import tkinter as tk
from tkinter import ttk

class CoffeeShopApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Coffee Shop App")
        self.geometry("400x300")

        self.current_state_index = 0
        self.states = [
            self.selectare_bautura,
            self.selectare_marime,
            self.adaugare_arome,
            self.selectare_mod_preparare,
            self.selectare_adaosuri,
            self.plasare_comanda
        ]

        self.user_data = {}

        self.create_widgets()
        self.set_initial_state()

    def create_widgets(self):
        self.label_text = tk.StringVar()
        self.label_text.set("Bine ati venit la Coffee Shop!")
        self.label = ttk.Label(self, textvariable=self.label_text, font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.option_frame = ttk.Frame(self)
        self.option_frame.pack(fill=tk.BOTH, expand=True)

        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(pady=10)

        self.next_button = ttk.Button(self.button_frame, text="Urmatorul", command=self.next_state)
        self.next_button.pack(side=tk.RIGHT, padx=5)

        self.previous_button = ttk.Button(self.button_frame, text="Anterior", command=self.previous_state)
        self.previous_button.pack(side=tk.RIGHT, padx=5)
        self.previous_button.pack_forget()

        self.quit_button = ttk.Button(self.button_frame, text="Iesire", command=self.destroy)
        self.quit_button.pack(side=tk.LEFT, padx=5)

    def set_initial_state(self):
        self.current_state, has_buttons = self.states[self.current_state_index]()
        self.current_state.pack(in_=self.option_frame, fill=tk.BOTH, expand=True)
        if has_buttons:
            self.button_frame.pack()
        else:
            self.button_frame.pack_forget()
        self.update_state_label()

    def update_state_label(self):
        if self.current_state_index == 0:
            self.previous_button.pack_forget()
            self.label_text.set("Bine ati venit la Coffee Shop!")
        elif self.current_state_index == len(self.states) - 1:
            self.previous_button.pack(side=tk.RIGHT, padx=5)
            self.label_text.set("Multumim pentru comanda!")
        else:
            self.previous_button.pack(side=tk.RIGHT, padx=5)
            self.label_text.set("Continuati comanda")

    def next_state(self):
        if all(self.option_selected(option) for option in self.user_data if not option.endswith("_optional")):
            self.current_state_index += 1
            if self.current_state_index < len(self.states):
                self.current_state.pack_forget()
                self.current_state, has_buttons = self.states[self.current_state_index]()
                self.current_state.pack(in_=self.option_frame, fill=tk.BOTH, expand=True)
                if has_buttons:
                    self.button_frame.pack()
                else:
                    self.button_frame.pack_forget()
                self.update_state_label()

    def previous_state(self):
        self.current_state_index -= 1
        if self.current_state_index < 0:
            self.current_state_index = 0
        self.current_state.pack_forget()
        self.current_state, has_buttons = self.states[self.current_state_index]()
        self.current_state.pack(in_=self.option_frame, fill=tk.BOTH, expand=True)
        if has_buttons:
            self.button_frame.pack()
        else:
            self.button_frame.pack_forget()
        self.update_state_label()

    def option_selected(self, option):
        if isinstance(self.user_data[option], dict):
            return any(value.get() == 1 for value in self.user_data[option].values())
        elif isinstance(self.user_data[option], list):
            return any(var.get() == 1 for _, var in self.user_data[option])
        else:
            return bool(self.user_data[option].get())

    def selectare_bautura(self):
        state_frame = ttk.Frame(self)
        label = ttk.Label(state_frame, text="Selectati bautura:")
        label.pack()

        self.user_data["bautura"] = tk.StringVar()
        options = ["Cafea", "Ceai", "Ciocolata calda"]
        for option in options:
            rb = ttk.Radiobutton(state_frame, text=option, variable=self.user_data["bautura"], value=option)
            rb.pack(anchor=tk.W)
        return state_frame, True

    def selectare_marime(self):
        state_frame = ttk.Frame(self)
        label = ttk.Label(state_frame, text="Selectati marimea bauturii:")
        label.pack()

        self.user_data["marime"] = tk.StringVar()
        options = ["Mica", "Medie", "Mare"]
        for option in options:
            rb = ttk.Radiobutton(state_frame, text=option, variable=self.user_data["marime"], value=option)
            rb.pack(anchor=tk.W)
        return state_frame, True

    def adaugare_arome(self):
        state_frame = ttk.Frame(self)
        label = ttk.Label(state_frame, text="Adaugati arome (optional):")
        label.pack()

        self.user_data["arome"] = {}
        options = ["Vanilie", "Caramel", "Ciocolata"]
        for option in options:
            self.user_data["arome"][option] = tk.IntVar(value=0)
            cb = ttk.Checkbutton(state_frame, text=option, variable=self.user_data["arome"][option])
            cb.pack(anchor=tk.W)
        return state_frame, True

    def selectare_mod_preparare(self):
        state_frame = ttk.Frame(self)
        label = ttk.Label(state_frame, text="Selectati modul de preparare:")
        label.pack()

        self.user_data["mod_preparare"] = tk.StringVar()
        options = ["Espresso", "Filtru", "Capsula"]
        for option in options:
            rb = ttk.Radiobutton(state_frame, text=option, variable=self.user_data["mod_preparare"], value=option)
            rb.pack(anchor=tk.W)
        return state_frame, True

    def selectare_adaosuri(self):
        state_frame = ttk.Frame(self)
        label = ttk.Label(state_frame, text="Selectati adaosurile (optional):")
        label.pack()

        self.user_data["adaosuri"] = []
        options = ["Lapte", "Zahar", "Sirop de vanilie"]
        for option in options:
            var = tk.IntVar(value=0)
            cb = ttk.Checkbutton(state_frame, text=option, variable=var)
            cb.pack(anchor=tk.W)
            self.user_data["adaosuri"].append((option, var))
        return state_frame, True

    def plasare_comanda(self):
        state_frame = ttk.Frame(self)
        label = ttk.Label(state_frame, text="Comanda dvs. a fost plasata cu succes!")
        label.pack()

        summary_label = ttk.Label(state_frame, text="Rezumat comanda:")
        summary_label.pack()

        for key, value in self.user_data.items():
            if key == "arome":
                selected_aromes = [arome for arome, var in value.items() if var.get() == 1]
                if selected_aromes:
                    data_label = ttk.Label(state_frame, text=f"Arome: {', '.join(selected_aromes)}")
                    data_label.pack()
            elif key == "adaosuri":
                selected_adaosuri = [adaos for adaos, var in value if var.get() == 1]
                if selected_adaosuri:
                    data_label = ttk.Label(state_frame, text=f"Adaosuri: {', '.join(selected_adaosuri)}")
                    data_label.pack()
            else:
                data_label = ttk.Label(state_frame, text=f"{key.replace('_', ' ').title()}: {value.get()}")
                data_label.pack()

        return state_frame, False


if __name__ == "__main__":
    app = CoffeeShopApp()
    app.mainloop()
