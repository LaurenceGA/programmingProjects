#include <iostream>
#include <stack>
#include <sstream>
#include <locale>
#include <map>
#include <string>
#include <stdexcept>

using namespace std;

/*
This program takes an in-fix expression and returns a post-fix expression
*/

class Token {
	/* This class represents expression tokens such as operators, operands and brackets */
	/*
	  Allowed kinds are:
	  'n': number
	  '+': +	addition
	  '-': -	subtraction
	  '*': *	multiplication
	  '/': /	division
	  '%': %	modulo
	 */
	
	public:
		char kind;
		double value;
		int precedence;

		// Constructor for operands
		Token(char k, double v) {
			// Where k is kind and v is value
			kind = k;
			value = v;
		}
		// Constructor for brackets and operators
		Token(char k, int p) {
			// Where k is kind and p is precedence
			kind = k;
			precedence = p;
		}
		Token(){};
};

class Token_stream {
	public:
		stringstream stream;
		Token_stream(string s) {
			stream.str(s);
		}
		Token get();
		bool empty();
	private:
		map<char, int> precedencies = {{'+', 0}, {'-', 0}, {'*', 1}, {'/', 1}, {'%', 1}, {'(', 3}, {')', 3}};
};

Token Token_stream::get() {
	char ch;
	stream >> ch;
	if (ch == '.' or isdigit(ch)) {
		stream.putback(ch);
		double val;
		stream >> val;
		return Token{'n', val};
	} else switch(ch) {
		case '+': case '-': case '*': case '/': case '%': case '(': case ')':
			return Token{ch, precedencies[ch]};
		default:
			throw runtime_error("Bad char detected ("+ch+')');
	}
}

bool Token_stream::empty() {
	char ch;
	bool empty = !(stream >> ch);
	if (!empty) {stream.putback(ch);}
	return empty;
}

int main() {
	stack<Token> tokenStack;

	cout << "Please enter an in-fix expression: " << endl;
	
	string expr;
	getline(cin, expr);

	Token_stream ts{expr};

	stringstream postfix;

	while (!ts.empty()) {
		try {
			Token t = ts.get();
			if (t.kind == 'n') {
				postfix << t.value << ' ';
			} else if (tokenStack.empty() || tokenStack.top().kind == '(' || t.kind == '(') {
				tokenStack.push(t);
			} else if (t.kind == ')') {
				Token popped = tokenStack.top(); tokenStack.pop();
				while(popped.kind != '(') {
					postfix << popped.kind << ' ';
					popped = tokenStack.top();
					tokenStack.pop();
				}
			} else {
				while((!tokenStack.empty()) &&
						tokenStack.top().precedence >= t.precedence) {
					if (tokenStack.top().kind == '(') break;
					postfix << tokenStack.top().kind << ' ';
					tokenStack.pop();
				}
			
				tokenStack.push(t);
			}
		} catch (runtime_error const& e) {
			cerr << e.what() << endl;
		}
	}

	while (!tokenStack.empty()) {
		postfix << tokenStack.top().kind << ' ';
		tokenStack.pop();
	}

	cout << postfix.str() << endl;

	return 0;
}
