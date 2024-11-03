.start
  prep main
  call 0
halt
resn 0
  .main
  resn 0
  push 1
  push 1
  or
  jumpf l0
  push 1
  dbg
  jump l1
.l0
.l1
  push 0
  ret
  drop 0
  ret
