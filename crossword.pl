
%%implementing the crossword
word(apastosaurus,a,p,a,t,o,s,a,u,r,u,s).
word(bones,b,o,n,e,s).
word(eggs,e,g,g,s).
word(extinct,e,x,t,i,n,c,t).
word(claws,c,l,a,w,s).
word(fossil,f,o,s,s,i,l).
word(raptor,r,a,p,t,o,r).
word(teeth,t,e,e,t,h).
word(triassic,t,r,i,a,s,s,i,c).
word(triceratops,t,r,i,c,e,r,a,t,o,p,s).


crossword(A,B,C,D,E,F,G,H,I,J) :-
                                word(A,_,AmapC,_,_,AmapD,_,_,_,_,_,AmapB),
                                word(B,_,_,_,AmapB),
                                word(C,AmapC,_,_,_,_,_),
                                word(D,AmapD,_,_,_,_,_,DmapE),
                                word(E,DmapE,_,_,EmapF,_,_,_,EmapG),
                                word(F,EmapF,_,_,FmapH,_,_,_,_,_,_,FmapJ),
                                word(G,EmapG,_,_,_,_),
                                word(H,_,_,_,FmapH,_),
                                word(I,_,ImapJ,_,_,_),
                                word(J,_,ImapJ,_,FmapJ,_,_).


    