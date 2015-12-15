#include "headers/token.h"
#include <sstream>
#include <locale>
#include <locale>
#include <memory>
#include <stdexcept>

#include <iostream>	// To be romoved - only for testing

Token::Token() { }

Token::Token(tokenKind k) : kind(k) { }

Number::Number(double val) : Token(operand), value(val) {
	//value = val;
}

Oprtor::Oprtor(char t) : Token(oprtor) {
	typ = t;
	precedence = precedencies[t];
}

TokenStream::TokenStream(std::string s) {
	stream.str(s);
	getForm();
	tokenize();
}

std::unique_ptr<Token> TokenStream::get() {
	if (!tokens.empty()) {
		std::unique_ptr<Token> t = std::move(tokens.top());
		tokens.pop();
		return t;
	} else {
		throw std::runtime_error("Accessing empty token stream");
	}
}

bool TokenStream::empty() {
	return tokens.empty();
}

void TokenStream::getForm() {
	frm = prefix;
}

void TokenStream::tokenize() {
	char ch;
	std::stack<std::unique_ptr<Token> > workingStack;	// We can go and pop it all into token stack to reverse it later

	while(stream >> ch) {
		if (ch == '.' or isdigit(ch)) {
			stream.putback(ch);
			double val;
			stream >> val;
			workingStack.push(std::make_unique<Number>(val));
		} else switch(ch) {
			case '(': case ')':
				workingStack.push(std::make_unique<Bracket>(ch));
				break;
			case '*': case '/': case '%': case '^':
				workingStack.push(std::make_unique<Oprtor>(ch));
				break;
			case '+': case '-':
				if (frm == infix) {
					// If the equation is infx then these tokens are only unary if the previous token is an operator
					if (workingStack.empty() || workingStack.top()->kind == oprtor) {
						double val;
						stream >> val;
						
						if (ch == '-') {
							val = -val;
						}

						workingStack.push(std::make_unique<Number>(val));
					} else {
						workingStack.push(std::make_unique<Oprtor>(ch));
					}
				} else  { // It's either pre or post fix
					std::locale loc;
					if (isspace(stream.str()[int(stream.tellg())], loc)) {
						workingStack.push(std::make_unique<Oprtor>(ch));
					} else {
						// Unary
						double val;
						stream >> val;

						if (ch == '-') {
							val = -val;
						}

						workingStack.push(std::make_unique<Number>(val));
					}
				}
				break;
			default:
				throw std::runtime_error("Invalid tokens");
		}
	}
	// Once it's all on the stack we want to reverse it so it's in a propper order
	// That is, calling TokenStream's .get() should give the first token in the equation
	while (!workingStack.empty()) {
		tokens.push(std::move(workingStack.top()));
		workingStack.pop();
	}
}

void TokenStream::putback(std::unique_ptr<Token> t) {
	tokens.push(std::move(t));
}

Bracket::Bracket(char bType) : Token(bracket) {
	typ = bType;
}

