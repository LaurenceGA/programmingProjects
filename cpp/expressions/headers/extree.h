#ifndef EXTREE_H
#define EXTREE_H
#include "token.h"
#include <memory>

class Node {
	public:
		// Constructors
		Node(std::unique_ptr<Token> t);
		Node(std::unique_ptr<Token> t, Node *l, Node *r);

		// Recursively print out the tree
		void printTree(eqnForm frm);

		std::unique_ptr<Token> token; // Root cargo
		Node *left;		// Left subtree
		Node *right;	// Right subtree
	private:
		void printToken();	// Handle print the right characters
};

class exprTree {
	public:
		// Constructors/destructor
		exprTree();
		exprTree(std::unique_ptr<Token> t);
		exprTree(std::unique_ptr<Token> t, exprTree *l, exprTree *r);
		exprTree(TokenStream &ts);
		~exprTree();

		void printTree(eqnForm frm);

		//void insert(Token t);
		void destroyTree();
	private:
		Node *root;
		
		// Make a tree from a postfix notation
		Node* treeFromPost(std::stack<std::unique_ptr<Token> > &postEqn);
		// Arrange infix tokens into postfix
		std::stack<std::unique_ptr<Token> > inToPost(TokenStream &ts);
		void destroyTree(Node *leaf);

};

#endif
