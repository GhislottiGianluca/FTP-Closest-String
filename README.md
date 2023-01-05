# FTP Closest String

## Problem description
The **closest string** is an *NP-hard* computational problem, which tries to find the geometrical center of a set of input strings.<br>
More formally, given n length-m strings s1, s2, ..., sn, the closest string problem seeks for a new length-m string s such that d(s,si) ≤ k for all i, where d denotes the Hamming distance, and where k is as small as possible.<br>

### Example
You could find a simple example on wikipedia: https://en.wikipedia.org/wiki/Closest_string#Example


## FTP approach
In this project, an FTP algorithm was realised by adding a parameter **k** as input, transforming the complexity of a problem as a function of these parameters.<br>
This allows the classification of NP-hard problems on a finer scale than in the classical setting, where the complexity of a problem is only measured as a function of the number of bits in the input.
