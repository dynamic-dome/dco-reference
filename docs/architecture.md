# Architektur

```text
submit -> validate -> queue -> synthetic worker -> verifier
                                             |
                                             v
                                  approval required?
                                    | yes       | no
                                    v           v
                              human approve -> complete
```

Der Referenzschnitt trennt absichtlich fuenf Verantwortlichkeiten:

- `Job` und `JobState` bilden den kleinen Zustandsvertrag.
- `InMemoryQueue` zeigt die Uebergabe ohne Infrastrukturabhaengigkeit.
- `SyntheticWorker` erzeugt ein deterministisches Artefakt.
- `Verifier` prueft das Artefakt unabhaengig vom Worker.
- `Orchestrator` erzwingt Zustandsfolge und Freigabegrenze.

Die Ereignisspur ist fuer Demonstration und Tests gedacht. Sie ist weder ein
unveraenderliches Audit-Ledger noch eine produktive Persistenzschicht.
