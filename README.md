# Doktorek_losowanko
biblioteki do zainstalowania:
openai, tkinter
sprawdz_bf(postac): Ta funkcja służy do komunikacji z OpenAI GPT-3, aby sprawdzić, czy istnieją audiodramy lub historie związane z daną postacią (taką jak doktor, towarzysz czy przeciwnik) w bazie Big Finish Productions. Generuje zapytanie na podstawie podanej postaci i wyświetla odpowiedź w okienku.

uzyskaj_informacje_z_ai(postac): Funkcja wykorzystuje GPT-3, aby uzyskać informacje o danej postaci z serialu "Doktor Who". Generuje pytanie na podstawie postaci i wyświetla uzyskaną informację.

generuj_scenariusz_historii(historia): Ta funkcja generuje scenariusz oparty na podanej historii, wykorzystując GPT-3. Tworzy prompt z opisem historycznym i otrzymuje odpowiedź od GPT-3 w postaci tekstu, który jest następnie dzielony na linie scenariusza.

losuj_konfiguracje(): Funkcja losuje konfigurację postaci (doktora, towarzysza i przeciwnika) z dostępnych list i wyświetla wylosowane postacie w etykietach.

edytuj_liste(lista): Ta funkcja pozwala na edycję list postaci (doktorów, towarzyszy i przeciwników). Wywołuje okienko, w którym użytkownik może podać nową wartość i dodaje ją do odpowiedniej listy.

wygeneruj_i_wyswietl_scenariusz(): Funkcja generuje scenariusz na podstawie aktualnie wylosowanych postaci i wyświetla go w nowym okienku. Pozwala również na sprawdzenie, czy istnieją związane z postaciami audiodramy w bazie Big Finish.

zapisz_postaci_do_pliku(): Funkcja pozwala na zapisanie aktualnych konfiguracji postaci (doktorów, towarzyszy i przeciwników) do pliku JSON. Użytkownik wybiera folder, do którego plik zostanie zapisany.

wczytaj_postaci_z_pliku(): Funkcja umożliwia wczytanie konfiguracji postaci z wcześniej zapisanego pliku JSON. Użytkownik wybiera folder z plikiem i dane zostają wczytane do odpowiednich list.

zmien_tlo(): Funkcja umożliwia zmianę tła aplikacji poprzez wybór pliku graficznego (JPG lub PNG) i wyświetlenie go na canvasie.

zmien_kolor_tla(): Ta funkcja pozwala na zmianę koloru tła aplikacji poprzez wybór koloru za pomocą okienka dialogowego.

change_font_size(delta): Funkcja służy do zmiany rozmiaru czcionki w etykietach. Użytkownik może zwiększać lub zmniejszać rozmiar czcionki.

zmien_ikone(): Funkcja pozwala na zmianę ikony aplikacji poprzez wybór pliku graficznego (ICO, PNG lub JPG) i ustawienie go jako ikonę okna.

wyswietl_historie(): Funkcja wyświetla historię losowań postaci w osobnym okienku. Użytkownik może zaznaczać wybrane losowania.

update_listbox(): Funkcja odświeża zawartość listboxa z historią losowań, uwzględniając zaznaczone elementy i wyróżnione najlepsze losowania.

wyroznij_jako_najlepsze(): Funkcja oznacza zaznaczone losowania jako najlepsze.

odznacz_jako_najlepsze(): Funkcja usuwa oznaczenie najlepszych losowań z tych, które były zaznaczone.

usun_z_historii(): Funkcja usuwa zaznaczone losowania z historii.

zapisz_historie_do_pliku(): Funkcja zapisuje historię losowań do pliku JSON.

wczytaj_historie_z_pliku(): Funkcja wczytuje historię losowań z wcześniej zapisanego pliku JSON.

zapisz_historie_scenariuszy_do_pliku(): Funkcja zapisuje historię scenariuszy do pliku JSON.

wczytaj_historie_scenariuszy_z_pliku(): Funkcja wczytuje historię scenariuszy z wcześniej zapisanego pliku JSON.

opis_zdarzenia(historia): Ta funkcja miałaby generować opis zdarzenia na podstawie historii. W kodzie jest umieszczony przykładowy opis.

zapisz_scenariusz_do_pliku(scenariusz, format): Funkcja zapisuje wygenerowany scenariusz do pliku w formacie podanym przez użytkownika.

wygeneruj_scenariusz(): Funkcja generuje scenariusz na podstawie aktualnie wylosowanych postaci i wyświetla go w oknie dialogowym.
