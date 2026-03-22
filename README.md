# The Operator

The Operator is a 4 key macropad with a rotary encoder, an OLED Display, and 16 LED's for underglow. It used KMK firmware.

This is my first macropad (and my first hardware project for Hack club ever!) and its purpose is to make the task of opening applications quicker, alongside looking cool. It works with hotkeys on my laptop to open applications like Fusion, Bambu Studio, VS Code, and Google at the click of a button, plus it controls volume and its LEDs with a Rotary Encoder. The OLED shows the last button clicked and it shows the on/off status of the LEDs. This project has helped me learn a lot, particularly in PCB design.

To use this, simply connect it to power via the USB-C on the XIAO 2040 and use like any other macropad.

## Features:
- Although only be visible once printed, the bottom layer uses clear filament to diffuse underglow and has a filleted bottom as tonot detract from the look of the black filament used in the top two layers.
- 128x32 OLED Display.
- EC11 Rotary encoder for volume and LED power. 
- 16 WS2812B RGB LEDs for underglow. Don't worry, their power is limited in firmware.
- 4 Keys.

## CAD Model:
Everything fits together using 4 M3 screws and heatset inserts. The screws go into the hols along the edges of the case

Case:

<img width="810" height="450" alt="image-3" src="https://github.com/user-attachments/assets/f87bb009-2b1f-49e0-8ecc-e96fbd7f42c2" />

It has 3 separate printed pieces. The clear bottom where the PCB sits, the middle, and the top.

Full CAD:

<img width="810" height="450" alt="image" src="https://github.com/user-attachments/assets/ec2163aa-0b69-4894-b093-bec66a8c9753" />

Made in Fusion360.

## PCB:
This PCB was made in KiCad, and all the components of the silkscreen were downloaded from the web and manually added inside of KiCad.

Schematic

<img width="837" height="572" alt="SchemFresh" src="https://github.com/user-attachments/assets/b902461e-0a89-466f-9156-43a6d7fd7271" />

PCB

<img width="627" height="402" alt="PCBFresh" src="https://github.com/user-attachments/assets/49deada9-5ba7-415f-87f0-02b66791cad8" />

I used MX_V1 for the keyswitch footprints, the generic footprint for the XIAO 2040, a 4-pin header for the OLED, the footprint from the guide for the rotary encoder, and the SK6812MINI-E for the LED footprints.

## Firmware Overview:
This hackpad uses KMK firmware for everything. 

- the rotary encoder changes volume. press to turn off LEDs.
- The 4 keys open applications by correlating with hotkeys on my laptop. Starting from the furthest left, they open Fusion, Bambu Studio, VS Code, and Google, respectivley. 
- The OLED shows the last key pressed and the LED on/off status.


In the future I really want to do more with the rotary encoder. I want to remove te volume feature and instead have it work with scripts on my laptop to preform a different function for each application (e.g, in VS turning would scroll, while pressing would run code, while in fusion, turning would do a 360 degree pan, while pressing would bring the veiw to home).

## BOM:
Everything needed to make this hackpad (aside from soldering iron and 3D printing things) can be found in the kit.

- 4x Cherry MX Switches
- 4x DSA Keycaps
- 4x M3x5x4 Heatset inserts
- 4x M3x16mm screws
- 16x WS2812B LEDs
- 1x 0.91" 128x32 OLED Display
- 1x EC11 Rotary Encoder
- 1x XIAO RP2040
- 1x Case (3 printed parts, one in clear filament the rest in black)
