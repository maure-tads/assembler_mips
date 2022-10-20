.text

main: addi $v0, $zero, 5
      syscall
      add $t0, $v0, $zero
      
      syscall
      add $t1, $v0, $zero
      
      mul $t0, $t0, $t1
      add $a0, $t0, $zero
      addi $v0, $zero, 1
      syscall
      addi $v0, $zero, 10
      syscall