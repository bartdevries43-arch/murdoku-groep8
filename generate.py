#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Murdoku (detective-logicapuzzel) voor groep 8 - print-klare zaken.
Eigen, originele zaken: verdachten x plaatsen x voorwerpen. Met aanwijzingen los
je drie kruistabellen op (✓/✗) en vind je de dader. Uniek oplosbaar.

Draai:  python3 generate.py
Levert: index.html (printbare links), murdoku.html (alle zaken), zaak-1..N.html,
        antwoorden.html
"""
import html


def V(naam, emoji):
    return {"naam": naam, "emoji": emoji}


ZAKEN = [
    {
        "titel": "Zaak 1: De verdwenen schoolbeker",
        "verhaal": ("De gouden schoolbeker is verdwenen uit de prijzenkast van de "
                    "sporthal! Drie leerlingen waren die middag op school. Ieder was "
                    "op een andere plek en had één opvallend voorwerp bij zich. "
                    "Slechts één van hen is de dief."),
        "verdachten": [V("James", "👦🏿"), V("Fatima", "👧🏽"), V("Sanne", "👧🏻")],
        "plaatsen": [V("Sporthal", "🏐"), V("Bibliotheek", "📚"), V("Bakkerij", "🥐")],
        "voorwerpen": [V("Zonnebril", "🕶️"), V("Paraplu", "☂️"), V("Pet", "🧢")],
        "aanwijzingen": [
            "Sanne was niet in de sporthal en ook niet in de bibliotheek.",
            "Fatima had geen pet en geen zonnebril bij zich.",
            "De persoon in de bakkerij droeg een pet.",
            "James was niet in de bibliotheek.",
            "De persoon met de zonnebril was in de sporthal.",
            "De beker verdween uit de sporthal.",
        ],
        "oplossing": {"James": ("Sporthal", "Zonnebril"),
                      "Fatima": ("Bibliotheek", "Paraplu"),
                      "Sanne": ("Bakkerij", "Pet")},
        "dader": "James",
    },
    {
        "titel": "Zaak 2: De gestolen telefoon",
        "verhaal": ("Tijdens de pauze is een telefoon uit de kantine verdwenen. "
                    "Drie leerlingen worden ondervraagd. Ieder was op een andere plek "
                    "en had één ding bij zich. Wie heeft het gedaan?"),
        "verdachten": [V("Mohammed", "👦🏾"), V("Lisa", "👧🏻"), V("Chen", "👦🏻")],
        "plaatsen": [V("Kantine", "🍽️"), V("Gymzaal", "🤸"), V("Schoolplein", "🏫")],
        "voorwerpen": [V("Rugzak", "🎒"), V("Koptelefoon", "🎧"), V("Skateboard", "🛹")],
        "aanwijzingen": [
            "Chen was buiten, op het schoolplein.",
            "Lisa was niet in de gymzaal.",
            "De persoon met het skateboard was in de gymzaal.",
            "Chen had geen rugzak bij zich.",
            "Lisa droeg geen koptelefoon.",
            "De telefoon verdween uit de kantine.",
        ],
        "oplossing": {"Mohammed": ("Gymzaal", "Skateboard"),
                      "Lisa": ("Kantine", "Rugzak"),
                      "Chen": ("Schoolplein", "Koptelefoon")},
        "dader": "Lisa",
    },
    {
        "titel": "Zaak 3: De gekraakte kluis",
        "verhaal": ("De kluis in de directiekamer is gekraakt en de laptop is weg. "
                    "Er zijn drie verdachten. Ieder was op een andere plek en had één "
                    "verdacht voorwerp bij zich. Volg de aanwijzingen en ontmasker de dader."),
        "verdachten": [V("Amara", "👩🏿"), V("Daan", "👦🏼"), V("Yusuf", "👦🏽")],
        "plaatsen": [V("Directiekamer", "🚪"), V("Aula", "🎭"), V("Fietsenstalling", "🚲")],
        "voorwerpen": [V("Sleutel", "🔑"), V("Zaklamp", "🔦"), V("Handschoen", "🧤")],
        "aanwijzingen": [
            "Yusuf was niet binnen in het schoolgebouw.",
            "De persoon in de directiekamer had een sleutel bij zich.",
            "Amara had geen sleutel en geen handschoen.",
            "De persoon met de zaklamp was in de aula.",
            "Daan droeg geen handschoen.",
            "De laptop verdween uit de directiekamer.",
        ],
        "oplossing": {"Amara": ("Aula", "Zaklamp"),
                      "Daan": ("Directiekamer", "Sleutel"),
                      "Yusuf": ("Fietsenstalling", "Handschoen")},
        "dader": "Daan",
    },
    {
        "titel": "Zaak 4: De verdwenen traktatie",
        "verhaal": ("De traktatie voor de jarige is verdwenen uit het klaslokaal! "
                    "Drie kinderen waren in de buurt. Ieder was op een andere plek "
                    "en had één ding bij zich. Wie heeft de traktatie gepakt?"),
        "verdachten": [V("Liam", "👦🏻"), V("Aisha", "👧🏾"), V("Sami", "👦🏽")],
        "plaatsen": [V("Speelplaats", "🛝"), V("Klaslokaal", "📒"), V("Gang", "🚪")],
        "voorwerpen": [V("Voetbal", "⚽"), V("Knuffel", "🧸"), V("Step", "🛴")],
        "aanwijzingen": [
            "Sami was in de gang.",
            "Liam was niet in het klaslokaal.",
            "De persoon op de speelplaats had een voetbal bij zich.",
            "Aisha had geen knuffel bij zich.",
            "De persoon met de step was in het klaslokaal.",
            "De traktatie verdween uit het klaslokaal.",
        ],
        "oplossing": {"Liam": ("Speelplaats", "Voetbal"),
                      "Aisha": ("Klaslokaal", "Step"),
                      "Sami": ("Gang", "Knuffel")},
        "dader": "Aisha",
    },
]

TINTS = ["#eef4fb", "#f2f8f3", "#fdf1f0", "#f6f2fc"]


def esc(s):
    return html.escape(str(s))


def kop_cel(item):
    return f'<th class="kh"><span class="em">{item["emoji"]}</span><span class="lb">{esc(item["naam"])}</span></th>'


def rij_cel(item):
    return f'<th class="rh"><span class="em">{item["emoji"]}</span> {esc(item["naam"])}</th>'


def render_grid(rij_titel, rijen, kol_titel, kolommen):
    kop = "".join(kop_cel(k) for k in kolommen)
    body = ""
    for r in rijen:
        cellen = "".join('<td></td>' for _ in kolommen)
        body += f'<tr>{rij_cel(r)}{cellen}</tr>'
    return (f'<div class="grid"><div class="gtitel">{esc(rij_titel)} '
            f'<span>×</span> {esc(kol_titel)}</div>'
            f'<table><tr><td class="hoek"></td>{kop}</tr>{body}</table></div>')


def render_zaak(zaak, index):
    tint = TINTS[index % len(TINTS)]
    verd, plt, vw = zaak["verdachten"], zaak["plaatsen"], zaak["voorwerpen"]
    aanw = "".join(f'<li>{esc(a)}</li>' for a in zaak["aanwijzingen"])
    grids = (render_grid("Verdachten", verd, "Plaatsen", plt)
             + render_grid("Verdachten", verd, "Voorwerpen", vw)
             + render_grid("Plaatsen", plt, "Voorwerpen", vw))
    return (f'<section class="zaak" style="--tint:{tint}">'
            f'<h1>🕵️ Murdoku</h1>'
            f'<h2>{esc(zaak["titel"])}</h2>'
            f'<p class="verhaal">{esc(zaak["verhaal"])}</p>'
            f'<div class="kolom2">'
            f'<div class="aanwijzingen"><h3>Aanwijzingen</h3><ol>{aanw}</ol>'
            f'<p class="tip">Zet een <b>✓</b> als iets zeker klopt en een <b>✗</b> als iets '
            f'onmogelijk is. Elke verdachte hoort bij precies één plek en één voorwerp.</p></div>'
            f'<div class="oplosvak"><h3>Wie is de dader?</h3>'
            f'<div class="regel">Dader: <span></span></div>'
            f'<div class="regel">Plek: <span></span></div>'
            f'<div class="regel">Voorwerp: <span></span></div></div>'
            f'</div>'
            f'<div class="grids">{grids}</div>'
            f'</section>')


def render_antwoorden():
    blokken = ""
    for z in ZAKEN:
        rijen = "".join(
            f'<tr><td class="n">{"🚨 " if naam == z["dader"] else ""}{esc(naam)}</td>'
            f'<td>{esc(pv[0])}</td><td>{esc(pv[1])}</td></tr>'
            for naam, pv in z["oplossing"].items())
        blokken += (f'<div class="antzaak"><h3>{esc(z["titel"])}</h3>'
                    f'<table class="anttab"><tr><th>Verdachte</th><th>Plek</th><th>Voorwerp</th></tr>'
                    f'{rijen}</table>'
                    f'<p class="dader">Dader: <b>{esc(z["dader"])}</b> '
                    f'({esc(z["oplossing"][z["dader"]][0])}, met '
                    f'{esc(z["oplossing"][z["dader"]][1]).lower()}).</p></div>')
    return f'<section class="zaak antwoordzaak" style="--tint:#ffffff"><h1>Antwoorden</h1>{blokken}</section>'


def htmldoc(titel, inner, printknop=True):
    btn = ('<button class="printknop" onclick="window.print()">🖨 Print deze pagina</button>'
           if printknop else "")
    return (f'<!doctype html><html lang="nl"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{esc(titel)}</title><style>{CSS}</style></head>'
            f'<body>{btn}{inner}</body></html>')


def bouw_index():
    kaartjes = ""
    for i, z in enumerate(ZAKEN, 1):
        kaartjes += (f'<a class="link zaak-link" href="zaak-{i}.html">'
                     f'<span class="lnr">Zaak {i}</span>'
                     f'<span class="lcats">{esc(z["titel"].split(": ",1)[1])}</span>'
                     f'<span class="lprint">🖨 openen &amp; printen</span></a>')
    return (f'<!doctype html><html lang="nl"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>Murdoku · groep 8</title><style>{INDEX_CSS}</style></head><body>'
            f'<div class="hero"><h1>🕵️ Murdoku</h1>'
            f'<p class="sub">Groep 8 · detective-logicapuzzels</p>'
            f'<p class="intro">Los de zaak op met de aanwijzingen: vul de kruistabellen in '
            f'met ✓ en ✗ en ontdek wie de dader is. Klik op een zaak om te openen en te printen. '
            f'Kies A4, marges "geen"/"standaard" en zet "achtergrondafbeeldingen" aan.</p>'
            f'<a class="link groot" href="murdoku.html">📄 Alle zaken + antwoordblad in één keer</a>'
            f'<div class="grid">{kaartjes}</div>'
            f'<a class="link antw" href="antwoorden.html">✅ Antwoordblad (voor de leerkracht)</a>'
            f'</div></body></html>')


CSS = """
*{margin:0;padding:0;box-sizing:border-box;}
body{background:#e7e9ec;font-family:"Trebuchet MS","Segoe UI",Verdana,sans-serif;color:#20272e;}
.zaak{width:210mm;min-height:297mm;margin:0 auto;background:var(--tint);padding:14mm 15mm;display:flex;flex-direction:column;}
h1{font-family:Georgia,serif;font-weight:700;letter-spacing:1px;text-align:center;font-size:30px;}
h2{text-align:center;font-size:21px;margin:4px 0 8px;color:#1b3a5c;}
.verhaal{font-size:15.5px;line-height:1.5;background:rgba(255,255,255,.6);border:1px solid rgba(0,0,0,.08);border-radius:12px;padding:12px 16px;}
.kolom2{display:flex;gap:16px;margin:12px 0;}
.aanwijzingen{flex:2;} .oplosvak{flex:1;}
h3{font-size:16px;margin-bottom:8px;color:#1b3a5c;}
.aanwijzingen ol{margin-left:20px;display:flex;flex-direction:column;gap:5px;font-size:14.5px;line-height:1.35;}
.tip{font-size:12.5px;color:#5c6772;margin-top:10px;line-height:1.4;}
.oplosvak{background:rgba(255,255,255,.6);border:2px dashed rgba(0,0,0,.2);border-radius:12px;padding:12px 14px;}
.oplosvak .regel{font-size:15px;margin-bottom:12px;}
.oplosvak .regel span{display:inline-block;border-bottom:1.5px solid #333;min-width:90px;height:16px;}
.grids{display:flex;gap:14px;justify-content:space-between;flex-wrap:wrap;margin-top:18px;}
.grid{flex:1;min-width:150px;}
.gtitel{font-size:12px;font-weight:bold;text-align:center;margin-bottom:5px;color:#1b3a5c;}
.gtitel span{color:#999;}
table{border-collapse:collapse;width:100%;}
.grid td,.grid th{border:1.3px solid #33414f;text-align:center;}
.grid td{height:30px;background:rgba(255,255,255,.55);}
.grid .hoek{background:transparent;border:none;}
.kh{padding:4px 2px;font-weight:normal;background:rgba(255,255,255,.35);}
.kh .em{display:block;font-size:16px;} .kh .lb{display:block;font-size:9px;line-height:1.1;}
.rh{padding:4px 6px;text-align:left;font-weight:normal;font-size:11px;white-space:nowrap;background:rgba(255,255,255,.35);}
.rh .em{font-size:14px;}
.printknop{position:fixed;top:14px;right:14px;z-index:50;border:none;cursor:pointer;background:#1b3a5c;color:#fff;
  font-family:"Trebuchet MS",sans-serif;font-weight:bold;font-size:15px;padding:12px 18px;border-radius:12px;box-shadow:0 4px 14px rgba(0,0,0,.2);}
.antwoordzaak h1{margin-bottom:10px;}
.antzaak{margin-bottom:18px;}
.anttab{border-collapse:collapse;width:100%;font-size:14px;}
.anttab th,.anttab td{border:1px solid #c7cfd6;padding:6px 10px;text-align:left;}
.anttab th{background:#eef2f6;}
.antzaak .dader{margin-top:6px;font-size:14.5px;}
@media print{
  body{background:#fff;} .printknop{display:none;}
  .zaak{margin:0;min-height:auto;height:297mm;page-break-after:always;}
  .zaak,.grid td,.kh,.rh,.verhaal,.oplosvak{-webkit-print-color-adjust:exact;print-color-adjust:exact;}
  @page{size:A4 portrait;margin:0;}
}
@media screen{.zaak{box-shadow:0 2px 14px rgba(0,0,0,.14);margin:16px auto;}}
"""

INDEX_CSS = """
*{margin:0;padding:0;box-sizing:border-box;}
body{font-family:"Trebuchet MS","Segoe UI",Verdana,sans-serif;color:#20272e;min-height:100vh;display:flex;
  align-items:center;justify-content:center;padding:26px;background:linear-gradient(135deg,#eef4fb,#f2f8f3,#fdf1f0);}
.hero{background:#fff;border-radius:22px;box-shadow:0 10px 40px rgba(0,0,0,.12);padding:34px 30px;max-width:600px;width:100%;text-align:center;}
h1{font-family:Georgia,serif;font-size:40px;letter-spacing:1px;margin-bottom:2px;}
.sub{color:#1b3a5c;font-weight:bold;text-transform:uppercase;letter-spacing:2px;font-size:13px;margin-bottom:14px;}
.intro{color:#6b7680;font-size:14px;line-height:1.5;margin:0 auto 22px;max-width:470px;}
.link{display:block;text-decoration:none;border-radius:14px;padding:16px 18px;font-weight:bold;transition:transform .08s;}
.link:hover{transform:translateY(-2px);}
.groot{background:#1b3a5c;color:#fff;font-size:17px;margin-bottom:18px;}
.antw{background:#eaf3ee;color:#2f7d4f;margin-top:18px;}
.grid{display:grid;grid-template-columns:1fr;gap:12px;}
.zaak-link{background:#eef3fb;color:#1b3a5c;text-align:left;display:flex;flex-direction:column;gap:3px;}
.lnr{font-size:17px;} .lcats{font-weight:normal;font-size:12.5px;color:#7c8088;}
.lprint{font-weight:normal;font-size:12px;color:#2f6bb0;margin-top:2px;}
"""


def schrijf(naam, inhoud):
    with open(naam, "w", encoding="utf-8") as f:
        f.write(inhoud)


def main():
    schrijf("index.html", bouw_index())
    alles = "".join(render_zaak(z, i) for i, z in enumerate(ZAKEN)) + render_antwoorden()
    schrijf("murdoku.html", htmldoc("Murdoku · alle zaken", alles))
    schrijf("antwoorden.html", htmldoc("Murdoku · antwoordblad", render_antwoorden()))
    for i, z in enumerate(ZAKEN, 1):
        schrijf(f"zaak-{i}.html", htmldoc(f"Murdoku · zaak {i}", render_zaak(z, i - 1)))
    print(f"Klaar: {len(ZAKEN)} zaken + antwoordblad.")
    print("  - index.html, murdoku.html, antwoorden.html, zaak-1.." + str(len(ZAKEN)) + ".html")


if __name__ == "__main__":
    main()
