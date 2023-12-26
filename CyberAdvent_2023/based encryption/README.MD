# based encryption
![](23a7e1b55c56eb626f14e8d4e91a5986)

Jak sam tytuł i opis podpowiada, wiadomość jest zakodowana za pomocą Base64.
`R1UzVEtNWlVIRTJVQ04yQ0dZMkRHTVpXR0kzRENNWlZHWTJUS1JSVEdFM1RJTktHR00yRE1RWldJTTJVTU1aWEdZNERHTVpWSVkzVE9NWlVHNDRUT1JBPQ==`

Odkodowaniu wiadomość pojawia się kolejna zakodowana wiadomość, tym razem w Base32.
`GU3TKMZUHE2UCN2CGY2DGMZWGI3DCMZVGY2TKRRTGE3TINKGGM2DMQZWIM2UMMZXGY4DGMZVIY3TOMZUG44TORA=`

Po odkodowaniu tej wiadomości okazuje się, że kryje się następna wiadomość. Ta jest zakodowana w Base16.
`5753495A7B6433626135655F31745F346C6C5F3768335F7734797D`

Na szczęście, po odkodowaniu tej wiadomości, pojawia się wreszcie flaga.

Program odszyfrowujący: `based.py`
Flaga: `WSIZ{d3ba5e_1t_4ll_7h3_w4y}`