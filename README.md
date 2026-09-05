# Isplan – träningsplanering för hockeytränare

Testapp i en enda HTML-fil för utvärdering i mobilen. Ingen server, inga beroenden – all data sparas lokalt i webbläsaren (localStorage).

## Testa i mobilen

`index.html` är helt fristående – typsnitt, stilar och kod ligger i filen och den fungerar utan internet.

**Dela som fil:** skicka `index.html` via mejl, AirDrop, Messenger eller liknande. Mottagaren öppnar den i webbläsaren och kan lägga till den på hemskärmen.

**Demo över eget Wi-Fi (gratis, inget konto):**
```
python3 demo-server.py
```
Skriptet skriver ut en adress i stil med `http://192.168.1.23:8000/`. Öppna den i telefonen, som måste vara på samma nätverk som datorn. Fungerar på iPhone och Android.

**Dela som webbadress (GitHub Pages):** gratis för publika repon, kräver betald plan för privata.
1. Slå ihop branchen till `main`.
2. Gå till repots *Settings → Pages* och välj *Source: GitHub Actions*.
3. Arbetsflödet `.github/workflows/pages.yml` publicerar sidan vid varje push till `main`. Adressen blir `https://<användare>.github.io/<repo>/`.

**Andra gratisalternativ:** Cloudflare Pages, Netlify eller Vercel – ladda upp `index.html` i deras webbgränssnitt.

Exempeldata (övningar, spelare, två pass) laddas första gången så att allt går att prova direkt. Rensa eller återställ under **Statistik → Inställningar**.

## Funktioner

- **Pass** – skapa pass med datum och istid, bygg upp dem i faserna Uppvärmning → Teknik → Spelövningar → Avslutning. Tidsbudget visar planerad tid mot istid per fas, med riktvärden (15 / 40 / 35 / 10 %). "Anpassa till istid" skalar övningarna så att summan blir exakt istiden. Flytta, ta bort, ändra minuter och lägg anteckning per övning. "Skapa från mall" bygger ett pass automatiskt.
- **Övningsbank** – egna övningar med fas, standardtid, antal grupper/stationer, redskap, beskrivning och vilka räknare som ska finnas under övningen (t.ex. Skott, Mål).
- **Spelare** – trupp med position (F/B/MV), närvaro per dag, notering (skada, sjuk t.o.m. …). Gruppindelningen räknas om direkt efter antal närvarande, balanserar forwards/backar och kan blandas om. Varje övning i passet visar hur grupperna blir med dagens antal.
- **Redskap** – lista över allt som behöver tas fram, sammanställd från passets övningar.
- **Genomför** – stega igenom passet med nedräkning per övning (vibration när tiden är ute, skärmen hålls tänd om webbläsaren tillåter). Sätt betyg 1–5, räkna skott/mål etc, skriv anteckningar. Verklig tid per övning sparas.
- **Statistik** – genomförda pass, betyg och planerad/verklig tid per övning, räknarsummor, närvaro per spelare, sammanfattning per pass.
- **Export/import** – flytta datan mellan enheter som text.

## Filer

- `index.html` – hela appen.
