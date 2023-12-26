# OCR-as-a-Service
![](4474be3c8e230eafef18284814b3b429)

Sprawdzając kod odkryłem, że aplikacja nie sprawdza, czy wysłana rzecz jest URLem (jedynie po stronie klienta). Sprawdzając wykorzystaną bibliotekę "tesseract" znalazłem, że używa programu z poziomu konsoli. Stworzyłem kod, który wysyła `> /dev/null; cat flag.txt #` jako URL i wyświetla zwróconą wartość. Program zwraca flagę.

Kod: `ocr.py`

Flaga: `WSIZ{d0nt_tru5t_sm4ll_l1bs}`