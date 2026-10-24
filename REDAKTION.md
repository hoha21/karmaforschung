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
  Alexander ihn in GitHub Desktop committet und pusht.

## Ablauf: vom Entwurf zur Veröffentlichung

Wie bei mysteriendramen.ch und alexanderhoehne.ch läuft alles über den lokalen
Ordner **`C:\GitBlog\karmaforschung`** auf Alexanders PC und **GitHub Desktop**.
Es gibt keine Pull Requests mehr.

1. **Vorher:** Alexander holt in GitHub Desktop den aktuellen Stand
   («Fetch origin», bei Bedarf «Pull origin»), damit der lokale Ordner und
   GitHub übereinstimmen.
2. Claude schreibt die Änderungen direkt in den lokalen Ordner:
   - den Beitrag `blog/JJJJ-MM-TT-kurztitel.html` (aus `tools/vorlage-beitrag.html`),
   - den Eintrag zuoberst in `blog/index.html`,
   - den Eintrag zuoberst in der Liste «Neueste Beiträge» in `index.html`
     (höchstens fünf Einträge),
   - einen `<url>`-Eintrag für den neuen Beitrag in `sitemap.xml`
     (`<lastmod>` = Erscheinungsdatum),
   - einen `<item>`-Eintrag zuoberst in `feed.xml` (RSS: Titel, Link, Datum,
     Rubrik, Anriss),
   - den Status in `REDAKTIONSPLAN.md` («Entwurf liegt vor»).
   Ist der lokale Ordner nicht auf dem Stand von GitHub, überschreibt Claude
   nichts, sondern legt den Entwurf im Unterordner `_entwuerfe/` ab und meldet das.
3. Alexander liest den Entwurf (die HTML-Datei lässt sich im Browser öffnen)
   und gibt Änderungswünsche an Claude oder ändert selbst.
4. **Veröffentlichen = in GitHub Desktop «Commit to main» und danach «Push origin».**
   GitHub Pages stellt die Seite automatisch online. Nicht pushen = nichts geht live.
5. Nicht gleichzeitig dieselbe Datei in einem Editor offen lassen, während Claude
   daran arbeitet; sonst kann eine ältere Fassung zurückgespeichert werden.

Claude veröffentlicht nie selbst: Claude committet und pusht nicht, das tut nur Alexander.

## Sprache und Stimme

- Schweizer Rechtschreibung: **ss statt ß** (wie mysteriendramen.ch).
- Anführungszeichen: deutsche „…“ (Hauskonvention wie auf mysteriendramen.ch).
- Vor jeder Veröffentlichung wird der Skill **mysteriendramen-blog-lektorat** sinngemäss
  angewendet (Sprachrichtigkeit, Stimme, Belegstatus).
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
- **Leitgedanke des Blogs:** gesucht sind Einsichten in eine «höhere», aber
  immer noch reflektierte Erkenntnis – sie gibt an, aus welchem Feld und auf
  welcher Erkenntnisstufe eine Aussage stammt, und trennt Anschauung, Deutung
  und Begriff.
- **Verstehen statt Erklären:** Karma fasst Ursache und Wirkung in ein Wort und
  klammert die zwingende Zeitfolge aus. Sinnzusammenhänge sind oft verborgen
  (okkult) und werden durch Reflexion, Differenzierung und hermeneutisches
  Verstehen entborgen (Heidegger im Anschluss an Husserl, Gadamer) – nicht
  naturwissenschaftlich erklärt.
- **Wissensbestände:** neben empirischem auch historisches, kulturell-spontanes
  (Legenden, Mythen), philosophisches, narratives, performatives/exploratives
  und meditatives Wissen.
- **Bedeutung der Lehre:** Reinkarnation und Karma sind dort bedeutsam, wo sie
  Erfahrung informieren oder differenzieren und den Horizont erweitern oder
  vertiefen. Beiträge zeigen, wo das der Fall ist.
- **Europäische Karmaforschung** wird verstanden aus der Entwicklung der Moderne
  um 1900 und ihren Vorläufern (Aufklärung): individuelle Erkenntnis und
  Lebensführung, Suche nach anderen Grundlagen als Tradition, vorgefundener
  Gesellschaftsordnung und institutioneller Religion.
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

## Kopfbereich der Beiträge (Vorschau, Suchmaschinen)

`tools/vorlage-beitrag.html` enthält im `<head>` neben `{{TITEL}}` und `{{ANRISS}}`
zwei weitere Platzhalter, die beim Erstellen eines Beitrags immer ersetzt werden:

- `{{DATEINAME}}`: Dateiname des Beitrags, z. B. `2026-11-08-begriffsgeschichte.html`
  (ergibt Canonical-Link und `og:url`),
- `{{DATUM_ISO}}`: Erscheinungsdatum im Format `JJJJ-MM-TT`.

Die Platzhalter kommen auch im Block `application/ld+json` (strukturierte Daten
für Suchmaschinen) vor; dort keine geraden Anführungszeichen " verwenden, sondern „…“.
Der Seitentitel (`<title>`) sollte höchstens etwa 65 Zeichen lang sein; ist er
mit dem Zusatz « — Karmaforschung» länger, entfällt der Zusatz. Der Anriss
(`description`) sollte höchstens 160 Zeichen haben.

Die Schriften liegen lokal unter `assets/fonts/`; es werden keine Google Fonts eingebunden.
Favicon (`favicon.svg`, `favicon.ico`, `apple-touch-icon.png`) und das Vorschaubild
`assets/img/og-image.png` gelten für alle Seiten.

## Rubriken

Jeder Beitrag erhält genau eine Rubrik aus diesem festen Satz (in `<span class="tag">`,
im JSON-LD als `articleSection` und im Feed als `<category>`):

- **Grundlagen** – Ausrichtung der Seite, Leitfrage, Menschenbild
- **Methode** – Erkenntniswege, Formen des Wissens, meditative Vertiefung
- **Begriffe** – Begriffsgeschichte und Begriffsklärung
- **Autoren** – einzelne Autoren der europäischen Spur (Lessing, Herder, Goethe, Schopenhauer, Steiner …)
- **Philosophie** – philosophische Gesprächspartner (Heidegger, Gadamer, Sloterdijk …)
- **Empirie** – empirische Forschung und Naturwissenschaft (Stevenson, Hirnforschung …)
- **Mysteriendramen** – Karma in Steiners Mysteriendramen

Die Rubrik steht auch im REDAKTIONSPLAN.md. Die Blogübersicht bietet einen
Rubriken-Filter (`assets/js/rubriken.js`); er übernimmt die Rubriken automatisch
aus den Einträgen. Direktlink auf eine Rubrik: `/blog/#rubrik=Methode`.
