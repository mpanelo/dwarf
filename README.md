# Dwarf Programming Language

## Instruction Set Architecture

### R Format Instructions
(6-bit Instruction Code) (3-bit Register Code)

000000 XXX : lb  
000001 XXX : push  
000010 XXX :  
000011 XXX :  
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
  
### I Format Instructions  
(2-bit Instruction Code) (3-bit Register Code) (4-bit Immediate)  
  
10 XXX XXXX : ori  
11 XXX XXXX : lui  
