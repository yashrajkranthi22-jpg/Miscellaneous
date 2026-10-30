

Solution Key for Exam-2Circuits and Network Analysis (EE1101)October 12, 2026
General Instructions for Paper Evaluation:
-  If the absolute value of the answer for any question from Section-A is correct although its sign is wrong, half marks
can still be given.
-  No procedure check is needed for the questions in Section-A, and marks should be given only based upon final answers
entered into the table provided.
-  For the questions in Section-A, only the final answers are to be entered into the table that is separately provided.
-  In the case the unit of an answer is not mentioned, the numerical value produced will be checked against the default
SI unit.
-  Minor computational errors may be ignored.
-  A phasor computation would be treated as correct only if both the real and imaginary part (in Cartesian coordinates)
or magnitude and angle (in polar coordinates) of the solution are correct.
-  The step-marking scheme for a question in Section-B should be invoked only if it is found that the solution is incomplete
or the procedure is incomprehensible.
-  The purpose of step marking is basically to give marks instead of deducting marks.
-  Stepwise marks specified in the step-marking scheme for any question cannot further be fractionalized.
-  Network  equations  and  associated  results  produced  without  showing  the  corresponding  labeled  electrical  circuit  or
network graph diagram cannot be checked.
-  It  is  permissible  to  use  a  different  symbol  and  different  reference  direction  for  any  electrical  quantity  involved  in  a
calculation.
-  If the sign of the answer for an electrical quantity related to any question in Section-B is incorrect with respect to its
positive direction defined in the circuit diagram, the particular answer is to be considered grossly erroneous.
-  There is no need to check the mathematical procedure for solving simultaneous algebraic equations.
-  There should not be any marks deduction because of the error propagation from wrongly calculated numerical values
in a step.  However, error propagation because of using wrong equations or circuit model cannot be ignored.
-  If a different procedure is adopted to solve a particular problem, an equivalent step-marking pattern may be created
with reference to the presently suggested step-marking pattern.
Section-A
## Question A.1
The equation given can be rewritten as,
d
## 2
v
dt
## 2
## + 0.5k
dv
dt
## + 16v = 0
In addition, for a critically damped system, damping ratio (i.e., ζ) is one.  Therefore,
ω
## 2
n
= 16  =⇒ ω
n
## = 4
## 2ζω
n
## = 2ω
n
= 0.5k  =⇒ k = 16.
## Question A.2
The steady-state representation of the given circuit is shown in Fig.  1.  Therefore,
i
sr
## (∞) =
## 96
## 16
## = 6 A
Department of Electrical EngineeringIIT HyderabadPage 1 of 12

Solution Key for Exam-2Circuits and Network Analysis (EE1101)October 12, 2026
## −
## +
## 96 V
i
sr
## (∞)
## 16 Ω
## 8 Ω
## Figure 1
## Question A.3
The time-domain expression of the inductor current in a series RL circuit fed with a dc voltage source appears as follows.
i
## L
## =
v
sr
## R
## +
n
i
sr
## (0)−
v
sr
## R
o
e
## −t/τ
## .
Note that,
i
## L
## (∞) =
v
sr
## R
## +
n
i
sr
## (0)−
v
sr
## R
o
e
## −∞/τ
## =
v
sr
## R
## .
Moreover, it is given that i
## L
## (0) = 0.  Therefore,
i
## L
= i
## L
## (∞)
n
1− e
## −t/τ
o
=⇒ i
## L
## (0.1) = 5
n
1− e
## −0.1/0.2
o
## = 1.9673 A.
## Question A.4
## V  = 100∠
π
## 3
V  =⇒ v = 100
## √
2 cos
## 
## 100πt +
π
## 3
## 
V  =⇒ v(0.005) =−100
## √
2 sin
## 
π
## 3
## 
## = 100
r
## 3
## 2
## V
## Question A.5
Refer to the parallel RC network shown in Fig.  2.
i
## C
## R
## AB
v
## +−
## Figure 2
For the given RC network,
## P  =
## V
## 2
## R
Q =−ωCV
## 2
## 
## 
## 
=⇒ τ = RC =−
## Q
ωP
## =−
## Q
2πfP
## .
It is given that f = 50 Hz, P = 100 W, and Q =−80 VAR.  Therefore,
τ =
## 80
2× π× 50× 100
= 0.0025 s.
## Question A.6
## P  = 1.25Q  =⇒ Q = 0.8P.
## Therefore,
cos (φ
v
− φ
i
## ) =
## P
p
## P
## 2
## + Q
## 2
## =
## P
## P
## √
## 1 + 0.8
## 2
## = 0.7809.
Department of Electrical EngineeringIIT HyderabadPage 2 of 12

Solution Key for Exam-2Circuits and Network Analysis (EE1101)October 12, 2026
Section-B
## Question B.1
The equivalent representation of the circuit at t = 0 is shown in Fig.  3.
## −
## +
## 80 V
## 8 Ω
i
## R1
## 5 Ω
i
## R2
i
## R3
## 4 Ω
i
## C
## (0)
## −
## +
## 20 V
i
## R4
## 3 Ω
## 5 A
## +
## −
v
## L1
## (0)
## 2 A
## +
## −
v
## L2
## (0)
## 03
## 21
## Figure 3
A simple branch current analysis can be carried out to determine different network quantities.  the corresponding
network equations are derived below.
KCL at Node-1: i
## R1
− i
## R2
## = 5(1)
KCL at Node-2: i
## R2
+ i
## R3
## = 2(2)
KCL at Node-3: i
## R3
+ i
## R4
## = 2(3)
KVL for the outermost loop:  8i
## R1
## + 5i
## R2
## − 4i
## R3
## + 3i
## R4
## = 60.(4)
From (2) and (3),
i
## R2
= i
## R4
## .(5)
Equation (4) can be simplified based upon the relationship shown in (5).
## 8i
## R1
## + 8i
## R2
## − 4i
## R3
## = 60.(6)
Solutions for i
## R1
, i
## R2
, and i
## R3
obtained from (1), (2), and (6) are produced below.
i
## R1
## = 6.4 A
i
## R2
## = 1.4 A
i
## R3
## = 0.6 A.
Finally, calculations of the derivatives of state variables are shown below.
i
## ′
## L1
## (0) =
v
## L1
## (0)
## 0.008
## = 125× (80− 8i
## R1
## ) = 3600 A/s
i
## ′
## L2
## (0) =
v
## L2
## (0)
## 0.004
## = 250× (80− 8i
## R1
## − 8i
## R2
## ) = 4400 A/s
v
## ′
c
## (0) =
i
c
## (0)
## 0.0001
## = 10000× (−i
## R3
## ) =−6000 V/s
Step marking scheme:
-  One mark for Fig.  3
-  Half-marks for writing at least one KCL or KVL equation correctly for the relevant nodes and loop
Department of Electrical EngineeringIIT HyderabadPage 3 of 12

Solution Key for Exam-2Circuits and Network Analysis (EE1101)October 12, 2026
-  Half-marks for correctly writing other relevant KCL and KVL equations as well
-  Half marks for correctly finding the values of at least two element/mesh currents or node voltages
-  Half marks for correctly finding the values of the other relevant voltage/current quantities as well
-  Half marks for correctly writing the equation to find the value of each derivative quantity
-  Half marks for correctly calculating the value of each derivative quantity
## Question B.2
First of all, we have to determine inductor currents at t = 0.  Circuit shown in Fig.  4 gives the initial inductor currents
as it is assumed that the circuit was in a steady-state before t = 0.  Therefore,
i
## L1
(0+) = i
## L1
## (0) =
## 50
## 10
## = 5 A
i
## L2
(0+) = i
## L2
## (0) =
## 30
## 10
## = 3 A.
## −
## +
## 50 V
i
## L1
## (0)i
## L2
## (0)
## −
## +
## 30 V
## 2 Ω2 Ω
## 8 Ω8 Ω
## Figure 4
The effective circuit diagram for t > is shown in Fig.  5.
## −
## +
## 50 V
## 0.1 H
i
## L1
i
## L2
## 0.2 H
## −
## +
## 30 V
## 2 Ω2 Ω
## 4 Ω
## Figure 5
## Approach 1
The following state-space equations can be derived for the circuit shown in Fig.  5.
## 0.1
di
## L1
dt
## = 50− 4(i
## L1
+ i
## L2
## )− 2i
## L1
## =⇒
di
## L1
dt
## = 500− 60i
## L1
## − 40i
## L2
## (7)
## 0.2
di
## L2
dt
## = 30− 4(i
## L1
+ i
## L2
## )− 2i
## L2
## =⇒
di
## L2
dt
## = 150− 20i
## L1
## − 30i
## L2
## .(8)
Department of Electrical EngineeringIIT HyderabadPage 4 of 12

Solution Key for Exam-2Circuits and Network Analysis (EE1101)October 12, 2026
Equations  (7)  and  (8)  are  to  be  converted  to  algebraic  equations  by  replacing d/dt  operation  with  an  algebraic
coefficient D.  That is,
(D + 60)i
## L1
## + 40i
## L2
## = 500(9)
## 20i
## L1
+ (D + 30)i
## L2
## = 150.(10)
Elimination of i
## L2
leads to the following equations.
(D + 30)(D + 60)i
## L1
## − 800i
## L1
## = (D + 30)× 500− 6000
## =⇒ D
## 2
i
## L1
+ 90Di
## L1
## + 1000i
## L1
## = D× 500 + 9000.
## (11)
Next, we have to convert the algebraic coefficient D back to the d/dt operation. The resultant second-order differential
equation in terms of i
## L1
is shown below.
d
## 2
i
## L1
dt
## 2
## + 90
di
## L1
dt
## + 1000i
## L1
## = 9000.(12)
A particular integral of i
## L1
, which is also its steady-state value, can be found as follows.
i
## L1,PI
## =
## 9000
## 1000
## = 9A.(13)
The complementary function for the solution of i
## L1
takes the following form.
i
## L1,CF
## = K
## 1
e
λ
## 1
t
## + K
## 2
e
λ
## 2
t
## (14)
where, λ
## 1
and λ
## 2
are the solutions of following characteristic equation.
λ
## 2
## + 90λ + 1000 = 0.(15)
## Therefore,
λ
## 1
## =−12.9844
λ
## 2
## =−77.0156.
Thus, the complete solution of i
## L1
takes the following form.
i
## L1
## = (K
## 1
e
## −12.9844t
## + K
## 2
e
## −77.0156t
## + 9) A.(16)
In order to calculate the values of K
## 1
and K
## 2
, both i
## L1
(0+) and i
## ′
## L1
(0+) should be known.  The value of i
## L1
## (0+)
has already been derived.  On the other hand, the value of i
## ′
## L1
(0+) can be obtained with the help of (7).  That is,
i
## ′
## L1
## (0+) = 500− 60i
## L1
## (0+)− 40i
## L2
## (0+) = 500− 60i
## L1
## (0)− 40i
## L2
## (0) = 500− 60× 5− 40× 3 = 80 A/s.
We need to then solve the following equations to get the values of K
## 1
and K
## 2
## .
## K
## 1
## + K
## 2
## = 5− 9 =−4(17)
## 12.9844K
## 1
## + 77.0156K
## 2
## =−80.(18)
The solutions are,
## K
## 1
## =−3.5617 A
## K
## 2
## =−0.4383 A.
Step marking scheme:
-  Half marks for correctly finding the initial value of each inductor current
-  Half marks for Fig.  5
Department of Electrical EngineeringIIT HyderabadPage 5 of 12

Solution Key for Exam-2Circuits and Network Analysis (EE1101)October 12, 2026
-  Half marks for the correct derivation of each of Equations (7) and (8)
-  One mark for the correct derivation of (12)
-  Half marks for the correct calculation of particular integral as in (13)
-  Half marks for correctly finding the general solution as in (16)
-  Half marks for correctly writing each of Equation (17) and (18)
-  Half marks for correctly finding both th coefficient values (i.e., K
## 1
and K
## 2
## )
## Approach 2
Fig.6 shows the Laplace-domain representation of the circuit under consideration.  According to the superposition
## −
## +
## 50
s
## V
## −
## +
## 0.1i
## L1
## (0) V
## 0.1s Ω
## I
## L1
(s)I
## L2
## (s)
## 0.2s Ω
## −
## +
## 0.2i
## L2
## (0) V
## −
## +
## 30
s
## V
## 2 Ω2 Ω
## 4 Ω
## Figure 6
theorem,
## I
## L1
## (s) =
## 50
s
## + 0.1i
## L1
## (0)
## 0.1s + 2 + 4||(2 + 0.2s)
## −
## 
## 
## 
## 30
s
## + 0.2i
## L2
## (0)
## 0.2s + 2 + 4||(2 + 0.1s)
## 
## 
## 
## 
## 4
## 6 + 0.1s
## 
## =
## (50 + 0.5s)(6 + 0.2s)
s(0.02s
## 2
+ 1.8s + s + 20)
## −
## 
## 4(30 + 0.6s)
s(0.02s
## 2
+ 1.8s + s + 20)
## 
## = 50
## 
## (50 + 0.5s)(6 + 0.2s)− 4(30 + 0.6s)
s(s + 12.9844)(s + 77.0156)
## 
## .
## (19)
The expression of I
## L1
(s) can be expressed in partial fraction form as follows.
## I
## L1
## (s) =
## A
s
## +
## B
## (s + 12.9844)
## +
## C
## (s + 77.0156)
## (20)
where,
A = lim
s→0
sI
## L1
## (s) = 50
## 
## (50 + 0.5× 0)(6 + 0.2× 0)− 4(30 + 0.6× 0)
## (0 + 12.9844)(0 + 77.0156)
## 
## = 9(21)
## B =lim
s→−12.9844
sI
## L1
## (s) = 50
## 
## (50− 0.5× 12.9844)(6− 0.2× 12.9844)− 4(30− 0.6× 12.9844)
## (−12.9844)(77.0156− 12.9844)
## 
## =−3.5617(22)
## C =lim
s→−77.0156
sI
## L1
## (s) = 50
## 
## (50− 0.5× 77.0156)(6− 0.2× 77.0156)− 4(30− 0.6× 77.0156)
## (−77.0156)(12.9844− 77.0156)
## 
## =−0.4383(23)
## Hence,
i
## L1
## = (−3.5617e
## −12.9844t
## − 0.4383e
## −77.0156t
## + 9) A.(24)
Department of Electrical EngineeringIIT HyderabadPage 6 of 12

Solution Key for Exam-2Circuits and Network Analysis (EE1101)October 12, 2026
Step marking scheme:
-  Half marks for correctly finding the initial value of each inductor current
-  Half marks for Fig.  5
-  One mark for Fig.  6
-  Half marks for correctly writing the initial expression of i
## L1
(s) [as in the first line of (19)]
-  Half marks for producing the final expression of i
## L1
(s) [as in the last line of (19)]
-  Half marks for correctly showing the partial fraction expansion as in (20)
-  Half marks for the correct calculation of each Coefficients A, B, and C
-  Half marks for correctly showing the expression of i
## L1
as in (24)
## Question B.3
In order to determine the maximum active power that can be drawn by the load impedance, it is first necessary to
find the Thevenin’s equivalent representation of the power supply network in the given electrical circuit.  The power
supply network is enclosed by broken lines in Fig.  7.
## −
## +
## 100∠0 V
## 20∠
π
## 4
## Ω
## −
## +
## 50∠0 V
## 10∠−
π
## 4
## Ω
j5 Ω
## Z
ld
## Power Supply Network
## A
## B
## Figure 7
Thevenin’s voltage of the power supply network is to be obtained from the circuit shown in Fig.  8.  Here,
## 100−
## V
th
## 20∠
π
## 4
## +
## 50−V
th
## 10∠−
π
## 4
## = 0
## =⇒ 100−V
th
+ j100− 2j×V
th
## = 0
## =⇒V
th
## = 100
## 
1 + j
## 1 + 2j
## 
= 60− j20 V.
## (25)
The circuit shown in Fig.  9 is to be analyzed to find the Thevenin’s impedance.  Thus,
## Z
th
− j5
## 20∠
π
## 4
## +
## Z
th
− j5
## 10∠−
π
## 4
## = 1
## =⇒ Z
th
− j5 + 2j× Z
th
## + 10 = 20∠
π
## 4
## =⇒ Z
th
## =
## 10
## √
2 + j10
## √
2− 10 + j5
## 1 + 2j
= 8.4853 + j2.1716 Ω.
## (26)
Fig.  10 shows the single-source equivalent circuit representation of the originally given circuit.  According to the
maximum  power  transfer  theorem  for  the  ac  network,  the  load  impedance  value  for  the  maximum  active  power
Department of Electrical EngineeringIIT HyderabadPage 7 of 12

Solution Key for Exam-2Circuits and Network Analysis (EE1101)October 12, 2026
## −
## +
## 100∠0 V
## 20∠
π
## 4
## Ω
## −
## +
## 50∠0 V
## 10∠−
π
## 4
## Ω
j5 Ω
## 0 A
## −
## +
## V
th
## A
## B
## Figure 8
## 20∠
π
## 4
## Ω10∠−
π
## 4
## Ω
j5 Ω
## 1 A
## −
## +
## Z
th
## × 1
## A
## B
## Figure 9
transfer can be calculated as follows.
## Z
ld
## = Z
## ∗
sr
## =⇒
## (
## R
ld
## = 8.4853 Ω
## X
ld
## =−2.1716 Ω
## (27)
Subsequently, the load reactive power consumption under the maximum active power transfer can be calculated as
follows.
## Q
ld
## =




## V
th
## Z
th
## + Z
ld




## 2
## X
ld
## =−2.1716×
## 60
## 2
## + 20
## 2
## (8.4853 + 8.4853)
## 2
## =−30.1610 VAR(28)
## +
## −
60− j20 V
8.4853 + j2.1716 Ω
## Z
ld
## Figure 10
Department of Electrical EngineeringIIT HyderabadPage 8 of 12

Solution Key for Exam-2Circuits and Network Analysis (EE1101)October 12, 2026
Step marking scheme:
-  One mark for Fig.  8
-  One mark for writing equations forV
th
calculation
-  Half marks for correctly finding the value ofV
th
-  One mark for Fig.  9
-  One mark for writing equations for Z
th
calculation
-  Half marks for correctly finding the value of Z
th
-  One mark for the maximum power calculation
## Question B.4
The particular problem can be solved in two different ways.
## Approach 1
An equivalent circuit representation of Circuit-2 given in the question is shown in Fig.  11.  Here, voltage sources are
replaced with equivalent current sources by means of Norton’s theorem.
## 8 Ω
## −
## +
## V
x
## I
x
## B
## A
## Network X
(Linear+Bilateral
+Passive)
j5 Ω−j10 A
## D
## C
## 10∠
π
## 3
## Ω
## 2∠−
π
## 6
## A
## EF
## Figure 11
A modified representation of the reference circuit results is shown in Fig.  12.
## 10∠0 A8 Ω
## B
## A
## Network X
(Linear+Bilateral
+Passive)
j5 Ω
## −
## +
j20 V
## D
## C
## 10∠
π
## 3
## Ω
## +−
## 10∠
π
## 2
## V
## EF
## Figure 12
According to the superposition principle, results for the circuit in Fig.  11 can be obtained by suitably combining
results from the circuits shown in Fig.  13.  On the other hand, solutions for
## V
x,1
andV
x,2
can directly be obtained
Department of Electrical EngineeringIIT HyderabadPage 9 of 12

Solution Key for Exam-2Circuits and Network Analysis (EE1101)October 12, 2026
by applying the reciprocity theorem.  Therefore,
## V
x,1
## = 10∠
π
## 2
## V  =⇒
## I
x,1
## =
## 10∠
π
## 2
## 8
## = 1.25∠
π
## 2
## A
## V
x,2
## = 20∠
π
## 2
## V  =⇒I
x,2
## =
## 20∠
π
## 2
## 8
## = 2.5∠
π
## 2
## A.
The final calculation ofI
x
based upon the superposition theorem is shown below.
## I
x
## =
## 
## −2∠−
π
## 6
## 10∠0
## 
## I
x,1
## +
## 
## 10∠
π
## 2
## 10∠0
## 
## I
x,2
## =−0.25∠
π
## 3
+ 2.5∠π =−2.6250− j0.2165 A = 2.6339∠− 3.0593 A.
## 8 Ω
## −
## +
## V
x,1
## I
x,1
## B
## A
## Network X
(Linear+Bilateral
+Passive)
j5 Ω
## D
## C
## 10∠
π
## 3
## Ω
## 10∠0 A
## EF
## (a) Circuit-1
## 8 Ω
## −
## +
## V
x,2
## I
x,2
## B
## A
## Network X
(Linear+Bilateral
+Passive)
j5 Ω10∠0 A
## D
## C
## 10∠
π
## 3
## Ω
## EF
## (b) Circuit-2
## Figure 13
Step marking scheme:
-  Two marks for Fig.  11
-  One mark for Fig.  13a
-  One mark for Fig.  13b
-  Half marks for
## I
x,1
calculation
-  Half marks forI
x,2
calculation
-  One mark forI
x
calculation
## Approach 2
The  current  source  in  Circuit-1  specified  in  the  question  can  be  replaced  with  a  voltage  source  resulting  in  the
equivalent circuit representation shown in Fig.  14.  The basis of such an equivalent representation is the Thevenin’s
theorem.
In order calculate the value ofI
x
for Circuit-2 specified in the question, the simpler circuits shown in Fig.  14 may
first be analyzed.  According to the reciprocity theorem based upon the results shown in Fig.  15,
## I
x,1
## = 1∠
π
## 6
## A
## I
x,2
## = 4∠0 A.
Department of Electrical EngineeringIIT HyderabadPage 10 of 12

Solution Key for Exam-2Circuits and Network Analysis (EE1101)October 12, 2026
## 8 Ω
## −+
## 80∠0 V
## B
## AA
## ′
## Network X
(Linear+Bilateral
+Passive)
## 4∠0 A
j5 Ω
## D
## CC
## ′
## 1∠
π
## 6
## A
## 10∠
π
## 3
## Ω
## E
## E
## ′
## F
## Figure 14
Finally, according to the superposition theorem,
## I
x
## =
## 
## −20∠
π
## 6
## 80∠0
## 
## I
x,1
## +
## 
## −50
## 80∠0
## 
## I
x,2
## =−0.25∠
π
## 3
+ 2.5∠π =−2.6250− j0.2165 A = 2.6339∠− 3.0593 A..
## 8 Ω
## I
x,1
## B
## AA
## ′
## Network X
(Linear+Bilateral
+Passive)
j5 Ω
## D
## CC
## ′
## +
## −
## 80∠0 V
## 10∠
π
## 3
## Ω
## E
## E
## ′
## F
## (a) Circuit-1
## 8 Ω
## I
x,2
## B
## AA
## ′
## Network X
(Linear+Bilateral
+Passive)
## +−
## 80∠0 V
j5 Ω
## D
## CC
## ′
## 10∠
π
## 3
## Ω
## E
## E
## ′
## F
## (b) Circuit-2
## Figure 15
Step marking scheme:
-  Two marks for Fig.  14
-  One mark for Fig.  15a
-  One mark for Fig.  15b
-  Half marks forI
x,1
calculation
-  Half marks forI
x,2
calculation
-  One mark for
## I
x
calculation
-Solution Key Ends-
Department of Electrical EngineeringIIT HyderabadPage 11 of 12

Solution Key for Exam-2Circuits and Network Analysis (EE1101)October 12, 2026
Answer Table for Section-A.
Question No.Answer
## Question A.116
## Question A.26 A
## Question A.31.9673 A
## Question A.4−100
q
## 3
## 2
## V
Question A.50.0025 s
## Question A.60.7809
Department of Electrical EngineeringIIT HyderabadPage 12 of 12