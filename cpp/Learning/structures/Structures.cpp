#include <iostream>
using namespace std;

typedef struct _MONEY {
	int		Dollars;	double	Cents;
} MONEY;

struct TEMP {
	int		Dollars;
	double	Cents;
};

int main()
{
	MONEY Change;
	TEMP Change2;

	Change.Cents = 0.02;
	Change.Dollars = 2;

	Change2.Cents = 0.04;
	Change2.Dollars = 4;
														
	cout << "The change comes out to " << Change.Dollars << " dollars and " << Change.Cents << " cents.\n";
	cout << "The change comes out to " << Change2.Dollars << " dollars and " << Change2.Cents << " cents.\n";
	
	return 0;
}