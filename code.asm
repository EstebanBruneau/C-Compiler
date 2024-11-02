.start
  prep main
  call 0
halt
resn 0
  .main
  resn 2
  push 0
  dup
  set 0
  drop 1
.l0
  get 0 ; i
  push 10
  cmplt
  jumpf l1
  get 0 ; i
  dbg
  push 0
  dup
  set 1
  drop 1
.l3
  get 1 ; j
  push 10
  cmplt
  jumpf l4
  get 1 ; j
  dbg
.l5
  get 1 ; j
  push 1
  add
  dup
  set 1
  drop 1
  jump l3
.l4
.l2
  get 0 ; i
  push 1
  add
  dup
  set 0
  drop 1
  jump l0
.l1
  drop 2
  ret
