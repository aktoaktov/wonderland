#include <chrono>
#include <iostream>

#include "constants.h"

constexpr int M = 1e9 + 7;

u32 inverse(u32 a) {
    u32 r = 1;
    int power = M - 2;

    while (power > 0) {
        if (power & 1)
            r = (static_cast<u64>(r) * a) % M;
        a = (static_cast<u64>(a) * a) % M;
        power >>= 1;
    }

    return r;
}

int main(int argc, char *argv[]) {
    constexpr auto LOOPS = 10000000;
    const auto start = std::chrono::high_resolution_clock::now();

    for (int a = 1; a < LOOPS; a++) {
        inverse(a);
    }

    const auto end = std::chrono::high_resolution_clock::now();
    const auto duration = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start);
    std::cout << duration.count() / LOOPS << " ns\n";
}
