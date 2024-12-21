#include <iostream>
#include <cmath> 

void cau1(int i, float f);
void cau2(int i, float f);
void cau3(int i, float f);
void cau4(int i, float f);
void cau5(int i, float f);
void cau6(int i, float f);
void cau7(int i, float f);
void cau8(int i, float f);
void cau9(int i, float f);

int main() 
{
    int i = 100;
    float f = 25.2525f;
    cau1(i,f);
    std::cout<<"\n";
    cau2(i,f);
    std::cout<<"\n";
    cau3(i,f);
    std::cout<<"\n";
    cau4(i,f);
    std::cout<<"\n";
    cau5(i,f);
    std::cout<<"\n";
    cau6(i,f);
    std::cout<<"\n";
    cau7(i,f);
    std::cout<<"\n";
    cau8(i,f);
    std::cout<<"\n";
    cau9(i,f);
    std::cout<<"\n";
    return 0;
}

void cau1(int i, float f)
{
    std::cout<<"1. Chuyen doi float -> int -> float\n";
    f = 25.2525f;
    std::cout<<"   => Before: "<<f<<"\n";
    i = static_cast<int>(f);
    f = static_cast<float>(i);
    std::cout<<"   => After: "<<f<<"\n";
}
void cau2(int i, float f)
{
    std::cout<<"2. Chuyen doi int -> float -> int\n";
    i = 25;
    std::cout<<"   => Before: "<<i<<"\n";
    f = static_cast<float>(i);
    i = static_cast<int>(f);
    std::cout<<"   => After: "<<f<<"\n";
}
void cau3(int i, float f)
{
    std::cout<<"3. (x+y)+z = x+(y+z)\n";
    float x = 1.1f,y=1.2f,z=1.3f;
    if((x+y)+z == x+(y+z)) std::cout<<"   => True\n";
    else std::cout<<"   => False\n";
}
void cau4(int i, float f)
{
    std::cout<<"4. i = (int) (3.14159 * f);\n";
    float x = 1.1f,y=1.2f,z=1.3f;
    if((x+y)+z == x+(y+z)) std::cout<<"   => True\n";
    else std::cout<<"   => False\n";
}
void cau5(int i, float f)
{
    std::cout<<"5. f = f + (float) i;\n"
            <<"   => "<< (int)(3.14159 * f)<<"\n";
}
void cau6(int i, float f)
{
    std::cout<<"6. => ";
    if (i == (int)((float) i)) 
    { 
        std::cout<<"True\n"; 
    }
    else std::cout<<"False\n";
}
void cau7(int i, float f)
{
    std::cout<<"7. => ";
    if (i == (int)((double) i)) 
    { 
        std::cout<<"True\n"; 
    }
    else std::cout<<"False\n";
}
void cau8(int i, float f)
{
    std::cout<<"8. => ";
    if (i == (float)((int) f)) 
    { 
        std::cout<<"True\n"; 
    }
    else std::cout<<"False\n";
}
void cau9(int i, float f)
{
    std::cout<<"9. => ";
    if (i == (double)((int) f)) 
    { 
        std::cout<<"True\n"; 
    }
    else std::cout<<"False\n";
}