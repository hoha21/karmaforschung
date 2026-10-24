# Redaktion karmaforschung.ch

Arbeitsgrundlage für Alexander und für Claude. Die geplante Aufgabe
«Karmaforschung: Blog-Entwurf» liest diese Datei bei jedem Lauf.

## Rhythmus

- Ein Beitrag alle zwei Wochen, **sonntags**, im Wechsel mit mysteriendramen.ch
  (dort erscheinen die Beiträge an den jeweils anderen Sonntagen).
- Erste Beiträge: 27.09. und 11.10.2026 (nachträglich angelegt); der Zyklus läuft ab
  **Sonntag, 25. Oktober 2026**, danach 8.11., 22.11., 6.12. usw.
- Der Entwurf entsteht jeweils **am selben Sonntag gegen 23 Uhr**; das
  Erscheinungsdatum im Beitrag ist dieser Sonntag. Online geht er, sobald
  Alexander den Pull Request mergt.

## Ablauf: vom Entwurf zur Veröffentlichung

1. Claude legt einen Zweig `entwurf/JJJJ-MM-TT-kurztitel` an und schreibt dort:
   - den Beitrag `blog/JJJJ-MM-TT-kurztitel.html` (aus `tools/vorlage-beitrag.html`),
   - den Eintrag zuoberst in `blog/index.html`,
   - den Eintrag zuoberst in der Liste «Neueste Beiträge» in `index.html`
     (höchstens fünf Einträge; der Hinweis `id="noch-keine"` wird beim ersten
     Beitrag entfernt),
   - den Status in `REDAKTIONSPLAN.md` («Entwurf liegt vor»).
   Sind noch frühere Entwurfs-Pull-Requests offen, baut der neue Zweig auf dem
   neuesten offenen Entwurfszweig auf, damit die Beitragslisten zusammenpassen.
2. Claude öffnet dazu einen **Pull Request** gegen `main` mit dem Titel
   «Entwurf: <Titel> (<Datum>)». In der Beschreibung: Kurzinhalt, verwendete
   Quellen, offene Fragen und alle Stellen, die als Deutung markiert sind.
3. Alexander liest den Entwurf (Handy: GitHub-App → Pull Requests; PC: GitHub
   Desktop oder Browser), kommentiert oder ändert.
4. **Veröffentlichen = Pull Request mergen.** GitHub Pages stellt die Seite
   danach automatisch online. Nicht mergen = nichts geht live.
5. Am PC danach in GitHub Desktop «Fetch/Pull», damit `C:\GitBlog\Karmaforschung`
   auf demselben Stand ist.

Claude veröffentlicht nie selbst, mergt nie selbst und schreibt nie direkt auf `main`.

## Sprache und Stimme

- Schweizer Rechtschreibung: **ss statt ß** (wie mysteriendramen.ch).
- Ich-Perspektive Alexanders; Ton zugänglich-essayistisch, nicht akademisch-schwer,
  aber genau. Länge etwa 900–1500 Wörter.
- Keine KI-Floskeln: keine Bedeutungsbehauptungen («spielt eine zentrale Rolle»),
  keine Meta-Floskeln («es ist wichtig zu betonen»), keine mechanischen
  Absatzanfänge («Zudem», «Darüber hinaus»), keine abgenutzten Metaphern.
  Massstab ist der Ton der bisherigen Beiträge auf mysteriendramen.ch.
- Frühere IT-Tätigkeiten werden nicht erwähnt.

## Methodische Haltung

- **Primärer methodischer Ausgangsort ist Rudolf Steiner**, gerade auch seine
  Darstellung karmischer Zusammenhänge in den vier Mysteriendramen. Wo es passt,
  wird auf mysteriendramen.ch verwiesen; Fakten zu den Dramen werden an den
  Texten geprüft (Steiner, GA 14).
- Von dort aus ist Alexanders Zugang **meditativ, seinsphilosophisch und
  hermeneutisch** (im Gespräch mit Heidegger und Gadamer) sowie **ästhetisch**
  (mit Sloterdijk).
- Empirische Reinkarnationsforschung (Ian Stevenson und Nachfolge an der
  University of Virginia) wird referiert und eingeordnet, aber nicht als
  eigene Methode vertreten. Die Beiträge machen keine empirischen Beweisansprüche.
- Philosophische Bezüge (Heidegger, Gadamer, Sloterdijk) werden genau belegt;
  ihre Anwendung auf die Karmafrage ist Alexanders Deutung und wird als solche
  erkennbar gemacht – keinem dieser Autoren wird eine Position zu Reinkarnation
  zugeschrieben, die er nicht nachweislich vertreten hat.

## Quellen

- **Nur verifizierte Quellen.** Jedes Zitat und jede Datierung wird vor dem
  Schreiben an einer zugänglichen Ausgabe geprüft (Werkausgabe, Digitalisat,
  rudolfsteiner.ch / Steiner-Online-Bibliothek, projekt-gutenberg, zeno.org o. ä.).
- Jeder Beitrag endet mit einer Quellenliste (Autor, Titel, Ausgabe, Stelle).
- Was sich nicht belegen lässt, wird ausdrücklich als **Deutung** oder
  **Arbeitshypothese** gekennzeichnet (im Text oder mit `<p class="note">`).
- Was sich gar nicht prüfen lässt, kommt nicht in den Text, sondern als offene
  Frage in die Pull-Request-Beschreibung.

## Technik

- Statische Seite auf GitHub Pages, Domain karmaforschung.ch (Datei `CNAME`).
- Grundseiten werden mit `tools/seite.py` erzeugt; Beiträge sind fertige
  HTML-Dateien nach `tools/vorlage-beitrag.html`.
- Datumsformat in Listen: «8. November 2026». Dateinamen: `2026-11-08-kurztitel.html`.
