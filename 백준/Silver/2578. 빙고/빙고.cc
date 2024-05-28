#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <queue>

#define endl '\n'
#define npos string::npos

#define ALL(x) begin(x), end(x)
#define REP(i, x) for (int i{0}; i < (x); ++i)

using namespace std;

vector<string> split(const string& line, char sep = ' ') {
    vector<string> result;

    stringstream ss(line);
    string buffer;
    while (getline(ss, buffer, sep))
        if (!buffer.empty()) result.push_back(buffer);

    return result;
}

template<typename to, typename from >
vector<to> convert(vector<from> vec) {
    vector<to> result;
    for (const auto& a : vec) {
        if constexpr (!is_same_v<from, string>) result.push_back(to_string(a));
        else result.push_back(stoi(a));
    }
    return result;
}

pair<int, int> rem(const vector<vector<int>>& bingo, int x) {
    REP(i, 5) REP(j, 5)
    if (bingo[i][j] == x) return {i, j};

    return {4, 4};
}

int solve(vector<vector<int>> bingo, vector<int> del) {
    int cnt{0};
    REP(k, 25) {
        auto[y, x] = rem(bingo, del[k]);
        bingo[y][x] = 0;

        if (*max_element(ALL(bingo[y])) == 0) ++cnt;

        bool flag{false};
        REP(i, 5) flag |= bingo[i][x];
        if (!flag) ++cnt;

        if (x == y) {
            flag = false;
            REP(i, 5) flag |= bingo[i][i];
            if (!flag) ++cnt;
        }

        if (4-x == y) {
            flag = false;
            REP(i, 5) flag |= bingo[i][4-i];
            if (!flag) ++cnt;
        }

        if (cnt >= 3) return k+1;
    }

    return 25;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    vector<vector<int>> bingo;

    REP(i, 5) {
        string line;
        getline(cin, line);
        bingo.push_back(convert<int>(split(line)));
    }

    vector<int> del(25, 0);
    for (auto& p : del) cin >> p;

    cout << solve(bingo, del) << endl;

    return 0;
}