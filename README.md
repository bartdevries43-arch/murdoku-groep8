# Murdoku · groep 8

Detective-logicapuzzels voor groep 8. Met de aanwijzingen los je drie
kruistabellen op (✓ / ✗) van **verdachten × plaatsen × voorwerpen** en ontdek
je wie de dader is. Print-klaar op A4.

Alle zaken, namen en aanwijzingen zijn origineel en uniek oplosbaar.

## Bestanden
- `index.html` — startpagina met printbare links
- `murdoku.html` — alle zaken + antwoordblad in één keer
- `zaak-1.html` … `zaak-3.html` — losse zaken (elk 1 A4)
- `antwoorden.html` — antwoordblad voor de leerkracht
- `generate.py` — generator (pas `ZAKEN` aan om zaken toe te voegen)

## Zelf uitbreiden
Voeg een zaak toe in `ZAKEN` (verdachten, plaatsen, voorwerpen, aanwijzingen en
de oplossing) en draai opnieuw:
```bash
python3 generate.py
```

## Printen
Open een zaak, klik op "Print deze pagina" (of Ctrl/Cmd + P). Kies A4, marges
"geen"/"standaard" en zet "achtergrondafbeeldingen" aan voor de kleuren.
