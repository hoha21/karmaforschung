"""Gemeinsames Seitengerüst für karmaforschung.ch.
Aufruf in neuen Beiträgen nicht nötig – Beiträge sind fertige HTML-Dateien.
Dieses Skript erzeugt nur die Grundseiten (Start, Blog, Über mich, Impressum)."""

FONTS = '''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css">'''

NAV = [("/", "Start"), ("/blog/", "Blog"), ("/ueber-mich.html", "Über mich"), ("/impressum.html", "Impressum")]

def seite(titel, beschreibung, aktiv, inhalt):
    nav = "\n".join(
        f'      <a href="{h}"{" aria-current=\"page\"" if h == aktiv else ""}>{t}</a>' for h, t in NAV)
    return f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titel}</title>
<meta name="description" content="{beschreibung}">
{FONTS}
</head>
<body>

<header class="site-header">
  <div class="wrap">
    <a class="brand" href="/">Karmaforschung</a>
    <div class="tagline">Reinkarnation und Karma in der europäischen Geistesgeschichte</div>
    <nav class="site-nav">
{nav}
    </nav>
  </div>
</header>

<main>
  <div class="wrap">
{inhalt}
  </div>
</main>

<footer class="site-footer">
  <div class="wrap">
    <span>© 2026 Alexander Höhne</span>
    <a href="/impressum.html">Impressum</a>
  </div>
</footer>

</body>
</html>
'''

if __name__ == "__main__":
    import pathlib
    root = pathlib.Path(__file__).resolve().parent.parent

    start = '''
    <h1>Eine europäische Karmaforschung</h1>

    <p>Die Vorstellung, dass ein Mensch mehr als ein Leben hat und dass diese Leben in einem Zusammenhang stehen, wird gewöhnlich im Osten verortet – in Indien, im Buddhismus, in Lehren, die Europa erst im 19. Jahrhundert breiter zur Kenntnis nahm. Diese Seite geht einer anderen Spur nach: Es gibt eine eigene, europäische Auseinandersetzung mit Reinkarnation und Karma. Ihre Anfänge lassen sich bei Lessing, Goethe und Schopenhauer finden, eine ausgearbeitete Gestalt gewinnt sie bei Rudolf Steiner – und sie ist bis heute akademisch erstaunlich wenig beachtet.</p>

    <p>Ein Grund dafür liegt wohl in ihrer Methode. Wer Karmaforschung nicht nur als Ideengeschichte betreiben will, kommt um die Frage nach meditativer Vertiefung nicht herum – und damit um einen Erkenntnisweg, der sich den gewohnten Verfahren der Wissenschaft nicht ohne Weiteres fügt. Gerade diese Spannung interessiert mich: Was lässt sich über diese Tradition genau und überprüfbar sagen, und wo beginnt das Feld der Deutung?</p>

    <p>Ganz neu ist dieses Vorhaben nicht. Schon einmal habe ich mich in einem Blog regelmässig mit Reinkarnation und Karma auseinandergesetzt; 2012 sind die Beiträge daraus gesammelt als Buch erschienen: <em>Europäische Karmaforschung. Fragmente einer Wissenschaft</em> (Books on Demand, 422 Seiten). Der Untertitel war ernst gemeint – es waren Bruchstücke aus einer fortlaufenden Arbeit, kein abgeschlossenes System. Jetzt nehme ich diese Arbeit wieder auf. In den Jahren seither haben mich eigene Studien zu einem erweiterten Bezugshorizont geführt. Mein methodischer Ausgangsort ist dabei Rudolf Steiner – gerade auch dort, wo er karmische Zusammenhänge nicht erklärt, sondern darstellt: in seinen vier Mysteriendramen, mit denen ich mich als Forscher und Dramaturg seit Jahrzehnten beschäftige (mehr dazu auf <a href="https://mysteriendramen.ch">mysteriendramen.ch</a>). Von dort aus gehe ich meditative, seinsphilosophische und hermeneutische Wege – im Gespräch mit Martin Heidegger und Hans-Georg Gadamer – und frage mit Peter Sloterdijk auch nach der ästhetischen Seite des Themas. Daneben gibt es neuere empirische Forschungen, allen voran die Fallstudien des Psychiaters Ian Stevenson an der University of Virginia und die Arbeiten, die an ihn anschliessen. Sie nehme ich zur Kenntnis und ordne sie ein; die empirische Arbeit selbst überlasse ich anderen. Diese Seite ist deshalb keine Neuauflage des Buches, sondern die Fortsetzung jenes Blogs in neuer Gestalt.</p>

    <p>Hier sammle ich dazu kurze, essayistische Beiträge – zu einzelnen Autoren und Texten, zu Begriffen und ihrer Geschichte und zu methodischen Fragen – auch dazu, was empirische Forschung zeigen kann und was nicht. Quellen werden belegt; wo ich deute oder eine Arbeitshypothese formuliere, sage ich das dazu.</p>

    <hr class="rule">

    <h2>Neueste Beiträge</h2>
    <ul class="post-list" id="recent-posts">
      <!-- Neueste Beiträge: wird bei jedem neuen Post oben ergänzt (max. 5) -->
    </ul>
    <p class="meta" id="noch-keine">Der erste Beitrag erscheint am 25. Oktober 2026.</p>

    <p><a href="/blog/">Alle Beiträge im Archiv →</a></p>
'''
    blog = '''
    <h1>Blog</h1>
    <p class="meta">Neue Beiträge erscheinen etwa alle zwei Wochen.</p>

    <ul class="post-list">
      <!-- Neuester Beitrag zuoberst; beim Hinzufügen eines neuen Posts hier einen <li>-Block einfügen -->
    </ul>
'''
    ueber = '''
    <h1>Über mich</h1>

    <p>Ich bin Alexander Höhne. Neben meiner Forschung zu Rudolf Steiners Mysteriendramen – dazu gibt es eine eigene Seite, <a href="https://mysteriendramen.ch">mysteriendramen.ch</a> – beschäftige ich mich seit vielen Jahren mit der Frage nach Reinkarnation und Karma in der europäischen Geistesgeschichte.</p>

    <p>Aus einem früheren Blogprojekt, in dem ich mich regelmässig mit diesen Fragen auseinandersetzte, ist 2012 das Buch <em>Europäische Karmaforschung. Fragmente einer Wissenschaft</em> hervorgegangen (Books on Demand, 422 Seiten), eine Sammlung jener Beiträge. Seine These: Es gibt eine europäische Karmaforschung mit Anfängen bei Lessing, Goethe, Schopenhauer, Steiner und anderen; sie ist akademisch zu wenig beachtet, unter anderem deshalb, weil sie meditative Vertiefung voraussetzt.</p>

    <p>Mein wissenschaftlicher Hintergrund liegt in der germanistischen Sprachwissenschaft im Grenzgebiet zur Literaturwissenschaft; promoviert habe ich 2005 am Deutschen Seminar der Universität Basel. Ich bin als Vortragsredner und Kursleiter tätig.</p>

    <p>Diese Seite knüpft an jenes Blogprojekt und das Buch an und führt beides weiter – in loser, essayistischer Form. Fragen, Anmerkungen und Hinweise sind willkommen; Kontaktangaben finden sich im <a href="/impressum.html">Impressum</a>.</p>
'''
    impressum = '''
    <h1>Impressum</h1>

    <p><strong>Verantwortlich für den Inhalt:</strong><br>
    Alexander G. Höhne<br>
    Dornacherstrasse 49-51<br>
    CH-4053 Basel</p>

    <p><strong>Kontakt:</strong><br>
    E-Mail: <a href="mailto:alexander@alexanderhoehne.ch">alexander@alexanderhoehne.ch</a></p>

    <h2>Haftungshinweis</h2>
    <p>Die Inhalte dieser Seite wurden mit Sorgfalt erstellt, erheben jedoch keinen Anspruch auf Vollständigkeit, Aktualität oder wissenschaftliche Letztgültigkeit. Für Links auf externe Webseiten wird keine Haftung übernommen; für deren Inhalte sind ausschliesslich die jeweiligen Betreiber verantwortlich.</p>

    <h2>Urheberrecht</h2>
    <p>Alle Texte auf dieser Seite unterliegen dem Urheberrecht des Autors, sofern nicht anders gekennzeichnet. Eine Weiterverwendung ist nur mit vorheriger Zustimmung und unter Angabe der Quelle gestattet.</p>
'''
    D = "Essays und Studien zu Reinkarnation und Karma in der europäischen Geistesgeschichte – von Lessing, Goethe und Schopenhauer bis Rudolf Steiner. Von Alexander Höhne."
    import re
    def behalte_liste(pfad, html, marker):
        """Übernimmt die bestehenden Beitragseinträge, damit ein Neuaufbau sie nicht löscht."""
        if not pfad.exists():
            return html
        alt = pfad.read_text()
        m = re.search(re.escape(marker) + r"\n(.*?)    </ul>", alt, re.S)
        eintraege = m.group(1) if m else ""
        if eintraege.strip():
            html = html.replace(marker + "\n", marker + "\n" + eintraege, 1)
            html = re.sub(r'    <p class="meta" id="noch-keine">.*?</p>\n', "", html)
        return html

    M_START = "      <!-- Neueste Beiträge: wird bei jedem neuen Post oben ergänzt (max. 5) -->"
    M_BLOG = "      <!-- Neuester Beitrag zuoberst; beim Hinzufügen eines neuen Posts hier einen <li>-Block einfügen -->"
    _orig_write = pathlib.Path.write_text
    def schreibe(pfad, html):
        for mk in (M_START, M_BLOG):
            if mk in html:
                html = behalte_liste(pfad, html, mk)
        _orig_write(pfad, html)

    schreibe(root/"index.html", seite("Karmaforschung — Reinkarnation und Karma in der europäischen Geistesgeschichte", D, "/", start))
    schreibe(root/"blog"/"index.html", seite("Blog — Karmaforschung", "Alle Beiträge zu Reinkarnation und Karma in der europäischen Geistesgeschichte.", "/blog/", blog))
    schreibe(root/"ueber-mich.html", seite("Über mich — Karmaforschung", "Alexander Höhne: Forschung zu Reinkarnation und Karma, Autor von «Europäische Karmaforschung. Fragmente einer Wissenschaft».", "/ueber-mich.html", ueber))
    schreibe(root/"impressum.html", seite("Impressum — Karmaforschung", "Impressum von karmaforschung.ch.", "/impressum.html", impressum))
