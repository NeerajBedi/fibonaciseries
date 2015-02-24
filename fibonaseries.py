#!/usr/bin/python3

a,b = 0,1

while(b < 100):
      print(b)
      a,b = b , a + b # First it will add right term then next term will be assigned
      
