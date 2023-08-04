import random
import tkinter as tk
from tkinter import simpledialog, filedialog, messagebox, colorchooser
import json
from lista import doktorzy, przeciwnicy, towarzysze
import openai
openai.api_key = "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"
root = tk.Tk()
root.title("Losowanko")
root.geometry("400x400")

sound_file_path = None
image_file_path = None
font_size = 12
historia_scenariuszy = []


############################AI#################################
def sprawdz_bf_wygenerowanych_postaci():
    pytanie = f"Czy postacie doktor {label_doktor.cget('text')[8:]}, towarzysz {label_towarzysz.cget('text')[11:]} i złoczyńca {label_przeciwnik.cget('text')[11:]} pojawiają się w innych konfiguracjach postaci?"
    sprawdz_bf(pytanie)

def sprawdz_bf(postac):
    prompt = f"Czy istnieją jakieś audiodramy lub historie związane z postacią '{postac}' w bazie Big Finish Productions?"

    response = openai.Completion.create(
        engine="text-davinci-003",  # Możesz dostosować do innego dostępnego silnika
        prompt=prompt,
        max_tokens=200  # Długość generowanej odpowiedzi
    )

    odpowiedz = response.choices[0].text.strip()
    messagebox.showinfo(f"Informacje o '{postac}' w BF", odpowiedz)

def zapisz_postaci_do_pliku():
    data = {
        "doktorzy": doktorzy,
        "towarzysze": towarzysze,
        "przeciwnicy": przeciwnicy
    }

    folder_path = filedialog.askdirectory(title="Wybierz folder z plikami")
    if folder_path:
        try:
            with open(folder_path + "/postaci.json", "w") as file:
                json.dump(data, file)
            messagebox.showinfo("Sukces", "Pomyślnie zapisano konfigurację.")
        except Exception as e:
            messagebox.showerror("Błąd", f"Wystąpił błąd przy zapisywaniu pliku: {e}")

def wczytaj_postaci_z_pliku():
    folder_path = filedialog.askdirectory(title="Wybierz folder z plikami")
    if folder_path:
        try:
            with open(folder_path + "/postaci.json", "r") as file:
                data = json.load(file)
                doktorzy.clear()
                towarzysze.clear()
                przeciwnicy.clear()
                doktorzy.extend(data["doktorzy"])
                towarzysze.extend(data["towarzysze"])
                przeciwnicy.extend(data["przeciwnicy"])
            messagebox.showinfo("Sukces", "Pomyślnie wczytano konfigurację.")
        except FileNotFoundError:
            messagebox.showinfo("Błąd", "Plik nie istnieje.")
        except json.JSONDecodeError:
            messagebox.showinfo("Błąd", "Niepoprawny format pliku.")

def opis_zdarzenia(historia):
    # Tutaj możesz wprowadzić kod, który na podstawie historii generuje opis zdarzenia dla promptu
    # Na przykład, można wykorzystać kluczowe informacje z historii do stworzenia opisu zdarzenia
    opis = "jaki plan ma złoczyńca? gdzie się dzieje wydarzenie?, co zrobi doktor?"
    return opis

def zapisz_scenariusz_do_pliku(scenariusz, format):
    try:
        file_path = filedialog.asksaveasfilename(defaultextension=format,
                                                 filetypes=[(f"{format} Files", f"*.{format}")])
        if file_path:
            with open(file_path, "w") as file:
                file.write("\n".join(scenariusz))
            messagebox.showinfo("Sukces", f"Pomyślnie zapisano scenariusz do pliku: {file_path}")
    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił błąd przy zapisywaniu pliku: {e}")

def wygeneruj_i_wyswietl_scenariusz():
    historia = f"Doktor: {label_doktor.cget('text')[8:]}, Towarzysz: {label_towarzysz.cget('text')[11:]}, Przeciwnik: {label_przeciwnik.cget('text')[11:]}"
    scenariusz = generuj_scenariusz_historii(historia)
    historia_scenariuszy.append(scenariusz)  # Dodaj scenariusz do historii
    scenariusz_window = tk.Toplevel(root)
    scenariusz_window.title("Wygenerowany scenariusz")
    scenariusz_window.geometry("400x550")

    scenariusz_text = tk.Text(scenariusz_window, wrap=tk.WORD)
    scenariusz_text.pack(fill=tk.BOTH, expand=True)

    for i, linia in enumerate(scenariusz):
        opis = f"Zdarzenie {i + 1}: {opis_zdarzenia(linia)}" if i < len(scenariusz) - 1 else ""
        scenariusz_text.insert(tk.END, f"{linia}\n{opis}\n\n")

    button_sprawdz_bf_doktor = tk.Button(scenariusz_window, text="Sprawdź w BF (Doktor)", command=lambda: sprawdz_bf(label_doktor.cget("text")[8:]))
    button_sprawdz_bf_towarzysz = tk.Button(scenariusz_window, text="Sprawdź w BF (Towarzysz)", command=lambda: sprawdz_bf(label_towarzysz.cget("text")[11:]))
    button_sprawdz_bf_przeciwnik = tk.Button(scenariusz_window, text="Sprawdź w BF (Przeciwnik)", command=lambda: sprawdz_bf(label_przeciwnik.cget("text")[11:]))

    button_sprawdz_bf_doktor.pack(pady=10)
    button_sprawdz_bf_towarzysz.pack(pady=10)
    button_sprawdz_bf_przeciwnik.pack(pady=10)

def uzyskaj_informacje_z_ai(postac):
    prompt = f"Kim jest ta postać  '{postac}' z serialu Doktor Who?"

    response = openai.Completion.create(
        engine="text-davinci-003",  # Możesz dostosować do innego dostępnego silnika
        prompt=prompt,
        max_tokens=150  # Długość generowanej odpowiedzi
    )

    informacja = response.choices[0].text.strip()
    messagebox.showinfo(f"Informacje o '{postac}'", informacja)

def wygeneruj_scenariusz():
    historia = f"Doktor: {label_doktor['text'][8:]}, Towarzysz: {label_towarzysz['text'][11:]}, Przeciwnik: {label_przeciwnik['text'][11:]}"
    scenariusz = generuj_scenariusz_historii(historia)
    messagebox.showinfo("Generowany scenariusz", scenariusz)

############################AI#################################

########################Losowanko##############################

def losuj_konfiguracje():
    wylosowany_doktor = random.choice(doktorzy)
    wylosowany_towarzysz = random.choice(towarzysze)
    wylosowany_przeciwnik = random.choice(przeciwnicy)

    label_doktor.config(text="Doktor: " + wylosowany_doktor)
    label_towarzysz.config(text="Towarzysz: " + wylosowany_towarzysz)
    label_przeciwnik.config(text="Przeciwnik: " + wylosowany_przeciwnik)

    # Add the current configuration to the history
    dodaj_do_historii(wylosowany_doktor, wylosowany_towarzysz, wylosowany_przeciwnik)

def edytuj_liste(lista):
    nowy_element = simpledialog.askstring("Edytuj", "Podaj nowy element:")
    if nowy_element:
        lista.append(nowy_element)

def losuj_z_cechami(lista, cechy, wartosci_cech):
    wylosowany_postac = {}
    for cecha in cechy:
        wylosowana_wartosc = random.choice(wartosci_cech[cecha])
        wylosowany_postac[cecha] = wylosowana_wartosc
    return wylosowany_postac

########################Losowanko##############################

####################Ustawienia GUI#############################

def zmien_ikone():
    file_path = filedialog.askopenfilename(title="Wybierz plik graficzny", filetypes=[("Image Files", "*.ico;*.png;*.jpg;*")])
    if file_path:
        try:
            root.iconbitmap(file_path)
            messagebox.showinfo("Informacja", "Zmieniono ikonę aplikacji.")
        except tk.TclError:
            messagebox.showerror("Błąd", "Nie udało się załadować ikony. Upewnij się, że plik jest w formacie ICO, PNG lub JPG.")

def change_font_size(delta):
    global font_size
    font_size += delta
    if font_size > 0:
        for label in [label_doktor, label_towarzysz, label_przeciwnik]:
            label.config(font=("Arial", font_size))

def zmien_tlo():
    file_path = filedialog.askopenfilename(title="Wybierz plik graficzny", filetypes=[("Image Files", "*.jpg;*.png;*")])
    if file_path:
        try:
            img = tk.PhotoImage(file=file_path)
            canvas.img = img
            canvas.create_image(0, 0, anchor=tk.NW, image=img)
        except tk.TclError:
            messagebox.showerror("Błąd", "Nie udało się załadować obrazu. Upewnij się, że plik jest w formacie JPG lub PNG.")

def zmien_kolor_tla():
    nowy_kolor = colorchooser.askcolor(title="Wybierz kolor tła")[1]
    if nowy_kolor:
        canvas.config(bg=nowy_kolor)
        messagebox.showinfo("Informacja", "Zmieniono kolor tła aplikacji.")

####################Ustawienia GUI#############################

######################Historia################################
def zapisz_historie_scenariuszy_do_pliku():
    folder_path = filedialog.askdirectory(title="Wybierz folder z plikami")
    if folder_path:
        try:
            with open(folder_path + "/historia_scenariuszy.json", "w") as file:
                json.dump(historia_scenariuszy, file)
            messagebox.showinfo("Sukces", "Pomyślnie zapisano historię scenariuszy.")
        except Exception as e:
            messagebox.showerror("Błąd", f"Wystąpił błąd przy zapisywaniu historii scenariuszy: {e}")

def wczytaj_historie_scenariuszy_z_pliku():
    folder_path = filedialog.askdirectory(title="Wybierz folder z plikami")
    if folder_path:
        try:
            with open(folder_path + "/historia_scenariuszy.json", "r") as file:
                historia = json.load(file)
                historia_scenariuszy.clear()
                historia_scenariuszy.extend(historia)
            messagebox.showinfo("Sukces", "Pomyślnie wczytano historię scenariuszy.")
        except FileNotFoundError:
            messagebox.showinfo("Błąd", "Plik nie istnieje.")
        except json.JSONDecodeError:
            messagebox.showinfo("Błąd", "Niepoprawny format pliku.")

def wyswietl_historie_scenariuszy():
    if not historia_scenariuszy:
        messagebox.showinfo("Informacja", "Historia scenariuszy jest pusta.")
        return

    historia_window = tk.Toplevel(root)
    historia_window.title("Historia scenariuszy")
    historia_window.geometry("400x300")

    text_widget = tk.Text(historia_window, wrap=tk.WORD)
    text_widget.pack(fill=tk.BOTH, expand=True)

    for i, scenariusz in enumerate(historia_scenariuszy):
        text_widget.insert(tk.END, f"Scenariusz {i + 1}:\n")
        for linia in scenariusz:
            text_widget.insert(tk.END, f"{linia}\n")
        text_widget.insert(tk.END, "\n")

    text_widget.config(state=tk.DISABLED)  # Ustaw tryb tylko do odczytu

def generuj_scenariusz_historii(historia):
    prompt = f"Doktor Who, tajemniczy kosmita podróżujący TARDIS-em, znalazł się w sytuacji, gdzie {historia}. Co teraz się wydarzy?jaki będzie dokładny przebieg wydazeń?co wymyślił złoczyńca?\n\n"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
        #
    )
    generated_text = response.choices[0].text.strip()
    return generated_text.split("\n")

# losowanie historia
historia_losowan = []

def dodaj_do_historii(doktor, towarzysz, przeciwnik, najlepsze=False):
    historia_losowan.append({"doktor": doktor, "towarzysz": towarzysz, "przeciwnik": przeciwnik, "najlepsze": najlepsze})

def usun_z_historii():
    global historia_losowan
    selected_indices = listbox.curselection()
    if not selected_indices:
        messagebox.showinfo("Informacja", "Zaznacz losowanie, które chcesz usunąć z historii.")
    else:
        indices_to_remove = sorted(selected_indices, reverse=True)
        for index in indices_to_remove:
            try:
                historia_losowan.pop(index)
            except IndexError:
                pass
        update_listbox()

def update_listbox():
    listbox.delete(0, tk.END)

    for i, h in enumerate(historia_losowan):
        text = f"Doktor: {h['doktor']}, Towarzysz: {h['towarzysz']}, Przeciwnik: {h['przeciwnik']}"

        if h.get('najlepsze', False):
            label_text = f"[Najlepsze] {text}"
            label = tk.Label(listbox, text=label_text, font=("Arial", font_size, "bold"), fg="black", bg="red")
            listbox.insert(tk.END, "")
            listbox.window_create(tk.END, window=label)
        else:
            label = tk.Label(listbox, text=text, font=("Arial", font_size), fg="black", bg="white")
            listbox.insert(tk.END, "")
            listbox.window_create(tk.END, window=label)

def wyswietl_historie():
    if not historia_losowan:
        messagebox.showinfo("Informacja", "Historia losowań jest pusta.")
        return

    history_window = tk.Toplevel(root)
    history_window.title("Historia losowań")
    history_window.geometry("400x300")

    global listbox
    listbox = tk.Listbox(history_window, font=("Arial", font_size))
    listbox.pack(fill=tk.BOTH, expand=True)

    for i, h in enumerate(historia_losowan):
        text = f"Doktor: {h['doktor']}, Towarzysz: {h['towarzysz']}, Przeciwnik: {h['przeciwnik']}"
        if h.get('najlepsze', False):
            listbox.insert(tk.END, f"[Najlepsze] {text}")
        else:
            listbox.insert(tk.END, text)


    scrollbar = tk.Scrollbar(history_window, command=listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    listbox.config(yscrollcommand=scrollbar.set)


    button_frame = tk.Frame(history_window)
    button_frame.pack()

    selected_indices = []


    def on_select(event):
        selected_items = listbox.curselection()
        selected_indices.clear()
        for index in selected_items:
            selected_indices.append(index)
        update_listbox()


    listbox.bind('<<ListboxSelect>>', on_select)


    def update_listbox():
        listbox.delete(0, tk.END)
        for i, h in enumerate(historia_losowan):
            text = f"Doktor: {h['doktor']}, Towarzysz: {h['towarzysz']}, Przeciwnik: {h['przeciwnik']}"
            if i in selected_indices:
                text = f"[Wybrane] {text}"
            if h.get('najlepsze', False):
                text = f"[Najlepsze] {text}"
            listbox.insert(tk.END, text)


    def wyroznij_jako_najlepsze():
        if not selected_indices:
            messagebox.showinfo("Informacja", "Zaznacz losowanie, które chcesz wyrożnić jako najlepsze.")
        else:
            for index in selected_indices:
                item = historia_losowan[index]
                item['najlepsze'] = True
        update_listbox()


    def odznacz_jako_najlepsze():
        if not selected_indices:
            messagebox.showinfo("Informacja", "Zaznacz losowanie, które chcesz odznaczyć jako najlepsze.")
        else:
            for index in selected_indices:
                item = historia_losowan[index]
                item['najlepsze'] = False
        update_listbox()


    def usun_z_historii():
        if not selected_indices:
            messagebox.showinfo("Informacja", "Zaznacz losowanie, które chcesz usunąć z historii.")
        else:
            for index in selected_indices:
                historia_losowan[index]['usuniete'] = True
        update_listbox()


    listbox.config(selectmode=tk.MULTIPLE)


    scrollbar = tk.Scrollbar(history_window, command=listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    listbox.config(yscrollcommand=scrollbar.set)


    button_wyroznij = tk.Button(history_window, text="Wyroźnij jako najlepsze", command=wyroznij_jako_najlepsze)
    button_wyroznij.pack(side=tk.LEFT, padx=10, pady=5)

    button_odznacz = tk.Button(history_window, text="Odznacz jako najlepsze", command=odznacz_jako_najlepsze)
    button_odznacz.pack(side=tk.LEFT, padx=10, pady=5)

    button_usun = tk.Button(history_window, text="Usuń z historii", command=usun_z_historii)
    button_usun.pack(side=tk.LEFT, padx=10, pady=5)

def zapisz_historie_do_pliku():
    folder_path = filedialog.askdirectory(title="Wybierz folder z plikami")
    if folder_path:
        try:
            with open(folder_path + "/historia.json", "w") as file:
                json.dump(historia_losowan, file)
            messagebox.showinfo("Sukces", "Pomyślnie zapisano historię losowań.")
        except Exception as e:
            messagebox.showerror("Błąd", f"Wystąpił błąd przy zapisywaniu historii: {e}")

def wczytaj_historie_z_pliku():
    folder_path = filedialog.askdirectory(title="Wybierz folder z plikami")
    if folder_path:
        try:
            with open(folder_path + "/historia.json", "r") as file:
                historia = json.load(file)
                historia_losowan.clear()
                historia_losowan.extend(historia)
            messagebox.showinfo("Sukces", "Pomyślnie wczytano historię losowań.")
        except FileNotFoundError:
            messagebox.showinfo("Błąd", "Plik nie istnieje.")
        except json.JSONDecodeError:
            messagebox.showinfo("Błąd", "Niepoprawny format pliku.")
##################################Historia############################################


###########GUI###########
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack(fill=tk.BOTH, expand=True)
button_losuj = tk.Button(canvas, text="Losuj konfigurację", command=losuj_konfiguracje)
button_losuj.pack(pady=20)
label_doktor = tk.Label(canvas, text="Doktor: ", font=("Arial", font_size))
label_doktor.pack(pady=10)
label_towarzysz = tk.Label(canvas, text="Towarzysz: ", font=("Arial", font_size))
label_towarzysz.pack(pady=10)
label_przeciwnik = tk.Label(canvas, text="Przeciwnik: ", font=("Arial", font_size))
label_przeciwnik.pack(pady=10)

# Tworzenie przycisków do edycji listy
def open_doktorzy_editor():
    edytuj_liste(doktorzy)

def open_towarzysze_editor():
    edytuj_liste(towarzysze)

def open_przeciwnicy_editor():
    edytuj_liste(przeciwnicy)

# Tworzenie menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
opcje_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Opcje", menu=opcje_menu)
edytuj_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edytuj", menu=edytuj_menu)
dodaj_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Dodaj", menu=dodaj_menu)
wygeneruj_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Wygeneruj", menu=wygeneruj_menu)
opcje_menu.add_command(label="Zmień tło", command=zmien_tlo)
opcje_menu.add_command(label="Zmień kolor tła", command=zmien_kolor_tla)
opcje_menu.add_separator()
opcje_menu.add_command(label="Zapisz postacie do pliku", command=zapisz_postaci_do_pliku)
opcje_menu.add_command(label="Wczytaj postacie z pliku", command=wczytaj_postaci_z_pliku)
opcje_menu.add_separator()
opcje_menu.add_command(label="Zwiększ czcionkę", command=lambda: change_font_size(2))
opcje_menu.add_command(label="Zmniejsz czcionkę", command=lambda: change_font_size(-2))
opcje_menu.add_separator()
opcje_menu.add_command(label="Zapisz historię losowań", command=zapisz_historie_do_pliku)
opcje_menu.add_command(label="Wczytaj historię losowań", command=wczytaj_historie_z_pliku)
opcje_menu.add_command(label="Wyświetl historię losowań", command=wyswietl_historie)
edytuj_menu.add_command(label="Edytuj Doktorów", command=open_doktorzy_editor)
edytuj_menu.add_command(label="Edytuj Towarzyszy", command=open_towarzysze_editor)
edytuj_menu.add_command(label="Edytuj Przeciwników", command=open_przeciwnicy_editor)
dodaj_menu.add_command(label="Zmień ikonę aplikacji", command=zmien_ikone)
wygeneruj_menu.add_command(label="Uzyskaj informacje o Doktorze z AI", command=lambda: uzyskaj_informacje_z_ai(label_doktor.cget("text")))
wygeneruj_menu.add_command(label="Uzyskaj informacje o Towarzyszu z AI", command=lambda: uzyskaj_informacje_z_ai(label_towarzysz.cget("text")))
wygeneruj_menu.add_command(label="Uzyskaj informacje o Przeciwniku z AI", command=lambda: uzyskaj_informacje_z_ai(label_przeciwnik.cget("text")))
wygeneruj_menu.add_separator()
wygeneruj_menu.add_command(label="Wygeneruj scenariusz", command=wygeneruj_i_wyswietl_scenariusz)
wygeneruj_menu.add_command(label="Sprawdź BF wygenerowanych postaci", command=sprawdz_bf_wygenerowanych_postaci)
wygeneruj_menu.add_separator()
wygeneruj_menu.add_command(label="Zapisz historię scenariuszy do pliku", command=zapisz_historie_scenariuszy_do_pliku)
wygeneruj_menu.add_command(label="Wczytaj historię scenariuszy z pliku", command=wczytaj_historie_scenariuszy_z_pliku)
wygeneruj_menu.add_command(label="Wyświetl historię scenariuszy", command=wyswietl_historie_scenariuszy)
root.mainloop()



###########GUI###########