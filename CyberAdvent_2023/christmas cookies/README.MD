# christmas cookies
![](d65936a89a934841837210efb4fd1cc0)

Tytuł challenge'u, udostępniony kod generowania sekretu i funkcja API "/health" zdradza, że należy stworzyć fałszywe ciasteczko.

Odszyfrowując wygenerowany id sesji dla mnie, uzyskujemy `{'id': 2}`. Do wygenerowania fałszywego ciasteczka należy znać sekret aplikacji.

Kod generuje sekret z dokładnego czasu startu aplikacji. Można go poznać sprawdzając funkcje API '/health' (zwraca uptime). Nie wiadomo, jaki jest dokładny czas (z dokładnością do mikrosekund), ale można po prostu złamać brute-forcem.

Używając "flask_unsign" (https://pypi.org/project/flask-unsign/) można spróbować generować sekret (używając dołączony kod w zadaniu) dla każdej mikrosekundy czasu z API i zweryfikować używając id sesji wygenerowany dla mnie przez aplikację.

Napisałem kod wykonujący te czynności.

Kod: `cookie.py`

Flaga: `WSIZ{do_you_like_christmas_c00ki3s?}`