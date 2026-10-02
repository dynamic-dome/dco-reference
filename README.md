# DCO Reference

Kleine, lokal ausfuehrbare Referenz fuer einen pruefbaren Agenten-Workflow:
Auftrag validieren, einreihen, synthetisch bearbeiten, Ergebnis pruefen und
eine schreibende Abschlussaktion bis zur menschlichen Freigabe blockieren.

Dieses Repository ist eine eigenstaendige Demonstration der oeffentlichen
Architekturidee. Es ist **kein Export des produktiven DCO**, enthaelt keine
Produktivkonfiguration und verbindet sich mit keinem externen Dienst.

Einordnung im Gesamtsystem: [DCO-Fallstudie auf dynamic-dome.com](https://dynamic-dome.com/systeme/dco/).

## Schnellstart

```bash
python -m pip install -e ".[test]"
python -m pytest
dco-reference demo
```

Der Demo-Lauf endet absichtlich im Zustand `awaiting_approval`. Erst ein
explizites `approve` schaltet den Abschluss frei:

```bash
dco-reference demo --approve
```

## Was der Schnitt belegt

1. Jeder Auftrag erhaelt eine stabile ID und ein validiertes Ziel.
2. Queue, Worker, Verifier und Approval Gate sind getrennte Komponenten.
3. Der Worker verarbeitet ausschliesslich synthetische Eingaben.
4. Das Ergebnis traegt eine nachvollziehbare Ereignisspur.
5. Eine als schreibend markierte Abschlussaktion bleibt ohne menschliche
   Freigabe blockiert.

## Bewusste Grenzen

- In-Memory-Queue statt produktiver Datenbank.
- Deterministischer Beispiel-Worker statt Modell- oder Tool-Aufruf.
- Keine Authentifizierung, Netzwerkschnittstelle oder Deployment-Konfiguration.
- Keine produktiven Adapter, Secrets, Hostnamen oder Betriebsdaten.
- Keine Behauptung, dass diese Demo den produktiven DCO vollstaendig abbildet.

Weitere Details: [`docs/architecture.md`](docs/architecture.md) und
[`docs/threat-model.md`](docs/threat-model.md).

## Lizenz

MIT, siehe [`LICENSE`](LICENSE).
