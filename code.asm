.start
  prep main
  call 0
halt
resn 0
  .main
  resn 1
  push 1
  dup
  push 0
  get 0
  dup
  swap
  add
  push 0
  swap
  set 0
  dup
  set 0 ; ptr
  drop 1
  get 0 ; ptr
  get 0
  push 42
  set 0
  get 0 ; ptr
  get 0
  dbg
  push 0
  ret
  drop 1
  ret
