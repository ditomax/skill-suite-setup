# Start — Skill-Suite für {{customer}}

Sie haben eine ZIP-Datei und diese Seite erhalten. Das ZIP enthält eine Planungsstruktur und die KI-Skill-Suite **{{skillsets_list}}** (die genauen Versionen stehen nach dem Entpacken in `planning/suite/VERSION`). Es wird nichts installiert: es sind Textdateien, die Ihre KI-Anwendung liest, sobald Sie den Ordner öffnen.

## 1. Entpacken

Entpacken Sie das ZIP in Ihren Projektordner — ein neuer leerer Ordner oder ein bestehendes Projekt. Ergebnis: ein Ordner `planning/` und zwei kurze Dateien `AGENTS.md` und `CLAUDE.md` auf oberster Ebene. Gibt es in Ihrem Projekt schon eine `AGENTS.md` oder `CLAUDE.md`, hängen Sie den Inhalt der ZIP-Datei an Ihre an, statt sie zu ersetzen (der Block hat fünf Zeilen und sagt nur „lies planning/AGENTS.md").

## 2. Ordner in der KI-Anwendung öffnen

{{platform_hint}}

Für Ideensammlung und Maquetten genügt es, `planning/` zu öffnen. Für build (Produktentwicklung) öffnen Sie den Projektordner selbst, weil der Code neben `planning/` entsteht, nicht darin.

## 3. „start" tippen

Die KI liest die Regeln aus dem Ordner, sagt Ihnen, wo die Arbeit steht und was als Nächstes kommt, und fragt nach jedem Schritt: **weiter**, **nochmal** oder **stopp**. Andere Befehle gibt es nicht. Sie können jederzeit aufhören — alles bleibt als lesbare Textdateien in `planning/` und geht beim nächsten Mal mit **weiter** weiter.

## Update

Wenn Sie ein neueres ZIP erhalten, drei Schritte — es wird nie etwas gelöscht, und Ihre Arbeit in `planning/idea`, `planning/maquette` und `planning/build` wird nicht berührt:

1. Verschieben Sie `planning/suite` und `planning/profile` nach `planning/_archive/` (z. B. `_archive/2026-10-01-suite-v1`).
2. Entpacken Sie das neue ZIP **an einer anderen Stelle** (Doppelklick im Finder/Explorer legt einen neuen Ordner an) und schieben Sie dessen Ordner `planning/suite` und `planning/profile` in Ihr `planning/`. Im Terminal tut `unzip -n <zip>` im Projektordner dasselbe und überschreibt nie etwas.
3. Fertig. `planning/suite/VERSION` zeigt die neue Version.

Oder geben Sie das ZIP der KI und sagen „update“; sie kennt diese Regel.

Änderungen an Ihrem Profil (Vorgaben, Fragen, Design) laufen über {{contact}} — sie kommen als neues ZIP zurück.

## Fragen

{{contact}}
