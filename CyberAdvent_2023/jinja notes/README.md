# jinja notes
![](692f7bf6438b35cb80e44ea9c1ebd26e)

W Jinja2 można użyć filtry, które wykonują kod Pythona i są przydatne w tworzeniu HTMLa. To w filtrach dającą możliwość wykonania złosliwego kodu należy szukać źródła ataku. Oczywiście normalne filtry dają mało możliwości do ataku.

Należy więc użyć filtra "dict" i bardzo sprytnej sztuczki: `{{dict.__base__.__subclasses__()}}`.
Po wykonaniu pojawia się duża lista z wieloma klasami. Uwagę zwraca `<class 'subprocess.Popen'>,`, które pozwola na wykonanie zdalnie komend w konsoli serwera.

Pierwszą komendą do wykonania musi być "ls" sprawdzająca bieżący folder. Normalnie Popen wyświetla wiadomości w konsoli, więc należy jeszcze ustawić wartość stdout na -1 (odpowiada subprocess.PIPE) i dodać funkcję "communicate()".

Ostatecznie kod do wykonania wygląda tak: 
```{% for x in dict.__base__.__subclasses__() %} {{x("ls", shell=True, stdout=-1).communicate()[0].decode() if "Popen" in x.__name__}} {%endfor%} ```

Ten kod zwrócił `Dockerfile app.py flag.txt requirements.txt templates`.
Oczywiste jest, że teraz należy wykonać komendę "cat flag.txt", co zwraca flagę.

Źródło: https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection/jinja2-ssti
Flaga: `WSIZ{plz_d0nt_r3nder_y0ur_input}`