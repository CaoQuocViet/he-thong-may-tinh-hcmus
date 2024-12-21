#include <iostream>
#include <cstring>
#include <cmath>
#include <limits>

void dumpFloat(float *p_float);
void forceFloat(float *p_float, const char *s);

int main()
{
    float number;

    std::cout << "\nBieu dien nhi phan cua 1.3E+20:                     ";
    number = 1.3E+20F;
    dumpFloat(&number);

    std::cout << "\nBieu dien nhi phan cua so float nho nhat lon hon 0: ";
    number = std::numeric_limits<float>::min();
    dumpFloat(&number);

    std::cout << "\nBieu dien nhi phan cua so float inf:                ";
    number = std::numeric_limits<float>::infinity();
    dumpFloat(&number);

    std::cout << "\nBieu dien nhi phan cua so float bao loi NaN:        ";
    number = std::numeric_limits<float>::quiet_NaN();
    dumpFloat(&number);

    std::cout << "\nBieu dien nhi phan cua so float X-(+ inf):          ";
    number = 1.3E+20F - std::numeric_limits<float>::infinity();
    dumpFloat(&number);

    std::cout << "\nBieu dien nhi phan cua so float (+ inf)-(+ inf):    ";
    number = std::numeric_limits<float>::infinity() - std::numeric_limits<float>::infinity();
    dumpFloat(&number);

    std::cout << "\nBieu dien nhi phan cua so float X/0:                ";
    number = 1.3E+20F / 0.0F;
    dumpFloat(&number);

    std::cout << "\nBieu dien nhi phan cua so float 0/0:                ";
    number = 0.0F / 0.0F;
    dumpFloat(&number);

    std::cout << "\nBieu dien nhi phan cua so float (+ inf)/(+ inf):    ";
    number = std::numeric_limits<float>::infinity() / std::numeric_limits<float>::infinity();
    dumpFloat(&number);

    std::cout << "\nBieu dien nhi phan cua so float sqrt(-X):           ";
    number = sqrt(-1.3E+20F);
    dumpFloat(&number);

    return 0;
}

// Function to dump the binary representation of a float
void dumpFloat(float *p_float)
{
    int index;
    
    char sign;
    char exp[8 + 1] = {0}; 
    char value[23 + 1] = {0}; 

    int *p_binary = reinterpret_cast<int*>(p_float);

    sign = (*p_binary & (1 << 31)) ? '1' : '0';

    // Compute the exponent
    index = 0;
    for (int i = 30; i >= 23; i--)
    {
        exp[index++] = (*p_binary & (1 << i)) ? '1' : '0';
    }
    exp[index] = '\0';

    // Compute the value
    index = 0;
    for (int i = 22; i >= 0; i--)
    {
        value[index++] = (*p_binary & (1 << i)) ? '1' : '0';
    }
    value[index] = '\0';

    std::cout << sign << " " << exp << " " << value << "\n";
}

// Function to convert a 32-bit binary string to a float
void forceFloat(float *p_float, const char *s)
{
    char s_new[33] = {0}; 

    int *p_binary = reinterpret_cast<int*>(p_float);

    // Validate the input
    if (std::strlen(s) > 32)
    {
        return;
    }

    // Validate the input
    for (int i = 0; i < std::strlen(s); i++)
    {
        if (s[i] != '0' && s[i] != '1')
        {
            return;
        }
    }

    // Check for special cases: Inf and NaN
    for (int i = 0; i < 32; i++)
    {
        s_new[i] = (i < std::strlen(s)) ? s[i] : '0';
    }
    s_new[32] = '\0';

    *p_binary = 0;

    // Compute the exponent
    for (int i = 0; i < 32; i++)
    {
        if (s_new[i] == '1')
        {
            *p_binary |= (1 << (31 - i));
        }
    }
}