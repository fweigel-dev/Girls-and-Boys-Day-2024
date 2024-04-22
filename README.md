# WebseitenParser Python

WillWillkommen bei deinem eigenen Webseiten-Parser! Mit diesem Parser kannst du ganz einfach Elemente wie Texte, Bilder und Videos auf deiner eigenen Webseite platzieren. Hier erfährst du, wie jede Funktion verwendet wird, und bekommst Beispiele, die dir helfen, diese selbst auszuprobieren.

## Grundlegende Funktionen

### Texte

#### `text(text: str)`

Fügt Text auf deiner Webseite hinzu.

- **Beispiel:**
  - Um "Hallo Welt!" auf deine Seite zu setzen, schreibst du:
    ```python
    text("Hallo Welt!")
    ```

### Bilder

#### `image(url: str)`
Fügt ein Bild auf deiner Webseite hinzu.

- **Beispiel:**
  - Um ein Bild von "https://example.com/image.jpg" auf deine Seite zu setzen, schreibst du:
    ```python
    image("https://example.com/image.jpg")
    ```

### Videos

#### `video(url: str)`
Fügt ein Video auf deiner Webseite hinzu.

- **Beispiel:**
  - Um ein Video von "https://example.com/video.mp4" auf deine Seite zu setzen, schreibst du:
    ```python
    video("https://example.com/video.mp4")
    ```

## Fortgeschrittene Funktionen

### Hintergrund

#### `titel(text: str)`
Ändert den Titel deiner Webseite.

- **Beispiel:**
  - Um den Titel deiner Webseite in "Meine Webseite" zu ändern, schreibst du:
    ```python
    titel("Meine Webseite")
    ```

#### `icon(url: str)`
Ändert das Icon deiner Webseite.

- **Beispiel:**
  - Um das Icon deiner Webseite in "https://example.com/icon.png" zu ändern, schreibst du:
    ```python
    icon("https://example.com/icon.png")
    ```

### Layout

#### `hintergrundbild(url: str)`
Ändert das Hintergrundbild deiner Webseite.

- **Beispiel:**
  - Um das Hintergrundbild deiner Webseite in "https://example.com/background.jpg" zu ändern, schreibst du:
    ```python
    hintergrundbild("https://example.com/background.jpg")
    ```

#### `hintergrundfarbe(farbe: str)`
Ändert die Hintergrundfarbe deiner Webseite.

- **Beispiel:**
  - Um die Hintergrundfarbe deiner Webseite in "blau" zu ändern, schreibst du:
    ```python
    hintergrundfarbe("blue")
    ```
### Bearbeitung von Elementen

### Beispiel mit Bild

```python
image("https://example.com/image.jpg")
```

#### `breiter()`
Macht das zuletzt erstellte Element breiter.

- **Beispiel:**
  - Um das zuletzt erstellte Bild breiter zu machen, schreibst du:
    ```python
    breiter()
    ```

#### `schmaler()`
Macht das zuletzt erstellte Element schmaler.

- **Beispiel:**
  - Um das zuletzt erstellte Bild schmaler zu machen, schreibst du:
    ```python
    schmaler()
    ```

#### `links()` und `rechts()`
Platziert das zuletzt erstellte Element links oder rechts.

- **Beispiel:**
    - Um das zuletzt erstellte Bild links zu platzieren, schreibst du:
        ```python
        links()
        ```
    - Um das zuletzt erstellte Bild rechts zu platzieren, schreibst du:
        ```python
        rechts()
        ```

#### `hoeher()` und `tiefer()`
Platziert das zuletzt erstellte Element auf der Y-Achse höher oder tiefer.

- **Beispiel:**
    - Um das zuletzt erstellte Bild höher zu platzieren, schreibst du:
        ```python
        hoeher()
        ```
    - Um das zuletzt erstellte Bild tiefer zu platzieren, schreibst du:
        ```python
        tiefer()
        ```
#### `oben()` und `unten()`
Platziert das zuletzt erstellte Element auf der X-Achse oben oder unten.

- **Beispiel:**
    - Um das zuletzt erstellte Bild oben zu platzieren, schreibst du:
        ```python
        oben()
        ```
    - Um das zuletzt erstellte Bild unten zu platzieren, schreibst du:
        ```python
        unten()
        ```

### Text bearbeiten

#### `textgroesser()` und `textkleiner()`
Macht den zuletzt erstellten Text größer oder kleiner.

- **Beispiel:**
    - Um den zuletzt erstellten Text größer zu machen, schreibst du:
        ```python
        textgroesser()
        ```
    - Um den zuletzt erstellten Text kleiner zu machen, schreibst du:
        ```python
        textkleiner()
        ```

#### `textdicker()` und `textduenner()`
Macht den zuletzt erstellten Text dicker oder dünner.

- **Beispiel:**
    - Um den zuletzt erstellten Text dicker zu machen, schreibst du:
        ```python
        textdicker()
        ```
    - Um den zuletzt erstellten Text dünner zu machen, schreibst du:
        ```python
        textduenner()
        ```

#### `farbe(farbe: str)`
Ändert die Farbe des zuletzt erstellten Textes.

- **Beispiel:**
    - Um die Farbe des zuletzt erstellten Textes in "rot" zu ändern, schreibst du:
        ```python
        farbe("red")
        ```

### Bauen
Nachdem alle Funktionen verwendet wurden, muss die Webseite gebaut werden.

#### `bauen()`
Baut die Webseite.

- **Beispiel:**
    - Um die Webseite zu bauen, schreibst du:
        ```python
        bauen()
        ```
    Diese funktion muss ans Ende des Codes gesetzt werden, damit die Webseite gebaut wird.

Nachdem die Webseite gebaut wurde, liegt nun eine index.html Datei im gleichen Ordner wie das Python-Script. Diese Datei kann nun in einem Browser geöffnet werden, um die Webseite zu betrachten.

