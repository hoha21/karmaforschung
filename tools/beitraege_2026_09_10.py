"""Erzeugt die beiden Auftaktbeiträge (27.09. und 11.10.2026) aus dem Seitengerüst."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from seite import seite

root = pathlib.Path(__file__).resolve().parent.parent

B1_TITEL = "Warum eine europäische Karmaforschung?"
B1_ANRISS = "Ein früherer Blog, ein Buch von 2012 und die Frage, warum ich die Arbeit an der Karmaforschung jetzt wieder aufnehme – mit erweitertem Bezugshorizont."
B1 = '''    <article>
      <div class="meta">27. September 2026 &middot; <span class="tag">Grundlagen</span> &middot; nachträglich veröffentlicht im Oktober 2026</div>
      <h1>Warum eine europäische Karmaforschung?</h1>

      <p>Wer heute das Wort „Karma“ hört, denkt meist an Indien. Das Wort stammt aus dem Sanskrit, und die Vorstellung, dass ein Mensch mehr als einmal lebt, verbinden die meisten mit Hinduismus und Buddhismus – oder mit einer westlichen Esoterik, die sich aus diesen Quellen bedient. Mich beschäftigt seit langem eine andere Spur: dass es in Europa eine eigene Auseinandersetzung mit Wiederverkörperung und Schicksal gibt, mit eigenen Fragen, eigenen Begriffen und einer eigenen Geschichte.</p>

      <h2>Wie die Frage zu mir kam</h2>

      <p>Zu mir kam diese Frage nicht zuerst über Bücher. Mit vierzehn Jahren war ich in Athen und hatte dort eine Erinnerung an ein Lernen von Mathematik im antiken Griechenland. Mit neunzehn erlitt ich einen anaphylaktischen Schock mit Herzstillstand und hatte eine Nahtoderfahrung. Sie hat mir fragmentarisch bestätigt, dass Bewusstsein von der Sinneserfahrung unabhängig sein kann, und sie hat mir eine Ich-Erfahrung im „Seelenraum“ erlaubt.</p>

      <p>Ich erzähle das nicht als Beweis. Es sind Erfahrungen, die mich nach einem Zusammenhang haben fragen lassen. Was sie bedeuten, lässt sich nicht einfach glauben; es will reflektiert, unterschieden und mit dem verbunden werden, was andere vor mir gedacht und erfahren haben. Genau darin liegt für mich die Aufgabe einer Karmaforschung.</p>

      <h2>Ein früherer Anlauf</h2>

      <p>Ganz neu ist dieses Vorhaben nicht. Schon einmal habe ich mich über längere Zeit in einem Blog regelmässig mit Reinkarnation und Karma beschäftigt. 2012 sind die Beiträge daraus gesammelt als Buch erschienen: <em>Europäische Karmaforschung. Fragmente einer Wissenschaft</em>. Der Untertitel war ernst gemeint. Es waren Bruchstücke aus einer fortlaufenden Arbeit, kein abgeschlossenes System, und ich habe sie bewusst so stehen lassen.</p>

      <p>Die These des Buches lässt sich in zwei Sätzen sagen. Es gibt eine europäische Karmaforschung, deren Anfänge sich bei Lessing, Goethe, Schopenhauer und Rudolf Steiner finden. Und sie ist in der akademischen Welt kaum beachtet worden, unter anderem deshalb, weil sie eine Voraussetzung hat, die sich den üblichen Verfahren der Wissenschaft nicht fügt: meditative Vertiefung.</p>

      <h2>Eine Frage aus dem 18. Jahrhundert</h2>

      <p>Wie früh diese Spur beginnt, zeigt ein kleiner Text von Gotthold Ephraim Lessing, <em>Die Erziehung des Menschengeschlechts</em>. Über weite Strecken handelt er davon, wie die Menschheit als Ganzes durch die Geschichte hindurch lernt. Gegen Ende aber wendet Lessing den Blick vom Geschlecht auf den einzelnen Menschen und stellt im Paragraphen 94 eine schlichte Frage: Warum sollte nicht jeder Einzelne „mehr als einmal auf dieser Welt vorhanden gewesen sein“? Im nächsten Paragraphen fragt er zurück, ob diese Hypothese etwa deshalb lächerlich sei, weil sie die älteste ist.</p>

      <p>Mich berührt an diesen Paragraphen weniger die Antwort als die Form. Lessing verkündet keine Lehre. Er stellt eine Frage, nennt sie eine Hypothese und denkt sie im Zusammenhang mit Lernen und Entwicklung. Darin sehe ich einen Grundzug der europäischen Auseinandersetzung mit dem Thema: Wiederverkörperung nicht als übernommene Überzeugung, sondern als Frage an das eigene Denken.</p>

      <p class="note">Deutung: Dass Lessings fragende Form für die europäische Tradition insgesamt typisch ist, ist meine Lesart und keine belegte Gesamtaussage. Ich werde sie an den einzelnen Autoren prüfen.</p>

      <h2>Eigene Einsicht statt vorgefundener Ordnung</h2>

      <p>Lessings Frage gehört in das Zeitalter der Aufklärung. Wenige Jahre später, im Dezember 1784, bestimmte Immanuel Kant in der <em>Berlinischen Monatsschrift</em> die Aufklärung als „Ausgang des Menschen aus seiner selbst verschuldeten Unmündigkeit“ und forderte dazu auf, sich des eigenen Verstandes zu bedienen. Damit ist ein Anspruch formuliert, der die europäische Moderne nicht mehr loslässt: Erkenntnis soll auf eigener Einsicht beruhen und nicht allein auf Autorität.</p>

      <p>Um 1900 wird dieser Anspruch für viele Menschen zu einer Frage der ganzen Lebensführung. Tradition, die vorgefundene Gesellschaftsordnung und die institutionelle Religion tragen nicht mehr selbstverständlich. Gesucht werden andere Grundlagen – für das Erkennen ebenso wie für die Art, wie man lebt, arbeitet und mit anderen umgeht. Rudolf Steiners <em>Philosophie der Freiheit</em> von 1894 trägt bezeichnenderweise den Untertitel „Grundzüge einer modernen Weltanschauung“ und fragt nach der Freiheit des Menschen von seinem eigenen Denken her.</p>

      <p>In diesem Umfeld gewinnt die Frage nach Wiederverkörperung und Karma eine besondere Gestalt. Sie wird nicht als übernommene Lehre aufgegriffen, sondern als Frage, die der Einzelne an seine eigene Biografie, sein Erkennen und seine Lebensführung richtet. Das ist für mich der Kern dessen, was ich „europäische Karmaforschung“ nenne: der Versuch, Schicksal aus individueller Erkenntnis zu verstehen statt aus Überlieferung.</p>

      <h2>Warum diese Spur so wenig beachtet ist</h2>

      <p>Rudolf Steiner hat 1904 in seiner Schrift <em>Theosophie</em> ein ganzes Kapitel der „Wiederverkörperung des Geistes und Schicksal“ gewidmet. Er argumentiert dort zunächst mit Mitteln des Denkens: Der Mensch sei als geistige Individualität nicht aus Vererbung erklärbar, und das, was er tut, wirke als selbstgeschaffenes Schicksal auf ihn zurück. Zugleich sagt Steiner deutlich, dass das Denken auf diesem Weg nur zu einem Umriss gelangt. Die volle Bestätigung erwartet er von einer Erkenntnis, die durch Schulung erst gewonnen werden muss.</p>

      <p>Hier liegt, so verstehe ich es, der Grund für die Zurückhaltung der Universitäten. Eine Forschung, die von ihren Teilnehmern eine innere Übung verlangt, passt schlecht zu einem Wissenschaftsverständnis, das Ergebnisse unabhängig von der Person des Forschenden überprüfbar machen will. Das muss kein Einwand gegen diese Forschung sein. Es ist aber eine Spannung, die man offen benennen sollte, statt sie zu überspielen.</p>

      <h2>Was sich seither verändert hat</h2>

      <p>Seit dem Buch sind viele Jahre vergangen, und eigene Studien haben meinen Bezugshorizont erweitert. Mein methodischer Ausgangsort ist Rudolf Steiner geblieben – gerade auch dort, wo er karmische Zusammenhänge nicht erklärt, sondern auf der Bühne darstellt: in seinen vier Mysteriendramen, mit denen ich mich als Forscher und langjähriger dramaturgischer Berater seit Jahrzehnten beschäftige (mehr dazu auf <a href="https://mysteriendramen.ch">mysteriendramen.ch</a>). Von dort aus suche ich das Gespräch mit der Seinsphilosophie Martin Heideggers und der Hermeneutik Hans-Georg Gadamers, und mit Peter Sloterdijk frage ich nach der ästhetischen Seite des Themas.</p>

      <p>Daneben gibt es eine empirische Forschung, die es 2012 in meinem Blickfeld kaum gab: die Fallstudien, die der Psychiater Ian Stevenson an der University of Virginia begonnen hat und die dort nach seinem Ruhestand fortgeführt wurden. Sie prüfen Aussagen von Kindern, die sich an ein früheres Leben zu erinnern scheinen, an Dokumenten und Zeugenaussagen. Ich werde diese Arbeiten hier darstellen und einordnen. Meine eigene Methode sind sie nicht.</p>

      <h2>Was hier entstehen soll</h2>

      <p>Diese Seite setzt den früheren Blog in neuer Gestalt fort. Etwa alle zwei Wochen erscheint ein Beitrag: zu einzelnen Autoren und Texten, zu Begriffen und ihrer Geschichte, zu methodischen Fragen. Jeder Beitrag nennt seine Quellen. Wo ich deute oder eine Arbeitshypothese formuliere, kennzeichne ich das.</p>

      <p>Was ich dabei suche, sind Einsichten in eine „höhere“ Erkenntnis, die dennoch reflektiert bleibt: die sich Rechenschaft darüber gibt, woher sie kommt, was sie zeigen kann und wo ihre Grenzen liegen. Weder blosse Spekulation noch ungeprüfte Schau, sondern ein Erkennen, das sich selbst über die Schulter schauen kann.</p>

      <p>Im nächsten Beitrag frage ich, bevor es um einzelne Autoren geht, nach den Voraussetzungen: Welche Arten von Wissen gibt es über Reinkarnation und Karma überhaupt – und auf welchen Ebenen lässt sich so etwas wie Ursache und Wirkung beobachten?</p>

      <hr class="rule">

      <h2>Quellen</h2>
      <ul class="sources">
        <li>Alexander G. Höhne: <em>Europäische Karmaforschung. Fragmente einer Wissenschaft</em>. Books on Demand, 2012, 422 Seiten.</li>
        <li>Gotthold Ephraim Lessing: <em>Die Erziehung des Menschengeschlechts</em> (1777/1780), §§ 93–100. Online: <a href="https://germanhistorydocs.org/de/das-heilige-roemische-reich-1648-1815/ghdi:document-3588">German History in Documents and Images</a>.</li>
        <li>Immanuel Kant: „Beantwortung der Frage: Was ist Aufklärung?“, in: <em>Berlinische Monatsschrift</em>, Dezember 1784. Online: <a href="https://www.uni-siegen.de/infme/start_ifm/downloads/podcast_offene_gesellschaft/kant_aufklaerung.pdf">Universität Siegen (PDF)</a>.</li>
        <li>Rudolf Steiner: <em>Die Philosophie der Freiheit. Grundzüge einer modernen Weltanschauung</em> (1894, GA 4). Online: <a href="https://www.gutenberg.org/ebooks/53493">Project Gutenberg</a>.</li>
        <li>Rudolf Steiner: <em>Theosophie. Einführung in übersinnliche Welterkenntnis und Menschenbestimmung</em> (1904, GA 9), Kapitel „Wiederverkörperung des Geistes und Schicksal“.</li>
        <li>Zu Ian Stevenson und der Fortführung seiner Forschung: <a href="https://psi-encyclopedia.spr.ac.uk/articles/jim-b-tucker/">Psi Encyclopedia, Artikel „Jim B Tucker“</a>.</li>
      </ul>

      <p class="meta"><a href="/blog/">← Alle Beiträge</a></p>
    </article>'''

B2_TITEL = "Wo sich Ursache und Wirkung zeigen"
B2_ANRISS = "Karma fasst Ursache und Wirkung in ein Wort. Über Sinnzusammenhänge, die verborgen sind, über Verstehen statt Erklären – und über die vielen Formen, in denen Wissen über das eigene Leben vorliegt."
B2 = """    <article>
      <div class="meta">11. Oktober 2026 &middot; <span class="tag">Methode</span> &middot; nachträglich veröffentlicht im Oktober 2026</div>
      <h1>Wo sich Ursache und Wirkung zeigen</h1>

      <p>Wer über Karma spricht, spricht über Ursache und Wirkung: Was ich tue, kommt in irgendeiner Form auf mich zurück. So einfach der Satz klingt, so unklar ist, wo dieses Zurückkommen stattfinden soll und wie man es bemerken könnte. Bevor ich mich einzelnen Autoren zuwende, möchte ich deshalb einige Vorfragen ordnen: Was für ein Zusammenhang ist mit dem Wort gemeint? Wie wird er erkannt? Und in welchen Formen liegt Wissen darüber überhaupt vor?</p>

      <h2>Ein Wort für einen Zusammenhang</h2>

      <p>Bemerkenswert ist schon das Wort selbst. Karma fasst Ursache und Wirkung in ein einziges Wort zusammen. Damit ist etwas ausgeklammert, was unser gewohntes Denken über Ursachen bestimmt: die zwingende zeitliche Folge, erst die Ursache, dann die Wirkung. Was das Wort zuerst bezeichnet, ist nicht eine Kette von Ereignissen, sondern ein Zusammenhang, in dem Tat und Schicksal zusammengehören, ohne dass man vorab wissen müsste, was zuerst war.</p>

      <h2>Sinnzusammenhänge entbergen</h2>

      <p>Damit bewegen wir uns auf der Ebene des Sinns. Martin Heidegger hat im Anschluss an die Phänomenologie Edmund Husserls beschrieben, dass wir nicht erst nachträglich Bedeutungen an eine sinnlose Welt herantragen, sondern immer schon in Sinnzusammenhängen stehen. Diese Zusammenhänge erschliessen sich mit der Wahrnehmung. Oft aber sind sie verborgen – das alte, heute verrufene Wort „okkult“ kommt vom lateinischen <em>occultus</em> und bedeutet nichts anderes. Sie müssen durch Reflexion und Unterscheidung erst hervorgeholt werden. Heidegger hat Wahrheit in <em>Sein und Zeit</em> von diesem Hervorholen her gedacht, als Unverborgenheit. In seinem späteren Vortrag <em>Die Frage nach der Technik</em> (1953) nennt er den Vorgang Entbergen.</p>

      <p>Eine Form dieses Entbergens ist die Kunst des Verstehens, wie sie Hans-Georg Gadamer in <em>Wahrheit und Methode</em> (1960) als philosophische Hermeneutik entfaltet hat. Verstehen ist etwas anderes als naturwissenschaftliches Erklären. Die Unterscheidung ist vor allem mit dem Namen Wilhelm Dilthey verbunden, der 1894 das Erklären der Naturwissenschaften vom Verstehen menschlichen Lebens abgehoben hat. Gadamer hat sich ausdrücklich dagegen gewandt, die Geisteswissenschaften nach dem Vorbild der Naturwissenschaften zu formen. Für die Karmafrage heisst das: Ein Schicksalszusammenhang wird nicht erklärt wie ein physikalischer Vorgang, sondern verstanden wie ein Text, in dem man selbst vorkommt.</p>

      <p class="note">Deutung: Die Übertragung von Heideggers Unverborgenheit und Gadamers Verstehen auf die Karmafrage ist meine Lesart. Keiner der beiden hat sich in dieser Weise zu Reinkarnation oder Karma geäussert.</p>

      <h2>Drei Felder bei Steiner</h2>

      <p>Wo aber liegt dieser Zusammenhang? Einen klaren Ausgangspunkt gibt Rudolf Steiner in seiner <em>Theosophie</em> von 1904. Er beschreibt den Menschen als Bürger dreier Welten: Durch den Leib gehört er der physischen Welt an, durch die Seele baut er sich eine eigene Innenwelt auf, und durch den Geist öffnet sich ihm eine Welt, die über beide hinausreicht. Im Kapitel über Wiederverkörperung und Schicksal ordnet Steiner jedem Glied eine eigene Gesetzmässigkeit zu: Der Leib folgt der Vererbung, die Seele dem selbstgeschaffenen Schicksal, das er Karma nennt, der Geist der Wiederverkörperung.</p>

      <table>
        <thead>
          <tr><th>Feld</th><th>Was dort wirkt (nach Steiner)</th><th>Wie es zugänglich wird (meine Zuordnung)</th></tr>
        </thead>
        <tbody>
          <tr><td>Leib</td><td>Vererbung</td><td>Sinne und Naturwissenschaft: Erklären</td></tr>
          <tr><td>Seele</td><td>selbstgeschaffenes Schicksal, Karma</td><td>Rückblick auf die eigene Biografie: Verstehen</td></tr>
          <tr><td>Geist</td><td>Wiederverkörperung</td><td>nach Steiner erst durch höhere Erkenntnis</td></tr>
        </tbody>
      </table>

      <p class="note">Die beiden ersten Spalten folgen Steiners Kapitel; die dritte Spalte ist meine Zuordnung und als Arbeitshypothese gemeint.</p>

      <h2>Stufen des Erkennens</h2>

      <p>Für den Weg in dieses dritte Feld hat Steiner Stufen des Erkennens beschrieben, in Aufsätzen, die 1905 in der Zeitschrift <em>Lucifer-Gnosis</em> erschienen und später als <em>Die Stufen der höheren Erkenntnis</em> (GA 12) gesammelt wurden. Die gewöhnliche Erkenntnis lebt von Sinneseindruck, Bild, Begriff und dem Ich, das alles zusammenhält. In der Imagination fallen die Sinneseindrücke weg, und es bleiben Bilder, die keinem äusseren Gegenstand entstammen. In der Inspiration treten auch die Bilder zurück; die geistige Welt wird eher wie eine Sprache vernommen. In der Intuition bleibt nur das Ich, das nicht mehr von aussen betrachtet, sondern in den Dingen selbst lebt. Das Denken, so Steiner in der <em>Theosophie</em>, kann den Gedanken wiederholter Erdenleben fassen, gelangt aber nur zu einem Umriss; dessen Anschauung setzt die höheren Stufen voraus.</p>

      <h2>Viele Formen des Wissens</h2>

      <p>Nicht alles Wissen liegt in naturwissenschaftlicher Form vor, und vieles kann es gar nicht. Wer über Reinkarnation und Karma nachdenkt, hat es mit sehr verschiedenen Wissensbeständen zu tun, die oft vermischt werden, obwohl sie Verschiedenes leisten:</p>

      <ul>
        <li><strong>Empirisches Wissen:</strong> etwa die Fallstudien Ian Stevensons, die Aussagen mit Dokumenten vergleichen. Sie können Übereinstimmungen feststellen, nicht aber einen Sinnzusammenhang verstehen.</li>
        <li><strong>Historisches Wissen:</strong> Daten, Quellen, Lebensläufe – auch über die Geschichte des Reinkarnationsgedankens selbst.</li>
        <li><strong>Kulturelles und spontanes Wissen:</strong> Legenden, Mythen und Überlieferungen, die Bilder bereithalten, lange bevor jemand sie begrifflich prüft.</li>
        <li><strong>Philosophisches Wissen:</strong> die Frage, ob eine Vorstellung in sich stimmig ist – so wie Lessing in der <em>Erziehung des Menschengeschlechts</em> fragt.</li>
        <li><strong>Narratives Wissen:</strong> Unsere Lebensführung wird nicht nur von Informationen geprägt, sondern von den Geschichten gesteuert und entwickelt, die wir über uns selbst erzählen.</li>
        <li><strong>Performatives und exploratives Wissen:</strong> Wissen, das sich im Vollzug zeigt, auf der Bühne oder im Ritual, und Wissen, das erst in einer Erkundung entsteht.</li>
        <li><strong>Meditatives Wissen:</strong> der Weg, den Steiner beschreibt. Er beansprucht, das Feld selbst anschauen zu können, ist aber an die Schulung desjenigen gebunden, der erkennt.</li>
      </ul>

      <p class="note">Arbeitshypothese: Diese Gliederung ist mein Vorschlag zur Ordnung des Feldes und findet sich so bei keinem der genannten Autoren.</p>

      <h2>Wann die Lehre Bedeutung hat</h2>

      <p>Aus alldem ziehe ich eine Folgerung, die für diese Seite massgeblich ist. Die Lehre von Reinkarnation und Karma ist nicht schon deshalb bedeutsam, weil sie alt ist oder weil viele Menschen sie vertreten. Bedeutung gewinnt sie nur dort, wo sie Erfahrung informiert oder differenziert – wo sie hilft, das eigene Leben genauer wahrzunehmen – und wo sie zu einer Erweiterung oder Vertiefung des Horizonts beitragen kann. Das Wort Horizont nehme ich dabei bewusst aus Gadamers Hermeneutik auf.</p>

      <p>Auch die Art von Erkenntnis, die ich hier suche, ist damit umrissen. Sie darf „höher“ sein als das gewöhnliche Erkennen, im Sinne der Stufen, die Steiner beschreibt. Sie muss aber reflektiert bleiben: Sie soll angeben können, in welchem Feld und aus welchem Wissensbestand eine Aussage stammt, und sie soll den Unterschied zwischen Anschauung, Deutung und Begriff nicht verwischen.</p>

      <p>Eine besondere Form des performativen Wissens ist das Theater. Wie Steiner karmische Zusammenhänge nicht nur beschrieben, sondern auf die Bühne gebracht hat, ist das Thema des nächsten Beitrags: Karma in den Mysteriendramen.</p>

      <hr class="rule">

      <h2>Quellen</h2>
      <ul class="sources">
        <li>Rudolf Steiner: <em>Theosophie. Einführung in übersinnliche Welterkenntnis und Menschenbestimmung</em> (1904, GA 9), Kapitel „Das Wesen des Menschen“ und „Wiederverkörperung des Geistes und Schicksal“. Englische Übersetzung online: <a href="https://www.rsarchive.org/Books/GA009/English/RSP1965/GA009_c02.html">Rudolf Steiner Archive</a>.</li>
        <li>Rudolf Steiner: <em>Die Stufen der höheren Erkenntnis</em> (GA 12), zuerst 1905 in <em>Lucifer-Gnosis</em>. Englische Übersetzung online: <a href="https://rsarchive.org/Books/GA012/English/AP1967/GA012_c01.html">Rudolf Steiner Archive</a>.</li>
        <li>Martin Heidegger: <em>Sein und Zeit</em> (1927), bes. § 44 zur Wahrheit als Unverborgenheit. Überblick: <a href="https://www.cambridge.org/core/books/abs/heideggers-being-and-time/truth/147E417B48F848BD74FC5E49D1D3CCFA">Cambridge University Press, Kapitel „Truth“</a>.</li>
        <li>Martin Heidegger: <em>Die Frage nach der Technik</em> (Vortrag 1953). Überblick: <a href="https://charlesreid1.com/wiki/The_Question_Concerning_Technology">„The Question Concerning Technology“</a>.</li>
        <li>Hans-Georg Gadamer: <em>Wahrheit und Methode. Grundzüge einer philosophischen Hermeneutik</em> (1960). Überblick: <a href="https://en.wikipedia.org/wiki/Truth_and_Method">Wikipedia, „Truth and Method“</a>.</li>
        <li>Wilhelm Dilthey: <em>Ideen über eine beschreibende und zergliedernde Psychologie</em> (1894). Zur Unterscheidung von Erklären und Verstehen: <a href="https://plato.stanford.edu/entries/dilthey">Stanford Encyclopedia of Philosophy, „Wilhelm Dilthey“</a>.</li>
        <li>Gotthold Ephraim Lessing: <em>Die Erziehung des Menschengeschlechts</em> (1777/1780), §§ 93–100. Online: <a href="https://germanhistorydocs.org/de/das-heilige-roemische-reich-1648-1815/ghdi:document-3588">German History in Documents and Images</a>.</li>
        <li>Zu Ian Stevenson: <a href="https://psi-encyclopedia.spr.ac.uk/articles/jim-b-tucker/">Psi Encyclopedia, Artikel „Jim B Tucker“</a>.</li>
      </ul>

      <p class="meta"><a href="/blog/">← Alle Beiträge</a></p>
    </article>"""

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
if "2026-09-27-europaeische-karmaforschung" not in s:
    marker = "      <!-- Neueste Beiträge: wird bei jedem neuen Post oben ergänzt (max. 5) -->\n"
    assert marker in s
    s = s.replace(marker, marker + liste_start)
    s = s.replace('    <p class="meta" id="noch-keine">Der erste Beitrag erscheint am 25. Oktober 2026.</p>\n', '')
    p.write_text(s)

p = root/"blog"/"index.html"; s = p.read_text()
if "2026-09-27-europaeische-karmaforschung" not in s:
    marker = "      <!-- Neuester Beitrag zuoberst; beim Hinzufügen eines neuen Posts hier einen <li>-Block einfügen -->\n"
    assert marker in s
    p.write_text(s.replace(marker, marker + liste_blog))
