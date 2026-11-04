## Circuits and Network Analysis EE1101

Department of Electrical Engineering, IIT Hyderabad, India


## Chapter 1

## Frequency Response and Filters

## 1. Concepts of Transfer Function and Frequency Response

Please learn the basic concepts of transfer function, frequency response, passband gain, cut-off or half-power frequency and resonant frequency from the notes given in the class. Just change the term “Maximum passband gain” to “Ideal passband gain”. The ideal passband gain occurs at ω = 0, ω = ∞, and ω = ω0 for low-pass, high-pass, and band-pass filters, respectively. In the case of a band-stop filter, the ideal pass-band gain can be seen at both ω = 0 and ω = ∞.

## 2. Frequency Response Analysis of Different Circuits

Please refer to the notes given in the class.

## 3. Quality Factor Analysis for Different Circuits

The concept of quality factor (symbolized as Qf) is used in two different contexts. First of all, it is used to indicate energy efficiency of an electric circuit with both energy dissipating and energy storing elements based upon the following definition.

The other definition of the quality factor is related to the frequency selectivity of a band-pass or band-stop filter. The frequency selectivity of a filter basically refers to the narrowness of its passband. The higher is the quality factor, the more frequency-selective is the filter. The definition of the quality factor from the point of view of the frequency selectivity appears as follows.

A different symbol (with an extra zero in the subscript) is used to indicate the quality factor that represents frequency selectivity as such a quality factor does not depend on the input signal fre- quency. On the other hand, the quality factor indicating energy efficiency varies with the frequency of the input signal. However, for a band-pass filter implemented with a series RLC circuit, it can be shown that the energy efficiency signifying quality factor at the resonant frequency is equal to the frequency selectivity signifying quality factor [i.e., Qf0 = Qf(ω0)].

For the derivation of quality factors for different circuits, please refer to the notes given in the class. The basic procedure is very simple. You have to express all the voltage and current phasors in terms of any reference phasor (say, current through any particular resistance). Later you have to convert all the phasors into time-domain signals and express energy dissipated or stored in terms of the magnitude and angle of the reference signal.


## 4. Steady-state analysis with Multiple Sources at Different Frequen- cies

Refer to the circuit shown in Fig. 1.1. Here,

vsr,1 = √ 2Vsr,1 cos(ω1t + ϕ1)

Note that each of the sources in the circuit is producing a sinusoidal voltage but the frequency of the voltage outputs of two sources are different. The superposition theorem can be applied to get the time-domain solutions for different quantities. That is,

Circuit shown in Fig. 1.2 needs to be analyzed to find each column on the right-hand side of (1.4). Since the circuit is in a steady-state, Equation (1.4) can alternatively be written as,

I1ejω1t + I2ejω2t + . . . + INejωNt

√

Phasor quantities in (1.5) can be obtained from the phasor-domain representation of the circuit in Fig. 1.2, which is shown in Fig. 1.3. Please note that no phasor value for any voltage or current quantity in Fig. 1.1 exists in this case. Thus, the superposition principle is not applicable in the phasor domain unless all the sources in the circuit are at the same frequency.

*Figure 1.1: A simple RLC circuit fed with voltage sources of different frequencies.*

## 5. Concept of Filter

The series connected voltage sources of different frequencies in Fig. 1.1 essentially represents a non-sinusoidal periodic signal containing harmonic pollutions or unwanted information. Equation (1.7) indicates that the none of the network quantities is also purely sinusoidal as every frequency component of the input signal leaves its effect on any network quantity. However, as per Fig. 1.3, every frequency component observes a different level of amplification or attenuation as the network


*Figure 1.2: Circuit for calculating the contribution of Source k in Fig. 1.1.*

*Figure 1.3: Phasor-domain representation of the circuit in Fig. 1.2.*

responds differently to different frequencies. Moreover, the relative amplification or attenuation of frequency component may be different in different network quantities. Thus, it is possible to suitably tune the network parameters and select the output signal to maximize the effects of certain frequency components while minimizing the effects of other frequency components. The same is referred to as signal filtering. A schematic diagram of the general filtering arrangement is shown in 1.4a. Here, the load can be either a microcontroller or amplifier or a power circuit. In the first two cases, current drawn by load is usually very small. On the other hand, the passband frequencies remain quite separated from the stop-band frequencies in the third case. Therefore, for all the frequencies that exist in the input signal, the filter acts as either an open-circuited path or a short- circuited path. Overall, the output of a filter typically does not significantly vary depending upon the load connected to it. Therefore, the filter design is often carried out by studying its frequency response in the open-circuited condition as per the configuration shown in Fig. 1.4b.

*Figure 1.4: Filter deployment and design.*

## 6. First-Order Low-Pass Filter

The transfer function and frequency response of a low-pass filter are shown in (1.6) and (1.7), respectively.


Expressions of ideal passband gain and cut-off frequency are presented below.

Here, the ideal passband gain corresponds to the gain value at ω = 0. The cut-off frequency is indicated by ωc. Alternatively, we can also use the symbol ωhp as cut-off frequency is also the hal- power frequency. A first-order low-pass filter can be realized with the help of an RL or RC circuit as is shown if Fig. 1.5. Based upon the equivalent RL or RC circuit representation, Qf = τω for a first order low-pass filter.

*Figure 1.5: First-order low-pass passive filters.*

In order to obtain the magnitude and phase plots of the frequency response by using the MATLAB function Filter Frequency Response, set num = [0 0 K] and den = [0 τ 1]. In addition, set plot type = 1 if you want to see the simple frequency response plots [i.e. |Hfr(ω)| vs. ω or ∠Hfr(ω) vs. ω]. On the other hand, if you want to produce the Bode plot [i.e. 20 log10 |Hfr(ω)| vs. log10 ω or ∠Hfr(ω) vs. log10 ω], set plot type = 2. If you want to get the polar plot, set plot type = 3. The polar plot basically shows the real part vs. imaginary part variation with an arrowhead showing the increasing direction of frequency. The third input argument (i.e., wrange) of the given MATLAB function is a 3×1 vector indicating the frequency range to be studied. The frequency range is basically specified by the first and last elements of wrange as a fraction of the cut-off or resonant frequency. The lower boundary is given by the first element, whereas the upper boundary is given by the last element. The middle element indicates the incremental step size of frequency variation (as a fraction of cut-off or resonant frequency) to pick up only finite number frequency values within the chosen range. Output arguments of the MATLAB function are cut-off frequencies, quality factor at the cut-off or resonant frequency, and the ideal passband gain of the filter under consideration.

## 7. First-Order High-Pass Filter

Equations (1.10) and (1.11) present the transfer function and frequency response of a first-order high-pass filter.

Expressions of the ideal passband gain, cutt-off frequency, and quality factor remain the same as those for the first order low-pass filter. For a high-pass filter, the ideal passband gain is obtained


at ω = ∞. Realization of a first-order high-pass filter with the help of a simple RL or RC circuit is illustrated in Fig. 1.6. Please set num = [0 Kτ 0] and den = [0 τ 1] to obtain the frequency response plots of a first-order high-pass filter.

*Figure 1.6: First-order high-pass passive filters.*

## 8. Second-Order Low-Pass Filter

The generalized transfer function and frequency response characteristics of a second-order low-pass filter are shown via Equations (1.12) and (1.13).

The cut-off frequency calculation is shown below, which is again based upon the fact that |Hfr|ideal = |K|.

The RLC circuit-based implementation of a second-order low-pass filter is illustrated in Fig. 1.7. The magnitude/angle or the polar plot of a second order low-pass filter can be obtained by setting num = [0 0 Kω2 n] and den = [1 2ζωn ω2 n].

*Figure 1.7: Second-order low-pass passive filter with an RLC network.*

## 9. Second-Order High-Pass Filter

The transfer function of a second-order high-pass filter is shown in Equation (1.15), whereas Equa- tion (1.16) presents its frequency response function.


(ω2 n − ω2) + j2ζωωn

The cut-off frequency calculation is shown below.

Fig. 1.8 demonstrates the RLC circuit based implementation of a second-order high-pass filter.

Please set num = [0 −K 0] and den = [1 2ζωn ω2 n] to get its frequency response characteristics.

*Figure 1.8: Second-order high-pass passive filter with an RLC network.*

## 10. Second-Order Band-Pass Filter

Equations (1.18) and (1.19) present the transfer function and frequency response function of a second-order band-pass filter.

(ω2 n − ω2) + j2ζωωn

The resonant frequency of second-order band-pass filter is the same as its undamped natural fre- quency (i.e., ω0 = ωn). Two cut-off frequencies exist for a second-order band-pass filter, which can be determined as follows.

The ideal passband frequency response magnitude is obtained at the resonant frequency. It can be seen that,

Fig. 1.9 shows the implementation of a second-order band-pass filter with the help of a series RLC circuit. In order to get the frequency response characteristics of a second-order band-pass filter, set num = [0 2Kζωn 0] and den = [1 2ζωn ω2 n].


*Figure 1.9: Second-order band-pass passive filter with an RLC network.*

## 11. Second-Order Band-Stop/Notch Filter

A second-order band-stop/notch filter has the following transfer function.

The frequency response function obtained after replacing s = jω in the transfer function is shown below.

Similarly to a second-order band-pass filter, a second-order band-stop filter also have two cut-off frequencies of identical expressions as derived below.

As before, ωn indicates the resonant frequency of the filter. However, the implications of the resonant frequency are different between band-pass and band-stop filters. In the case of a band- pass filter, the frequency response magnitude becomes maximum at the resonant frequency, whereas a reverse phenomenon happens for a band-stop filter. The ideal passband gain for a band-stop filter is obtained at both ω = 0 and ω = ∞. Two possible options for the implementation of a band-stop filter by using an RLC network is shown in Fig. 1.10. The passband gain of filter in Fig. 1.10a is unity, and it is less than one for the filter in Fig. 1.10b. Under resonance, the net admittance offered by the parallel LC combination becomes zero. This is opposite to the zero resultant impedance of a series LC combination. Thus, the quality factor of a band-stop filter from the point of view of its frequency selectivity differs from the quality factor of its implementation RLC circuit signifying energy efficiency.

*Figure 1.10: Second-order band-stop/notch passive filter with an RLC network.*
