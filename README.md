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

### Rückgabefeld: `request`

Jede Antwort der Schnittstellen enthält ein Objekt `request` welches die Requestparameter die übergeben wurden, oder die von der Schnittstelle genutzten Standardwerte enthält.

## Schnittstellen

TODO