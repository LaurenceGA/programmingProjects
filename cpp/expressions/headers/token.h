// token.h
#ifndef TOKEN_H
#define TOKEN_H

#include <sstream>
#include <stack>
#include <map>
#include <memory>

enum tokenKind {
	oprtor,
	operand,
	bracket
};

enum eqnForm {
	prefix,
	infix,
	postfix
};

const char negate = '_';

class Token {
	public:
		Token();
		Token(tokenKind k);
		
		tokenKind kind;
};

class TokenStream {
	public:
		TokenStream(std::string s);

		std::unique_ptr<Token> get();
		void putback(std::unique_ptr<Token>);
		void tokenize();
		bool empty();

		std::stringstream stream;
		eqnForm frm;
	private:
		std::stack<std::unique_ptr<Token> > tokens;

		void getForm();
};

class Number : public Token {
	public:
		Number(double val);

		double value;
};

class Variable : public Token {
	public:
		char name;
};

// Operators
// +, -, *, /, %, ^ (include unary + & -)
class Oprtor : public Token {
	public:
		Oprtor(char t);

		char typ; // Which operation it is
		int precedence = 0;
	private:
		std::map<char, int> precedencies = {{'+', 0}, {'-', 0}, {'*', 1}, {'/', 1}, {'%', 1}};
};

class Bracket : public Token {
	public:
		Bracket(char bType);

		tokenKind kind = bracket;
		char typ;
};

#endif
