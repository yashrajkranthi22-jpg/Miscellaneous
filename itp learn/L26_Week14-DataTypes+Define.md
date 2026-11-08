

## Week 14
ID1063 Introduction to Programming in C
## Lecture 26: Looking Ahead

## Announcements
•Theory exam: Wed Nov 11
•Lab exam: Sat, Nov 14
•Results from midsemwill be declared soon (moodle?)
•Practice questions on pointers, structs, file I/O will be
posted over the weekend to try out.

Inclusions for endsem
•Mostofthecontent of today’s slides are not part of the
endsemtheory syllabus.
•Unitsthatareincluded :
•Data types and formats: int types, float and related types
•#define:named constants
•The rest of the material is there for you to explore further
if interested.

## Recap
•File IO writing to a file:
•Readingfromafile(fscanf):
FILE *out = fopen("report.txt", "w");
if (out == NULL)
return 1;
fprintf(out, "Roll Name Marks\n");
fprintf(out, "%d %s %.1f\n", s.roll, s.name, s.marks);
fclose(out);
Student s;
while (fscanf(fp, "%d %19s %lf",
&s.roll, s.name, &s.marks) == 3)
printf("%s has %.1f\n", s.name, s.marks);

Read using fgets and sscanf
•Robust: using a combination of fgets and sscanf
char line[100];
Student s;
while (fgets(line, sizeofline, fp) != NULL) {
if (sscanf(line, "%d %s %lf",
&s.roll, s.name, &s.marks) == 3)
printf("%s has %.1f\n", s.name, s.marks);
else
printf("Skipping bad line: %s", line);
## }

Data types and formats
(beyond int, float, double and char)

More integer types
•Integer types differ in size, and so in the range of values they can hold.
TypeSize (bytes)*Range (about)printf
char
1−128 to 127
## %cor %d
short
2−32,768 to 32,767
## %hd
int
4±2.1 billion
## %d
long
8 (4 on Windows)±9.2 ×10^18
## %ld
long long
## 8±9.2 ×10^18
## %lld
unsigned int
40 to 4,294,967,295
## %u
size_t
80 and up: sizes and counts
## %zu
•*C fixes only minimum sizes; check withsizeof(long).
•limits.hgives INT_MAX, LONG_MAX, ...

Unsigned types and overflow
•unsigned: no negative values, twice the positive range. Arithmetic
wraps around.
unsigned int u = 0;
u = u -1;
printf("%u\n", u);            /* 4294967295 */
long longbig = 3000000000LL; /* too big for int */
printf("%lld\n", big);        /* 3000000000 */
•Going past INT_MAXin a signed intis undefined: the result cannot be
trusted.
•Choose a type wide enough for your largest value; LLmakes a constant
long long.

Floating-point and other types
TypeSizePrecision / valuesprintfscanf
float
4about 6-7 digits
## %f%f
double
8about 15-16 digits
## %f%lf
long double
## 16*more (varies)
%Lf%Lf
bool(stdbool.h)
## 1
trueor false%d
## —
float f = 0.1f;
double d = 0.1;
printf("%.10f %.10f\n", f, d);
## /* 0.1000000015 0.1000000000 */
•Most decimals are stored approximately: prefer double, andnever test
floating values with ==.

Format specifiers summary
## Typeprintfscanf
int/ unsigned int%d/ %u%d/ %u
long/ long long%ld/ %lld%ld/ %lld
size_t%zu%zu
char%c" %c"(space skips whitespace)
string (chararray)%s%19s(with a width!)
float/ double%f/ %f%f/ %lf(note the l)
pointer, hex, a % sign
## %p, %x, %%
## —
•A wrong specifier is a silent bug, asautomatic conversion can lead to
unexpected results.

Summary of widthand precision in printf
•Between %and the letter: a width(minimum characters), -to left-align,
.nfor precision.
FormatValueOutput (brackets show the width)
## %5d
## 42
## [   42]
## %-5d
## 42
## [42   ]
## %05d
## 42
## [00042]
## %8.2f
## 3.14159
## [    3.14]
## %.3e
## 123456.789
## [1.235e+05]
## %-10s
"Arjun"
[Arjun]

## #define
(named constants and macros)

Named constants
•Can define constants to use later. Do this at the start of the file before
main.
#define MAX_STUDENTS 100
#define LINE_MAX100
#define PASS_MARK    40.0
## ...
Student cls[MAX_STUDENTS];
char line[LINE_MAX];
## ...
if (cls[i].marks < PASS_MARK)
result = "FAIL";
•Gives clarity to code. Can
change pass mark in one place
to reflect throughout.
•Style: names in CAPITALS. No =
and no ;.

How it works: text replacement
•The preprocessorreplaces the names with their text before compiling.
Written:What the compiler sees
#define MAX 100
Student cls[MAX];
if (n < MAX)
Student cls[100];
if (n < 100)
•A stray ;is copied too:
•#define MAX 100;turns cls[MAX]into cls[100;], and gives a
compile error.
Student cls[100];
if (n < 100)

Macros with parameters
#define SQUARE(x) ((x) * (x))
printf("%d\n", SQUARE(5));        /* 25 */
printf("%d\n", SQUARE(2 + 3));    /* 25 */
DefinitionSQUARE(2 + 3) becomesValue
#define SQUARE(x) x * x2 + 3 * 2 + 3
## 11
#define SQUARE(x) ((x) * (x))((2 + 3) * (2 + 3))
## 25
•A macro is text substitution: always put brackets around each
parameter and the whole body.

Some topics not covered

Programs in several files
•Real programs have thousands of lines: one file is hard to read, test and
share.
•Group related code into a module: a header student.hsays whatit
offers; student.csays how.
•Any other file #includes the header and can then use the type and
call the functions.
student.h
types, prototypes
student.c
function bodies
main.c
uses the module
both: #include "student.h"

A minimal example: three files
student.h(declarations)
#ifndef STUDENT_H
#define STUDENT_H
typedef struct {
int roll;
char name[20];
double marks;
## } Student;
void printStudent(const Student *sp);
## #endif
student.c(definitions)
## #include <stdio.h>
## #include "student.h"
void printStudent(const Student *sp)
## {
printf("%d %s %.1f\n", sp->roll,
sp->name, sp->marks);
## }
main.c
## #include "student.h"
int main(void)
## {
Student s = {101, "Arjun", 72.5};
printStudent(&s);
return 0;
## }
•Output: 101 Arjun72.5
•Both .cfiles include the header

Compile each file, then link
gcc-c student.c# student.c-> student.o
gcc-c main.c# main.c-> main.o
gccmain.ostudent.o-o app     # link the pieces into one program
## ./app
student.cstudent.o
main.cmain.o
app
compile (-c)link
•Shortcut: gcc-Wall main.cstudent.c-o appdoes all three
steps at once.
•After editing only student.c, only it needs recompiling; the tool make
automates this.

## Structure
FilePut hereExample
student.h
types, function prototypes, #define
constants
void printStudent(const Student
## *sp);
student.c
function bodies; #includeits own
header
void printStudent(...) { ... }
main.c
main; #includethe headers it uses
## #include "student.h"
MistakeWhat gcc says
gcc main.c -o app(forgot student.c)undefined reference to `printStudent' (from the linker)
main.cwithout #include "student.h"error: unknown type name 'Student'
Header without #ifndef, included twiceerror: conflicting types for 'Student'

Command-line arguments
•main can receive arguments too!
•maincan be passedthe words typed after the program name.
int main(int argc, char *argv[])
## {
if (argc!= 2) {
fprintf(stderr, "usage: %s file\n", argv[0]);
return 1;
## }
FILE *fp= fopen(argv[1], "r");    /* the user's file */
## ...
## }
Typed commandargcargv[0]argv[1]
./report class.txt
## 2
## "./report""class.txt"

2D arrays on the heap: int **
int **m = malloc(rows * sizeof(int *));  /* row pointers */
for (int i= 0; i< rows; i++)
m[i] = malloc(cols * sizeof(int));   /* each row */
m[1][2] = 7;                             /* like a 2D array */
for (int i= 0; i< rows; i++)
free(m[i]);                          /* rows first */
free(m);
m
m[0]
m[1]7
m[2]

More on pointersto pointers
•Can pass the pointer’s address: e.g.an int **.
void makeArray(int **p, int n)
## {
*p = malloc(n * sizeof(int));   /* changes the caller's pointer */
## }
int *a = NULL;
makeArray(&a, 10);                  /* a now points to 10 ints*/
•Same rule as swap(int *x, int *y): to change something, pass its
address.
•An array of strings is an array of pointers: char *names[] =
{"Asha", "Ravi", "Meera"};
•names[1]is "Ravi"; argvin mainis exactly this kind of array.

Redirection, pipes and stderr
•Can “redirect” stdin and stdout from/to files, instead of keyboard and
screen
## Commandstdinstdout
## ./upper
keyboardscreen
./upper < class.txt
class.txtscreen
./upper < class.txt > out.txt
class.txtout.txt
./upper < class.txt | ./count
class.txtinput of ./count
•A pipe | sends one program’s output into the next one’s input.
•Error messages go to stderr (fprintf(stderr, ...) or perror),
so they still reach the screen when stdout is redirected.

Tools that find bugs for you
ToolWhat it finds
gcc -Wall -Wextra
suspicious code: unused variables, wrong printf formats,
## ...
gcc -g -fsanitize=address
reading or writing outside an array; use after free
valgrind ./prog
memory leaks (malloc without free), uninitialised values
gdb ./prog
run step by step, stop at a line, print variables
Example: one past the end of a heap array
int *a = malloc(5 * sizeof(int));
a[5] = 1;                      /* line 5: one past the end */
ERROR: AddressSanitizer: heap-buffer-overflow
WRITE of size 4 ...
#0 ... in main oob.c:5

Good to know (1)
TopicWhat it isExample
Function pointers and
qsort
pass a function as an argument; the
library sorts any array using your
comparison function
qsort(cls, n,
sizeof(Student), byMarks);
Binary files
write whole structs as raw bytes; jump
straight to the k-th record
fwrite, fread, fseek
enum
named integer constants that belong
together
enum Result { FAIL, PASS
## };

Good to know (2)
TopicWhat it isExample
staticlocal variables
keep their value between calls of the
function
static int count = 0;
Global variablesvisible to every function; use sparinglylong calls = 0;
snprintf
build a string safely, with a size limit
snprintf(buf, sizeof buf,
"report_%d.txt", roll);
math.h, rand
sqrt, pow(link with -lm); random
numbers
srand(time(NULL)); d = rand()
## % 6 + 1;
limits.h, overflow
an inthas a largest value; going past
it is undefined
INT_MAXis 2147483647 (typically)

More: Data structures,
algorithms

How much work?
•The same answer can cost very different amounts of work.
TaskSimple wayBetter way
fib(40)
331,160,281 calls (plain
recursion)
79 calls (remember answers)
Find a roll number among
1,000,000 sorted ones
up to 1,000,000 checks (one
by one)
about 20 checks (binary
search)
long long memo[100];                /* 0 means: not computed yet */
long long fibMemo(int n)
## {
if (n <= 1)
return n;
if (memo[n] == 0)
memo[n] = fibMemo(n -1) + fibMemo(n -2);
return memo[n];
## }

Linked lists
•The chain of people from Lecture 24, with the pointer called next: a
linked list.
Node *pushFront(Node *head, int value)
## {
Node *n = malloc(sizeof(Node));
if (n == NULL)
return head;
n->data = value;
n->next = head;        /* point to the old first node */
return n;              /* the new head */
## }
head = pushFront(head, 10);
head
## 102030
## NULL
new node

Stacks, queues and trees
•Each one is a rule for how data goes in and comes out. All can be built
from arrays or linked nodes.
StructureRuleLike ...Used for
Stacklast in, first out (push, pop)a pile of platesfunction calls, undo
Queuefirst in, first outa ticket-counter lineprint jobs, scheduling
Binary tree
each node has up to two
children
a family treefast searching, sorting
•You have already used a stack: the call stackthat held the waiting calls
of factand fib.

Binary search trees
•Smaller keys go left,larger keys go right: each step skips half of what is
left.
int contains(TreeNode *t, int key)
## {
if (t == NULL)
return 0;                 /* not found */
if (key == t->key)
return 1;                 /* found */
if (key < t->key)
return contains(t->left, key);
return contains(t->right, key);
## }
## 8
## 310
## 16
contains(root, 6): 8 → 3 → 6
•Recursion with two self-pointers, like the family tree in Lecture 24, but
only one branch is followed.