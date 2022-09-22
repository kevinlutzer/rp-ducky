/*
    Creates labels for the diode ring modulator pcb

    Author: Kevin Lutzer
    Date: Sat Sept 10 2022
*/

// generates a rounded box with some text in the center



module generateLabel(width, height, radius, label, ts) {
    $fn=40;

    difference() {
        translate([- width / 2, - height / 2]) {
            minkowski() {
              square([width, height]);
              circle(r=radius);
            }
        }

        text(label, font="Liberation Sans:style=Bold", valign="center", halign="center", size=ts);        
    }       
}

// Each label was made with the dimensions of 4mm by 2.666mm 
//generateLabel(4.5, 2, 0.25, "RST", 1.5); 
//generateLabel(6, 2, 0.25, "BOOT", 1.5); 

generateLabel(5, 2, 0.25, "Rev3", 1.5); 
