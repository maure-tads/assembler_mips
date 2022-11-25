main:   addi $8, $0, 0  # soma

laco:   addi $2, $0, 5
        syscall
        srl $9, $2, 31
        bne $0, $9, prn
        add $8, $8, $2
        j laco
       
prn:    add $4, $8, $0
        addi $2, $0, 1
        syscall        
           
sai:    addi $2, $0, 10
        syscall