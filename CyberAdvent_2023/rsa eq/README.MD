# rsa eq
![](images/ff1f9e448cbcf817eb815ba1a3a5705b)

Używając komendy podanej w zadaniu uzyskałem wartości `n`, `e`, `x` oraz `m`.
Do wyliczenia `p` i `q` potrzeba wyliczyć zależność `p` (lub `q`) od `n` i `x`.
Można wykorzystać do tego Wolfram Alpha.
![](images/097870ea14c25b58de0625f984db50ac)

Następnie należy obliczyć `p` z podanego wzoru i `q` dzieląc `n` przez uzyskane `p`.
Napisałem kod, który oblicza `p` i `q` (kod w `rsa.py`).
Do odszyfrowania wykorzystałem stronę dCode (https://www.dcode.fr/rsa-cipher).
![](images/cca565042700c88dc0209a60be6650d8)

Flaga: `WSIZ{huge_math_with_huge_Pr!m37}`