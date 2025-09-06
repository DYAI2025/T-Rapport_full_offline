# TransRapport - Benutzerhandbuch

*Eine Schritt-für-Schritt Anleitung für Therapeuten und Anwender*

---

## Was ist TransRapport?

TransRapport ist ein intelligenter Assistent für Therapiegespräche. Es analysiert sowohl **Präsenz-Sitzungen** als auch **Online-Gespräche** (Zoom, Teams, Skype) und erkennt automatisch wichtige Momente - wie emotionale Veränderungen, Pausen oder therapeutische Durchbrüche.

### 🌐 Online-Therapie & Video-Konferenzen
**Revolutionär für Remote-Therapie**: TransRapport erfasst **System-Audio direkt vom Computer** - kein zusätzliches Mikrofon zwischen Personen nötig! Die Desktop-App (Windows/macOS) zapft virtuelle Audio-Loopbacks an und analysiert beide Gesprächspartner in Echtzeit.

**🔒 Datenschutz durch Einfachheit**: TransRapport bleibt **immer offline** - egal ob Präsenz-Gespräch oder Online-Konferenz. Alle Audio-Daten werden nur lokal verarbeitet und gespeichert. **Uns ist egal, woher das Audio kommt** - Hauptsache es bleibt bei TransRapport auf Ihrem Computer!

## Schnellstart in 3 Schritten

### 1. 🎯 System starten
- Öffnen Sie das TransRapport-Symbol auf Ihrem Desktop
- Warten Sie, bis "System bereit" angezeigt wird
- Das dauert beim ersten Start etwa 1-2 Minuten

### 2. 🎙️ Sitzung beginnen
**Für Präsenz-Gespräche:**
- Klicken Sie auf den großen **"Start"** Button  
- Sprechen Sie normal - das System hört automatisch zu

**Für Online-Gespräche (Zoom/Teams/Skype):**
- Starten Sie Ihre Video-Konferenz wie gewohnt
- Klicken Sie in TransRapport auf **"System-Audio erfassen"**
- Das Tool erfasst automatisch beide Audio-Streams (Ein- und Ausgang)
- Beobachten Sie die Live-Transkription beider Sprecher

### 3. 📋 Sitzung beenden
- Klicken Sie auf **"Stop"** wenn das Gespräch zu Ende ist
- Ihre Analyse wird automatisch gespeichert
- Laden Sie den Bericht als PDF herunter

---

## Die Benutzeroberfläche verstehen

### Hauptbildschirm

```
┌─────────────────────────────────────────────────────┐
│                 TransRapport                        │
├─────────────────────────────────────────────────────┤
│ 🎙️ Präsenz   🌐 Online   ⏸️ Pause   ⏹️ Stop   📁 Datei │
├─────────────────────────────────────────────────────┤
│ Audio-Quelle: 🔗 System-Audio (Zoom erfasst)       │
│ Modus: 📊 Vollanalyse + LLM                        │
├─────────────────────────────────────────────────────┤
│  📝 Live-Transkription:                            │
│  👨‍⚕️ Therapeut: "Wie geht es Ihnen heute?"          │
│  👤 Klient: "Ich fühle mich etwas besser als       │
│       letzte Woche. Die Übungen haben geholfen..." │
├─────────────────────────────────────────────────────┤
│  🏷️ Erkannte Muster:                               │
│  • Positive Veränderung (85%) - SEM_POSITIVE_FUTURE│
│  • Lange Pause (12 Sek.) - ATO_PAUSE_LONG         │
│  • Zögernde Sprechweise - ATO_HESITATION_VOICE    │
└─────────────────────────────────────────────────────┘
```

### 🎛️ Die 3 Analyse-Modi

TransRapport bietet **drei verschiedene Analyse-Tiefen** - wählen Sie je nach Bedarf und Rechenleistung:

#### **Modus 1: 📝 Nur Transkription**
- **Schnell & ressourcenschonend** - läuft auf jedem Computer
- **Live-Transkription** mit Sprecher-Erkennung 
- **Einfacher Export** als TXT oder DOCX
- **Ideal für**: Einfache Dokumentation, schwächere Computer

#### **Modus 2: 🎯 Transkription + Marker + Kurzreport**  
- **Standardmodus** - optimales Preis-Leistungs-Verhältnis
- **152 therapeutische Marker** in Echtzeit
- **Automatischer Kurzreport** mit wichtigsten Erkenntnissen
- **Prosody-Analyse** (Tonfall, Pausen, Emotionen)  
- **Ideal für**: Reguläre Therapiesitzungen, professionelle Nutzung

#### **Modus 3: 🤖 Vollanalyse + lokales LLM**
- **Maximum-Analyse** - benötigt leistungsstarken Computer
- **Alles aus Modus 2** + zusätzlich:
- **Lokales LLM** für detaillierte Interpretationen
- **Therapeutische Empfehlungen** und Interventions-Vorschläge
- **Tiefere Muster-Analyse** und Verlaufs-Prognosen
- **Ideal für**: Supervision, Forschung, komplexe Fälle

### Was bedeuten die Farben?

| Farbe | Bedeutung | Beispiel |
|-------|-----------|----------|
| 🟢 **Grün** | Positive Entwicklung | Einsichten, Fortschritte |
| 🟡 **Gelb** | Neutrale Beobachtung | Pausen, Füllwörter |  
| 🔴 **Rot** | Attention needed | Starke Emotionen, Blockaden |
| 🔵 **Blau** | Technische Info | Sprecher-Wechsel, Audio-Qualität |

---

## Schritt-für-Schritt Anleitungen

### 🎙️ Präsenz-Sitzung durchführen

#### Vorbereitung (2 Minuten)
1. **Computer einschalten** und TransRapport öffnen
2. **Mikrofon testen**: Sprechen Sie kurz - sehen Sie Wellenlinien?
3. **Platz arrangieren**: Mikrofon zwischen Therapeut und Klient
4. **Ruhe schaffen**: Handy stumm, Türe zu

#### Sitzung starten (30 Sekunden)
1. **"Präsenz" Modus wählen** - für lokales Mikrofon
2. **"Start" klicken** - der Button wird zu einem pulsierenden Kreis
3. **Normal sprechen** - das System passt sich automatisch an
4. **Transkription beobachten** - Text erscheint mit 2-3 Sekunden Verzögerung

### 🌐 Online-Sitzung durchführen (Zoom/Teams/Skype)

#### Vorbereitung (3 Minuten)
1. **TransRapport Desktop-App starten** (Windows/macOS)
2. **Video-Konferenz vorbereiten** (Zoom/Teams/Skype)
3. **Audio-Setup prüfen**: Kopfhörer empfohlen für saubere Trennung
4. **System-Audio aktivieren**: Virtueller Audio-Driver wird automatisch installiert

#### Online-Sitzung starten (1 Minute)
1. **"Online" Modus wählen** - für System-Audio Erfassung
2. **Konferenz-Typ auswählen**: Zoom, Teams, Skype oder "Automatisch erkennen"
3. **"System-Audio erfassen" klicken** - beide Audio-Streams werden erfasst
4. **Ihre Videokonferenz normal starten** - TransRapport läuft im Hintergrund
5. **Live-Transkription beider Sprecher beobachten** - automatische Sprecher-Trennung

#### Während der Online-Sitzung (laufend)
- **Normale Videokonferenz führen** - TransRapport arbeitet unsichtbar im Hintergrund
- **Keine spezielle Software in der Konferenz** - kein Bot oder Plugin nötig
- **Beide Audio-Streams werden erfasst** - Ihr Mikrofon + Lautsprecher/Kopfhörer
- **Live-Analyse läuft parallel** - STT, Marker-Erkennung, Sprecher-ID in Echtzeit
- **Bei Problemen**: "Pause" klicken, Audio-Quelle neu wählen, "Start" klicken

#### Sitzung beenden (1 Minute)
1. **"Stop" klicken** - Aufnahme wird beendet
2. **Kurz warten** - "Analyse wird erstellt..." 
3. **Ergebnisse ansehen** - automatische Zusammenfassung
4. **Speichern** - "Bericht herunterladen" klicken

### 📁 Bestehende Aufnahme analysieren

#### Audiodatei vorbereiten
- **Formate**: WAV, MP3, M4A (bis 2 Stunden)
- **Qualität**: Normale Diktiergerät-Qualität reicht
- **Größe**: Bis zu 500 MB

#### Upload und Analyse
1. **"Datei auswählen"** klicken
2. **Audiodatei auswählen** aus Ihren Dokumenten
3. **"Analysieren"** klicken
4. **Warten** - je nach Länge 2-10 Minuten
5. **Ergebnisse ansehen** - wie bei Live-Sitzung

---

## Die Analyseergebnisse verstehen

### 📊 Sitzungsübersicht

```
Sitzung vom 06.09.2025, 14:30-15:20 (50 Min.)
═══════════════════════════════════════════════

👥 Sprecher:
• Therapeut: 22 Minuten (44%)
• Klient: 28 Minuten (56%)

🎯 Wichtige Momente:
• 3 emotionale Durchbrüche
• 7 längere Pausen (>5 Sek.)
• 2 Lachmomente
• 1 therapeutische Einsicht

📈 Gesprächsdynamik:
• Positive Entwicklung: 78%
• Offenheit: 82%  
• Widerstand: 23%
```

### 🏷️ Marker-Typen erklärt

#### **Emotionale Marker**
- **Freude/Lachen**: Positive Momente, Humor
- **Trauer/Seufzer**: Schwere Themen, Verlust
- **Angst/Zögern**: Unsicherheit, Vermeidung
- **Wut/Intensität**: Konflikte, Frustration

#### **Gesprächs-Marker** 
- **Lange Pausen**: Nachdenkpausen, Verarbeitung
- **Unterbrechungen**: Ungeduld, Aufregung
- **Füllwörter**: Unsicherheit, Suchbewegung
- **Sprechtempo**: Aufregung (schnell) vs. Depression (langsam)

#### **Therapeutische Marker**
- **Einsichten**: "Aha-Momente" des Klienten
- **Widerstand**: Vermeidung, Ablehnung
- **Übertragung**: Projektionen auf Therapeut
- **Fortschritt**: Positive Veränderungen

#### **Beziehungs-Marker**
- **Therapeutische Allianz**: Vertrauen, Zusammenarbeit
- **Macht-Dynamik**: Dominanz, Unterwerfung  
- **Empathie**: Verstehen, Mitgefühl
- **Grenzen**: Professionalität, Abgrenzung

---

## Praktische Tipps

### 🎙️ Optimale Audio-Qualität

#### Präsenz-Sitzungen: Mikrofon-Setup
- **Position**: 50-100 cm von beiden Sprechern entfernt
- **Höhe**: Auf Tischhöhe, nicht versteckt
- **Richtung**: Zu beiden Sprechern hin orientiert
- **Test**: Kurz sprechen und Pegel prüfen

#### Online-Sitzungen: System-Audio Setup
- **Kopfhörer verwenden**: Verhindert Audio-Feedback und Echo
- **Gute Internet-Verbindung**: Für stabile Audio-Qualität in der Konferenz
- **Audio-Einstellungen**: Automatische Rauschunterdrückung aktivieren
- **Test vor Sitzung**: "System-Audio Test" in TransRapport durchführen

#### 🔧 Technische Komponenten (Echtzeitverarbeitung)

**STT-Engine (Sprache → Text)**:
- **Whisper-CT2**: Optimiert für deutsche Sprache, läuft offline
- **Latenz**: <200ms für Live-Transkription  
- **Genauigkeit**: 94%+ bei guter Audio-Qualität

**ProSADi (Prosody-Analyse)**:
- **Tonfall-Erkennung**: Pitch, Intensität, Rhythmus
- **Emotions-Detektion**: Aus Audio-Features, nicht aus Text
- **Pause-Analyse**: Micro-Pausen bis längere Denkpausen

**Marker-Engine**: 
- **152 therapeutische Marker** aus LEAN.DEEP 3.4 Schema
- **Echtzeit-Matching**: Pattern-Recognition während des Sprechens
- **Multi-Modal**: Text + Audio + Prosody gleichzeitig

**Sprecher-Erkennung (SID)**:
- **ECAPA-TDNN**: State-of-the-art Speaker Identification
- **Automatische Trennung**: Therapeut vs. Klient(en)  
- **Enrollment**: Lernt Stimmen in den ersten 30 Sekunden

#### Raum-Akustik (bei Präsenz-Sitzungen)
- **Ruhig**: Klimaanlage, Handy, Straßenlärm minimieren
- **Weich**: Teppich, Vorhänge reduzieren Hall
- **Geschlossen**: Türe zu, "Nicht stören" Schild
- **Backup**: Bei wichtigen Sitzungen zusätzliches Diktiergerät

### 💻 Computer-Performance

#### Vor der Sitzung
- **Andere Programme schließen** (Email, Browser, Musik)
- **Festplatte**: Mindestens 2 GB freier Speicher
- **Stromkabel**: Bei Laptop immer anschließen  
- **Updates**: Nicht während Therapiezeiten

#### Während der Sitzung
- **Bildschirm**: Kann zugeklappt werden nach dem Start
- **Maus/Tastatur**: Nicht berühren - läuft automatisch
- **WLAN**: Ist nicht nötig - System arbeitet offline

### 📋 Dokumentation und Berichte

#### Automatische Berichte
Das System erstellt automatisch:
- **Transkript**: Wortgetreue Mitschrift  
- **Marker-Liste**: Alle erkannten Muster
- **Zeitachse**: Chronologischer Verlauf
- **Statistiken**: Sprecher-Anteile, Emotionen
- **Zusammenfassung**: Wichtigste Erkenntnisse

#### Manuelle Notizen hinzufügen
1. **Während der Sitzung**: Notizen auf Papier
2. **Nach der Sitzung**: In Kommentarfeld eintragen
3. **Beim Speichern**: Zusätzliche Beobachtungen ergänzen
4. **Für Verlauf**: Tags vergeben (z.B. "Durchbruch", "Krise")

---

## Datenschutz und Sicherheit

### 🔒 Ihre Daten bleiben bei Ihnen

#### Vollständig Offline - Einfach & Sicher
- **TransRapport ist immer offline** - egal ob Präsenz oder Online-Gespräche
- **Audio-Quelle ist irrelevant** - Mikrofon oder System-Audio, alles bleibt lokal
- **Keine Internet-Verbindung nötig** - weder für Analyse noch für Speicherung
- **Alle Daten bleiben bei Ihnen** - verschlüsselt auf Ihrem Computer
- **Keine Cloud, kein Upload, keine Übertragung** - niemals, nirgendwohin

**🎯 Datenschutz-Prinzip**: Wir machen es uns einfach - TransRapport "weiß" nicht mal, dass es Online-Gespräche gibt. Es verarbeitet nur lokales Audio und speichert nur lokal. Fertig.

#### Daten-Management
- **Speicherort**: `/TransRapport/Sitzungen/`
- **Format**: Verschlüsselte JSON-Dateien
- **Backup**: Auf externe Festplatte kopieren
- **Löschen**: Dateien sicher überschreiben

#### DSGVO-Konformität - Einfach durch Offline-First
- **Einverständnis**: Klienten über Aufzeichnung informieren (gilt für alle Modi)
- **Zweckbindung**: Nur für therapeutische Zwecke nutzen
- **Löschfristen**: Nach Behandlungsende archivieren/löschen
- **Zugriff**: Nur autorisierte Personen
- **Audio-Quelle irrelevant**: TransRapport ist immer datenschutzkonform - egal ob Mikrofon, System-Audio oder Online-Konferenz
- **Keine zusätzlichen Risiken**: Online-Modus ändert nichts am Datenschutz-Level von TransRapport

### 🛡️ Sicherheits-Checkliste

#### Computer-Sicherheit
- [ ] **Passwort-Schutz** für Benutzer-Konto
- [ ] **Bildschirmsperre** nach 10 Minuten Inaktivität  
- [ ] **Antivirus** aktuell und aktiv
- [ ] **Firewall** aktiviert
- [ ] **Automatische Updates** für Sicherheits-Patches

#### Praxis-Sicherheit
- [ ] **Bildschirm** nicht einsehbar für Wartende
- [ ] **Dateien** nicht auf Desktop/öffentlichen Ordnern
- [ ] **USB-Sticks** verschlüsselt für Backup
- [ ] **Weitergabe** nur mit Klienten-Einverständnis
- [ ] **Entsorgung** alter Computer professionell

---

## Häufige Fragen (FAQ)

### 🤔 Allgemeine Fragen

**F: Wie genau ist die Spracherkennung?**
A: Bei guter Audioqualität 85-95% korrekt. Dialekte und Fremdwörter können Fehler verursachen.

**F: Versteht das System verschiedene Sprachen?**  
A: Aktuell Deutsch und Englisch. Weitere Sprachen auf Anfrage.

**F: Kann ich das System anpassen?**
A: Ja - Empfindlichkeit, Marker-Typen und Berichte sind konfigurierbar.

**F: Wie lange dauert die Analyse?**
A: Live-Analyse in Echtzeit. Datei-Analyse: ca. 1/4 der ursprünglichen Länge.

### 🔧 Technische Fragen  

**F: Welche Computer-Anforderungen gibt es?**
A: Windows 10/Mac OS 10.15+, 8GB RAM, 5GB Speicher. Für Online-Modus: Virtuelle Audio-Driver (automatisch installiert).

**F: Funktioniert es ohne Internet?**
A: Ja, komplett offline. TransRapport braucht nie Internet - weder für Präsenz noch für "Online"-Gespräche. Das Audio wird immer nur lokal verarbeitet, egal woher es kommt.

**F: Kann ich mehrere Sitzungen parallel aufnehmen?**
A: Eine Live-Sitzung pro Computer. Datei-Analysen können parallel laufen.

**F: Was passiert bei Computer-Absturz?**
A: Auto-Save alle 30 Sekunden. Daten gehen nicht verloren.

### 🌐 Online-Therapie Fragen

**F: Funktioniert es mit allen Video-Konferenz-Tools?**
A: Ja - Zoom, Microsoft Teams, Skype, Google Meet, WebEx und andere. System-Audio Erfassung ist universal.

**F: Merken die anderen Teilnehmer etwas davon?**
A: Nein - TransRapport läuft komplett im Hintergrund. Kein Bot in der Konferenz, keine Plugins nötig.

**F: Wird die Audio-Qualität der Konferenz beeinflusst?**
A: Nein - TransRapport "hört nur zu" über virtuelle Audio-Loopbacks. Die Konferenz läuft normal weiter. TransRapport ist für Zoom/Teams unsichtbar.

**F: Was ist mit Gruppen-Gesprächen?**  
A: Bis zu 5 Sprecher werden automatisch erkannt und getrennt dargestellt.

**F: Kann ich Breakout-Rooms in Zoom analysieren?**
A: Ja - TransRapport erfasst automatisch den aktiven Audio-Stream, auch bei Raum-Wechseln.

### 👩‍⚕️ Therapeutische Fragen

**F: Ersetzt das System meine Notizen?**
A: Nein, es ergänzt Ihre professionelle Dokumentation.

**F: Lenkt die Technik ab?**
A: Nach 2-3 Sitzungen vergessen die meisten das System.

**F: Was mache ich mit den Erkenntnissen?** 
A: Nutzen Sie sie für Supervision, Verlaufsdokumentation und Selbstreflexion.

**F: Können Klienten die Ergebnisse sehen?**
A: Nur wenn Sie es teilen. Sie haben vollständige Kontrolle.

**F: Ist TransRapport bei Online-Gesprächen auch DSGVO-konform?**
A: **Ja, absolut!** TransRapport selbst ist immer offline, egal woher das Audio kommt. Wir speichern nur lokal - ob das Audio vom Mikrofon oder aus Zoom kommt, ist für den Datenschutz irrelevant. **Einfach = sicher.**

---

## Problemlösung

### 🚨 Wenn etwas nicht funktioniert

#### **Problem**: Mikrofon wird nicht erkannt
```
🔧 Lösungsschritte:
1. Mikrofon-Kabel prüfen
2. Windows: Geräte-Manager → Audio
3. Mac: Systemeinstellungen → Ton → Eingabe  
4. TransRapport neu starten
5. Computer neu starten
```

#### **Problem**: Schlechte Spracherkennung
```
🔧 Lösungsschritte:  
1. Näher zum Mikrofon sprechen
2. Hintergrundgeräusche reduzieren
3. Deutlicher artikulieren (nicht lauter!)
4. Mikrofon-Position anpassen
5. Audioqualität in Einstellungen erhöhen
```

#### **Problem**: System läuft langsam
```
🔧 Lösungsschritte:
1. Andere Programme schließen
2. Computer neu starten  
3. Festplatte aufräumen (>2GB frei)
4. Energieeinstellungen: "Höchstleistung"
5. IT-Support kontaktieren
```

#### **Problem**: Marker werden nicht erkannt
```
🔧 Lösungsschritte:
1. Empfindlichkeit erhöhen (Einstellungen)
2. Längere Gesprächsabschnitte abwarten
3. Verschiedene Marker-Profile testen
4. Kalibrierung durchführen
5. Update prüfen
```

#### **Problem**: Online-Audio wird nicht erfasst
```
🔧 Lösungsschritte:
1. Audio-Berechtigungen prüfen (macOS/Windows)
2. Virtueller Audio-Driver neu installieren
3. Konferenz-Audio testen (sprechen Sie in Zoom)
4. "Audio-Quelle" in TransRapport neu wählen
5. Computer neu starten, dann Konferenz neu starten
```

#### **Problem**: Nur eine Seite wird transkribiert  
```
🔧 Lösungsschritte:
1. Kopfhörer verwenden (nicht Lautsprecher)
2. Audio-Einstellungen: "Stereo Mix" aktivieren
3. Konferenz-Einstellungen: "Original Sound" aktivieren
4. TransRapport: "Beide Kanäle erfassen" wählen
5. Audio-Test mit Freund/Kollege durchführen
```

#### **Problem**: Echo oder doppelte Transkription
```
🔧 Lösungsschritte:  
1. Kopfhörer verwenden (nie Lautsprecher bei Online-Sitzungen)
2. Echo-Unterdrückung in Konferenz-Software aktivieren
3. TransRapport: "Echo-Filter" aktivieren
4. Mikrofon-Pegel in Konferenz reduzieren
5. Bei hartnäckigem Echo: "Nur Mikrofon erfassen" wählen
```

### 📞 Support kontaktieren

Bei anhaltenden Problemen:

**Email**: support@transrapport.de  
**Telefon**: +49 (0)123 456789 (Mo-Fr, 9-17 Uhr)  
**Remote-Hilfe**: Nach Terminvereinbarung  

**Bitte bereithalten:**
- Fehlermeldung (Screenshot)  
- Computer-Details (Windows/Mac, Version)
- TransRapport-Version (Über → Info)
- Beschreibung: Was haben Sie gemacht, was ist passiert?

---

## Erste Schritte - 7-Tage-Plan

### Tag 1: Installation und Setup ⚙️
- [ ] Software installieren
- [ ] Mikrofon anschließen und testen
- [ ] Kurze Test-Aufnahme (2 Minuten)
- [ ] Ergebnis ansehen und verstehen

### Tag 2: Erste Präsenz-Sitzung 🎯  
- [ ] Mit vertrauter Person üben (Freund/Kollege)
- [ ] 15-20 Minuten normales Gespräch im Präsenz-Modus
- [ ] System ignorieren, natürlich sprechen
- [ ] Bericht gemeinsam durchgehen

### Tag 3: Online-Sitzung testen 🌐
- [ ] Zoom/Teams-Testanruf mit Freund/Kollege
- [ ] Online-Modus in TransRapport ausprobieren
- [ ] System-Audio Erfassung testen (beide Seiten hörbar?)
- [ ] Verschiedene Analyse-Modi (1, 2, 3) vergleichen

### Tag 4: Einstellungen anpassen 🔧
- [ ] Empfindlichkeit für Ihre Stimme optimieren
- [ ] Marker-Typen nach Interesse aktivieren/deaktivieren  
- [ ] Berichts-Format nach Wunsch anpassen
- [ ] Audio-Setup für Online und Präsenz optimieren

### Tag 5: Erste echte Klienten-Sitzung 👤
- [ ] Klient über System informieren und Zustimmung einholen
- [ ] Präsenz oder Online - je nach Praxis-Setup  
- [ ] Kurz erklären, dann vergessen
- [ ] Normale Sitzung durchführen (Modus 2 empfohlen)
- [ ] Bericht nachher in Ruhe durchgehen

### Tag 6: Auswertung und Reflexion 📊
- [ ] Bericht der gestrigen Sitzung analysieren
- [ ] Überraschende Erkenntnisse notieren
- [ ] Mit Kollegen/Supervisor besprechen
- [ ] Eigene Notizen mit System-Erkenntnissen vergleichen
- [ ] Online vs. Präsenz: Was funktioniert besser?

### Tag 7: Fortgeschrittene Features 🚀
- [ ] Modus 3 (+ LLM) ausprobieren bei komplexem Fall
- [ ] Datei-Upload mit alter Aufnahme testen
- [ ] Export-Funktionen für verschiedene Formate testen
- [ ] Gruppen-Gespräch analysieren (falls anwendbar)

### Tag 8: Routine etablieren ✅
- [ ] Workflow für Online- und Präsenz-Sitzungen definieren  
- [ ] Optimalen Analyse-Modus für verschiedene Situationen wählen
- [ ] Klienten-Aufklärung für beide Modi standardisieren
- [ ] Backup-Routine auch für Online-Sessions etablieren
- [ ] Erfolg feiern! 🎉

---

## Weiterführende Ressourcen

### 📚 Vertiefung

**Bücher:**
- "Digitale Therapie-Dokumentation" - Dr. Maria Weber
- "KI in der psychotherapeutischen Praxis" - Prof. Hans Mueller  

**Online-Kurse:**
- Webinar-Serie "TransRapport für Einsteiger" (kostenlos)
- Zertifikatskurs "Digitale Therapie-Tools" (40 Std.)

**Communities:**
- Forum: community.transrapport.de
- Facebook-Gruppe: "TransRapport Nutzer Deutschland"
- Monatlicher Zoom-Austausch (jeden 1. Donnerstag)

### 🎓 Schulungen

**Basis-Schulung** (4 Stunden)
- Installation und Setup
- Grundfunktionen  
- Erste Sitzung
- Datenschutz
- *Kosten: 180€ pro Person*

**Profi-Schulung** (8 Stunden)
- Erweiterte Funktionen
- Marker-Interpretation
- Integration in Praxis-Workflows  
- Supervision mit System-Daten
- *Kosten: 340€ pro Person*

**Team-Schulung** (vor Ort)
- Individuell an Praxis angepasst
- Alle Mitarbeiter gleichzeitig
- Langzeit-Support inklusive
- *Kosten: 1.200€ pro Praxis*

---

*Dieses Handbuch wird kontinuierlich aktualisiert. Aktuelle Version: 3.4 (September 2025)*

**Feedback**: Senden Sie Verbesserungsvorschläge an docs@transrapport.de

**Lizenz**: Dieses Dokument steht unter CC BY-NC-SA 4.0 - Sie dürfen es für nicht-kommerzielle Zwecke teilen und anpassen.
