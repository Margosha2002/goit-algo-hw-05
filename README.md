# Search Methods Research Results

##

### Input Data

1. "UA5.ORG" | ID1
2. "Карпов" | ID2

##

### Tests

#### Boyer-Moore

1. Arcticle 1| ID1 | 0.0007011890411376953 sec | :white_check_mark:
2. Arcticle 1| ID2 | 0.001092672348022461 sec | :x:
3. Arcticle 2| ID1 | 0.001009225845336914 sec | :x:
4. Arcticle 2| ID2 | 0.0013916492462158203 sec | :white_check_mark:

#### Rabin-Karp :x:

1. Arcticle 1| ID1 | 0.0025420188903808594 sec | :white_check_mark:
2. Arcticle 1| ID2 | 0.0037539005279541016 sec | :x:
3. Arcticle 2| ID1 | 0.002588987350463867 sec | :x:
4. Arcticle 2| ID2 | 0.003538846969604492 sec | :white_check_mark:

#### Knut-Morris-Pratt

1. Arcticle 1| ID1 | 0.0013370513916015625 sec | :white_check_mark:
2. Arcticle 1| ID2 | 0.002033710479736328 sec | :x:
3. Arcticle 2| ID1 | 0.00152587890625 sec | :x:
4. Arcticle 2| ID2 | 0.0021529197692871094 sec | :white_check_mark:

### Conclusion

Boyer-Moore has shown the best results in comparison.
