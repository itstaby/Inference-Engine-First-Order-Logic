# Inference-Engine-First-Order-Logic
Inference Engine First Order Logic

An inference enigine that identifies queries as being facts or not based on the "Resolution" inference method.

Knowledge base for the engine is expressed in First Order Logic.

The input.txt and output.txt are used for representing queries, knowledge base, and answers, as shown:

Format for input.txt:

<NQ = NUMBER OF QUERIES>

<QUERY 1>

…

<QUERY NQ>
  
<NS = NUMBER OF GIVEN SENTENCES IN THE KNOWLEDGE BASE>

<SENTENCE 1>

…

<SENTENCE NS>
  
where

• Each query will be a single literal of the form Predicate(Constant) or ~Predicate(Constant).

• Variables are all single lowercase letters.

• All predicates (such as Sibling) and constants (such as John) are case-sensitive alphabetical strings that
begin with an uppercase letter.

• Each predicate takes at least one argument. Predicates will take at most 100 arguments. A given
predicate name will not appear with different number of arguments.

• There will be at most 100 queries and 1000 sentences in the knowledge base.

• See the sample input below for spacing patterns.

• You can assume that the input format is exactly as it is described. There will be no syntax errors in the
given input.


Format for output.txt:

For each query, determine if that query can be inferred from the knowledge base or not, one query per line:

<ANSWER 1>

…

<ANSWER NQ>

where

each answer should be either TRUE if you can prove that the corresponding query sentence is true given the

knowledge base, or FALSE if you cannot.







Example 1:

For this input.txt:

6

F(Joe)

H(John)

~H(Alice)

~H(John)

G(Joe)

G(Tom)

14

~F(x) | G(x)

~G(x) | H(x)

~H(x) | F(x)

~R(x) | H(x)

~A(x) | H(x)

~D(x,y) | ~H(y)

~B(x,y) | ~C(x,y) | A(x)

B(John,Alice)

B(John,Joe)

~D(x,y) | ~Q(y) | C(x,y)

D(John,Alice)

Q(Joe)

D(John,Joe)

R(Tom)



your output.txt should be:

FALSE

TRUE

TRUE

FALSE

FALSE

TRUE





Example 2:

For this input.txt:

2

Ancestor(Liz,Billy)

Ancestor(Liz,Joe)

6

Mother(Liz,Charley)

Father(Charley,Billy)

~Mother(x,y) | Parent(x,y)

~Father(x,y) | Parent(x,y)

~Parent(x,y) | Ancestor(x,y)

~Parent(x,y) | ~Ancestor(y,z) | Ancestor(x,z)



your output.txt should be:

TRUE

FALSE





Example 3:

For this input.txt:

1

Criminal(West)

6

~American(x) | ~Weapon(y) | ~Sells(x,y,z) | ~Enemy(z,America) | Criminal(x)

Owns(Nono,M1)

Missile(M1)

~Missile(x) | ~Owns(Nono,x) | Sells(West,x,Nono)

~Missile(x) | Weapon(x)

Enemy(Nono,America)

your output.txt should be:

TRUE



