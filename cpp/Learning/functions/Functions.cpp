#include <iostream>
using namespace std;

// Prototype
void DrawMenu();

void DrawMenu()
{
	cout << "\t\t ****************Game Menu**************** \n";
	cout << "\t\t *                                       * \n";
	cout << "\t\t *   1) New Game                         * \n";
	cout << "\t\t *   2) Load Game                        * \n";
	cout << "\t\t *   3) Save Game                        * \n";
	cout << "\t\t *   4) Inventory                        * \n";
	cout << "\t\t *   5) Options                          * \n";
	cout << "\t\t *   6) Quit                             * \n";
	cout << "\t\t *                                       * \n";
	cout << "\t\t ***************************************** \n";	
}															

int main()
{
	bool bStillPlaying=true;
	int choice=0;

	while(bStillPlaying)
	{
		DrawMenu();
	
		cout << "Choose from the menu: ";

		cin >> choice;

		switch(choice)
		{
			case 1: cout << "You chose a New Game!\n";
					break;
			case 2: cout << "You chose to Load a Game!\n";
					break;
			case 3: cout << "You chose to Save a Game!\n";
					break;
			case 4: cout << "You chose your Inventory!\n";
					break;
			case 5: cout << "You chose Options!\n";
					break;
			case 6: bStillPlaying = false;
					cout << "Game over.\n";
					break;
		}
	}
	
	return 0;
}