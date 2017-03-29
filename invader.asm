start:
set mouse 3840
set mouse2 3840
set offset 3840
set sixtyfour 64
set p1 1002
set p1x 32
set p1y 32
set p1dx 0
set p1dy 1
loop:
seti p1 0
add p1x p1dx
add p1y p1dy
mul p1 p1y sixtyfour
add p1 p1x
seti p1 255
add mouse 1 offset
jumpe mouse mouse2 mousenotmoved
seti mouse2 0
addi mouse2 1
seti mouse2 0
subi mouse2 1
mov mouse2 mouse
seti mouse 255
addi mouse 1
seti mouse 255
subi mouse 1
mousenotmoved:
;check if particle is at mouse position
jumpn mouse p1 unequal
add p1x 1
unequal:
jump loop
