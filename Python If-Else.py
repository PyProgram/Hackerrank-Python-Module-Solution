#!/bin/python3
import math
import os
import random
import re
import sys

r1=range(2,6)
r2=range(6,21)
r3=range(1,101)
num=int((input()))

if num not in r3 :
    exit()
stat=num%2
if stat==1 :
    print("Weird")
elif stat==0 and num in r1 :
    print("Not Weird")
elif stat==0 and num in r2 :
    print("Weird")
elif stat==0 and num>20 :
    print("Not Weird")
