# Correlation Power Analysis (CPA) Attack Implementation


## Introduction
Correlation Power Analysis (CPA) is a form of side-channel attack that exploits variations in power consumption during cryptographic operations to extract secret keys. Unlike brute-force attacks, CPA attacks leverage physical leakages from devices, making them more efficient and practical against vulnerable cryptographic systems. CPA attacks are based on the principle that the power consumption of a cryptographic device correlates with the data it processes. By observing the power consumption during encryption and correlating it with hypothesized operations (like S-Box outputs), the CPA attack aims to reveal crucial information.

---

## Implementation

### Software and Tools Used:
- Python programming language
- NumPy library for numerical computations
- Struct and Matplotlib libraries for data processing and visualization



### helperFunctions.py:
- **calculateHammingWeight(number)**:
  - **Purpose**: Computes the Hamming weight, indicating the number of '1' bits in the binary representation of a number.
  - **Implementation**: Converts the input number into its binary form and counts the occurrence of '1' bits.

- **calculateCorrelationTrace(vector, matrix)**:
  - **Purpose**: Calculates the correlation coefficient between a given vector and each row of a matrix representing power consumption data.
  - **Implementation**: Employs NumPy for computing correlation coefficients.

### calculateSboxOutput.py:
- **S-Box Array**:
  - **Purpose**: Essential for introducing non-linearity in cryptographic operations in symmetric key algorithms like AES.
  - **Implementation**: Contains a predefined array representing the S-Box for the cryptographic algorithm.

- **calculateSboxOutput(plainText, key)**:
  - **Purpose**: Compute the S-Box output for given inputs.
  - **Implementation**: Returns the S-Box output based on the XOR of `plainText` and `key`.

### getInput.py:
- **loadTrace(fileName, numberOfTraces, traceSize)**:
  - **Purpose**: Loads power consumption traces from a binary file.
  - **Implementation**: Reads the binary file and extracts the specified number of traces.

- **loadData(fileName)**:
  - **Purpose**: Loads additional cryptographic data, such as plaintexts or ciphertexts.
  - **Implementation**: Parses a file and converts the contents into a 2D array of integers.

### Main.py:
- Coordinates data loading, key hypothesis iteration, output calculation, and correlation analysis to determine the most likely key.

---

## Results
The CPA attack successfully revealed the secret key, with the following outcomes:

| Byte | Original Key | Obtained Key | Computation Time (hour) |
| ---- | ------------ | ------------ | ----------------------- |
| 0    | 0x00         | 0x00         | 1.85                    |
| ...  | ...          | ...          | ...                     |
| 15   | 0xff         | 0xff         | 1.93                    |

Total Computation Time: **30.18** hours
