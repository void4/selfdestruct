start:
set mouse 3840
set mouse2 3840
set offset 3840
set one 1
set sixtyfour 64
set sixty 60
set p1 3041
set p1x 32
set p1y 32
set p1dx 1
set p1dy 1
set dir 0
set dummy 2
loop:

;move particle
jumpe dir one else
add p1x p1dx
add p1y p1dy
jump eif
else:
sub p1x p1dx
sub p1y p1dy
eif:

;draw particle
seti p1 0
mul p1 p1y sixtyfour
add p1 p1x
seti p1 255

;draw cursor
add mouse 1 offset
jumpe mouse mouse2 mousenotmoved
seti mouse2 0
addi mouse2 1
seti mouse2 0
subi mouse2 2
seti mouse2 0
addi mouse2 1
mov mouse2 mouse
seti mouse 255
addi mouse 1
seti mouse 255
subi mouse 2
seti mouse 255
addi mouse 1
mousenotmoved:

;check if particle is at mouse position
jumpn mouse p1 unequal
set dir 1
jump endif
unequal:
jumpg p1y one skip
set dir 0
skip:
endif:
jump loop
