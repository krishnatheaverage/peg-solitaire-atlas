// Exact peg-solitaire solver for graphs on <= 30 vertices.
// Input: "n u1 v1 u2 v2 ..." per line.  Output: CSV with solvability per hole.

#include <cstdint>
#include <cstdio>
#include <cstring>
#include <string>
#include <unordered_map>
#include <vector>

namespace {

struct Move {
    uint32_t need, hole, flip;
};

std::vector<Move> moves;
std::unordered_map<uint32_t, uint16_t> memo;

uint16_t value(uint32_t state) {
    auto it = memo.find(state);
    if (it != memo.end()) return it->second;
    int mn = 255, mx = 0;
    for (const Move& m : moves) {
        if ((state & m.need) == m.need && !(state & m.hole)) {
            uint16_t v = value(state ^ m.flip);
            int cmn = v >> 8, cmx = v & 0xff;
            if (cmn < mn) mn = cmn;
            if (cmx > mx) mx = cmx;
        }
    }
    if (mx == 0) {
        mn = mx = __builtin_popcount(state);
    }
    uint16_t packed = static_cast<uint16_t>(mn << 8 | mx);
    memo.emplace(state, packed);
    return packed;
}

}  // namespace

int main(int argc, char** argv) {
    FILE* in = argc > 1 ? std::fopen(argv[1], "r") : stdin;
    if (!in) { std::perror("open"); return 1; }

    std::printf(
        "id,n,edges,solvable_mask,class,ps,fs,per_hole_min,per_hole_max,states\n");

    char line[4096];
    long id = 0;
    while (std::fgets(line, sizeof line, in)) {
        int n, u, v, off = 0, read;
        if (std::sscanf(line, "%d%n", &n, &off) != 1) continue;
        std::vector<std::vector<int>> adj(n);
        std::string edges;
        const char* p = line + off;
        while (std::sscanf(p, "%d %d%n", &u, &v, &read) == 2) {
            adj[u].push_back(v);
            adj[v].push_back(u);
            if (!edges.empty()) edges += ' ';
            edges += std::to_string(u) + "-" + std::to_string(v);
            p += read;
        }

        moves.clear();
        for (int mid = 0; mid < n; ++mid)
            for (int from : adj[mid])
                for (int to : adj[mid])
                    if (from != to)
                        moves.push_back({(1u << from) | (1u << mid), 1u << to,
                                         (1u << from) | (1u << mid) | (1u << to)});

        memo.clear();
        const uint32_t full = (n >= 32) ? ~0u : (1u << n) - 1;
        uint32_t solvable_mask = 0;
        int ps = 255, fs = 0;
        std::string mins, maxs;
        for (int s = 0; s < n; ++s) {
            uint16_t val = value(full ^ (1u << s));
            int mn = val >> 8, mx = val & 0xff;
            if (mn == 1) solvable_mask |= 1u << s;
            if (mn < ps) ps = mn;
            if (mx > fs) fs = mx;
            if (s) { mins += ' '; maxs += ' '; }
            mins += std::to_string(mn);
            maxs += std::to_string(mx);
        }
        char cls = solvable_mask == full ? 'F' : (solvable_mask ? 'S' : 'U');
        std::printf("%ld,%d,%s,%u,%c,%d,%d,%s,%s,%zu\n", id++, n, edges.c_str(),
                    solvable_mask, cls, ps, fs, mins.c_str(), maxs.c_str(),
                    memo.size());
    }
    if (in != stdin) std::fclose(in);
    return 0;
}
