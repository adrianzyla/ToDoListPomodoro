# Lista Zadań & Timer Pomodoro

Aplikacja składa się z dwóch części:

## Lista Zadań
W module Lista Zadań użytkownik może:
- Dodawać nowe zadania do listy (wpisuje zadania w okienku tekstowym i dodaje je za pomocą przycisku lub klawisza Enter). Jeśli użytkownik nie wpisze żadnych zadań, program wyświetli stosowną wiadomość.
- Zaznaczać i usuwać wybrane zadania z listy.
- Zapisywać zadania do pliku `tasks.dat`. Jeśli użytkownik próbuje zapisać pustą listę zadań, program wyświetli odpowiednią informację.
- Po kliknięciu przycisku X (zamykanie okna) program wyświetli pytanie, czy użytkownik chce zapisać wprowadzone zmiany przed wyjściem. Jeśli użytkownik próbuje zapisać pustą listę zadań, program poinformuje go o tym.

## Timer Pomodoro
Timer Pomodoro to czasomierz, który odmierza bloki czasowe: 25 minut pracy, po których następuje 5-minutowa przerwa. Po 4 takich blokach czasowych następuje 15-minutowa przerwa, i tak dalej. Po każdym zakończonym odliczaniu 25 minut program odtwarza krótki dźwięk, informujący o rozpoczęciu przerwy.
Użytkownik ma możliwość zresetowania timera lub pominiecia bieżącego odliczania.

**UWAGA:**
Przed uruchomieniem aplikacji zaleca się pobranie pliku `tasks.dat`, który zawiera przykładowe zadania do wyświetlenia, jednak nie jest to konieczne.
