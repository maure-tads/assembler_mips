#include <bits/stdc++.h>

using namespace std;

map<string, string> instruction_set;

void init() {
    ifstream myfile("dictionary.txt");
    string inst, bitset;
    int size;
    for (int i = 0; i < 27; i++) {
        myfile >> inst >> bitset;
        instruction_set[inst] = bitset;
    }
}

void toHex(string s) {
    for (int i = 0; i < s.size() - 3; i += 4) {
        string k = string(s.begin() + i, s.begin() + i + 4);
        unsigned int j = bitset<4>(k).to_ulong();
        cout << hex << j;
    }
}

string getBinaryString(string a) {
    return bitset<5>(atoi(string(a.begin() + 1, a.end()).c_str())).to_string();
}

void parse(vector<string> instruction) {
    string command = instruction[0];
    string c = instruction_set[command];
    instruction.erase(instruction.begin());

    int argc = 0;
    for (int i = 0; i < instruction.size(); i++) {
        if (instruction[i][0] == '$') {
            instruction[i] = getBinaryString(instruction[i]);
            argc++;
        }
    }

    if (argc == 2) {
        if (*(prev(c.end())) == '*') {
            c.replace(c.find("s"), 1, instruction[1]);
            c.replace(c.find("t"), 1, instruction[0]);
            c.replace(c.find("*"), 1, bitset<16>(atoi(instruction[2].c_str())).to_string());
        } else if (command[0] == 's') {
            c.replace(c.find("t"), 1, instruction[1]);
            c.replace(c.find("d"), 1, instruction[0]);
            string num = instruction[2][0] == '$' ? getBinaryString(instruction[2]) : bitset<5>(atoi(instruction[2].c_str())).to_string();
            c.replace(c.find("a"), 1, num);
        } else {
            c.replace(c.find("s"), 1, instruction[0]);
            c.replace(c.find("t"), 1, instruction[1]);
        }
    } else if (argc == 3) {
        c.replace(c.find("s"), 1, instruction[1]);
        c.replace(c.find("t"), 1, instruction[2]);
        c.replace(c.find("d"), 1, instruction[0]);
    }
    //cout << c << " ~> ";
    toHex(c);
}

vector<string> split(string s, char delimiter) {
    vector<string> out;
    int k = 0;
    string sbs = "";
    while (s.size() > 0) {
        int del = s.find(delimiter);
        sbs = s.substr(0, del);
        out.push_back(sbs);
        if (del < 0) break;
        s.erase(s.begin(), s.begin() + sbs.size() + 1);
    }
    return out;
}
void read() {
    vector<string> instructions;
    string line;
    char delimiter = 32;  // ASCII CODE FOR SPACE
    while (getline(cin, line)) {
        instructions = split(line, delimiter);
        parse(instructions);
        cout << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    init();
    read();
    return 0;
}