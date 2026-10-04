

Week 8: Functions+Midsem
week

Midsemtheory exam format
•Seating in LHC5/6/13. Details will be posted by tomorrow
## 11am.
•Multiplechoicewithnegative marking (can have up two correct
options)
•-0.25  (for every wrong option marked)
•1markforsingle correct answer, or 0.5 per correct option if two
correct answers are there.
•Check the Qpaperfor exact marking guidelines.
•Fillintheblanks(1-2sentencesperquestion)
•Mark answers with black/blue pen on OMR for the multiple
choice
•ExtraOMRsheetswillnotbeprovidedifyoumakeerrors.

•Roll num:
•Dept Code+digitsof roll
num
•Write actualroll
numberand name on
the space provided

Sample questions



## Functions Recap
int maximum(int first, int second) { //function definition
if (first > second) {
return first;
## }
return second;
## }
int main() {
int a = 73, b;
scanf(“%d”, &b);
int largest = maximum(73, b);  // function call
printf(“Largest number is %d”, largest);
## }

Local variables
int squareplus(int value) {
int ans = value * value;
int result = ans+4;
return result;
## }
Q: Is the variable ‘ans’ available in the main program? If we did printf(“%d”, ans) in the main
program, what would happen?

Pass by value
void addOne(int number) {
number = number + 1;
## }
int main(void) {
int count = 4;
addOne(count);
printf(“Count value is: %d \n”,count);
return 0;
## }
Q: What is printed by the program?
A: Normal variables are passed by value: i.e. only a copy is passed to the function
So, the printed output is still 4, since addOne works on the copy of the count variable.

Function prototypes
int square(int value);   /* prototype */
int main(void) {
int answer = square(5);
return 0;
## }
int square(int value) {
return value * value;
## }
The definition can come later if the prototype is
specified first (a contract).
The prototype is the “contract” that is made visible

Example 2: Composing functions
•If item price is above 2000, add a 10% discount and then
5% tax
•Else directly add tax

Example 3: Nested function calls
int square(int value) {
return value * value;
## }
int sumOfSquares(int first, int second) {
return square(first) + square(second);
## }

## Example 4: Lab 5 P3
•We will look at how to pass arrays as arguments to
functions after the midsem.

## Checking Primality
Write int isPrime(int number)
Start with:
- values less than 2
- a divisor loop
- return 0 or 1
## Test 1, 2, 9, 11.