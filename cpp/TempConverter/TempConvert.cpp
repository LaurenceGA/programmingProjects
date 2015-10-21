#include <iostream>
#include <stdlib.h>
#include <vector>

using namespace std;

inline void showUsage(string progName) {
	cerr << "usage: " + progName + " lower_limit upper_limit step_size [-reversed]" << endl;
}

float celToFah(float temp) {
	return temp * (9/5.0) + 32;
}

float fahToCel(float temp) {
	return (temp - 32) * (5/9.0);
}

int main(int argc, char *argv[]) {
	/*
	 Program to convert from Celcius to Fahrenheit (default) or vice versa

	Takes 3 or 4 command line arguments
	1- lower limit
	2 - upper limit
	3 - step size
	4(optional) - reverse conversion

	Outputs a table of conversions between the upper and lower limit
	*/
	if (argc < 4 or argc > 5) {
		showUsage(argv[0]);
	} else {
		int lowerLimit = atoi(argv[1]);
		int upperLimit = atoi(argv[2]);
		float stepSize = atoi(argv[3]);
		
		bool reversed = false;
		
		if (argc == 5) {
			string arg4(argv[4]);
			cout << (arg4 == "-reversed" || arg4 == "-r");
			if (arg4 == "-reversed") {
				reversed = true;
			} else {
				showUsage(argv[0]);
				return 0;
			}
		}
	
		if (upperLimit < lowerLimit) {
			// Exception here
			throw "Upper limit can't be less than lower limit";
		}
		
		if (!reversed) {
			if (lowerLimit < -273.15) {
				throw "Lower limit cannot below absolute zero";
			}
		} else {
			if (lowerLimit < -459.67) {
				throw "Lower limit cannot be below absolute zero";
			}
		}

		if (stepSize == 0) {
			throw "Step size must be greater than 0";	
		}

	int t_size = (upperLimit - lowerLimit) / stepSize;
	vector<pair<float, float> > tempTable(t_size);
	
	for (int i=0; i < t_size; i++) {
		tempTable[i].first = lowerLimit + i*stepSize;
		if (!reversed) {
			tempTable[i].second = celToFah(lowerLimit + i*stepSize);
		} else {
			tempTable[i].second = fahToCel(lowerLimit + i*stepSize);
		}
	}

	string heading = "Celcius        Fahrenheit";
	
	if (reversed) {
		heading = "Fahrenheit        Celcius";
	}

	cout << heading << endl;
	for (int i=0; i < t_size; i++) {
		cout << tempTable[i].first << "	" << tempTable[i].second << endl;
	}

	}

	return 0;
}
