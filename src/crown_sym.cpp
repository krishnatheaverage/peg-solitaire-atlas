// Pendant-symmetric solvability for crowns C(k;p).
// Usage: crown_sym <k> <p>

#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <unordered_map>
#include <vector>
#include <array>

static int K, P;
static std::unordered_map<uint64_t, bool> memo;
static std::vector<std::array<int, 3>> jumps;

static bool reach(uint32_t mask, int j) {
    int pegs = __builtin_popcount(mask) + j;
    if (pegs == 1) return true;
    uint64_t key = (uint64_t)mask | ((uint64_t)j << K);
    auto it = memo.find(key);
    if (it != memo.end()) return it->second;
    memo.emplace(key, false);
    bool ok = false;
    for (auto& t : jumps) {
        int u = t[0], m = t[1], w = t[2];
        if ((mask >> u & 1) && (mask >> m & 1) && !(mask >> w & 1)) {
            if (reach(mask ^ (1u << u) ^ (1u << m) ^ (1u << w), j)) {
                ok = true;
                break;
            }
        }
    }
    if (!ok && (mask & 1)) {
        int g1 = 1, g2 = K - 1;
        // A: pendant exits into empty gate
        if (j >= 1) {
            for (int g : {g1, g2})
                if (!(mask >> g & 1) &&
                    reach((mask & ~1u) | (1u << g), j - 1)) { ok = true; break; }
        }
        // B: pendant over x_0 into empty pendant slot (count unchanged)
        if (!ok && j >= 1 && P - j >= 1)
            ok = reach(mask & ~1u, j);
        // C: gate feeds pendant
        if (!ok && P - j >= 1) {
            for (int g : {g1, g2})
                if ((mask >> g & 1) &&
                    reach((mask & ~1u) & ~(1u << g), j + 1)) { ok = true; break; }
        }
    }
    memo[key] = ok;
    return ok;
}

int main(int argc, char** argv) {
    K = std::atoi(argv[1]);
    P = std::atoi(argv[2]);
    for (int m = 0; m < K; ++m) {
        int a = (m + K - 1) % K, b = (m + 1) % K;
        jumps.push_back({a, m, b});
        jumps.push_back({b, m, a});
    }
    uint32_t full = (1u << K) - 1;
    bool any = false;
    std::string holes;
    for (int h = 0; h < K; ++h)
        if (reach(full ^ (1u << h), P)) { any = true; holes += " x" + std::to_string(h); }
    if (P >= 1 && reach(full, P - 1)) { any = true; holes += " q"; }
    if (any)
        std::printf("C(%d;%d): SOLVABLE from%s\n", K, P, holes.c_str());
    else
        std::printf("C(%d;%d): UNSOLVABLE (all %d holes)\n", K, P, K + 1);
    return 0;
}
