#include <iostream>
#include <sstream>
#include <locale>

#include "headers/extree.h"

/*
The goal of this program is to take expressions in either:
-in-fix notation
-pre-fix notation
-post-fix notation

These can then be solved or expressed in any of these notations

Interace:
The program works with one expression at a time
If one is entered, it becomes the working expression

Case insensitive:
Solve -> solve equation
Pre -> express in pre-fix notation
Post -> express in post-fix notation
In -> express in in-fix notation
*/

std::string lowercase(std::string str) {
	// This function iterates through the characters of a string
	// and returns a new one all lowercase
	std::locale loc;
	std::string newString = "";

	for (char ch : str) {
		newString += std::tolower(ch);
	}

	return newString;
}

void showHelp() {
	// Make sure the user knows what to do
	std::cout << "Enter an expression to work with" << std::endl
		<< "quit(q): quit" << std::endl
		<< "help(?): show help" << std::endl
		<< "solve: solve equation" << std::endl
		<< "infix: express as infix" << std::endl
		<< "postfix: express as postfix" << std::endl
		<< "prefix: express as prefix" << std::endl
		<< std::endl;
}

int main() {
	exprTree* workingExpr = nullptr;
	bool running = true;
	
	std::cout << "Please enter an expression (type '?' for help):" << std::endl;

	while (running) {
		std::cout << ">";
		
		std::string inputString;
	   	getline(std::cin, inputString);
		std::istringstream iss(inputString);

		std::string word;
		iss >> word;
		std::string lword = lowercase(word);		// Case insensitive		

		if (lword == "q" || lword == "quit") {
			running = false;
			std::cout << "Goodbye" << std::endl;
		} else if (lword == "help" || lword == "?") {
			showHelp();
		} else if (lword == "solve") {
			/*SOLVE*/
		} else if (lword == "infix") {
			/*INFIX*/
			if (workingExpr != nullptr) {
				std::cout << "infix: ";
				workingExpr->printTree(infix);
				std::cout << std::endl;
			}
		} else if (lword == "prefix") {
			/*PREFIX*/
			if (workingExpr != nullptr) {
				std::cout << "prefix: ";
				workingExpr->printTree(prefix);
				std::cout << std::endl;
			}
		} else if (lword == "postfix") {
			/*POSTFIX*/
			if (workingExpr != nullptr) {
				std::cout << "postfix: ";
				workingExpr->printTree(postfix);
				std::cout << std::endl;
			}
		} else if (lword == "") {
			//std::cerr << "Invalid command" << std::endl;
			//std::cout << "Command can't be empty" << std::endl;
		} else {
			iss.seekg(0);
			try {
				TokenStream ts {iss.str()};
				std::cout << "Working with: " << iss.str() << std::endl;

				// Clearn up when we're done
				if (workingExpr != nullptr) {
					delete workingExpr;
				}

				workingExpr = new exprTree(ts);
			} catch (std::runtime_error) {
				std::cerr << "Command invalid" << std::endl;
			}
		}
	}

	return 0;
}
