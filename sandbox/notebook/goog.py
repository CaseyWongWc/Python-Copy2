yes=f" '\n _     ___\n#_~`--'__ `===-,\n`.`.     `#.,//\n,_|_|     ## #《\n`__.__    `####《\n     ~~< ,###'~\n        》##'\nWolves\n'"
yes
# val:  '
# val:  _     ___
# val: #_~`--'__ `===-,
# val: `.`.     `#.,//
# val: ,_|_|     ## #《
# val: `__.__    `####《
# val:      ~~< ,###'~
# val:         》##'
# val: Wolves
# val: '
with """ '\n _     ___\n#_~`--'__ `===-,\n`.`.     `#.,;《\n,_|_|     ## #《\n`__.__    `####《\n     ~~< ,###'~\n        》##'\nWolves\n'""" as f:
  print("hello")
  # out: hello
  # f.out: hello
with bash:
  ls -alf
  # out: total 8
  # out: drwxr-xr-x 1 runner runner 506 May  8 04:11 .
  # out: drwxr-xr-x 1 runner runner 472 May  8 03:19 ..
  # out: -rw-r--r-- 1 runner runner  15 May  8 04:11  '
  # out:  _     ___
  # out: #_~`--'__ `===-,
  # out: `.`.     `#.,;《
  # out: ,_|_|     ## #《
  # out: `__.__    `####《
  # out:      ~~< ,###'~
  # out:         》##'
  # out: Wolves
  # out: '.py
  # out: -rw-r--r-- 1 runner runner  15 May  8 04:11  '
  # out:  _     ___
  # out: #_~`--'__ `===-,
  # out: `.`.     `#.,;《
  # out: ,_|_|     ## #《
  # out: `__.__    `####《
  # out:      ~~< ,###'~
  # out:         》##'
  # out: Wolves
  # out: '
h=""" '\n _     ___\n#_~`--'__ `===-,\n`.`.     `#.,//\n,_|_|     ## #《\n`__.__    `####《\n     ~~< ,###'~\n        》##'\nWolves\n'"""
h
# val:  '
# val:  _     ___
# val: #_~`--'__ `===-,
# val: `.`.     `#.,//
# val: ,_|_|     ## #《
# val: `__.__    `####《
# val:      ~~< ,###'~
# val:         》##'
# val: Wolves
# val: '

