.start
  prep main
  call 0
halt
resn 0
  .main
  resn 2
  push 42
  dup
  set 0 ; x
  drop 1
  get 0 ; x
  dbg
  push 0 ; address of x
  dup
  set 1 ; ptr
  drop 1
  get 1 ; ptr
  dbg
  get 1 ; ptr
  get 0
  push 43
  set 0
  get 0 ; x
  dbg
  get 1 ; ptr
  get 0
  dbg
  get 1 ; ptr
  dbg
  push 0
  ret
  drop 2
  ret
