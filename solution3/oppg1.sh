#!/bin/bash

echo "Kjører oppgave 1..."
echo 
cat fil1.c
echo 
cat fil2.c
echo 
diff fil1.c fil2.c
echo
diff -u fil1.c fil2.c > patchfil
echo 
cat patchfil
echo 
patch fil1.c < patchfil
echo 
cat fil1.c
echo 
patch -R fil1.c < patchfil
echo 
cat fil1.c

