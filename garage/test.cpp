#include <chrono>
#include <iostream>

#include "arithmetic/montgomery.h"

constexpr int M = 1e9 + 7;

constexpr arithmetic::Montgomery space(M);

u32 inverse(u32 _a) {
    u64 a = space.transform(_a);
    u64 r = space.transform(1);

    int power = M - 2;
    while (power > 0) {
        if (power & 1)
            r = space.multiply(r, a);
        a = space.multiply(a, a);
        power >>= 1;
    }

    return space.reduce(r);
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
