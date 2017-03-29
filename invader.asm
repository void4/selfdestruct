start:
set mouse 1001
set mouse2 1001
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
mov mouse2 mouse
seti mouse 255
mousenotmoved:
;check if particle is at mouse position
jumpn mouse p1 unequal
add p1x 1
unequal:
jump loop
