# TransRapport Marker-Referenz

*Vollständige Übersicht aller therapeutischen Marker im LEAN.DEEP 3.4 Schema*

---

## Marker-Hierarchie

Das LEAN.DEEP 3.4 System organisiert therapeutische Marker in vier Ebenen, von atomaren Bausteinen bis zu komplexen Meta-Mustern.

### Hierarchie-Übersicht

```
MEMA (Meta-Marker)
├── Therapeutische Durchbrüche
├── Prozess-Regressions  
└── Systemische Dynamiken

CLU (Cluster-Marker)
├── Gesprächsmuster
├── Emotionale Zyklen
└── Beziehungsdynamiken

SEM (Semantic-Marker)  
├── Inhaltsanalyse
├── Emotionale Bedeutung
└── Therapeutische Konzepte

ATO (Atomic-Marker)
├── Einzelne Sprach-Events
├── Prosodische Elemente
└── Audio-Grundbausteine
```

---

## ATO - Atomic Markers

*Grundlegende, isolierte Sprachereignisse und Audio-Elemente*

### Prosodische Marker

#### Sprechgeschwindigkeit
| Marker ID | Beschreibung | Auslöser | Therapeutische Relevanz |
|-----------|--------------|----------|-------------------------|
| `ATO_SPEECHRATE_SLOW` | Langsame Sprechweise | <80 WPM | Depression, Müdigkeit, Nachdenklichkeit |
| `ATO_SPEECHRATE_FAST` | Schnelle Sprechweise | >180 WPM | Aufregung, Angst, Manie |
| `ATO_SPEECHRATE_DROP` | Plötzliche Verlangsamung | >30% Reduktion | Emotionale Belastung, Erschöpfung |

#### Pausen und Timing
| Marker ID | Beschreibung | Auslöser | Therapeutische Relevanz |
|-----------|--------------|----------|-------------------------|
| `ATO_PAUSE_MICRO` | Kurze Pausen | 0.3-1s Stille | Suchbewegung, Unsicherheit |
| `ATO_PAUSE_LONG` | Lange Pausen | >2s Stille | Verarbeitung, Blockade, Nachdenken |
| `ATO_PAUSE_FILLED` | Gefüllte Pausen | "äh", "ehm" | Nervosität, Denkpause |
| `ATO_LONG_RESPONSE_GAP` | Verzögerte Antwort | >5s nach Frage | Widerstand, Überforderung |

#### Tonhöhe und Intensität
| Marker ID | Beschreibung | Auslöser | Therapeutische Relevanz |
|-----------|--------------|----------|-------------------------|
| `ATO_PITCH_HIGH` | Hohe Stimmlage | >+20Hz vom Baseline | Stress, Aufregung, Lügen |
| `ATO_PITCH_LOW` | Tiefe Stimmlage | >-20Hz vom Baseline | Depression, Müdigkeit |
| `ATO_PITCH_SPREAD_NARROW` | Monotone Sprechweise | <50Hz Varianz | Depression, Apathie |
| `ATO_PITCH_SPREAD_WIDE` | Lebhafte Intonation | >200Hz Varianz | Emotionalität, Aufregung |
| `ATO_RISING_INTONATION` | Fragende Intonation | Pitch-Anstieg am Ende | Unsicherheit, Bestätigung-suchend |
| `ATO_F0_RISE_FINAL` | Finale Tonhöhen-Steigerung | Satz-Ende +50Hz | Zweifel, Nachfragen |

#### Stimm-Qualität
| Marker ID | Beschreibung | Auslöser | Therapeutische Relevanz |
|-----------|--------------|----------|-------------------------|
| `ATO_JITTER_SHIMMER_HIGH` | Stimmzittern | Hohe Irregularität | Emotionale Erregung, Stress |
| `ATO_BREATHINESS` | Behauchte Stimme | Hohes H/N Ratio | Intimität, Verletzlichkeit |
| `ATO_CREAKY_VOICE` | Knarrende Stimme | Niederfrequente Pulse | Müdigkeit, Resignation |

### Emotionale Audio-Events

#### Atmung und Seufzer
| Marker ID | Beschreibung | Auslöser | Therapeutische Relevanz |
|-----------|--------------|----------|-------------------------|
| `ATO_SIGH` | Seufzer | Langes Ausatmen >2s | Resignation, Erleichterung, Müdigkeit |
| `ATO_SHARP_INTAKE` | Scharfes Einatmen | Schnelles Einatmen | Schreck, Überraschung, Realisierung |
| `ATO_BREATH_HOLD` | Atem anhalten | Atemunterbrechung >3s | Anspannung, Kontrolle |

#### Lachen und Vergnügen
| Marker ID | Beschreibung | Auslöser | Therapeutische Relevanz |
|-----------|--------------|----------|-------------------------|
| `ATO_LAUGHTER` | Echtes Lachen | Spontane Lach-Sequenz | Freude, Entspannung, Humor |
| `ATO_NERVOUS_LAUGHTER` | Nervöses Lachen | Kurze, gepresste Lacher | Unbehagen, Verlegenheit |
| `ATO_BITTER_LAUGHTER` | Bitteres Lachen | Sarkastisches Lachen | Zynismus, Verletztheit |

#### Weinen und Emotionalität
| Marker ID | Beschreibung | Auslöser | Therapeutische Relevanz |
|-----------|--------------|----------|-------------------------|
| `ATO_CRY_ONSET` | Beginnende Tränen | Stimmbruch, Schluchzen | Emotionaler Durchbruch |
| `ATO_VOICE_BREAK` | Stimmbruch | Stimm-Unterbrechung | Starke Emotion, Überwältigung |
| `ATO_SNIFFLING` | Schniefen | Nasen-Geräusche | Weinen, Erkältung, Emotion |

### Sprachliche Marker

#### Füllwörter und Verzögerungen
| Marker ID | Beschreibung | Auslöser | Therapeutische Relevanz |
|-----------|--------------|----------|-------------------------|
| `ATO_FILLER` | Füllwörter | "äh", "ehm", "also" | Unsicherheit, Denkpause |
| `ATO_REPETITION` | Wort-Wiederholung | Gleiche Wörter >2x | Nervosität, Betonung |
| `ATO_FALSE_START` | Falsche Starts | Abgebrochene Sätze | Selbstkorrektur, Unsicherheit |

#### Gesprächs-Dynamik
| Marker ID | Beschreibung | Auslöser | Therapeutische Relevanz |
|-----------|--------------|----------|-------------------------|
| `ATO_OVERLAP_INTERRUPT` | Unterbrechung | Sprecher-Überlappung | Dominanz, Ungeduld |
| `ATO_BACK_CHANNEL` | Bestätigung | "mhm", "ja", "genau" | Aufmerksamkeit, Zustimmung |
| `ATO_VOLUME_INCREASE` | Lauter werden | >+10dB Anstieg | Betonung, Ärger |
| `ATO_VOLUME_DECREASE` | Leiser werden | >-10dB Abfall | Scham, Rückzug |

---

## SEM - Semantic Markers

*Bedeutungsebene - Inhalte, Emotionen und therapeutische Konzepte*

### Emotionale Semantik

#### Grundemotionen
| Marker ID | Beschreibung | Text-Indikatoren | Therapeutische Relevanz |
|-----------|--------------|------------------|-------------------------|
| `SEM_JOY_EXPRESSION` | Freude ausdrücken | "glücklich", "toll", "wunderbar" | Positive Entwicklung |
| `SEM_SADNESS_EXPRESSION` | Trauer ausdrücken | "traurig", "deprimiert", "niedergeschlagen" | Depression, Verlust |
| `SEM_ANGER_EXPRESSION` | Ärger ausdrücken | "wütend", "sauer", "frustriert" | Konflikt, Abgrenzung |
| `SEM_FEAR_EXPRESSION` | Angst ausdrücken | "ängstlich", "besorgt", "panisch" | Angststörung, Trauma |
| `SEM_DISGUST_EXPRESSION` | Ekel ausdrücken | "widerlich", "abscheulich" | Ablehnung, Grenzen |

#### Emotionale Regulation
| Marker ID | Beschreibung | Text-Indikatoren | Therapeutische Relevanz |
|-----------|--------------|------------------|-------------------------|
| `SEM_EMOTIONAL_SUPPRESSION` | Gefühls-Unterdrückung | "ist nicht wichtig", "egal" | Vermeidung, Kontrolle |
| `SEM_EMOTIONAL_AMPLIFICATION` | Gefühls-Verstärkung | "total", "extrem", "unglaublich" | Dramatisierung |
| `SEM_EMOTIONAL_REGULATION` | Gefühls-Steuerung | "beruhigen", "kontrollieren" | Bewältigungsstrategie |

### Therapeutische Prozesse

#### Einsicht und Bewusstsein
| Marker ID | Beschreibung | Text-Indikatoren | Therapeutische Relevanz |
|-----------|--------------|------------------|-------------------------|
| `SEM_INSIGHT_MOMENT` | Erkenntnis-Moment | "jetzt verstehe ich", "aha!" | Therapeutischer Fortschritt |
| `SEM_SELF_REFLECTION` | Selbstreflexion | "ich merke", "mir fällt auf" | Selbstbeobachtung |
| `SEM_PATTERN_RECOGNITION` | Muster erkennen | "immer wieder", "das Gleiche" | Bewusstseinserweiterung |
| `SEM_CONNECTION_MAKING` | Verbindungen herstellen | "das hängt zusammen mit" | Integration |

#### Widerstand und Abwehr
| Marker ID | Beschreibung | Text-Indikatoren | Therapeutische Relevanz |
|-----------|--------------|------------------|-------------------------|
| `SEM_THERAPY_RESISTANCE` | Therapie-Widerstand | "bringt nichts", "hilft nicht" | Ambivalenz |
| `SEM_INTELLECTUALIZATION` | Intellektualisierung | "theoretisch", "objektiv" | Abwehrmechanismus |
| `SEM_MINIMIZATION` | Bagatellisierung | "nicht so schlimm" | Verleugnung |
| `SEM_EXTERNALIZATION` | Externalisierung | "die anderen", "das System" | Verantwortungs-Abgabe |

#### Beziehungs-Themen
| Marker ID | Beschreibung | Text-Indikatoren | Therapeutische Relevanz |
|-----------|--------------|------------------|-------------------------|
| `SEM_ATTACHMENT_ANXIETY` | Bindungsangst | "verlassen werden", "Angst vor Nähe" | Bindungsmuster |
| `SEM_ATTACHMENT_AVOIDANCE` | Bindungsvermeidung | "brauche niemanden" | Autonomie-Konflikt |
| `SEM_TRUST_ISSUES` | Vertrauens-Probleme | "kann niemandem trauen" | Beziehungsstörung |
| `SEM_INTIMACY_FEAR` | Intimität-Angst | "zu nah", "Grenzen" | Nähe-Distanz-Konflikt |

### Kognitive Muster

#### Denkverzerrungen
| Marker ID | Beschreibung | Text-Indikatoren | Therapeutische Relevanz |
|-----------|--------------|------------------|-------------------------|
| `SEM_CATASTROPHIZING` | Katastrophisieren | "furchtbar", "das Schlimmste" | Angststörung |
| `SEM_BLACK_WHITE_THINKING` | Schwarz-Weiß-Denken | "immer", "nie", "alle" | Cognitive Verzerrung |
| `SEM_MIND_READING` | Gedankenlesen | "die denken bestimmt" | Projektion |
| `SEM_FORTUNE_TELLING` | Wahrsagen | "wird sicher schief gehen" | Pessimismus |

#### Selbstbild
| Marker ID | Beschreibung | Text-Indikatoren | Therapeutische Relevanz |
|-----------|--------------|------------------|-------------------------|
| `SEM_SELF_CRITICISM` | Selbstkritik | "bin zu dumm", "schaffe nichts" | Niedriges Selbstwertgefühl |
| `SEM_SELF_COMPASSION` | Selbstmitgefühl | "bin okay", "darf Fehler machen" | Gesunde Selbstakzeptanz |
| `SEM_PERFECTIONISM` | Perfektionismus | "muss perfekt sein" | Leistungsdruck |

---

## CLU - Cluster Markers

*Mustergruppen - Wiederkehrende Gesprächssequenzen und Dynamiken*

### Gesprächsmuster

#### Vermeidungs-Cluster
| Marker ID | Beschreibung | Komponenten | Therapeutische Relevanz |
|-----------|--------------|-------------|-------------------------|
| `CLU_AVOIDANCE_PATTERN` | Vermeidungsverhalten | ATO_PAUSE_LONG + SEM_TOPIC_CHANGE | Widerstand gegen schwierige Themen |
| `CLU_DEFLECTION_SEQUENCE` | Ablenkungsmanöver | SEM_HUMOR + ATO_NERVOUS_LAUGHTER | Überspielung von Schmerz |
| `CLU_MINIMIZATION_CYCLE` | Verharmlosungs-Zyklus | SEM_MINIMIZATION + ATO_VOLUME_DECREASE | Selbstschutz-Mechanismus |

#### Engagement-Cluster
| Marker ID | Beschreibung | Komponenten | Therapeutische Relevanz |
|-----------|--------------|-------------|-------------------------|
| `CLU_DEEP_EXPLORATION` | Tiefe Erforschung | SEM_INSIGHT + ATO_PAUSE_LONG | Therapeutische Arbeit |
| `CLU_EMOTIONAL_OPENING` | Emotionale Öffnung | SEM_VULNERABILITY + ATO_VOICE_BREAK | Vertrauen, Fortschritt |
| `CLU_COLLABORATIVE_WORK` | Zusammenarbeit | SEM_AGREEMENT + ATO_BACK_CHANNEL | Therapeutische Allianz |

### Emotionale Zyklen

#### Eskalations-Muster
| Marker ID | Beschreibung | Komponenten | Therapeutische Relevanz |
|-----------|--------------|-------------|-------------------------|
| `CLU_ANGER_ESCALATION` | Ärger-Eskalation | SEM_ANGER + ATO_VOLUME_INCREASE | Affekt-Regulation |
| `CLU_ANXIETY_SPIRAL` | Angst-Spirale | SEM_CATASTROPHIZING + ATO_SPEECHRATE_FAST | Panik-Entwicklung |
| `CLU_DEPRESSION_DESCENT` | Depressions-Abwärtsspirale | SEM_SADNESS + ATO_SPEECHRATE_SLOW | Stimmungsverfall |

#### Regulations-Muster
| Marker ID | Beschreibung | Komponenten | Therapeutische Relevanz |
|-----------|--------------|-------------|-------------------------|
| `CLU_SELF_SOOTHING` | Selbstberuhigung | SEM_EMOTIONAL_REGULATION + ATO_SIGH | Bewältigungsfähigkeit |
| `CLU_GROUNDING_SEQUENCE` | Erdung | SEM_REALITY_CHECK + ATO_PAUSE_MICRO | Stabilisierung |
| `CLU_INTEGRATION_PROCESS` | Integrations-Prozess | SEM_CONNECTION_MAKING + ATO_REPETITION | Verarbeitung |

### Beziehungsdynamiken

#### Macht und Kontrolle
| Marker ID | Beschreibung | Komponenten | Therapeutische Relevanz |
|-----------|--------------|-------------|-------------------------|
| `CLU_POWER_STRUGGLE` | Machtkampf | SEM_RESISTANCE + ATO_OVERLAP_INTERRUPT | Kontroll-Konflikt |
| `CLU_SUBMISSION_PATTERN` | Unterwerfung | SEM_COMPLIANCE + ATO_VOLUME_DECREASE | Macht-Ungleichgewicht |
| `CLU_BOUNDARY_TESTING` | Grenzen-Test | SEM_CHALLENGE + ATO_PAUSE_LONG | Rahmen-Exploration |

#### Allianz und Vertrauen
| Marker ID | Beschreibung | Komponenten | Therapeutische Relevanz |
|-----------|--------------|-------------|-------------------------|
| `CLU_THERAPEUTIC_ALLIANCE` | Therapeutische Allianz | SEM_COLLABORATION + ATO_SYNCHRONY | Arbeitsbeziehung |
| `CLU_TRUST_BUILDING` | Vertrauensaufbau | SEM_VULNERABILITY + ATO_VOICE_SOFTENING | Beziehungsentwicklung |
| `CLU_RUPTURE_REPAIR` | Bruch-Reparatur | SEM_APOLOGY + ATO_TONE_RECONCILIATION | Beziehungsarbeit |

---

## MEMA - Meta Markers

*Übergeordnete therapeutische Dynamiken und Prozess-Indikatoren*

### Prozess-Stadien

#### Therapie-Phasen
| Marker ID | Beschreibung | Indikator-Cluster | Therapeutische Relevanz |
|-----------|--------------|-------------------|-------------------------|
| `MEMA_ENGAGEMENT_PHASE` | Engagement-Phase | CLU_TRUST_BUILDING | Therapie-Beginn |
| `MEMA_WORKING_PHASE` | Arbeits-Phase | CLU_DEEP_EXPLORATION | Kernarbeit |
| `MEMA_INTEGRATION_PHASE` | Integrations-Phase | CLU_INTEGRATION_PROCESS | Therapie-Ende |
| `MEMA_TERMINATION_PHASE` | Abschluss-Phase | CLU_CLOSURE_SEQUENCE | Beendigung |

#### Veränderungs-Prozesse
| Marker ID | Beschreibung | Indikator-Cluster | Therapeutische Relevanz |
|-----------|--------------|-------------------|-------------------------|
| `MEMA_BREAKTHROUGH_MOMENT` | Durchbruch-Moment | SEM_INSIGHT + CLU_EMOTIONAL_OPENING | Wendepunkt |
| `MEMA_REGRESSION_PHASE` | Rückschritt-Phase | CLU_AVOIDANCE + SEM_RESISTANCE | Prozess-Rückschritt |
| `MEMA_CONSOLIDATION_PERIOD` | Festigungs-Phase | CLU_INTEGRATION + SEM_STABILITY | Stabilisierung |

### Systemische Dynamiken

#### Familien-Systeme
| Marker ID | Beschreibung | Indikator-Cluster | Therapeutische Relevanz |
|-----------|--------------|-------------------|-------------------------|
| `MEMA_FAMILY_DYNAMICS` | Familien-Dynamik | CLU_ROLE_PATTERNS | System-Verständnis |
| `MEMA_INTERGENERATIONAL` | Generationen-Muster | SEM_FAMILY_HISTORY | Übertragung |
| `MEMA_BOUNDARY_ISSUES` | Grenzen-Problematik | CLU_ENMESHMENT | System-Störung |

#### Trauma-Dynamiken
| Marker ID | Beschreibung | Indikator-Cluster | Therapeutische Relevanz |
|-----------|--------------|-------------------|-------------------------|
| `MEMA_TRAUMA_ACTIVATION` | Trauma-Aktivierung | CLU_HYPERAROUSAL | Trigger-Erkennung |
| `MEMA_DISSOCIATION_STATE` | Dissoziations-Zustand | CLU_DISCONNECTION | Schutz-Mechanismus |
| `MEMA_TRAUMA_INTEGRATION` | Trauma-Integration | CLU_COHERENCE_BUILDING | Heilungs-Prozess |

---

## Audio-Spezifische Marker

### Prosody-Marker (`M_PROSODY_*`)

#### Basis-Prosody
| Marker ID | Parameter | Schwellenwert | Bedeutung |
|-----------|-----------|---------------|-----------|
| `M_PROSODY_RATE_SLOW` | WPM | <80 | Langsame Sprechweise |
| `M_PROSODY_RATE_FAST` | WPM | >180 | Schnelle Sprechweise |
| `M_PROSODY_PITCH_HIGH` | Hz | >+50 Baseline | Hohe Tonlage |
| `M_PROSODY_PITCH_LOW` | Hz | >-50 Baseline | Tiefe Tonlage |
| `M_PROSODY_VOLUME_HIGH` | dB | >+15 Baseline | Laute Stimme |
| `M_PROSODY_VOLUME_LOW` | dB | >-15 Baseline | Leise Stimme |

#### Erweiterte Prosody
| Marker ID | Parameter | Schwellenwert | Bedeutung |
|-----------|-----------|---------------|-----------|
| `M_PROSODY_HESITATION` | Pause-Häufigkeit | >3 pro Minute | Zögernde Sprechweise |
| `M_PROSODY_FLUENCY_LOW` | Unterbrechungen | >5 pro Minute | Gestörter Redefluss |
| `M_PROSODY_MONOTONE` | Pitch-Varianz | <30Hz | Monotone Sprechweise |
| `M_PROSODY_EMPHATIC` | Betonungs-Stärke | >2 StdDev | Emphatic Betonung |

### Speaker-ID Marker (`M_POSEID_*`)

#### Sprecher-Erkennung
| Marker ID | Confidence | Beschreibung | Verwendung |
|-----------|------------|--------------|------------|
| `M_POSEID_CLIENT_HIGH` | >0.9 | Klient sicher erkannt | Hauptsprecher |
| `M_POSEID_CLIENT_MEDIUM` | 0.7-0.9 | Klient wahrscheinlich | Sekundär-Check |
| `M_POSEID_CLIENT_LOW` | 0.5-0.7 | Klient möglich | Unsicher |
| `M_POSEID_THERAPIST_HIGH` | >0.9 | Therapeut sicher erkannt | Professioneller Sprecher |
| `M_POSEID_UNKNOWN` | <0.5 | Unbekannter Sprecher | Dritte Person |

---

## Scoring und Gewichtung

### Gewichtungs-Schema

```json
{
  "weights": {
    "poseid": 1.5,      // Sprecher-Identifikation wichtig
    "risk": 1.2,        // Risiko-Marker verstärken  
    "negation": 1.0,    // Verneinungen neutral
    "intent": 0.9,      // Absichten leicht reduziert
    "action": 0.8,      // Handlungen geringer gewichtet
    "prosody": 1.0      // Prosody als Baseline
  }
}
```

### Score-Interpretation

| Score-Bereich | Interpretation | Aktion |
|---------------|----------------|--------|
| 0.9 - 1.0 | Sehr sicher | Sofortige Aufmerksamkeit |
| 0.7 - 0.9 | Wahrscheinlich | Dokumentation empfohlen |
| 0.5 - 0.7 | Möglich | Kontext prüfen |
| 0.3 - 0.5 | Schwach | Optional vermerken |
| 0.0 - 0.3 | Unwahrscheinlich | Ignorieren |

### Fusion-Methoden

#### Weighted Sum (Standard)
```
final_score = Σ(marker_score * category_weight) / Σ(weights)
```

#### Maximum Confidence
```
final_score = max(marker_score * category_weight)
```

#### Bayesian Fusion
```
final_score = P(marker|evidence) * prior_probability
```

---

## Klinische Anwendung

### Therapie-Phasen Mapping

#### Phase 1: Diagnostik (Sitzungen 1-3)
**Fokus-Marker**:
- `SEM_SYMPTOM_PRESENTATION`: Symptom-Darstellung
- `CLU_AVOIDANCE_PATTERN`: Vermeidungsverhalten  
- `MEMA_ENGAGEMENT_PHASE`: Engagement-Level
- `M_PROSODY_ANXIETY`: Angst-Indikatoren

#### Phase 2: Behandlung (Sitzungen 4-20)
**Fokus-Marker**:
- `SEM_INSIGHT_MOMENT`: Erkenntnisse
- `CLU_THERAPEUTIC_ALLIANCE`: Arbeitsbeziehung
- `MEMA_BREAKTHROUGH_MOMENT`: Durchbrüche
- `CLU_EMOTIONAL_OPENING`: Emotionale Öffnung

#### Phase 3: Integration (Sitzungen 21+)
**Fokus-Marker**:
- `CLU_INTEGRATION_PROCESS`: Verarbeitung
- `SEM_PATTERN_RECOGNITION`: Mustererkennung
- `MEMA_CONSOLIDATION_PERIOD`: Festigung
- `CLU_SELF_SOOTHING`: Selbstregulation

### Störungs-spezifische Profile

#### Depression
**Kern-Marker**:
```
- M_PROSODY_RATE_SLOW (hoch)
- SEM_SADNESS_EXPRESSION (hoch)
- CLU_DEPRESSION_DESCENT (mittel)
- ATO_SIGH (häufig)
```

#### Angststörung  
**Kern-Marker**:
```  
- M_PROSODY_RATE_FAST (hoch)
- SEM_CATASTROPHIZING (hoch)
- CLU_ANXIETY_SPIRAL (mittel)
- ATO_PAUSE_FILLED (häufig)
```

#### Persönlichkeitsstörung
**Kern-Marker**:
```
- CLU_POWER_STRUGGLE (hoch)
- SEM_BLACK_WHITE_THINKING (hoch) 
- MEMA_BOUNDARY_ISSUES (mittel)
- CLU_EMOTIONAL_DYSREGULATION (häufig)
```

---

## Entwicklung und Anpassung

### Eigene Marker definieren

#### YAML-Template
```yaml
id: CUSTOM_MARKER_ID
category: semantic
type: composed_of
description: "Beschreibung des Markers"
pattern:
  - trigger: "Auslöser-Text"
  - context: "Kontext-Bedingung"  
  - confidence: 0.75
meta:
  clinical_relevance: "Therapeutische Bedeutung"
  severity: medium
  requires_attention: false
```

#### Registrierung
```json
{
  "id": "DET_CUSTOM",
  "module": "engine.detectors.custom",
  "fires_marker": ["CUSTOM_MARKER_ID"],
  "threshold": 0.6
}
```

### Kalibrierung für Praxis

#### Empfindlichkeits-Anpassung
```json
{
  "thresholds": {
    "emit_event": 0.4,        // Niedrigere Schwelle = mehr Marker
    "prosody_min": 0.7,       // Höhere Prosody-Schwelle
    "semantic_min": 0.5,      // Moderate Semantik-Schwelle
    "risk_markers": 0.3       // Sensitive Risiko-Erkennung
  }
}
```

#### Praxis-spezifische Gewichtung
```json
{
  "weights": {
    "couples_therapy": {
      "poseid": 2.0,          // Sprecher-Unterscheidung wichtiger
      "interaction": 1.5       // Interaktions-Marker betonen
    },
    "trauma_therapy": {
      "dissociation": 1.8,    // Dissoziations-Marker verstärken
      "activation": 1.6        // Trauma-Aktivierung wichtig
    }
  }
}
```

---

*Marker-Referenz Version 3.4 - Letzte Aktualisierung: 6. September 2025*

Für Rückfragen und Erweiterungen: markers@transrapport.de
