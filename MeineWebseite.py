from WebseitenBuilder import bauen, text, bild, video, titel, icon, hintergrundbild, hintergrundfarbe, \
     verschieben_nach_unten, verschieben_nach_rechts, textgroesser, farbe, textdicker, verschieben_nach_oben, \
     verschieben_nach_links, schmaler, tiefer

titel("Programmieren einer eigenen Webseite")
hintergrundbild("https://img.freepik.com/fotos-premium/der-gruene-code-machte-das-programmieren-zu-einem-dunklen-hintergrund_250994-1553.jpg")
hintergrundfarbe("#A2D2FF")
icon("https://static.vecteezy.com/system/resources/previews/023/736/519/non_2x/programmer-icon-image-suitable-for-mobile-apps-web-apps-and-print-media-vector.jpg")

text("Station: Programmieren einer eigenen Webseite")
textgroesser()
textgroesser()
textdicker()
verschieben_nach_rechts(20)
farbe("#cc1d0a")

text("Was kannst du hier machen?")
textgroesser()
textdicker()
farbe("#a712c4")
verschieben_nach_unten(100)
verschieben_nach_rechts(20)


bild("https://img.freepik.com/fotos-kostenlos/grunge-schwarzer-beton-strukturierter-hintergrund_53876-124541.jpg")
schmaler()
schmaler()
tiefer()
tiefer()
tiefer()
tiefer()
verschieben_nach_unten(200)

text("Du kannst hier deine eigene Webseite erstellen. Dazu kannst du Texte, Bilder und Videos einfügen.<br>"
     "Du kannst auch die Farben und die Größe der Schrift ändern.<br><br>"
     "Um Text einzufügen musst das folgendermaßen machen:<br>"
     "text(\"Hier steht dein Text\")<br><br>"
     "Um ein Bild einzufügen musst du folgendes machen:<br>"
     "bild(\"Link des Bildes\")<br><br>"
     "Um ein Video einzufügen musst du folgendes machen:<br>"
     "video(\"Link des Videos\")<br><br>"
     "Um den Titel zu ändern musst du folgendes machen:<br>"
     "titel(\"Hier steht dein Titel\")<br><br>")
verschieben_nach_unten(200)
verschieben_nach_rechts(20)
textdicker()
textdicker()
farbe("#fff")

text('Mehr Funktionen findest du hier: <a href="https://github.com/fweigel-dev/Girls-and-Boys-Day-2024">https://github.com/fweigel-dev/Girls-and-Boys-Day-2024</a>')
verschieben_nach_unten(600)
verschieben_nach_rechts(20)
farbe("#ffff00")

bauen()
