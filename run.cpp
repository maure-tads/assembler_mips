#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main(int argc, char* argv[]) {
    vector<string> args;
    for(int i = 0; i < argc; i++) {
        args.push_back(string(argv[i]));
    }

    string input_file = args[1], command = "python ./src/python/main.py " + input_file + " > out.txt";
    vector<string>::iterator run_cpp =  find(args.begin(), args.end(), "--cpp");
    if(run_cpp != args.end()){
        
        system(string("g++ ./src/cpp/main.cpp -o main_assembler").c_str());
        system(string("main_assembler <" + input_file + " > out").c_str());
    } else {
        system(command.c_str());
    }

    return 0;
}