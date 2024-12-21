#include <iostream>

void dumpFloat(float *p);

int main() {
    float x;
    while(true) {
        std::cout << "Nhap vao mot so thuc floating-point: ";
        std::cin >> x;
        std::cout<<"Bieu dien nhi phan:                    ";
        dumpFloat(&x);
        std::cout <<"\n";
    }
    return 0;
} 

// Function to dump the binary representation of a float
void dumpFloat(float *p) {
    unsigned int val = *(unsigned int*)p;
    unsigned int sign = val >> 31;
    unsigned int exponent = (val >> 23) & 0xFF;
    unsigned int significand = val & 0x7FFFFF;
    std::cout <<sign << " ";
    for (int i = 7; i >= 0; --i) {
        std::cout << ((exponent >> i) & 1);
    }
    std::cout << " ";
    for (int i = 22; i >= 0; --i) {
        std::cout << ((significand >> i) & 1);
    }
    std::cout << '\n';
}