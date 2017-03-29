start:
set mouse 1001
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
seti mouse 0
add mouse 1 offset
seti mouse 255

;check if particle is at mouse position
;jumpe mouse p1 equal

jump loop
