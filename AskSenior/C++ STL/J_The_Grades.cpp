#include <bits/stdc++.h>
using namespace std;

void solve()
{
    int n;
    cin >> n;

    vector<pair<string, vector<int>>> students;

    for (int i = 0; i < n; i++) {
        string name;
        int a, b, c, d;
        cin >> name >> a >> b >> c >> d;

        students.push_back({name, {a, b, c, d}});
    }

    sort(students.begin(), students.end(), [](const pair<string, vector<int>>& s1, const pair<string, vector<int>>& s2) {
        int sum1 = accumulate(s1.second.begin(), s1.second.end(), 0);
        int sum2 = accumulate(s2.second.begin(), s2.second.end(), 0);

        if (sum1 == sum2) {
            return s1.first < s2.first;
        }
        return sum1 > sum2; 
    });

    for (const auto& student : students) {
        int total = accumulate(student.second.begin(), student.second.end(), 0);
        cout << student.first << " " << total;
        for (int marks : student.second) {
            cout << " " << marks;
        }
        cout << "\n";
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    solve();

    return 0;
}
