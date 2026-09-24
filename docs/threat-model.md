# Threat Model

## Schutzbehauptung

Die Demo verhindert im eigenen Prozess, dass ein als freigabepflichtig
markierter Job ohne expliziten Aufruf von `approve` abgeschlossen wird.

## Nicht abgedeckt

- Authentifizierung oder Autorisierung des Freigabe-Akteurs;
- Persistenz, Nebenlaeufigkeit oder Manipulationsschutz der Ereignisspur;
- Isolation nicht vertrauenswuerdigen Codes;
- Netzwerk-, Supply-Chain- oder Deployment-Sicherheit;
- Schutz produktiver DCO-Systeme.

## Vertrauensgrenzen

Eingaben, Worker-Ausgaben und Adapter waeren in einem realen System nicht
vertrauenswuerdig. Die mitgelieferte CLI-Demo verwendet eine synthetische,
lokale Eingabe. Die Bibliothek validiert jedoch nur, dass `objective` nicht
leer ist; sie erkennt oder blockiert keine realen Daten. Eine spaetere
Erweiterung darf externe Adapter erst nach eigener Validierung, Sandbox- und
Credential-Strategie anbinden.
