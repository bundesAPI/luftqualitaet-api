# Luftdaten / Luftqualität (Umweltbundesamt)

Schnittstellen der unterschiedlichen Visualisierungen der [Luftdaten](https://www.umweltbundesamt.de/daten/luft/luftdaten)-Seite des Umweltbundesamtes

## Dokumentation

Die OpenAPI Specification für die API befindet sich auf [luftqualitaet.api.bund.dev](https://luftqualitaet.api.bund.dev/)

## Funktionalität

### Host

Der Schnittstellen-Host inklusive Version lautet

```
https://www.umweltbundesamt.de/api/air_data/v2
```

### Sicherheit

Die Schnittstelle ist nicht gesichert. Kein Sessionhandling oder CSRF.

### Request-Parameter

Über alle Schnittstellen hinweg gibt es eine handvoll Parameter welche immer identisch sind. Diese sind mal mehr und mal weniger sinnvoll (sie verändern das Ergebnis dann nicht).

| Parameter | Beschreibung |
|-----------|--------------|
| `use`     | Genutzt bei den Metadaten beschreibt dieser Parameter für welche Schnittstelle die Daten bezogen werden |
| `lang`    | Die Sprache in der die Datensätze zurückgegeben werden |
| `index`   | Schnittstellen welche in Objekten indizierte Daten enthalten können hiermit den Objektschlüssel anpassen (bei Stationen bespielweise deren `id` oder `code`)
| `date_from` | Startdatum für Datensätze (Format `YYYY-MM-DD`) |
| `date_to` | Enddatum für Datensätze |
| `time_from` | Startzeit für Datensätze (in Stunden `1` bis `24`)|
| `time_to` | Endzeit für Datensätze |

**Zur Filterung:** Im Frontend der Luftdaten ist es an einigen Stellen möglich nach der Wetterstation/Region zu filtern. Diese Filterung ist rein clientseitig umgesetzt. In den Schnittstellen ist es nur möglich anhand der `date_*` und `time_*`-Parameter zu filtern.

### Rückgabeformat

Jede Schnittstelle endet auf `/{format}` welches in allen Fällen immer nur `json` ist. Hier scheint sich offen gehalten zu sein eventuell andere Formate zu unterstützen aber hier returned die Schnittstelle dann meistens nur ein Statuscode 405 mit folgendem Body:

```
{endpoint} with {format} not implemented
```

### Rückgabefeld: `indices`

Einige Schnittstellen (bspw. die Stationenliste) enthalten einen Punkt `indices`. Hier werden die Felder welche innerhalb von Data zurückgegeben werden beschrieben.

Das ist notwendig, da ein Großteil der Schnittstellendaten nicht als Objekte/Key-Value-Paare ausgegeben wird, sondern als einfache Arrays.

`indices` kann aber nicht nur ein Array sein, sondern auch ein genestetes Objekt in dem Felder und dann wieder enthaltene Arrays beschrieben werden, um auch komplexere Datenstrukturen aufzuschlüsseln.

### Rückgabefeld: `headers`

Einige Schnittstellen (bspw. Überschreitungen) enthalten tabellarische Daten, und wie der Name bereits suggeriert werden in diesem Feld die Tabellenüberschriften zu den Datenfeldern angegeben.

Manche der Felder enthalten nur einen Kürzel wie z.B. `sta_name`, während andere Felder komplette Beschreibungen enthalten. Erstere sind Felder die über Requests hinweg gleich sind und in der Anwendung übersetzt sind, und das nur der Schlüssel für die Übersetzung ist.

### Rückgabefeld: `request`

Jede Antwort der Schnittstellen enthält ein Objekt `request` welches die Requestparameter die übergeben wurden, oder die von der Schnittstelle genutzten Standardwerte enthält.

## Schnittstellen

### `/stations/{format}` - Stationen

Genutzt auf:
* [Aktuelle Luftdaten - Luftqualität](https://www.umweltbundesamt.de/daten/luft/luftdaten/luftqualitaet)
* [Aktuelle Luftdaten - Stationen](https://www.umweltbundesamt.de/daten/luft/luftdaten/stationen)


### `/meta/{format}` - Meta

Genutzt auf: _Allen Luftdaten-Seiten_

### `/maps/{format}` - Karten

Genutzt auf: [Aktuelle Luftdaten - Karten](https://www.umweltbundesamt.de/daten/luft/luftdaten/karten)

Diese Schnittstelle enthält eigentlich nur Zusatzinformationen zu den Karten, welche unter einem anderen Endpunkt/Bildpfad erreichbar sind, dieser setzt sich folgendermaßen zusammen:

```
https://www.umweltbundesamt.de/sites/default/files/w21ad_luftdaten/maps/{component}/{scope}/{version}/{component}_{scope}_{version}_{date}.png
```

* `component`: Der Name eines Schadstoffs, kann aus der Meta-Schnittstelle entnommen werden
* `scope`: Name der Auswertungsart
* `version`: Ist immer `v1`
* `date`: Datum für die Karte im Format `YYYYMMDD`

Beispiel: 

```
https://www.umweltbundesamt.de/sites/default/files/w21ad_luftdaten/maps/O3/1SMW_MAX/v1/O3_1SMW_MAX_v1_20210829.png
```

### `/measures/{format}` - Stationen

Genutzt auf: [Aktuelle Luftdaten - Stationen](https://www.umweltbundesamt.de/daten/luft/luftdaten/stationen)

### `/airquality/{format}` - Luftqualität

Genutzt auf: [Aktuelle Luftdaten - Luftqualität](https://www.umweltbundesamt.de/daten/luft/luftdaten/luftqualitaet)

### `/annualbalances/ajaxdata` - Jahresbilanzen

Genutzt auf: [Aktuelle Luftdaten - Jahresbilanzen](https://www.umweltbundesamt.de/daten/luft/luftdaten/jahresbilanzen)

### `/transgressions/ajaxdata` - Überschreitungen

Genutzt auf: [Aktuelle Luftdaten - Überschreitungen](https://www.umweltbundesamt.de/daten/luft/luftdaten/ueberschreitungen)