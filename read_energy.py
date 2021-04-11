import sys
import re

args = sys.argv

fin = open("OSZICAR", "rt") #args[2] is the output file name

F = 0.0 # free energy
E0 = 0.0 # ground state energy

while True:
  line = fin.readline()
  if not line:
    break

  match_pattern = re.match("   1 F=", line)
  if match_pattern:
    line_split = line.split(" ")
    line_split = [x for x in line_split if x != ""]
    E0 = float(line_split[4])
    F = float(line_split[2])

print("E0 = " + str(E0))
print("F = " + str(F))

fin.close()


