.start
  prep main
  call 0
halt
resn 2
  .f1
  resn 1
  get 0 ; a
  get 1 ; b
  add
  dup
  set 0
  drop 1
  get 0 ; c
  ret
  drop 1
  ret
resn 0
  .main
  resn 1
  prep f1 ;f1
  get 0 ; a
  push 3
  call 2
  dup
  set 0
  drop 1
  get 0 ; a
  dbg
  drop 1
  ret
