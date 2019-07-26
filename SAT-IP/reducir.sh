#!/bin/bash
for file in InstanciasSAT/*.cnf
do
  echo "Procesando archivo $file..."
  filename=$(basename "$file" .cnf)
  mzn_file="${filename}.mzn" 
  echo "$mzn_file"
  python Reductor/reductor.py $file "InstanciasMiniZinc/$mzn_file"
done