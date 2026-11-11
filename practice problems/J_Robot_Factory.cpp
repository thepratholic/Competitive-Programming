#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<vector<int>> grid;
vector<vector<bool>> visited;

// West, South, East, North
int dr[] = {0, 1, 0, -1};
int dc[] = {-1, 0, 1, 0};

int dfs(int r, int c) {
    visited[r][c] = true;
    int size = 1;

    for (int bit = 0; bit < 4; bit++) {
        // If there is NO wall
        if ((grid[r][c] & (1 << bit)) == 0) {
            int nr = r + dr[bit];
            int nc = c + dc[bit];

            if (nr >= 0 && nr < n && nc >= 0 && nc < m && !visited[nr][nc]) {
                size += dfs(nr, nc);
            }
        }
    }

    return size;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;

    grid.assign(n, vector<int>(m));
    visited.assign(n, vector<bool>(m, false));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> grid[i][j];
        }
    }

    vector<int> rooms;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (!visited[i][j]) {
                rooms.push_back(dfs(i, j));
            }
        }
    }

    sort(rooms.rbegin(), rooms.rend());

    for (int x : rooms) {
        cout << x << " ";
    }
    cout << "\n";

    return 0;
}