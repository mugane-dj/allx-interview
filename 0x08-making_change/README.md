# Minimum number of coins to make change for a given amount (total) using a given set of coin denominations.

Pseudocode:
```
FOR i = 0 To length(coins) - 1
    FOR j = 0 To total + 1
        IF i = 0
            IF coins[i] > j
                table[i][j] = 0
            ELSE
                table[i][j] = table[i][j - coins[i]] + 1

        ELSE
            IF coins[i] > j
                table[i][j] = table[i - 1][j]
            ELSE
                table[i][j] = MIN(table[i - 1][j], table[i][j - coins[i]] + 1)
    ENDFOR
ENDFOR
RETURN table[Length(coins) - 1][total]
```
