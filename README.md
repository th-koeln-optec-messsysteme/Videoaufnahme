# Projekt Videoaufnahme

Auftrag:

Erstellung eines 360° Kamerasystems mit Raspberry Pi für einen Wetterballonflug.


Gewicht:
StereoPi (inkl. CM3) + Kamearas : 62g


Materialien:

1 StereoPi (Standard Edition)
1 Raspberry Pi CM3/lite
2 Waveshare 14037 RPi Camera (M)
1 MicroSD Karte 64GB
1 USB Kabel (Für StereoPi wenn nicht vorhanden)


Anleitung:

1: Das Kabel zur Spannungsversorgung in den dafür vorgesehenen 2 Pin Anschluss stecken. 
Ist kein fertiges Kabel mit dem StereoPi mitgeliefert, muss aus einem USB Kabel und den mitgelieferten Anschlüssen eines erstellt werden, da der Micro USB Anschluss des StereoPi nicht für den normalen Betrieb geeignet ist. Wird der StereoPi über Micro USB betrieben, sind Ethernet und USB Typ A Anschlüsse deaktiviert.

2: Die Kameramodule werden an den StereoPi angeschlossen. 
Dafür wird die schwarze Kunststofflippe des Kameraanschlusses hochgezogen. Dann werden die Flachbandkabel mit der blauen Seite zur Kunststofflippe hin eingesteckt und die Lippe wieder heruntergedrückt um das Kabel zu fixieren. 

3: RaspianOS auf der MicroSD Karte installieren. 
Dazu den Anweisungen von raspberrypi.org folgen.

4: Skript zur Videoaufnahme erstellen.
Erstelle ein neues Skript mit Thonny und füge den Code aus
