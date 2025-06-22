# PanelTPP-HTMX-Alpine-Flask

Prototyp systemu zarządzania placówką medyczną oparty o Flask, HTMX, Alpine.js i Tailwind CSS.

## Plan rozwoju

1. **Autoryzacja i sesje** – prosta obsługa logowania użytkowników (na start użytkownik `admin` z hasłem `password`).
2. **Kalendarz wizyt** – widok tabelaryczny z listą umówionych wizyt oraz przyciskiem do odświeżania danych przy użyciu HTMX.
3. **Zarządzanie klientami i personelem** – kolejne moduły będą dodawane stopniowo. Na początek dane przechowywane są w pamięci aplikacji.
4. **Rozbudowa panelu** – w przyszłości planowane są statystyki, moduł księgowy i portal klienta.

Aby uruchomić aplikację:

```bash
pip install -r requirements.txt
python app.py
```

Następnie przejdź do [http://localhost:5000](http://localhost:5000) i zaloguj się.
