#include <bits/stdc++.h>

using namespace std;

map<string, string> instruction_set; 


void init() {
    ifstream myfile("esboco");
    string inst, bitset;
    int size;
    for(int i = 0; i < 27; i++) {
        myfile >> size >> inst >> bitset;
        instruction_set[inst] = bitset;
    }
}

void parse(vector<string> instruction) {
    string command = instruction_set[instruction[0]];
    cout << command << endl;

    for(auto it = instruction.begin() + 1; it != instruction.end(); it++) {
        string k = "";
        if((*it)[0] == '$') {
            int i = atoi(string((*it).begin()+1, (*it).end()).c_str());
        }
    }


}

vector<string> split(string s, char delimiter) {
    vector<string> out;
    int k = 0;
    string sbs = "";
    while(s.size() > 0) {
        int del = s.find(delimiter);
        sbs = s.substr(0, del);
        out.push_back(sbs);
        if(del < 0) break;
        s.erase(s.begin(), s.begin() + sbs.size() + 1);
    }
    return out;    
}
void read() {
    string line;
    char delimiter = 32; //ASCII CODE FOR SPACE
    while(getline(cin, line)) {
        vector<string> instructions = split(line, delimiter);
        parse(instructions);
    }
}


int main() {
    init();
   /*   for (const auto& [key, value] : instruction_set)
        std::cout << '[' << key << "] = " << value << "; \n"; */
    read();
    return 0;
}