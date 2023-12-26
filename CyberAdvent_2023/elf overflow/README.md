# elf overflow
![](0255e6950014a93d2ebd1eaf031fa124)

Samo słowo "overflow" w tytule i w opisie sugeruje, że należy wykonać jakieś typu przepełnienie.

W kodzie "main.cc" można zauważyć, że zostaje utworzona zmienna o nazwie "elf" typu struktualnego "Elf". Następnie wykonuje się funkcja "gets" czytająca tekst z standardowego wejścia i zapisuje go w wartości "name" zmiennej "elf". Wartość "power" w zmiennej nie zostaje ruszona. Następnie program sprawdza, czy wartość "power" została zmieniona. Jeżeli tak wykonuje się komenda `system("/bin/sh")`.

Aby dostać się do flagi należy zmienić wartość "power". Wartość "name", która jest zapisywania, jest typu `char[64]`. Ponieważ w funkcji "gets" nie ma możliwości ustawianie maksymalnej liczby znaków, to możliwie jest wykonanie przepełnienie bufora i nadpisanie wartości "power".

Po wpisaniu `9210392103912039103912039120391203912039120390123901239102391023910239120391203912039102391023912031`, przepełnienie zostaje wykonane i zyskałem dostęp do konsoli. Trzeba jedynie wpisać `cat file.txt`.


Flaga: `WSIZ{0v3rflow1ng_3lf_w4s_4_b4d_ide4}`