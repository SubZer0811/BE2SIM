# BE2SIM
This repository contains a python script that converts a Boolean Expression to a .SIM file (circuit netlist description) which can be used in softwares like irsim.

## Running
```
python3 be2sim.py
```

DISCLAIMER: Make sure to use paranthesis wherever possible. <br>e.g. !A.B.C should be writtern as (((!(A)).B).C). The input variables can be any alphabet. The final output is 'out'.The following gates can be used: 
1.+ (OR)
2. . (AND)
3. ! (NOT)

