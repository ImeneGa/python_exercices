# python_exercices
Problems requiring algorithmic resolution, implemented in python

Exercise 1:
Knowing that a prime number is a number which accepts no other divisor than 1 and itself.
How do you know if a number is prime?

Exercise 2:
A perfect number is a number that is equal to the sum of all its divisors except itself.
Find all perfect numbers between 1 and n

Exercise 3:
A Janus number is a number that represents the same value when reading it both ways, example: 78987
Give the Janus numbers between the limits a and b

Exercise 4:
Harshad numbers are numbers divisible by the sum of the digits that compose them. So, in all number bases we find Harshad numbers.
In addition, there are special numbers called complete Harshad because they are Harshad in all bases between 2 and 10, we count them at 4!
Find the first n Harshad numbers in all bases, and also find the 4 prime Harshad numbers.

Exercise 5:
We wish, from a number of 7 positions, to extract the 3 central positions of the number and:
Put them in an elementary object a
Replace them with 0s and put the result in b

Exercise 6:
Convert a base 10 integer to a binary base integer (2)

Exercise 7:
Build a solution that allows us to write a number n in full, with n < 1000

Exercise 8:
Convert a number to Roman numerals.

Exercise 9:
Knowing that a palindrome is a sentence that can be read in both directions, construct the solution that allows you to know if a sentence is a palindrome or not.

Exercise 10:
How to check if two integers a and b are composed of the same digits?

Exercise 11:
From an integer n we would like to obtain two other numbers
a and b
The first will consist of the even digits of n and the second by the digits
odd of n

Exercise 12:
Knowing that two numbers a and b are said to be friends if the sum of the divisors of b is equal to b and the sum of the divisors of b is equal to a.
Show friendly numbers less than 500.

Exercise 13:
Mirror multiplication is such that for two numbers ABC and DE we have ABC * DE = CBA * ED
Find all possible combinations.

Exercise 14:
Among the mathematical curiosities, we find the band of 9s: if you take 3 numbers a, b and c, each of which is composed of 3 digits, and such that a + b = c and if the 9 digits used are 1, 2, 3 , 4, 5, 6, 7, 8, 9 then the sum of the digits constituting c is always equal to 18
Build the solution that will allow you to find all the cases that respect this quirk as well as their number.

Exercise 15:
Do you know what day of the week you were born? The following formula will give you the day of the week corresponding to a given date in the form DDMMYYYY:
day = expression % 7
expression = DD – 1 + |5x / 4| - |x / 100| + |x / 400| + |13(y + 1) / 5|
If MM = 1 or 2
y = MM + 12
x = YYYY - 1
If MM > 2
y = MM
x = YYYY
0 = Sunday, 1 = Monday…
Build the solution to this problem.

Exercise 16:
It can be shown that GCD (a,b) = GCD (b,r) where r is the remainder of the division of a by b. So the search for the GCD (Greatest Common Divisor) of a and b is replaced by the search for the GCD of b and r
If we repeat this process, we obtain pairs (a,b), (b,r), ... increasingly smaller until (g,o) where g is the GCD of a and b
This method is better known as the EUCLID algorithm.
Construct the solution to this problem.

Exercise 17:
Another method close to that of EUCLID is called the NICOMACHOS algorithm.
It is based on subtraction instead of division.
GCD (a,b) = GCD (b, a-b) with a >= b
Build the solution to this problem.

Exercise 18:
The square root of a number a can be obtained by an iterative method using the recurrence relation Xi+1 = ½ (Xi + a / Xi) which converges to the square root of a, i being the number of the iteration .
We will begin the calculation by giving X0 the value a / 2. The calculation stops if
the precision you set has been achieved.
The precision is: |(Xi+1 - Xi) / Xi+1|
Calculate the square root of a number with this method.

Exercise 19:
In asymmetric methods of cryptography (public key encryption), there are 2 keys:
A public key used for encryption
A private key used for decryption
The most popular method is called RSA, which works as follows:
Initially, we must take two prime numbers p and q, to ​​determine them we will take the prime numbers closest to any two random numbers
We calculate n = p * q
We calculate n2 = (p - 1) * (q - 1)
We are looking for a prime number e which is also prime with n2
We look for d such that (e * d) mod (n2) = 1
The pair (e, n) constitutes the public key and the pair (d, n) the private key. Of course, d, p and q must remain secret.
If we want to encrypt the message m with the public key, sending it must apply the formula:
c = m (power e) mod n
And to decrypt the message the receiver will have to apply the formula:
m = c (power d) mod n
Build the solution for this asymmetric encryption.

Exercise 20:
How can you make change for any amount given in centimes but with the minimum number of notes and/or coins?

Exercise 21:
In a small town, a virus begins to spread. On the first day, one person becomes infected. Every day, each infected person infects two others. If the city has 20,000 residents, how many days will it take for the entire city to become infected, assuming there are no recoveries or deaths?
