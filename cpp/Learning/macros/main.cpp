#define DOUBLE_SPACE() cout << endl << endl;

#define PI 3.141592653589

#define DEG2RAD(x) ((x) * PI / 180.0f)

#define TRIPLE_SPACE() cout << endl \
					        << endl \
							<< endl;

#include <iostream>
using namespace std;

int main()
{
//	***** MACRO 1 *****

	cout << "Hello";

	DOUBLE_SPACE()

	cout << "World";

	DOUBLE_SPACE()

//	***** MACRO 2 *****

	int deg = 90;

	cout << deg << " degrees = " << DEG2RAD(deg) << " radians";

//	***** MACRO 3 *****

	TRIPLE_SPACE()
		
	cout << "And we're out..." << endl;
	return 0;
}