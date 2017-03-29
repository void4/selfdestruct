start:
set mouse 3840
set mouse2 3840
set one 1
set p1 3041
set p1x 32
set p1y 32
set p1dx 1
set p1dy 1

loop:

;move particle
addi p1y 1

;draw particle
seti p1 0
muli p1 p1y 64
add p1 p1x
seti p1 255

;draw cursor
addi mouse 1 3840
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


jump loop
