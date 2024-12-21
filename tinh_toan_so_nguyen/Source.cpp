#include <iostream>
#include <bitset>
#include <vector>
#include <stdexcept>
#include <limits>

// Convert an 8-bit two's complement bit array to an integer
int bitArrayToInt(const std::bitset<8>& bits) {
    if (bits[7] == 1) {  // Check the sign bit
        return static_cast<int>(bits.to_ulong()) - 256; // Two's complement adjustment
    }
    return static_cast<int>(bits.to_ulong());
}

// Convert an integer to an 8-bit two's complement bit array
std::bitset<8> intToBitArray(int value) {
    if (value < -128 || value > 127) {
        throw std::overflow_error("Value out of range for 8-bit signed integer");
    }
    return std::bitset<8>(static_cast<unsigned char>(value));
}

// Function to add two two's complement numbers
std::bitset<8> addBinary(const std::bitset<8>& a, const std::bitset<8>& b) {
    int result = bitArrayToInt(a) + bitArrayToInt(b);
    if (result > 127 || result < -128) {
        throw std::overflow_error("Overflow occurred in addition");
    }
    return intToBitArray(result);
}

// Function to subtract two two's complement numbers
std::bitset<8> subtractBinary(const std::bitset<8>& a, const std::bitset<8>& b) {
    int result = bitArrayToInt(a) - bitArrayToInt(b);
    if (result > 127 || result < -128) {
        throw std::overflow_error("Overflow occurred in subtraction");
    }
    return intToBitArray(result);
}

// Function to multiply two two's complement numbers
std::bitset<8> multiplyBinary(const std::bitset<8>& a, const std::bitset<8>& b) {
    int result = bitArrayToInt(a) * bitArrayToInt(b);
    if (result > 127 || result < -128) {
        throw std::overflow_error("Overflow occurred in multiplication");
    }
    return intToBitArray(result);
}

// Function to divide two two's complement numbers
std::bitset<8> divideBinary(const std::bitset<8>& a, const std::bitset<8>& b) {
    int denominator = bitArrayToInt(b);
    if (denominator == 0) {
        throw std::runtime_error("Division by zero");
    }

    int numerator = bitArrayToInt(a);
    int result = numerator / denominator;

    // Ensure result is within 8-bit signed integer range
    if (result > 127 || result < -128) {
        throw std::overflow_error("Overflow occurred in division");
    }

    return intToBitArray(result);
}

// Display the binary representation of an integer X
void displayBinary(int X) {
    std::bitset<32> bits(X);  // Represent X with 32 bits
    std::cout << "Binary representation of " << X << " is: " << bits << std::endl;
}

// Build an integer from a bit array and display it
int buildNumberFromBits(const std::vector<int>& A) {
    int X = 0;
    for (size_t i = 0; i < A.size(); ++i) {
        X |= (A[i] << (31 - i));  // Shift bit to the correct position
    }
    return X;
}

int main() {
    // Exercise 1.1
    int X;
    std::cout << "Enter an integer X (4 bytes): ";
    std::cin >> X;
    displayBinary(X);

    // Exercise 1.2
    std::vector<int> A(32);
    std::cout << "Enter 32 elements of the array (0 or 1): ";
    for (int& bit : A) {
        std::cin >> bit;
        if (bit != 0 && bit != 1) {
            std::cerr << "Invalid input. Must be 0 or 1.\n";
            return 1;
        }
    }
    int number = buildNumberFromBits(A);
    std::cout << "The integer X from the array is: " << number << std::endl;
    displayBinary(number);

    // Input 8-bit bit arrays for calculations
    std::bitset<8> bitset1, bitset2;
    std::string bitString;

    std::cout << "Enter the first 8-bit binary string: ";
    std::cin >> bitString;
    if (bitString.size() != 8 || bitString.find_first_not_of("01") != std::string::npos) {
        std::cerr << "Invalid input. Must be an 8-bit binary string containing only 0 and 1.\n";
        return 1;
    }
    bitset1 = std::bitset<8>(bitString);

    std::cout << "Enter the second 8-bit binary string: ";
    std::cin >> bitString;
    if (bitString.size() != 8 || bitString.find_first_not_of("01") != std::string::npos) {
        std::cerr << "Invalid input. Must be an 8-bit binary string containing only 0 and 1.\n";
        return 1;
    }
    bitset2 = std::bitset<8>(bitString);

    int num1 = bitArrayToInt(bitset1);
    int num2 = bitArrayToInt(bitset2);

    std::cout << "The integer corresponding to the first bit array is: " << num1 << std::endl;
    std::cout << "The integer corresponding to the second bit array is: " << num2 << std::endl;

    try {
        // Addition
        std::bitset<8> sum = addBinary(bitset1, bitset2);
        std::cout << "Addition result: " << sum << " (decimal: " << bitArrayToInt(sum) << ")" << std::endl;

        // Subtraction
        std::bitset<8> diff = subtractBinary(bitset1, bitset2);
        std::cout << "Subtraction result: " << diff << " (decimal: " << bitArrayToInt(diff) << ")" << std::endl;

        // Multiplication
        std::bitset<8> prod = multiplyBinary(bitset1, bitset2);
        std::cout << "Multiplication result: " << prod << " (decimal: " << bitArrayToInt(prod) << ")" << std::endl;

        // Division
        std::bitset<8> quotient = divideBinary(bitset1, bitset2);
        std::cout << "Division result: " << quotient << " (decimal: " << bitArrayToInt(quotient) << ")" << std::endl;
    }
    catch (const std::overflow_error& e) {
        std::cerr << "Overflow error: " << e.what() << std::endl;
    }
    catch (const std::runtime_error& e) {
        std::cerr << e.what() << std::endl;
    }

    return 0;
}