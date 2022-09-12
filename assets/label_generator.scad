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

        text(label, font="Liberation Sans", valign="center", halign="center", size=ts);        
    }

            
}



module generateBoardTitle(width, height, radius, ts) {
    $fn=40;

    difference() {
        translate([- width / 2, - height / 2]) {
            minkowski() {
              square([width, height]);
              circle(r=radius);
            }
        }

        translate([-width/2, ts + 0.2])
            text("Pico Duck", font="Liberation Sans", valign="center", halign="left", size=ts);
        translate([-width/2, 0])
            text("Kevin Lutzer", font="Liberation Sans", valign="center", halign="left", size=ts);
        translate([-width/2, -(ts + 0.2)])
            text("Revision 2", font="Liberation Sans", valign="center", halign="left", size=ts);
                
    }            
}


// Each label was made with the dimensions of 4mm by 2.666mm 
//generateLabel(3, 2, 0.25, "RST", 1.2); 
generateLabel(4.5, 2, 0.25, "BOOT", 1.2); 
//generateLabel(4, 2.6667, 0.25, "V LO", 1.2);
//generateLabel(20, 10, 0.25, "Kevin Lutzer \n Diode Ring Modulator ", 1.2);
//generateBoardTitle(9, 5, 0.25, 1.2);
