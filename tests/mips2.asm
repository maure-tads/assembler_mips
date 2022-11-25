.text

main: addi $v0, $zero, 5
      syscall
      add $t0, $v0, $zero
test:
      mul $t0, $t0, $t0
      add $a0, $t0, $zero
      addi $v0, $zero, 1
      syscall
      addi $v0, $zero, 10
      syscall
      j main
      j test
      beq $1 $2 main