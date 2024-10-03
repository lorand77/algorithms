    for (int i=0; i<N; i++) {
        if (x[i] == N/2) {
            ix = i;
            break;
        }
    }


movl	$0, -12(%rbp)          # Initialize loop variable i = 0 and store it at -12(%rbp)
LBB0_5:                         # Loop label (start of the for loop)
    cmpl	$100000000, -12(%rbp)   # Compare i with N (100,000,000)
    jge	LBB0_10                 # If i >= N, jump to LBB0_10 (exit loop)
    
    movslq	-12(%rbp), %rcx        # Sign-extend i from -12(%rbp) and store in %rcx
    leaq	_main.x(%rip), %rax     # Load the base address of the array x into %rax
    cmpl	$50000000, (%rax,%rcx,4) # Compare x[i] (x[i] = *(rax + rcx * 4)) with 50,000,000 (N/2)
    jne	LBB0_8                  # If x[i] != N/2, jump to LBB0_8 to continue the loop
    
    movl	-12(%rbp), %eax        # If x[i] == N/2, move i from -12(%rbp) into %eax
    movl	%eax, _main.ix(%rip)   # Store i in the static variable ix
    jmp	LBB0_10                 # Break the loop (jump to LBB0_10, the end of the loop)

LBB0_8:                         # Continue loop (if x[i] != N/2)
    movl	-12(%rbp), %eax        # Load i into %eax
    addl	$1, %eax               # Increment i by 1
    movl	%eax, -12(%rbp)        # Store the updated value of i back into -12(%rbp)
    jmp	LBB0_5                  # Jump back to the beginning of the loop (LBB0_5)
    
LBB0_10:                        # End of loop


100003f1a: 89 45 f8                    	movl	%eax, -8(%rbp)
100003f1d: e9 d4 ff ff ff              	jmp	0x100003ef6 <_main+0x16>
100003f22: c7 45 f4 00 00 00 00        	movl	$0, -12(%rbp)
100003f29: 81 7d f4 00 e1 f5 05        	cmpl	$100000000, -12(%rbp)
100003f30: 0f 8d 39 00 00 00           	jge	0x100003f6f <_main+0x8f>
100003f36: 48 63 4d f4                 	movslq	-12(%rbp), %rcx
100003f3a: 48 8d 05 cf 40 00 00        	leaq	16591(%rip), %rax  # 100008010 <_main.x>
100003f41: 81 3c 88 80 f0 fa 02        	cmpl	$50000000, (%rax,%rcx,4)
100003f48: 0f 85 0e 00 00 00           	jne	0x100003f5c <_main+0x7c>
100003f4e: 8b 45 f4                    	movl	-12(%rbp), %eax
100003f51: 89 05 b9 c4 d7 17           	movl	%eax, 400016569(%rip)  # 117d80410 <_main.ix>
100003f57: e9 13 00 00 00              	jmp	0x100003f6f <_main+0x8f>
100003f5c: e9 00 00 00 00              	jmp	0x100003f61 <_main+0x81>
100003f61: 8b 45 f4                    	movl	-12(%rbp), %eax
100003f64: 83 c0 01                    	addl	$1, %eax
100003f67: 89 45 f4                    	movl	%eax, -12(%rbp)
100003f6a: e9 ba ff ff ff              	jmp	0x100003f29 <_main+0x49>
