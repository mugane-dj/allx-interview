# UTF-8 Validation
UTF-8 validation can be done by checking the octet sequence from the list of integers provided.
Lets assume a the following dataset [229, 65, 127, 256]

229 = (11100101)<sub>2</sub>

65 = (1000001)<sub>2</sub>

127 = (1111111)<sub>2</sub>

256 = (100000000)<sub>2</sub>

The dataset is represented by the octet sequence: `11100101 1000001 1111111 100000000`

Valid byte types determine if a UTF-8 encoding is valid and there are five kinds of valid byte type: `0**, 10**, 110**,1110** and 11110**`. Hence, based on the octet sequence, the integer 127 invalidates the dataset as a valid UTF-8 encoding since it is not a valid byte type. 

The bitwise right shift operator can also be used to determine if the integers are valid byte types.

| Binary condition | Bitwise right shift equivalent |
| ---------------- | ------------------------------  |
| int / 128 (2<sup>7</sup>) = 0       |  num >> 7 = 0 |
| int / 64 (2<sup>6</sup>) = 0b10 | num >> 6 = 0b10 |
| int / 32 (2<sup>5</sup>) = 0b110 | num >> 5 = 0b110 |
| int / 16 (2<sup>4</sup>) = 0b1110 | num >> 4 = 0b1110 |
| int / 8 (2<sup>3</sup>) = 0b11110 | num >> 3 = 0b11110 |
