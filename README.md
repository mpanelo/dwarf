# Dwarf Programming Language

## Instruction Set Architecture

### R Format Instructions
(6-bit Instruction Code) (3-bit Register Code)

000000 XXX : push  
000001 XXX : lb  
000010 XXX : sb  
000011 XXX : add  
000100 XXX :  
000101 XXX :  
000110 XXX :  
000111 XXX :  
001000 XXX :  
001001 XXX :  
001010 XXX :  
001011 XXX :  
001100 XXX :  
001101 XXX :  
001110 XXX :  
001111 XXX :  
  
### J Format Instructions
(4-bit Instruction Code) (5-bit Address)  
  
0100 XXXXX : bne  
0101 XXXXX : beq  
0110 XXXXX : jmp  
0110 XXXXX :  
  
### I Format Instructions  
(5-bit Instruction Code) (4-bit Immediate)  
10000 XXXX : lui  
10001 XXXX : ori  
10010 XXXX : sll  
10011 XXXX : srl    
10100 XXXX :  
10101 XXXX :  
10110 XXXX :  
10111 XXXX :  
11000 XXXX :  
11001 XXXX :  
11010 XXXX :  
11011 XXXX :  
11100 XXXX :  
11101 XXXX :  
11110 XXXX :  
11111 XXXX :  
