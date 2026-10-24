"""Erzeugt die beiden Auftaktbeiträge (27.09. und 11.10.2026) aus dem Seitengerüst."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from seite import seite

root = pathlib.Path(__file__).resolve().parent.parent

B1_TITEL = "Warum eine europäische Karmaforschung?"
B1_ANRISS = "Ein früherer Blog, ein Buch von 2012 und die Frage, warum ich die Arbeit an der Karmaforschung jetzt wieder aufnehme – mit erweitertem Bezugshorizont."
B1 = '''    <article>
      <div class="meta">27. September 2026 &middot; <span class="tag">Grundlagen</span></div>
      <h1>Warum eine europäische Karmaforschung?</h1>

      <p>Wer heute das Wort «Karma» hört, denkt meist an Indien. Das Wort stammt aus dem Sanskrit, und die Vorstellung, dass ein Mensch mehr als einmal lebt, verbinden die meisten mit Hinduismus und Buddhismus – oder mit einer westlichen Esoterik, die sich aus diesen Quellen bedient. Mich beschäftigt seit langem eine andere Spur: dass es in Europa eine eigene Auseinandersetzung mit Wiederverkörperung und Schicksal gibt, mit eigenen Fragen, eigenen Begriffen und einer eigenen Geschichte.</p>

      <h2>Ein früherer Anlauf</h2>

      <p>Ganz neu ist dieses Vorhaben nicht. Schon einmal habe ich mich über längere Zeit in einem Blog regelmässig mit Reinkarnation und Karma beschäftigt. 2012 sind die Beiträge daraus gesammelt als Buch erschienen: <em>Europäische Karmaforschung. Fragmente einer Wissenschaft</em>. Der Untertitel war ernst gemeint. Es waren Bruchstücke aus einer fortlaufenden Arbeit, kein abgeschlossenes System, und ich habe sie bewusst so stehen lassen.</p>

      <p>Die These des Buches lässt sich in zwei Sätzen sagen. Es gibt eine europäische Karmaforschung, deren Anfänge sich bei Lessing, Goethe, Schopenhauer und Rudolf Steiner finden. Und sie ist in der akademischen Welt kaum beachtet worden, unter anderem deshalb, weil sie eine Voraussetzung hat, die sich den üblichen Verfahren der Wissenschaft nicht fügt: meditative Vertiefung.</p>

      <h2>Eine Frage aus dem 18. Jahrhundert</h2>

      <p>Wie früh diese Spur beginnt, zeigt ein kleiner Text von Gotthold Ephraim Lessing, <em>Die Erziehung des Menschengeschlechts</em>. Über weite Strecken handelt er davon, wie die Menschheit als Ganzes durch die Geschichte hindurch lernt. Gegen Ende aber wendet Lessing den Blick vom Geschlecht auf den einzelnen Menschen und stellt im Paragraphen 94 eine schlichte Frage: Warum sollte nicht jeder Einzelne «mehr als einmal auf dieser Welt vorhanden gewesen sein»? Im nächsten Paragraphen fragt er zurück, ob diese Hypothese etwa deshalb lächerlich sei, weil sie die älteste ist.</p>

      <p>Mich berührt an diesen Paragraphen weniger die Antwort als die Form. Lessing verkündet keine Lehre. Er stellt eine Frage, nennt sie eine Hypothese und denkt sie im Zusammenhang mit Lernen und Entwicklung. Darin sehe ich einen Grundzug der europäischen Auseinandersetzung mit dem Thema: Wiederverkörperung nicht als übernommene Überzeugung, sondern als Frage an das eigene Denken.</p>

      <p class="note">Deutung: Dass Lessings fragende Form für die europäische Tradition insgesamt typisch ist, ist meine Lesart und keine belegte Gesamtaussage. Ich werde sie an den einzelnen Autoren prüfen.</p>

      <h2>Warum diese Spur so wenig beachtet ist</h2>

      <p>Rudolf Steiner hat 1904 in seiner Schrift <em>Theosophie</em> ein ganzes Kapitel der «Wiederverkörperung des Geistes und Schicksal» gewidmet. Er argumentiert dort zunächst mit Mitteln des Denkens: Der Mensch sei als geistige Individualität nicht aus Vererbung erklärbar, und das, was er tut, wirke als selbstgeschaffenes Schicksal auf ihn zurück. Zugleich sagt Steiner deutlich, dass das Denken auf diesem Weg nur zu einem Umriss gelangt. Die volle Bestätigung erwartet er von einer Erkenntnis, die durch Schulung erst gewonnen werden muss.</p>

      <p>Hier liegt, so verstehe ich es, der Grund für die Zurückhaltung der Universitäten. Eine Forschung, die von ihren Teilnehmern eine innere Übung verlangt, passt schlecht zu einem Wissenschaftsverständnis, das Ergebnisse unabhängig von der Person des Forschenden überprüfbar machen will. Das muss kein Einwand gegen diese Forschung sein. Es ist aber eine Spannung, die man offen benennen sollte, statt sie zu überspielen.</p>

      <h2>Was sich seither verändert hat</h2>

      <p>Seit dem Buch sind viele Jahre vergangen, und eigene Studien haben meinen Bezugshorizont erweitert. Mein methodischer Ausgangsort ist Rudolf Steiner geblieben – gerade auch dort, wo er karmische Zusammenhänge nicht erklärt, sondern auf der Bühne darstellt: in seinen vier Mysteriendramen, mit denen ich mich als Forscher und Dramaturg seit Jahrzehnten beschäftige (mehr dazu auf <a href="https://mysteriendramen.ch">mysteriendramen.ch</a>). Von dort aus suche ich das Gespräch mit der Seinsphilosophie Martin Heideggers und der Hermeneutik Hans-Georg Gadamers, und mit Peter Sloterdijk frage ich nach der ästhetischen Seite des Themas.</p>

      <p>Daneben gibt es eine empirische Forschung, die es 2012 in meinem Blickfeld kaum gab: die Fallstudien, die der Psychiater Ian Stevenson an der University of Virginia begonnen hat und die dort nach seinem Ruhestand fortgeführt wurden. Sie prüfen Aussagen von Kindern, die sich an ein früheres Leben zu erinnern scheinen, an Dokumenten und Zeugenaussagen. Ich werde diese Arbeiten hier darstellen und einordnen. Meine eigene Methode sind sie nicht.</p>

      <h2>Was hier entstehen soll</h2>

      <p>Diese Seite setzt den früheren Blog in neuer Gestalt fort. Etwa alle zwei Wochen erscheint ein Beitrag: zu einzelnen Autoren und Texten, zu Begriffen und ihrer Geschichte, zu methodischen Fragen. Jeder Beitrag nennt seine Quellen. Wo ich deute oder eine Arbeitshypothese formuliere, kennzeichne ich das.</p>

      <p>Im nächsten Beitrag frage ich, bevor es um einzelne Autoren geht, nach den Voraussetzungen: Welche Arten von Wissen gibt es über Reinkarnation und Karma überhaupt – und auf welchen Ebenen lässt sich so etwas wie Ursache und Wirkung beobachten?</p>

      <hr class="rule">

      <h2>Quellen</h2>
      <ul class="sources">
        <li>Alexander G. Höhne: <em>Europäische Karmaforschung. Fragmente einer Wissenschaft</em>. Books on Demand, 2012, 422 Seiten.</li>
        <li>Gotthold Ephraim Lessing: <em>Die Erziehung des Menschengeschlechts</em> (1777/1780), §§ 93–100. Online: <a href="https://germanhistorydocs.org/de/das-heilige-roemische-reich-1648-1815/ghdi:document-3588">German History in Documents and Images</a>.</li>
        <li>Rudolf Steiner: <em>Theosophie. Einführung in übersinnliche Welterkenntnis und Menschenbestimmung</em> (1904, GA 9), Kapitel «Wiederverkörperung des Geistes und Schicksal».</li>
        <li>Zu Ian Stevenson und der Fortführung seiner Forschung: <a href="https://psi-encyclopedia.spr.ac.uk/articles/jim-b-tucker/">Psi Encyclopedia, Artikel «Jim B Tucker»</a>.</li>
      </ul>

      <p class="meta"><a href="/blog/">← Alle Beiträge</a></p>
    </article>'''

B2_TITEL = "Wo sich Ursache und Wirkung zeigen"
B2_ANRISS = "Bevor es um einzelne Autoren geht: welche Arten von Wissen es über Reinkarnation und Karma gibt – und auf welchen Ebenen sich Ursache und Wirkung beobachten lassen."
B2 = '''    <article>
      <div class="meta">11. Oktober 2026 &middot; <span class="tag">Methode</span></div>
      <h1>Wo sich Ursache und Wirkung zeigen</h1>

      <p>Wer über Karma spricht, spricht über Ursache und Wirkung: Was ich tue, kommt in irgendeiner Form auf mich zurück. So einfach der Satz klingt, so unklar ist, wo dieses Zurückkommen eigentlich stattfinden soll und wie man es bemerken könnte. Bevor ich mich in den nächsten Beiträgen einzelnen Autoren zuwende, möchte ich deshalb zwei Vorfragen ordnen. Welche Arten von Wissen über Reinkarnation und Karma gibt es? Und in welchen Feldern lässt sich ein Zusammenhang von Ursache und Wirkung überhaupt beobachten?</p>

      <h2>Drei Felder bei Steiner</h2>

      <p>Einen klaren Ausgangspunkt gibt Rudolf Steiner in seiner <em>Theosophie</em> von 1904. Er beschreibt den Menschen als Bürger dreier Welten: Durch den Leib gehört er der physischen Welt an, durch die Seele baut er sich eine eigene Innenwelt auf, und durch den Geist öffnet sich ihm eine Welt, die über beide hinausreicht.</p>

      <p>Im Kapitel über Wiederverkörperung und Schicksal ordnet Steiner jedem dieser Glieder eine eigene Gesetzmässigkeit zu. Der Leib folgt der Vererbung. Die Seele steht unter dem Schicksal, das sie sich durch ihre eigenen Taten selbst geschaffen hat; dafür verwendet Steiner das Wort Karma. Der Geist schliesslich folgt dem Gesetz der Wiederverkörperung. Damit sind drei Felder unterschieden, in denen jeweils etwas anderes als Ursache wirkt.</p>

      <table>
        <thead>
          <tr><th>Feld</th><th>Was dort wirkt (nach Steiner)</th><th>Wie es zugänglich wird (meine Zuordnung)</th></tr>
        </thead>
        <tbody>
          <tr><td>Leib</td><td>Vererbung</td><td>Sinne und Naturwissenschaft</td></tr>
          <tr><td>Seele</td><td>selbstgeschaffenes Schicksal, Karma</td><td>Rückblick auf die eigene Biografie, Denken</td></tr>
          <tr><td>Geist</td><td>Wiederverkörperung</td><td>nach Steiner erst durch höhere Erkenntnis</td></tr>
        </tbody>
      </table>

      <p class="note">Die beiden ersten Spalten folgen Steiners Kapitel; die dritte Spalte ist meine Zuordnung und als Arbeitshypothese gemeint.</p>

      <p>Für die Karmaforschung folgt daraus etwas Einfaches, das oft übersehen wird. Wer Karma im Feld des Leibes sucht, etwa in einer Krankheit als «Strafe», verwechselt die Ebenen. Was Steiner Karma nennt, wirkt in der Seele, also dort, wo Erlebnisse, Fähigkeiten und Begegnungen ein Leben prägen.</p>

      <h2>Stufen des Erkennens</h2>

      <p>Wie aber wird dieses Feld sichtbar? Auch hier gibt Steiner eine Gliederung, in den Aufsätzen, die 1905 in der Zeitschrift <em>Lucifer-Gnosis</em> erschienen und später als <em>Die Stufen der höheren Erkenntnis</em> (GA 12) gesammelt wurden. Er unterscheidet vier Stufen. Die gewöhnliche, materielle Erkenntnis lebt von Sinneseindruck, Bild, Begriff und dem Ich, das alles zusammenhält. In der Imagination fallen die Sinneseindrücke weg, und es bleiben Bilder, die keinem äusseren Gegenstand entstammen. In der Inspiration treten auch die Bilder zurück; die geistige Welt wird eher wie eine Sprache vernommen. In der Intuition schliesslich bleibt nur das Ich, das nicht mehr von aussen betrachtet, sondern in den Dingen selbst lebt.</p>

      <p>Im Kapitel der <em>Theosophie</em> über Wiederverkörperung zieht Steiner daraus eine methodische Folgerung. Das Denken kann den Gedanken wiederholter Erdenleben fassen und seine Folgerichtigkeit einsehen. Es gelangt dabei aber nur zu einem Umriss. Die Anschauung dessen, was ihn ausfüllt, setzt die höheren Stufen voraus.</p>

      <h2>Vier Wissensbestände</h2>

      <p>Wenn man diese Unterscheidungen auf das Ganze dessen anwendet, was heute über Reinkarnation und Karma gesagt wird, lassen sich nach meinem Eindruck vier Wissensbestände unterscheiden. Sie werden oft vermischt, obwohl sie Verschiedenes leisten.</p>

      <ul>
        <li><strong>Überlieferung:</strong> religiöse und mythologische Traditionen, in Indien ebenso wie in der europäischen Antike. Sie geben Bilder und Lehren weiter, aber keinen Weg, sie selbst zu prüfen.</li>
        <li><strong>Philosophisches Denken:</strong> die Frage, ob die Vorstellung wiederholter Leben in sich stimmig ist und was sie erklären würde. Lessings Frage in der <em>Erziehung des Menschengeschlechts</em> gehört hierher. Dieses Wissen prüft Begriffe, nicht Tatsachen.</li>
        <li><strong>Empirische Forschung:</strong> etwa die Fallstudien Ian Stevensons. Sie vergleicht Aussagen mit Dokumenten und kann Übereinstimmungen feststellen. Wie sie zustande kommen, kann sie aus ihrer Methode heraus nicht zeigen.</li>
        <li><strong>Meditative Erkenntnis:</strong> der Weg, den Steiner beschreibt. Er beansprucht, das Feld selbst anschauen zu können, ist aber an die Schulung desjenigen gebunden, der erkennt.</li>
      </ul>

      <p class="note">Arbeitshypothese: Die Vierteilung und die Beschreibung dessen, was jeder Wissensbestand leistet, ist mein Vorschlag zur Ordnung des Feldes, keine Gliederung, die sich so bei Steiner findet.</p>

      <h2>Was daraus folgt</h2>

      <p>Ursache und Wirkung zeigen sich je nach Feld auf verschiedene Weise. Im Leib sind sie messbar. In der Seele werden sie im Rückblick auf ein Leben ahnbar: in Wiederholungen, in Fähigkeiten, deren Herkunft rätselhaft bleibt, in Begegnungen, die mehr Gewicht haben, als ihr Anlass erklärt. Über die Grenze eines Lebens hinaus aber lassen sie sich, wenn man Steiner folgt, nur noch mit einer geschulten Erkenntnis verfolgen.</p>

      <p>Für die Beiträge dieser Seite bedeutet das zweierlei. Ich werde jeweils sagen, aus welchem Wissensbestand eine Aussage stammt. Und ich werde nicht so tun, als könne ein Essay leisten, was nach Steiner nur der eigene Erkenntnisweg leisten kann. Ein Essay kann den Umriss nachzeichnen und die Fragen genau stellen.</p>

      <p>Wie Steiner selbst diese Felder nicht nur beschrieben, sondern auf der Bühne dargestellt hat, ist das Thema des nächsten Beitrags: Karma in den Mysteriendramen.</p>

      <hr class="rule">

      <h2>Quellen</h2>
      <ul class="sources">
        <li>Rudolf Steiner: <em>Theosophie. Einführung in übersinnliche Welterkenntnis und Menschenbestimmung</em> (1904, GA 9), Kapitel «Das Wesen des Menschen» und «Wiederverkörperung des Geistes und Schicksal». Englische Übersetzung online: <a href="https://www.rsarchive.org/Books/GA009/English/RSP1965/GA009_c02.html">Rudolf Steiner Archive</a>.</li>
        <li>Rudolf Steiner: <em>Die Stufen der höheren Erkenntnis</em> (GA 12), zuerst 1905 in <em>Lucifer-Gnosis</em>. Englische Übersetzung online: <a href="https://rsarchive.org/Books/GA012/English/AP1967/GA012_c01.html">Rudolf Steiner Archive</a>.</li>
        <li>Gotthold Ephraim Lessing: <em>Die Erziehung des Menschengeschlechts</em> (1777/1780), §§ 93–100. Online: <a href="https://germanhistorydocs.org/de/das-heilige-roemische-reich-1648-1815/ghdi:document-3588">German History in Documents and Images</a>.</li>
        <li>Zu Ian Stevenson und der Fortführung seiner Forschung: <a href="https://psi-encyclopedia.spr.ac.uk/articles/jim-b-tucker/">Psi Encyclopedia, Artikel «Jim B Tucker»</a>.</li>
      </ul>

      <p class="meta"><a href="/blog/">← Alle Beiträge</a></p>
    </article>'''

(root/"blog"/"2026-09-27-europaeische-karmaforschung.html").write_text(seite(B1_TITEL + " — Karmaforschung", B1_ANRISS, "/blog/", B1))
(root/"blog"/"2026-10-11-ursache-und-wirkung.html").write_text(seite(B2_TITEL + " — Karmaforschung", B2_ANRISS, "/blog/", B2))

def eintrag(datum, href, titel, anriss, tag=None):
    meta = datum + (f' &middot; <span class="tag">{tag}</span>' if tag else '')
    return f'''      <li>
        <div class="meta">{meta}</div>
        <h2><a href="{href}">{titel}</a></h2>
        <p class="post-excerpt">{anriss}</p>
      </li>
'''

liste_start = eintrag("11. Oktober 2026", "/blog/2026-10-11-ursache-und-wirkung.html", B2_TITEL, B2_ANRISS) + eintrag("27. September 2026", "/blog/2026-09-27-europaeische-karmaforschung.html", B1_TITEL, B1_ANRISS)
liste_blog = eintrag("11. Oktober 2026", "/blog/2026-10-11-ursache-und-wirkung.html", B2_TITEL, B2_ANRISS, "Methode") + eintrag("27. September 2026", "/blog/2026-09-27-europaeische-karmaforschung.html", B1_TITEL, B1_ANRISS, "Grundlagen")

p = root/"index.html"; s = p.read_text()
marker = "      <!-- Neueste Beiträge: wird bei jedem neuen Post oben ergänzt (max. 5) -->\n"
assert marker in s
s = s.replace(marker, marker + liste_start)
s = s.replace('    <p class="meta" id="noch-keine">Der erste Beitrag erscheint am 25. Oktober 2026.</p>\n', '')
p.write_text(s)

p = root/"blog"/"index.html"; s = p.read_text()
marker = "      <!-- Neuester Beitrag zuoberst; beim Hinzufügen eines neuen Posts hier einen <li>-Block einfügen -->\n"
assert marker in s
p.write_text(s.replace(marker, marker + liste_blog))
