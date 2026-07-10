#include <iostream>

unsigned long long getFactorialIterative(int n) {
    // Negative numbers have no defined factorial
    if (n < 0) return 0; 
    
    unsigned long long result = 1;
    
    // Multiply numbers sequentially from 2 up to n
    for (int i = 2; i <= n; ++i) {
        result *= i;
    }
    
    return result;
}

int main() {
    std::cout << "5! = " << getFactorialIterative(5) << std::endl; // Output: 120
    return 0;
}
