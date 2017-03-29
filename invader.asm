start:
set mouse 3840
set mouse2 3840
set one 1
set p1 3041
set p1x 32
set p1y 32
set dirx 0
set diry 0
set walll 2
set wallr 62
loop:

;move particle
jumpe dirx one eright
addi p1x 1
jump eleftright
eright:
subi p1x 1
eleftright:

jumpe diry one eup
addi p1y 1
jump eupdown
eup:
subi p1y 1
eupdown:

;draw particle
seti p1 0
muli p1 p1y 64
add p1 p1x
seti p1 255

set collision 0

;draw cursor
addi mouse 1 3840
;jumpe mouse mouse2 mousenotmoved
seti mouse2 0
addi mouse2 1
seti mouse2 0
subi mouse2 2
seti mouse2 0
addi mouse2 1
mov mouse2 mouse

jumpn mouse p1 check1
set collision 1
check1:

seti mouse 255
addi mouse 1
jumpn mouse p1 check2
set collision 1
check2:

seti mouse 255
subi mouse 2
jumpn mouse p1 check3
set collision 1
check3:

seti mouse 255
addi mouse 1
;mousenotmoved:

;check if particle is at mouse position
jumpn collision one unequal
set diry 1
sub dirx one dirx
jump endif

unequal:
jumpg p1y one skip
set diry 0
skip:
endif:

;check for wall collision
jumpg p1x walll skipleft
set dirx 1
skipleft:

jumpg wallr p1x skipright
set dirx 0
skipright:



jump loop
