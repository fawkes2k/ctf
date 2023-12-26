# santas vault
![](cf69a1aaed554bfeb524a7df88b21041)

Czytając opis zadania, natychmiast przychodzi do głowy rozwiązanie. Należy użyć `git reflog`, aby znaleźć usunięty commit. Po rozpakowaniu dołączonego archiwum i wykonaniu komendy, wyświetla się poniższa lista:
```
703d0dd (HEAD -> master) HEAD@{0}: commit: update naughtylist.txt
3087674 HEAD@{1}: reset: moving to HEAD~1
57582f6 HEAD@{2}: commit: update naughtylist.txt
3087674 HEAD@{3}: commit: update naughtylist.txt
823a72f HEAD@{4}: commit: update naughtylist.txt
f29ef2a HEAD@{5}: commit (initial): update naughtylist.txt
```
Można zauważyć, że commit `57582f6` został usunięty i plik został przywrócony do stanu z commitu `3087674`. Po wykonaniu `git diff 57582f6 3087674` pojawia się usunięta flaga.

Flaga: `WSIZ{refl0g_sometim3s_c4n_he1p_s4nta}`