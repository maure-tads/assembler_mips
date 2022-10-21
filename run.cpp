#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(int argc, char* argv[]) {
    vector<string> args;
    for(int i = 0; i < argc; i++) {
        args.push_back(string(argv[i]));
    }


    bool run_python = args.find("--python") > -1;
    bool change_dictionary = args.find("-d") + 1;
    string command = "";

    if(run_python) {
        command = "./src/cpp/main";
    } else {
        command = "python ./src/python/main.py";
    }

    if(change_dictionary) {
        command += " " + change_dictionary;
    }

    cout << command << endl;    

    return 0;
}