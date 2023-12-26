# wtf
![](c4624c3634d6eb1ccf9886b511f127f4)

Po otwarciu pliku "output.txt" i krótkiej analizie, odkryłem że jest to wiadomość zakodowana w Base64.
Po odkodowaniu pojawia się bardzo długi ciąg znaków składający się z nawiasów kwadratowych i okrągłych, wykrzykników i plusów.

Zaczyna się od `(()=>{})`, co przypomina krótszy sposób na tworzenie funkcji w JavaScript.
Po wykonaniu tego ciągu w konsoli przeglądarki, pojawia się wiadomość "wtf" i wielokrotnie flaga.

Strona HTML ze skryptem wykonująca kod: `index.html`
Flaga: `WSIZ{j4v4scr!pt_!s_s3nt_str@ight_fr0m_th3_g0D}`