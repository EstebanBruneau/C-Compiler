.start
  prep main
  call 0
halt
resn 2
  .power
  resn 0
  get 1 ; b
  push 0
  cmpeq
  jumpf l0
  push 1
  ret
  jump l1
.l0
  get 0 ; a
  prep power ;power
  get 0 ; a
  get 1 ; b
  push 1
  sub
  call 2
  mul
  ret
.l1
  drop 0
  ret
resn 0
  .main
  resn 4
  push 2
  dup
  set 0 ; a
  drop 1
  push 3
  dup
  set 1 ; b
  drop 1
  prep power ;power
  get 0 ; a
  get 1 ; b
  call 2
  dup
  set 2 ; result
  drop 1
  get 2 ; result
  dbg
  drop 4
  ret
