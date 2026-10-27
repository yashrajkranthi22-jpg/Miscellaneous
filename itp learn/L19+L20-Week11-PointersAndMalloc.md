

## Week 11
ID1063 Introduction to Programming in C
Lectures 19–20: pointers, dynamic memory, long int, string.h

## Announcements
•Lab exam today: report as planned
•Tomorrow (Batch 3, Wed):
•We may have to split into two batches due to unavailability of
machines
•Will account for exam Math for Physics at 5:30pm
•Tentative split:
•3A: BM, IC, ES, CO + more? (2pm-4pm)
•3B: CE, BT, MA (4:30pm-6:30pm)
•Some from 3B may be moved into 3A

Pointers: recap
ID1063  •  Week 11  •  2
int score = 12;
int *location = &score;
printf("%d\n", *location);    /* 12 */
## *location = 20;
printf("%d\n", score);       /* 20 */
printf(“%p”, location);
& gives the address; * accesses that int.

## Copyingpointers
int score = 12;
int *location = &score;
int *other = location;
## *other = 20;
printf("%d %d\n", score, *location);
Predict the two printed values.

Pointers and functions
•We can pass pointers to functions, just like any other
variable
int func_name(int *ptr1, int a, int *ptr2)
•Use case: Can modify the original variables
•Remember arrays? More on this soon.

Pass by value in C
A copied int
addOne(count) changes only a
local parameter.
count in main remains 4.
Suppose ptr is a pointer to count
How do we use it?
A copied address
addOne(int *ptr)
addOne(ptr) gives the function a
pointerto reach count.
Use *ptrto change it.
C copies every argument, including a pointer value.



Changing caller’s variables
ID1063  •  Week 11  •  4
## #include <stdio.h>
void addBonus(int *p, int bonus) {
*p = *p + bonus;
## }
int main(void) {
int score = 12;
addBonus(&score, 5);
printf("%d\n", score);   /* 17 */
return 0;
## }
&score: address
p: copied address
*p: original int

Swap the caller’s variables
## #include <stdio.h>
void swap(int *a, int *b) {
int temp = *a;
## *a = *b;
*b = temp;
## }
int main(void) {
int x = 3, y = 8;
swap(&x, &y);
printf("%d %d\n", x, y);   /* 8 3 */
return 0;
## }
Trace temp,
*a, *b after
each
assignment.

“Return” multiple values
void quotientRemainder(int amount, int divisor,
int *quotient, int *remainder) {
*quotient = amount / divisor;
*remainder = amount % divisor;
## }
int q, r;
quotientRemainder(17, 5, &q, &r);
/* q is 3; r is 2 */
Use pointers to write a function to “return” two values:
Eg. Write a function to compute quotient and remainder?

Pointers and Arrays
•In C, an array is basically a pointer!
•int a[]   is the same internally as int *a
•It stores a pointer to the first location of the array
elements

Pointers and Arrays-II
•Array stores elements contiguously in memory
•a[0], a[1], a[2], .... are one after the other
•Typically accessed as a[i], a[i+1], ... by incrementing a counter
variable i
•Pointers can be incremented too! (pointer arithmetic)
## •int *p
•*(p+1) will go to the *next* memory location based on size of
int
•For double pointers, it moves to the next appropriate location (+
8 bytes?)

Arrays and element addresses
ID1063  •  Week 11  •  9
int data[3] = {10, 20, 30};  /* fragment */
int *p = data;
printf("%d %d\n", data[1], *(p + 1));
printf("%d %d\n", data[1], *(p + 1));
a[i] is equivalent to*(a + i).
An array holds elements; a pointer holds an address.

Arrays vs pointers in functions
void process(int *arr, int size);
void process(int arr[], int size);
void process(int arr[10], int size); // Dimension '10' is completely
ignored
•The above three are internally equivalent for a compiler
•This explains why caller’s array elements are modifiable in
function calls

Differences: arrays and pointers
int arr[3]={1,2,2};
int* ptr = &arr[0];
Arrays are non-modifiable, pointers can be made to point to
different locations.
Other differences:
- sizeof operator
-        &arr vs &ptr?

## Recap: Pointers
•Caller can pass pointers to variables as function arguments
•Can be used to modify the original variables
•Can be used to “return” multiple values from a function
•Can also return pointers from functions, will cover this later
today
•Pointers and array equivalence in C
•The pointer points to the first element of the array
•Pointer arithmetic

Dynamic memory allocation

Storage sized at runtime
Fixed capacity
int marks[100];
Capacity is written in the
declaration.
Dynamic capacity
Read n; request storage for n ints;
check it; use it; free it.
•Option 1: Variable length arrays
•int arr[n];
•Option 2: Dynamic allocation

Why option 2?
•Variable Length Arrays live on the stack memory
•Has some issues
•Stack memory is generally limited(~1MB to ~8MB). Large
VLAs crash the program.
•No error handling possible
•Local to functions (e.g. if you allocate a VLA within a
function)

malloc : Dynamic memory allocation
•Purpose: malloc requests a block of memory from the
heap memory
•Must include #include<stdlib.h>
•Syntax:
int count;
int *ptr = malloc(count* sizeof(int))

malloc : characteristics
•Syntax:
int count;
int *ptr = malloc(count* sizeof(int))
•Properties:
•Initial value is a garbage value
•malloc returns a pointer to the allocated memory location
•(technical) By default, a void* pointer, that is converted to the requested
type
•Returns NULL (a special pointer that can be checked), if the allocation
fails -> allows error handling

Releasing allocated memory
•Purpose: Returns allocated memory back to the system
•Syntax:
free(ptr);
•Heap memory does not delete itself when a function call
ends
•Forgetting to call free() leads to a memory leak
•Good practice: Set the pointer to NULL immediately after
freeing

Allocatingone integer
## #include <stdio.h>
## #include <stdlib.h>
int main(void) {
int *answer = malloc(sizeof(int));
if (answer == NULL) return 1;
## *answer = 42;
printf("%d\n", *answer);
free(answer);
return 0;
## }
malloc →
address or
## NULL
free → release
storage

Allocating an array of size n
int n;
if (scanf("%d", &n) != 1 || n <= 0 || n > 100)
return 1;
int *marks = malloc((size_t)n * sizeof(int));
if (marks == NULL)
return 1;

Variable length arrays vs Dynamically
allocated arrays
•Memory:
•VLA : Stack, small but faster
•malloc : Persists until explicitly released with free()
•Failure handling
•Portability: malloc is also available in C++. VLAs are not.
•VLAs cannot be resized; dynamically allocated ones can
(next class)

## Memory Management Rules
•Every successful malloc must be paired with a free
•Don’t free twice: may lead to unpredictable crashes
•Use sizeof(type) when using malloc, where type is the
requested type
•Use free before reassigning a pointer that is allocated
memory


Returning pointers from Functions
•Syntax: The return type is  a pointer type
int* find_max(float x, int n)
•Why do this: The function can hand back where something
is, not just what is it
•The pointer must point back memory that still exists after
the function returns

Example: Find max and location
•Write a function that returns a pointer to the maximum
element in an array
•Using this pointer find both the maximum element, and its
location

Memory management caution
•Pointers should not return addresses of variables local to the
function, since these are destroyed when it returns
•A pointer to a destroyed variable is a dangling pointer.
•Using it is undefined behaviour: you may get garbage, a crash, or
output that seems to work and then fails later.
int* make_squares(void) {
int sq[5];
for (int i = 0; i < 5; i++)
sq[i] = i * i;
return sq;          /* BUG: sq disappears when the
function returns */
## }

How to fix?
•Option 1: Make the array in the caller function
•Use the function only to fill in the array
•Option 2: Use heap memory
•Memory from malloc lives on the heap. It is not destroyed when
the function returns; it stays until someone calls free.
•So a function can create an array whose size is decided at
runtime and return a pointer to it safely.
•When the function hands back heap memory, the caller
becomes responsible for calling free on it.

Heap memory in functions
int *make_squares(int n) {
int *sq = malloc(n * sizeof(int));
if (sq == NULL)
return NULL;          /* if allocation failed */
for (int i = 0; i < n; i++)
sq[i] = i * i;
return sq;          /* safe: heap memory outlives the fn */
## }

Example 3: Strings, detecting email
•Write a function to find if a given string is an email address
•Check for the presence of ‘@’
•The function will return NULL, to indicate that it is not an
email address