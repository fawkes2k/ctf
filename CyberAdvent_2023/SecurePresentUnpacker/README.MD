# SecurePresentUnpacker
![](e943ec959fb4463f8f695b9f42234950)

Inżynieria wsteczna dołączonego pliku DLL została przeprowadzona za pomocą programu ILSpy. Wygenerowany kod został przeanalizowany. Funkcja Main() przechowuje flagę w zaszyfrowanej formie
```
Dictionary<string, string> presents = new Dictionary<string, string>
	{
		{ "RC Car", "97F8D84D1DCA712D67C29153A9313AF17BE7C883993A090EDD0714A965E81009" },
		{ "OTP Code", "04FB0288B10A5CA5908F2465C3F5D35E" },
		{ "Flag", "FEFAF3C16ACE95C26072B9425DAA94923053E310345F6ECDEE0820DF72DADCBD9F2A0283FAFED0781DE87C0034107C8A" },
		{ "Wimdoms 95 License Key", "6F3BA281D72CB07311F90351C229289F" }
	};
```

Po wybraniu przez użytkownika elementu z listy (`string data = Console.ReadLine();`) wykonuje poniższy kod:
```
byte[] selectedPresent = passwordor.StringToPasswordifable(presents[data]);
string decoded = passwordor.DePasswordify(selectedPresent);
```

Funkcja `PasswordifiedToString` wykonuje `Convert.ToHexString` na podanej wartości. Kod funkcji `DePasswordify` jest następujący:
```
public string DePasswordify(byte[] password) {
	byte[] key = Encoding.ASCII.GetBytes("1Q6PHZreF-jd6rBZeMQZ.z#1j3bb4h/%");
	byte[] iv = Encoding.ASCII.GetBytes("JHeR)jX=/aQFXm8b");
	AesManaged aes = new AesManaged();
	try {
		ICryptoTransform encryptor = ((SymmetricAlgorithm)aes).CreateDecryptor(key, iv);
		using MemoryStream ms = new MemoryStream(password);
		CryptoStream cs = new CryptoStream((Stream)ms, encryptor, (CryptoStreamMode)0);
		try {
			using StreamReader sw = new StreamReader((Stream)(object)cs);
			return sw.ReadToEnd();
		} finally { ((IDisposable)cs)?.Dispose(); }
	} finally { ((IDisposable)aes)?.Dispose(); }
```

Ten kod odszyfruje podaną wartość kluczem AES `1Q6PHZreF-jd6rBZeMQZ.z#1j3bb4h/%` oraz IV `JHeR)jX=/aQFXm8b`.
Po dokonaniu odszyfrowaniu wartości z `presents["Flag"]` uzyskujemy flagę.

Program odszyfrowujący: `aes.py`

Flaga: `WSIZ{5ymme7ric_pr35ent_g1v3r}`