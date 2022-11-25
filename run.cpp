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

    string input_file = args[1], command, out_path = "out.txt";
    
    if(argc == 3)
        out_path = args[2];

    command = "python ./src/python/main.py " + input_file + " > " + out_path;
    cout << command << endl;

     
    try {
        system(command.c_str());
    } catch(exception &e) {
        cout << "Exception " << e.what() << "\n";
    }
        cout << "Código de máquina gerado com sucesso!\n";

    return 0;
}