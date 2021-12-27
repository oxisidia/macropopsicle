# macropopsicle
An open source two key macro-pad modeled to look like a cartoony melting popsicle. 

#Build instructions

## Parts List

  -1x Top case half (3D printed)
  
  -1x Bottom case half (3D printed)
  
  -1x Switch plate (3D printed)
  
  -1x Ice Cream piece (3D printed)
  
  -1x Ice cream bite (3D printed)
  
  -2x Key caps cherry style (3D printed or sourced)
  
  -1x Popsicle stick 
  
  -2x Cherry style switches 
  
  -3x Black wires (for ground)
  
  -2x Colored wires (for data)
  
  -5x short M3 bolts 
  
  -3x long M3 bolts
  
  -Solder (consumable)
  
  -1x Adafruit QT Py - SAMD21 Dev Board 
  
  ![alt text](https://github.com/oxisidia/macropopsicle/blob/main/Images/exploded_assembly.PNG)
  
   A note on the dev board: Boards of a similar form factor to the Adafruit QT Py - SAMD21 may also work with this case without needing any modifications.
   However the Adafruit QT Py - SAMD21 is the only board that has currently been tested and confirmed to work.

## Fabrication

All parts except the development board, wires, switches, popsicle stick and bolts need to be fabricated the parts have been designed for 3D printing however they could also be made through machining or other fabrication methods such as machining. 

All are designed to print with very little to no support material. All parts feature large flat surfaces I recommend printing with these face down on the build plate if using a filament extrusion 3D printer.

## Assembly

The case consists of five pieces main pieces. 

Of the five pieces the two main halves, colored orange provide the majority of the structural support.

Before assembling the case insert the switches into the switch plate. 

### Soldering: 

Solder the 1 black wire onto the ground pin of the dev board make sure the wire does not poke through to the side. Then splice the remaining two wires onto the ground wire.

Next Solder the data wires onto the A1 and A2 pins, once again make sure the wires do not poke through to the other side of the dev board. 

Once all wires have been soldered onto the dev board. Solder one ground wire and one data wire onto the leads of each switch. The polarity does not matter. 

### Software:

-Before assembling the case ensure that the firmware has is loaded onto the dev board and that all wiring is correct. 

If using Circuit Python load the Circuit Python boot loader. Please see the instructions for your specific dev board to install circuit python. 

Once the dev board is flashed with the Circuit Python boot loader add the code that will allow our macro pad to function. The code file (code.py) is included with this repository 

Drag and drop the code file onto the Circuit Python drive. 

Some libraries are also required for this code to function. Links are included below. Adds all libraries to the Libraries folder on the Circuit Python Drive. 

### Mechanical Assembly:

The keyplate is secured by four 4mm long bolts into the top case half. 

![alt text](https://github.com/oxisidia/macropopsicle/blob/main/Images/keyplate_assembly.PNG)

The white small bite piece is secured to the lower case half with a single bolt 4mm bolt.

![alt text](https://github.com/oxisidia/macropopsicle/blob/main/Images/bite_piece_assembly.PNG)

The larger white piece secures first to the lower orange case half and then to the upper case half once fully assembled.

![alt text](https://github.com/oxisidia/macropopsicle/blob/main/Images/Icecream_piece_assembly1.PNG)

![alt text](https://github.com/oxisidia/macropopsicle/blob/main/Images/Icecream_piece_assembly2.PNG)

Position the microcontroller in place (use the tweezers if neccessary to ensure it's properly seated) 

**position the dev board with tweezers image

Assemble two halves are assembled togeather using three 20mm long bolts. 

![alt text](https://github.com/oxisidia/macropopsicle/blob/main/Images/finalbolt_assembly.PNG)

All pieces which have bolts seated into them have holes designed to allow M3 bolts to screw into the plastic.

Once the popsicle case is assembled the keycaps and popsicle switch can be press fitted into place. Your macropopsicle is should now be assembled and appear like the one in the image at the top of this document.

## License
I have invested time and resources providing this open source design. If you have benefited from this design being open source, please consider making a small donation if you are able to. Donations are never expected but always appreciated, donations will help me create more open source designs in the future.

Designed by Dylan Rice / oxisidia. 

Creative Commons Attribution/Share-Alike, all text above must be included in any redistribution. See license.txt for additional details.
