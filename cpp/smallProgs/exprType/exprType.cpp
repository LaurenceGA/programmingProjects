#include <iostream>
#include <regex>

void showUsage(std::string progName) {
	std::cerr << "usage: " << progName <<
		" expression\n\tIf expression contains spaces put in quotes (\"\")" << std::endl;
}

const std::string OPERATOR = R"([\-\+/\*\^])";
const std::string NUMBER = R"(\d*\.?\d+)";
const std::string VARIABLE = R"([A-Za-z]{1})";

const std::string NUMORVAR = "("+ NUMBER + "|" + VARIABLE + ")";
const std::string SPACE = R"(\s+)";
const std::string OPTSPACE = R"(\s*)";

const std::string PREFIX = OPERATOR + SPACE + NUMORVAR + SPACE + NUMORVAR;
const std::string INFIX = NUMORVAR + OPTSPACE + OPERATOR + OPTSPACE + NUMORVAR;
const std::string POSTFIX = NUMORVAR + SPACE + NUMORVAR + SPACE + OPERATOR;

int const regexCount(std::string text, std::string pat) {
	std::regex rpat(pat);
	auto wordsBegin = std::sregex_iterator(text.begin(), text.end(), rpat);
	auto wordsEnd = std::sregex_iterator();

	return std::distance(wordsBegin, wordsEnd);
}

int const charCount(std::string text, char ch) {
	int count = 0;

	for(char c : text) {
		if (c == ch) count++;
	}

	return count;
}

int main(int argc, char* argv[]) {
	if (argc != 2) {
		showUsage(argv[0]);
	} else {
		std::string expr(argv[1]);

		auto operatorNum = regexCount(expr, OPERATOR);
		auto operandNum = regexCount(expr, NUMORVAR);

		if (operatorNum != operandNum-1) {	// Doesn't account for unary operators
			std::cerr << "This equation isn't formed correctly" << std::endl;
		} else if (charCount(expr, '(') != charCount(expr, ')')) {
				std::cerr << "Unequal brackets" << std::endl;
		} else {
			bool infixM, prefixM, postfixM;
			infixM = std::regex_search(expr, std::regex(INFIX));
			prefixM = std::regex_search(expr, std::regex(PREFIX));
			postfixM = std::regex_search(expr, std::regex(POSTFIX));
		
			// Another check for pre and postifx
			if (postfixM) {
				std::string postMatch = "^" + OPTSPACE + NUMORVAR +
				   	"(.*)" + OPERATOR + OPTSPACE + "$";

				postfixM = std::regex_match(expr, std::regex(postMatch));
			}

			if (prefixM) {
				std::string preMatch = "^" + OPTSPACE + OPERATOR +
				   	"(.*)" + NUMORVAR + OPTSPACE + "$";

				prefixM = std::regex_match(expr, std::regex(preMatch));
			}

			if (infixM) {
				std::string inMatch = R"(^\(*)" + OPTSPACE + R"(\(*)" + NUMORVAR +
				   	"(.*)" + NUMORVAR + R"(\)*)" + OPTSPACE + R"(\)*$)";

				infixM = std::regex_match(expr, std::regex(inMatch));
			}

			if (postfixM) {
				std::cout << "postfix" << std::endl;
			} else if (prefixM) {
				std::cout << "prefix" << std::endl;	
			} else if (infixM) {
				std::cout << "infix" << std::endl;
			} else {
				std::cout << "Not sure about that one";
			}
		}
	}

	return 0;
}
