#pragma once

#include "../constants.h"


namespace arithmetic {
    struct Montgomery {
        u32 M, Mr;

        explicit constexpr Montgomery(u32 M) noexcept;

        [[nodiscard]] constexpr u32 reduce(u64 x) const noexcept;

        [[nodiscard]] constexpr u32 lax_reduce(u64 x) const noexcept;

        [[nodiscard]] constexpr u32 multiply(u32 x, u32 y) const noexcept;

        [[nodiscard]] constexpr u32 transform(u32 x) const noexcept;
    };

    constexpr Montgomery::Montgomery(const u32 M) noexcept
        : M(M), Mr(1) {
        for (int i = 0; i < 5; i++)
            Mr *= 2 - M * Mr;
    }

    constexpr u32 Montgomery::reduce(const u64 x) const noexcept {
        const u32 q = static_cast<u32>(x) * Mr;
        const u32 m = (static_cast<u64>(q) * M) >> 32;
        const u32 result = (x >> 32) + M - m;
        return result < M ? result : result - M;
    }

    constexpr u32 Montgomery::lax_reduce(const u64 x) const noexcept {
        const u32 q = static_cast<u32>(x) * Mr;
        const u32 m = (static_cast<u64>(q) * M) >> 32;
        return (x >> 32) + M - m;
    }

    constexpr u32 Montgomery::multiply(const u32 x, const u32 y) const noexcept {
        return reduce(static_cast<u64>(x) * y);
    }

    constexpr u32 Montgomery::transform(const u32 x) const noexcept {
        return (static_cast<u64>(x) << 32) % M;
    }
}
