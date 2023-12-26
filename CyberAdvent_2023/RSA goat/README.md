# RSA goat
![](22c078e2bda47f22f7863f5423c3d33f)

Podany kod szyfruje tekst obliczając dla każdego znaku c^e % n, gdzie "c" to numer pozycji kodu Unicode znaku, a "e" i "n" są wartościami podanymi przez użytkownika. Wynik jest wypełniany zerami, tak aby zawsze długość wynosiła 4 znaki. Uzyskaną wartość jest łączona w 1 ciąg.

Szybko można zauważyć, że ponieważ wartości "e" i "n" są podane w kodzie, możliwe jest stworzenie tabeli wartości dla każdego znaku (w tym przypadku znaków występujących w fladze). Po stworzeniu tabeli można przeiterować podany zaszyfrowany ciąg szukający każdej zaszyfrowanego znaku w tabeli. Wynikiem jest flaga.

Program odszyfrowujący: `rsa.py`
Flaga: `WSIZ{RSA_is_hard_but_you_did_it}`