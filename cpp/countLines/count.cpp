#include <iostream>
#include <fstream>

using namespace std;

inline void showUsage(string progName) {
	cerr << "usage: " + progName + " filename" << endl;
}

int main (int argC, char *argv[]) {
	if (argC != 2) {
		cerr << "Incorrect number of arguments" << endl;;
		showUsage(argv[0]);
		return 1;
	} else {
		ifstream file(argv[1]);
		int lineCount = 0;
		
		if (!file.is_open()) {
			cerr << "Could not open file" << endl;
			showUsage(argv[0]);
			return 1;
		} else {
			string tempStore;
			while (getline(file, tempStore)) {
				lineCount++;
			}

			cout << lineCount << " lines long." << endl;
		}

		file.close();
	}

	return 0;
}
