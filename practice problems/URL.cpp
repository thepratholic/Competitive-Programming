#include <iostream>
#include <string>
using namespace std;

int main() {
    string url;
    getline(cin, url);

    size_t start = url.find('?');
    
    string query = url.substr(start + 1);

    size_t pos = 0;
    while ((pos = query.find('&')) != string::npos) {
        string param = query.substr(0, pos);
        size_t equal_pos = param.find('=');
        string key = param.substr(0, equal_pos);
        string value = param.substr(equal_pos + 1);
        cout << key << ": " << value << endl;
        query.erase(0, pos + 1);
    }

    size_t equal_pos = query.find('=');
    string key = query.substr(0, equal_pos);
    string value = query.substr(equal_pos + 1);
    cout << key << ": " << value << endl;

    return 0;
}
