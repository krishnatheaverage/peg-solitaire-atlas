// Two-cluster pendant-symmetric solvability for DC(k,d).
// Usage: dc_sym <k> <d> <p0> <pd>

#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <unordered_map>
#include <vector>
#include <array>
#include <string>

static int K, D, P0, PD;
static std::unordered_map<uint64_t, bool> memo;
static std::vector<std::array<int, 3>> jumps;

static bool reach(uint64_t mask, int j0, int jd) {
    int pegs = __builtin_popcountll(mask) + j0 + jd;
    if (pegs == 1) return true;
    uint64_t key = mask | ((uint64_t)j0 << K) | ((uint64_t)jd << (K + 4));
    auto it = memo.find(key);
    if (it != memo.end()) return it->second;
    memo.emplace(key, false);
    bool ok = false;
    for (auto& t : jumps) {
        int u = t[0], m = t[1], w = t[2];
        if ((mask >> u & 1) && (mask >> m & 1) && !(mask >> w & 1)) {
            if (reach(mask ^ (1ull << u) ^ (1ull << m) ^ (1ull << w),
                      j0, jd)) { ok = true; break; }
        }
    }
    struct CL { int v, j, p; };
    CL cls[2] = {{0, j0, P0}, {D, jd, PD}};
    for (int ci = 0; ci < 2 && !ok; ++ci) {
        int v = cls[ci].v, j = cls[ci].j, p = cls[ci].p;
        if (!(mask >> v & 1)) continue;
        int g1 = (v + 1) % K, g2 = (v + K - 1) % K;
        int nj0, njd;
        if (j >= 1) {
            for (int g : {g1, g2}) {
                if (!(mask >> g & 1)) {
                    nj0 = j0 - (ci == 0); njd = jd - (ci == 1);
                    if (reach((mask & ~(1ull << v)) | (1ull << g), nj0, njd))
                        { ok = true; break; }
                }
            }
        }
        if (!ok && j >= 1 && p - j >= 1)
            ok = reach(mask & ~(1ull << v), j0, jd);
        if (!ok && p - j >= 1) {
            for (int g : {g1, g2}) {
                if (mask >> g & 1) {
                    nj0 = j0 + (ci == 0); njd = jd + (ci == 1);
                    if (reach((mask & ~(1ull << v)) & ~(1ull << g), nj0, njd))
                        { ok = true; break; }
                }
            }
        }
    }
    memo[key] = ok;
    return ok;
}

int main(int argc, char** argv) {
    K = std::atoi(argv[1]); D = std::atoi(argv[2]);
    P0 = std::atoi(argv[3]); PD = std::atoi(argv[4]);
    for (int m = 0; m < K; ++m) {
        int a = (m + K - 1) % K, b = (m + 1) % K;
        jumps.push_back({a, m, b});
        jumps.push_back({b, m, a});
    }
    uint64_t full = (1ull << K) - 1;
    std::string holes;
    for (int h = 0; h < K; ++h)
        if (reach(full ^ (1ull << h), P0, PD)) holes += " " + std::to_string(h);
    if (P0 >= 1 && reach(full, P0 - 1, PD)) holes += " q0";
    if (PD >= 1 && reach(full, P0, PD - 1)) holes += " qd";
    std::printf("DC(%d,%d;%d,%d): solvable holes:%s\n", K, D, P0, PD,
                holes.empty() ? " NONE (unsolvable)" : holes.c_str());
    return 0;
}
