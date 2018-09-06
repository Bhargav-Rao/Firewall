### Host Based Firewall

The host based firewall reads from a list of rules provided in the input.csv file and then 
validates whether a particular packet is allowed according to the given rules or not. 

> how you tested your solution

Given that it was a single functionality which we were testing, unit testing was the most 
appropriate choice. The FirewallTest.py consists of many sub-tests. As it was clarified earlier 
that the inputs are always valid, the input sanitation tests were avoided. The tests conducted 
were mostly the edge and corner cases. The different test cases were stored in test.csv file 
and are tested against the Firewall. The different test cases were: 

 - All valid values
 - 4 combinations where one was invalid and the others were valid. 
 - The IPs and the ports at the start and the end of the range (as the specifications mentioned 
 that the ranges were inclusive)
 - IPs with different values in the 3rd octet but valid value in the 4th octet. 
 
 > any interesting coding, design, or algorithmic choices you’d like to point out
 
The 60 minutes available was divided into 20 minutes of development time and 40 minutes of 
testing (the other 30 minutes went into this writeup). More time was allotted to testing because
there were a lot of test cases that had to be considered. Due to the time constraint, the best 
approach was to use a hash map (a dictionary). There were four separate branches for the hash map,
one each for the direction x protocol pairs. The ports were made into paired tuples so that they 
could be stored as keys, and a lookup would be easy. 

The IPs were converted to integers and then compared using the comparision operators. In this way
the multi octet spanning IP ranges could also be handled. 
 
 > any refinements or optimizations that you would’ve implemented if you had
   more time
   
The insertion algorithm was something which I wanted to try before time ran out. My idea was to 
use an insertion-sort-like algorithm while adding IPs to the list. This implies that instead of 
just appending the new IP rules to the end of the list, we place the new IP rule in a sorted manner
In this way, if there is an overlap, we can simply ignore that rule, thereby saving storage space.
I tried to implement this but rolled back to the initial approach after the time had ended. 
   
 > anything else you’d like the reviewer to know
 
The challenge was very interesting and good to work on. The sentence "You may use any language of your 
choice and the *standard libraries that come with the language*." (emphasis mine) in the write up 
made me go with Python3. 

----

I'm interested in both the Platform and the Data Team. 