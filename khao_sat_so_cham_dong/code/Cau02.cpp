#include <iostream>
#include <cstring> 
#include <cmath>
#include <limits>

void forceFloat(float *p, const char *s);

int main() {
    float myFloat;
    while(true) {
        char binaryString[33];
        std::cout << "Nhap vao chuoi nhi phan 32 bit: ";
        std::cin >> binaryString;
        forceFloat(&myFloat, binaryString);
        std::cout << "So thuc: " << myFloat << std::endl;
        std::cout << "\n";
    }

    return 0;
}

 // Function to convert a 32-bit binary string to a float
void forceFloat(float *p, const char *s) {
    if (strlen(s) != 32) {
        std::cerr << "Input phai co do dai 32 ki tu." << std::endl;
        return;
    }

    int sign = (s[0] == '1') ? -1 : 1;    
    int exponent = 0; 
    float mantissa = 1.0f;

    // Check for special cases: Inf and NaN
    bool isInf = true;
    bool isNaN = false;

    // Validate the input
    for (int i = 0; i < 32; i++) {
        if (s[i] != '0' && s[i] != '1') {
            std::cerr << "Input phai chi chua cac ki tu 0 hoac 1." << std::endl;
            return;
        }
    }

    // Compute the exponent
    for (int i = 1; i <= 8; i++) {
        exponent += (s[i] - '0') * std::pow(2, 8 - i);
    }

    // Check if exponent is all 1s (255 in decimal)
    if (exponent == 255) {
        // If exponent is all 1s, check mantissa
        for (int i = 9; i < 32; i++) {
            if (s[i] == '1') {
                isInf = false;
                isNaN = true;
            }
        }
        if (isNaN) {
            *p = std::numeric_limits<float>::quiet_NaN();
            return;
        } else if (isInf) {
            if (sign == 1) {
                *p = +std::numeric_limits<float>::infinity();
            } else {
                *p = -std::numeric_limits<float>::infinity();
            }
            return;
        }
    }

    // Normal case
    exponent -= 127; // Bias of 127 for single precision

    for (int i = 9; i < 32; i++) {
        mantissa += (s[i] - '0') * std::pow(2, 8 - i);
    }
    *p = sign * mantissa * std::pow(2, exponent);
}