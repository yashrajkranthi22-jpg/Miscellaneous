### 5 V Charger Using a Low Pass Filter
Yashraj Kranthi
September 2026
1 Acquired components from core labs
I took the components required for the charger from core labs on 18th Septem-
ber, 2026.
Figure 1: All components for the charger
The reference PDF for the charger states that the transformer must be a
12-0-12 center-tapped transformer, meaning that there should be 3 wires which
have 12V, 0V and -12V alternating currents from the source 230V alternating
current but, the transformer I got from the core labs only had 230V, 0, 12V
and 0 written on it. I think that it is only a simple 12V step down transformer
instead of 12-0-12 center-tapped transformer.
1
Figure 2: Front view of transformer
Figure 3: Back view of transformer
2
Figure 4: Top view of transformer
2 Learning how the circuit works
2.1 Component list
//update the comp list
3
2.2 Basic voltage flow chart
```
2.3 Measurement list(Not Updated)
```
Figure 5: Checklist of all quantities to be measured using multimeter
2.4 Workings of the full wave bridge rectifier
The four diodes joined in this way act as a full wave bridge rectifier. When
one terminal is positive and the other negative, the circuit works in a way so
as to complete the circuit through the use of forward and backward biases of
the diodes. It works in the same way when the polarities of the terminals are
exchanged.
4
Figure 6: Voltage wavefront after passing trough rectifier
Since the diodes used are not ideal, they are going to cause the Vpeak to
decrease as compared to before passing through the rectifier.
Figure 7: Diodes used in making the rectifier
5
2.5 Capacitor filtering
When the AC voltages are decreasing the capacitor which have already been
charged, will provide voltage to the 7805, hence increasing the minimum voltage
accessible to the 7805 as the minimum voltage it needs is 7.5V.
This leads to the formation of ripple voltage. The wavefront will not be
as long as before as the minimum voltage will increase leading to some sharp
graphs.
Figure 8: V=Vripple
```
Vripple = potential difference between peak and the lowest part of the wave-
```
front.
6
Figure 9: 10 micro farad capacitor used for capacitor filtering
2.6 7805 regulator
It is a voltage regulator which when given a minimum of 7.5V input will give a
nearly constant 5V output.
The excess energy due to voltage reduction will be expelled as heat.
7
Figure 10: The 7805 regulator used for converting rippling DC voltage to 5V
DC
2.7 Updating the circuit diagram
My understanding of the circuit is that when the source voltage from the trans-
former is increasing the circuit is complete and the current flows to the ca-
pacitor which starts charging up to the peak voltage, while the main current
passes straight through the 7805 into whatever device you are powering, and
from there it returns to the transformer hence completing the circuit. When
the source voltage is decreasing there will be a point when it drops below Vca-
pacitor, and when that happens the diodes will act as reverse bias and the
transformer part does not do anything, the capacitor will supply the 7805 with
the voltage and once again when the source voltage is increasing on the next
wave, at some point Vsource=Vcapacitor and the transformer will start working
as normal and the capacitor will start charging again, this cycle will repeat and
lead to formation of a rippling dc voltage. This rippling dc voltage will then
```
enter the regulator(7805) and give a stable 5v dc voltage across the 7805 output
```
and ground.
8
I changed the overall circuit to fit the 12V step down transformer.
Figure 11: Updated circuit
3 Performing theoretical calculations
9
4 Some problems I noticed
4.1 7805 heat dissipation
I learned what junction to ambient thermal resistance means when I was reading
the datasheet for 7805, it is a measure that tells us by how much the junction
temperature inside the 7805 rises as compared to ambient air temperature per
watt of power dissipated.
I also learned what junction temperature is, it refers to the highest temper-
ature inside the instrument where the electrical power is being converted into
heat.
Figure 12: Junction to ambient thermal resistance - Source Texas Instrument
datasheet -https://www.ti.com/lit/ds/symlink/lm7800.pdf
Figure 13: Maximum junction temperature - Source Texas Instrument datasheet
-https://www.ti.com/lit/ds/symlink/lm7800.pdf
10
According to Texas Instrument LM7805 datasheet, the junction to ambient
```
thermal resistance of the 7805 family is around 65◦C/W when left standing(not
```
```
connected to PCB) and around 23.9◦C/W when it is soldered to a PCB(the
```
```
copper rings act as heat sink), a normal phone charger requires a minimum of
```
```
500mA of current the diode I am using(IN4007) has a rating of 1A. Considering
```
the fact that the surrounding temperature can reach 35◦C and that the absolute
maximum junction temperature can only be 150◦C and factoring in an absolute
maximum potential difference of the 7805 as 13V, the maximum load current
can only be around 370mA which is far less that wwhat is required.
It is to be noted that if the junction temperature reaches 150◦C, it will cause
irreversible damage to the 7805.
Figure 14: Current calculation worst case scenario
```
Figure 15: Load current calculation for general case(V7085 = 11V)
```
Even when the 7805 is working within safe limits the 7805 is prone to heating
and prolonged heating of the 7805 can lead to decreased effectiveness and may
lead to permanent damage. Hence, it is better to use a heat sink along with the
7805.
11
Figure 16: The 7805 received from core labs already had a heat sink attached
4.2 Ripple voltage problem
The filtered voltage input for the 7805 must be more than 7.5V. Assume the
minimum filtered voltage supplied is 7.5V an the maximum value of peak voltage
is around 16V. The maximum value of ripple voltage would be -
```
∆Vr(max) = Vpeak − Vin(min) ≈ 16.0 V − 7.5 V ≈ 8.5 V
```
If we factor in the values of the components we have, capacitance = 100
micro farad, ripple frequency = 100 Hz and the formula relating load current
and ripple voltage -
∆Vr ≈ Iload2f C = Iload100 × 100 × 10−6 F = 100 · Iload
```
Iload(max) ≈ 8.5 V100 Ω ≈ 85 mA
```
12
Then the maximum value of load current would be 85mA for a properly
functioning circuit, any load current more than that will lead to problems like
damaging the 7805 and many more. This load current is much lower than what
is needed for a phone charger.
Figure 17: Calculating maximum load current with given specifications
4.3 My later reflection on the problems I thought of
I later realized that both the problems are actually interconnected. They are
both dependent on load current, both the problems complement each other, the
ripple voltage formula gives a maximum safe load current for proper functioning
of the 7805, though the problem of issues faced due to extended period of heating
of 7805 remain the same.
4.4 Simulating the circuit having a 7805 without a heat
sink
If I had connected my phone to the USB output after completing the circuit,
the 7805 would have been subjected to the high filtered DC voltage produced
by the rectifier and capacitor. This voltage could be around 15–17 V, depend-
ing on the transformer output and mains voltage. Even though this is below
the 7805’s absolute maximum input voltage of approximately 35 V, it would
cause significant power dissipation when supplying around 500 mA, potentially
resulting in excessive heating and thermal shutdown or damage. If the 7805
were to fail in a way that allowed its output voltage to rise toward the input
voltage, the phone could then be exposed to a dangerously high voltage and
could potentially be damaged.
Parallel to the overheating, when the phone draws a high current like 500mA,
it leads to a big ripple and the input voltage to the 7805 may fall below 7.5 hence
causing the 7805 to be unable to provide a stable 5V output.
13
The 100 μF capacitor would not impose a strict 85 mA current limit on the
phone. The phone could attempt to draw a much higher current, such as 500
mA, causing the capacitor voltage to fall rapidly and the 7805 to experience
substantial power dissipation. The theoretical ripple equation gives an unre-
alistically large 50 V ripple at 500 mA because its simplifying assumptions no
longer hold at such a heavy load. In practice, the supply voltage would collapse
and the 7805 could overheat and enter thermal shutdown or potentially be dam-
aged. If the 7805 failed in a way that allowed its output to rise toward its input
voltage, the phone could be exposed to the unregulated rectified voltage and
could potentially be damaged.
5 Final theoretical circuit
5.1 Filtering capacitors
Components - 4700μF, 100nF capacitors and a 10kΩ resistor
• R=10kΩ is used to discharge capacitors after turning it off.
• The 4700μF is for filling any voltage disturbances which have low fre-
quency.
• The 100nF is for filling any voltage disturbances which have very high
frequency.
```
• A real capacitor has ESR (Equivalent series resistor) and ESL (Equivalent
```
```
series inductance).
```
• When a high frequency disturbance occurs, the 4700μF gains inductor
```
properties which will resist change in current in short time (V = L di/dt).
```
• The 100nF has much smaller inductance supply the current/charge.
Figure 18: Circuit diagram of filtering capacitors
5.2 7805 section
Components - 0.33μF, 0.1μF, 10μF capacitors, LM7805 regulator
• 0.33μF capacitor is placed very close to the input of the 7805 so as to work
as a source / sink to the 7805 to deal with any disturbances / immediate
current needs.
14
• It is placed close so that it may provide charge fast as the wires also have
an inductance which resist change in current.
• 0.1μF capacitor is placed very close to the output of the 7805 which is simi-
lar to the 0.33μF. It deals with any high frequency disturbances and partly
provides any immediate load current requirement until 7805 responds.
• 10μF capacitor works similar to 4700μF in filtering capacitors part.
• We do not have a capacitor like 100μF before the 0.33μF near the input
for 7805 as the buck pre regulator already has an output capacitor.
Figure 19: Circuit diagram of 7805 section
5.3 Buck pre regulator
It is used to decrease the input voltage of the 7805 so as to decrease the heat
dissipated by the 7805.
5.4 7805 reverse - protection diode
```
Component - Diode(1N4007) Join like this so that if input suddenly becomes 0,
```
the output will have higher potential due to capacitor and so that the current
```
will go through the diode instead of the 7805. (Most current may go through
```
```
diode, not all).
```
Figure 20: Circuit diagram of 7805 reverse - protection diode
5.5 Final 5V smoothing
• 470μF works same as prev cases.
```
• Finally place 100nF very close to TPS2553. (works same as prev cases).
```
15
Figure 21: Circuit diagram of current limiting section
5.6 Current limiting
```
The current limiter(TPS2553) limits current according to what resistor we con-
```
nect to ILIM.
Figure 22: TPS2553 pinout
5.7 Charging port controller
• We need to connect a TPS2514 to d+ and d- to make the USB recognizable
as a charger to the phone.
• We connect a 0.1μF in parallel before connecting to the input pin so
that it acts as a local source for any immediate high frequency current
requirements.
Figure 23: TPS2514 pinout
5.8 USB output indicator
The LED only shows that a voltage enough for it to glow is present, it does not
show that there is 5v nor does it show 500mA of current passing through.
16
Figure 24: Circuit diagram including the led
6 Component list
Figure 25: Component list for new circuit
17
6.1 Final circuit diagram
Figure 26: Final circuit with all components
7 Problems I encountered
7.1 Unavailability of components
The staff at the core labs told me that they do not have TPS2553 and TPS2514
or their equivalent. This majorly changed my circuit design and use, as now I
will have to work without a current limiter and no device to control the D+ and
D- pins of the usb.
7.2 Unavailability of resistors
They also did not have 1KΩ resistors so I have to use a 560Ω resistor.
7.3 Unavailability of capacitors
They did not have 0.33μF capacitors so I am using a 100nF capacitor, they also
did not have 4700μF capacitor so I am using a 2200μF capacitor.
18
8 Making the physical circuit
8.1 Checking step down voltage of transformer
Figure 27: Reads around 13.55V
I first checked the AC voltage across the transformer
8.2 Checking voltage across rectifier
19
8.3 Preliminary soldering
I later realized that I connected the buck converter’s connections wrong as it
was supposed to be a connections from in+ to out+, but I connected in+ and
out+ to a common rectifier voltage bus. This would effectively bypass the buck
converter as it would create a low resistance path from the in+ to out+.
8.4 Incorrect connection
Before checking for the buck output I decided to connect all the capacitors to
ground before I checked the buck output.
This led to errors as after I thought I finished all the connections, I noticed
that some of the capacitors were not even connected to the ground and for some
of the capacitors I connected the positive and negative terminals using a metal
wire which would essentially short the connection.
I had to remove the metal wires and once again make all the proper connec-
tions.
20
8.5 Buck showing 0V
After connecting the major components before the buck, that are the trans-
former, rectifier, filter capacitors by soldering the required connections, when
I connected the multimeter across the out+ and out- of the buck, the reading
showed 0V even though it was not supposed to be zero.
Figure 28: Multimeter voltage reading shows 0V
8.6 After fixing the problem
I tried changing the wires connecting the transformer to the circuit and when I
turned it on, the buck read 17.23V.
I thought of changing the transformer wires because the wires connecting
the transformer and the circuit had broken multiple times before.
Figure 29: After changing the transformer wires
21
Figure 30: Buck output after rotating the screw on the buck to regulate its
output
8.7 Burst capacitor
After getting the buck to work, I went to the hostel and came back at around 3
PM. I first connected the transformer to check if the circuit is still working or
if any wire snapped. As soon as I connected the plug to the extension board,
something on the circuit burst with a pop. At that time I did not know that a
100nF capacitor had exploded.
```
Figure 31: Damage to board after the capacitor burst(rear view)
```
```
Figure 32: Damage to board after the capacitor burst(top view)
```
I later found out that the capacitor that burst was an input filter for the
7805. But this was strange as the 7805 was not even connected to the buck
out+ connection and the capacitor was also not connected to the high volt line.
22
Figure 33: Transformer primary input top view
Looking at the above picture, I thought that there was some relation between
the transformer and the burst capacitor.
Looking at the way the wires connecting the primary section of the and the
plug broke apart, and factoring in the black scorch marks I believed that the
capacitor burst when it came into contact to the exposed wires carrying the
main voltage.
8.8 After the capacitor burst
After the capacitor burst, I had to reconnect the buck wires and the transformer
wires properly as the wires had broken after the burst.
8.9 Buck problem
When I originally measured the voltage across the out+ and out- of the buck,
I got a reading of 17.23V and after rotating it in a direction i got around 19V.
At that time I did not think of the problem that the buck was supposed to be
a step down voltage regulator and the input would be around 15-17V and the
output it gave was more than the input. I later tried rotating it in the opposite
direction hoping to reduce the voltage but even though i rotated it more than
50 times the voltage did not go below 16V. The next day I tried again but the
voltage still did not budge, here I thought that the buck I received was a step
```
up(a boost) instead of a step down.
```
When i told the person in charge at the lab, he tried to set the buck to 9V
output but had the same problem as me, one of his coworkers pointed out that
a buck is supposed to have 2 capacitors while the one I had only had one.
I later got another buck which when adjusted gave me a 9V output.
23
Figure 34: The defective buck having only one capacitor instead of two
Figure 35: New buck I recieved
9 I burnt my finger
I burnt my finger during soldering the components.
24
10 7805 problems
I finished soldering all the components and finally plugged the transformer in
but the voltage across the usb was 9V which is the same as the buck output
voltage.
I first began by checking the transformer voltage.
25
Figure 36: Getting proper transformer step down voltage
Next I checked the potential difference between the in and the gn pins of the
7805 and found it was around 9V which is to be expected as it is connected to
the buck output. I then checked the potential difference between the out and
gnd pins of the 7805 and found it was the same as the buck.
26
Figure 37: Multimeter reading 8.98V
27
Figure 38: Multimeter reading 8.98V
I later checked the potential difference between the in and out pins of the
7805 and noted that it was 0V.
Figure 39: Multimeter reading 0V
To check if I may have caused a short and hence bypass the 7805, I ran the
ohms check with the transformer not plugged in.
I first ran the test for buck out+ and the 7805 in pin, which gave a 0.3
28
reading and was expected as they are connected.
Figure 40: Ohms test on multimeter
Next I ran the test for buck out+ and the 7805 out pin. The result showed
some resistance between the buck and 7805 out pin, this showed that there was
no direct connections between the buck out+ and the 7805 out pin.
Figure 41: Ohms test showing 0.4Ω on multimeter
29
After this I concluded that the 7805 was defective as there was no direct
connections and the output was not 5V.
I removed the 7805 by making major changes in the circuit due to it being
an integral part of the circuit.
Figure 42: Removing the 7805
Figure 43: Defective 7805
30
I tried to get the 7805 replaced and told the person in charge that the 7805
was defective as the output it gave was the same as the input. He told me to
check it using a dc power source and I didn’t really know how to use it so he
helped and we connected the 0-30V source to the input pin and the black gnd
wire below it to the gnd pin of the 7805 and we checked the voltage at the out
pin of the 7805 using a multimeter and it was giving the same voltage as the
input hence proving that the 7805 was defective.
Figure 44: New 7805
11 Updating the circuit
11.1 Removing the 7805
After receiving a message in the group that we could use any component and
that the 7805 was not necessary, I decided to just remove the 7805 and its
respective filter capacitors as they were not needed and only served to further
complicate the circuit. I decided to only use the buck converter as the sole
31
voltage regulator in the circuit and set the output voltage of the buck converter
to 5V.
Figure 45: Removing the 7805 filter capacitors
I decided to leave one 10μF to act as a filter capacitor and a local source/sink
for the usb.
11.2 Configuring the buck
I set the output voltage of the buck to 5V after rewiring the circuit.
32
Figure 46: Checking voltage across the usb using multimeter
11.3 Shorting the D- and D+ pins of the usb
I learned that shorting the D+ and the D- pins of the usb will create a USB
```
Battery Charging (BC) 1.2 — Dedicated Charging Port (DCP). When the D+
```
and D- are shorted, the phone will recognize it as a dedicated charging port
rather than a regular usb port.
11.4 Hot gluing the usb to the perf board
I ho glued the edges of the usb to the perf board, at first I had problems as
when I pressed the trigger after switching it on, there was no glue coming out.
I later realized that I had to wait for some time for the glue to become hot.
33
11.5 Final circuit
Figure 47: Final circuit after all updates
34
11.6 Final ripple voltage calculations
Figure 48: Final ripple voltage after all updates
12 Connecting the phone
I connected my friends phone to the charger and the net current was 1084mA,
it was not the current drawn from the charger but the net current after using
some current for basic functions.
Figure 49: My friends phone
35
12.1 My phone in discharge mode
Figure 50: Uses around 200mA
12.2 After connecting my phone
Figure 51: Draws around 670mA from the charger
36
12.3 Voltage across the usb before connecting my phone
37
12.4 Voltage after connecting my phone
Figure 52: Multimeter reads 4.947V
12.5 Voltage and current after connecting the phone
Figure 53: Draws around 0.67A
38
13 My finger got burnt again
14 Oscilloscopic measurement across filter ca-
pacitor
I initially had difficulty operating the oscilloscope. Through this attempt I
learned the basic purpose of the time base, voltage scale, probe ground and
waveform display. I was not able to obtain a sufficiently reliable quantitative
ripple measurement, so I did not use the oscilloscope result as a final numerical
validation.
39
15 Another finger burn
16 Component measurements
16.1 Perfboard
• Length = 70 mm
• Width = 50 mm
16.2 Transformer
• Length = 78 mm
• Width = 50 mm
• Height = 50 mm
40
16.3 Transformer Mains Cable
• Cable length = approximately 500–800 mm
• Cable diameter = approximately 5 mm
16.4 USB-A Connector
• Relevant body dimension = approximately 12.4–12.6 mm
• Width/depth = approximately 6 mm
• Position from reference edge = approximately 12.5 mm
16.5 Buck Converter – LM2596S
• PCB length = approximately 43.18 mm
• PCB width = approximately 21.08 mm
• Maximum overall component height = approximately 14 mm
16.6 2200μF capacitor
• Diameter = 12.6 mm
• Height = 20 mm
• lead spacing = 5mm
17 3d charger casing creation
I learned some concepts regarding the use of openscad but majority of the
creation of the code for the casing was made using ai tools. I made the the base
design factoring things like ventilation, placement of components, structural
support, division of transformer and main circuit among other things. The AI
assistance was mainly used to convert my requirements and measurements into
a parametric, printable enclosure and to help check the CAD.
17.1 Studying the actual hardware
I used the real charger assembly and photographs to identify the parts that
would have to fit physically. I recorded the perfboard as 70 mm × 50 mm and
noted the measured position of the USB and LED along the 70 mm front edge. I
also recorded the measured 2200 μF capacitor dimensions and the approximate
```
transformer and LM2596 module(buck) envelope.
```
I chose the 70 mm perfboard front edge as the interface datum. The USB
position is 12.5 mm from the left edge of that board and the LED position is 39
mm from the same edge. This was important because the USB and LED both
face the same direction.
41
17.2 Planning component placement
Before working on the detailed enclosure geometry, I thought through where
the major components should go. I decided to keep the transformer in a lower
section and the perfboard/electronics in an upper section. I also wanted the
USB port and LED to be visible from the front without being blocked by the
board-retaining structure. I planned the approximate arrangement as:
• Transformer in the lower compartment
• Perfboard above the transformer section
• Buck converter in a separate supported position in the upper compartment
• USB and LED together on the front face
• A dedicated opening for low-voltage wires through the divider
17.3 Thinking about ventilation and heat
I identified the transformer, rectifier area and buck converter as the areas that
need attention for heat. I learned that ventilation should have a reason and
should not simply be decorative holes.
I thought of making multiple holes for proper ventilation while avoiding big
holes above main wirings, I also wanted to make it so that the hot air rose up
and exited through the top.
17.4 Mechanical retention ideas
I looked at how the parts would actually stay in place after printing. I learned
why a USB connector should not rely only on its solder joints, why the perfboard
should have proper locating/retaining features, and why the transformer should
have mechanical restraint and cable strain relief.
I chose a removable top cover, mechanical board supports, a transformer
clamp arrangement, and a separate buck holder instead of relying on glue alone.
I also wanted the mains cable to enter through a split/U-shaped channel so the
factory-fitted plug would remain outside the enclosure.
17.5 Using AI chatbots for the enclosure implementation
At this stage I used AI chatbots as a CAD-development assistant. I used Chat-
GPT to help translate my measurements, placement requirements, ventilation
ideas, mounting requirements and safety/separation constraints into a struc-
tured OpenSCAD design.
I also used Claude Desktop as part of the OpenSCAD workflow so that
the CAD could be treated as an iterative test-and-correct process rather than
accepting the first generated model.
42
What I personally decided: the component placement logic, front USB/LED
arrangement, two-section architecture, ventilation concept, cable-entry idea,
and the need for serviceability.
What the AI assisted with: writing/refactoring OpenSCAD modules, param-
eterising dimensions, creating printable enclosure parts, generating debug/preview
geometry, and helping organise validation checks.
17.6 Discovering and correcting the USB/LED fit prob-
lem
The original design had a problem near the usb and the led section as in the
physical circuit, the usb and the led are placed along the 7cm edge of the perf
board but in the design, there were some obstructions near the usb placing which
woul not allow the perf board to be placed properly and the measurements were
also wrong as the usb in the design was placed along the 5cm side.
Figure 54: USB obstructions
17.7 Improving the transformer and buck mounting strat-
egy
The transformer needs to be installed before the upper electronics section, so
I used an open-top lower transformer tray and made the divider part of the
removable upper section. This preserves the intended assembly order.
For the buck converter, I used a separate cradle because the exact mounting-
hole coordinates of the actual LM2596 board were not fully measured. The
cradle supports the board while leaving room underneath for solder joints and
wiring.
During the final review I also made the buck cradle fastening explicit: the
cradle is supported by rear support towers tied into the upper shell, with the
cradle secured using M3 screws into heat-set inserts. This is easier to explain
and assemble than leaving the cradle as an unsupported loose platform.
43
17.8 Validation and final review
I learned to separate software validation from physical validation. The CAD
was checked for compilation/export, STL integrity, enclosure geometry, interface
alignment, and the intended assembly relationships.
The final physical checks still include actual perfboard fit, USB insertion
support, LED fit, transformer fit, cable strain relief, lid fit, printer tolerances,
thermal behaviour, and inspection of the mains-side separation.
18 Final Project Outcome
The project progressed from an initial theoretical 7805-based charger concept
to a physically constructed charger using the available components. During
construction I encountered multiple wiring, component and hardware problems
and used multimeter measurements and troubleshooting to identify and correct
them.
The final implemented circuit uses the transformer, bridge rectifier, filtering
components, LM2596 buck converter adjusted to approximately 5 V, USB-A
output and LED indicator.
I subsequently measured the physical dimensions of the major components
and developed requirements for a 3D-printed enclosure, including component
placement, ventilation, mechanical retention, cable management, electrical sep-
aration and serviceability.
I used AI conversational tools to assist with OpenSCAD implementation,
parameterisation, CAD iteration and validation, while the physical measure-
ments, placement requirements and overall enclosure design requirements were
based on my hardware and engineering decisions.
19 Use of AI Tools
AI-based conversational tools were used during the design-development process
for circuit-design discussions, troubleshooting, enclosure ideation, parametric
CAD implementation and iterative design review. Technical component speci-
fications were checked against manufacturer datasheets and relevant technical
references.
44