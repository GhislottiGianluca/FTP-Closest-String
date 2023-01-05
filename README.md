# FTP Algorithm for Closest String problem

## Problem description
The **closest string** is an *NP-hard* computational problem, which tries to find the geometrical center of a set of input strings.<br>
More formally, given n length-m strings s1, s2, ..., sn, the closest string problem seeks for a new length-m string s such that d(s,si) ≤ k for all i, where d denotes the Hamming distance, and where k is as small as possible.<br>

### Example
You could find a simple example on wikipedia: https://en.wikipedia.org/wiki/Closest_string#Example


## FTP approach
In this project, an FTP algorithm was realised by adding a parameter **k** as input, transforming the complexity of a problem as a function of this parameter.<br>
**k** is fixed at a small value and the growth of the function over k is relatively small then such problems can still be considered "tractable" despite their traditional classification as "intractable". The **Closest String** problem can be solved by algorithms that are exponential only in the size of a fixed parameter while polynomial in the size of the input; hence the name **fixed-parameter tractable (fpt-)algorithm**, because the problem can be solved efficiently for small values of the fixed parameter.<br>
This allows the classification of NP-hard problems on a finer scale than in the classical setting, where the complexity of a problem is only measured as a function of the number of bits in the input.<br>

## How to run it
### Clone the project repository:
      git clone https://github.com/GhislottiGianluca/FTP-Closest-String.git

### Execute the algorithm
#### First option
Run the script:

      python FTP-CS.py

Use the *flask application* that I already made, making a post request at this URL:

      http://localhost:5000/FTP-Closest-String
      
Finally passing as the body of the request a json of this form:

      {
        "string_set": ["str1", "str2", "str3", "ecc"],
        "d": n,
        "first_string": "str"
      }
      
The endpoint will return a json containing the result in this form:

      {"result": "str"}
      
#### Second option
Write a data initialisation script yourself and use the functions I have written to observe the results of the algorithm.
