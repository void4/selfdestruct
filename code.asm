start:
set ball 4046
set width 64
set mouse 1000
loop:
sub ball width
draw:
seti ball 255
seti mouse 0
mov mouse 3
seti mouse 128
jump loop
