#include "headers/extree.h"
#include "headers/token.h"

#include <stack>
#include <iostream>
#include <memory>

Node::Node(std::unique_ptr<Token> t) : token(std::move(t)) { }

Node::Node(std::unique_ptr<Token> t, Node *l, Node *r) {
	token = std::move(t);
	left = l;
	right = r;
}

void Node::printToken() {
	switch (token->kind) {
		case oprtor:
			{
			auto o = static_cast<Oprtor*>(token.release());
			std::cout << o->typ << " ";
			token = std::unique_ptr<Token>(o);
			}
			break;

		case operand:
			{
			auto n = static_cast<Number*>(token.release());
			std::cout << n->value << " ";
			token = std::unique_ptr<Token>(n);
			}
			break;
		default:
			{}	
	}
}

void Node::printTree(eqnForm frm) {
	if (frm == prefix) {printToken();}
	if (left != nullptr) {left->printTree(frm);}
	if (frm == infix) {printToken();}
	if (right != nullptr) {right->printTree(frm);}
	if (frm == postfix) {printToken();}
}

exprTree::exprTree() {
	root = nullptr;
}

exprTree::exprTree(std::unique_ptr<Token> t) {	// Creates a one node tree
	root = new Node(std::move(t), nullptr, nullptr);
}

exprTree::exprTree(std::unique_ptr<Token> t, exprTree *l, exprTree *r) {
	root = new Node(std::move(t),
			l == nullptr ? nullptr : l->root,
			r == nullptr ? nullptr : r->root);
}	

exprTree::exprTree(TokenStream &ts) {
	root = nullptr;
	if (ts.frm == infix) {
		std::stack<std::unique_ptr<Token> > postEqn = inToPost(ts);
		root = treeFromPost(postEqn);
	} else if (ts.frm == prefix) {
		auto preEqn = getStack(ts);
		root = buildPre(preEqn)->root;
	} else if (ts.frm == postfix) {
		auto postEqn = getStack(ts);
		root = treeFromPost(postEqn);
	}
}

void exprTree::printTree(eqnForm frm) {
	root->printTree(frm); 
}

Node* exprTree::treeFromPost(std::stack<std::unique_ptr<Token> > &postEqn) {
	std::stack<exprTree*> treeStack;

	while(!postEqn.empty()) {
		std::unique_ptr<Token> t = std::move(postEqn.top());
		postEqn.pop();
		
		if (t->kind == operand) {
			exprTree *singleT = new exprTree(std::move(t));
			treeStack.push(singleT);
		} else if (t->kind == oprtor) {
			auto t1 = treeStack.top(); treeStack.pop();
			auto t2 = treeStack.top(); treeStack.pop();

			exprTree *newTree = new exprTree(std::move(t), t1, t2);

			treeStack.push(newTree);
		} else {
			// Shouldn't be anything else in a postfix equation
			std::cerr << "Malformed equation" << std::endl;
		}
	}
	
	Node *n = treeStack.top()->root;
	treeStack.pop();

	return n;
}

exprTree* exprTree::buildPre(std::stack<std::unique_ptr<Token> > &preEqn) {
	if (preEqn.empty()) {
		std::cerr << "Malformed equation" << std::endl;
		return nullptr;
	} else {
		std::unique_ptr<Token> t = std::move(preEqn.top());
		preEqn.pop();

		if (t->kind == operand) {
			exprTree *singleT = new exprTree(std::move(t));
			return singleT;
		} else if (t->kind == oprtor) {
			auto left = buildPre(preEqn);
			auto right = buildPre(preEqn);
			return new exprTree(std::move(t), left, right);
		} else {
			std:: cerr << "Malformed equation" << std::endl;
			return nullptr;
		}
	}
}

exprTree::~exprTree() {
	destroyTree();
}

void exprTree::destroyTree() {
	destroyTree(root);
}

void exprTree::destroyTree(Node *leaf) {
	if (leaf != nullptr) {
		destroyTree(leaf->left);
		destroyTree(leaf->right);
		delete leaf;
	}
}

// To cast static pointers
template<typename Derived, typename Base, typename Del>
std::unique_ptr<Derived, Del>
static_unique_ptr_cast(std::unique_ptr<Base, Del>&& p)
{
	auto d = static_cast<Derived *>(p.release());
	return std::unique_ptr<Derived, Del>(d, std::move(p.get_deleter()));
}

std::stack<std::unique_ptr<Token> > exprTree::getStack(TokenStream &ts) {
	std::stack<std::unique_ptr<Token> > reverse;

	while(!ts.empty()) {
		std::unique_ptr<Token> t = ts.get();

		reverse.push(std::move(t));
	}

	
	std::stack<std::unique_ptr<Token> > returnStack;
	while (!reverse.empty()) {
		returnStack.push(std::move(reverse.top()));
		reverse.pop();
	}

	return returnStack;
}

std::stack<std::unique_ptr<Token> > exprTree::inToPost(TokenStream &ts) {
	/* This will take your lousy stream of infix tokens and turn it into
	 * a glorious stack of tokens in postfix notation
	 *
	 * It is created in such a way the the begginning of the equation lies at the bottom of the stack
	 * so the stack is reversed at the end */
	std::stack<std::unique_ptr<Token> > postEqn;	// Reverse
	std::stack<std::unique_ptr<Token> > workingStack;

	while (!ts.empty()) {
		std::unique_ptr<Token> t = ts.get();

		if (t->kind == operand) {
			postEqn.push(std::move(t));
		} else if (t->kind == bracket) {
			auto temp = static_cast<Bracket*>(t.release());
			auto b = std::unique_ptr<Bracket>(temp);

			if (b->typ == '(') {
				workingStack.push(std::move(b));
			} else {
				// Closed bracket
				bool matched = false;	// Used for error checking
				while(!workingStack.empty()) {
					if (workingStack.top()->kind == bracket) {
						// It must be open becuse closed don't go on this stack
						workingStack.pop();	// We discard that open bracket
						matched = true;
						break;
					} else { // a little redundant beause if true it returns anyway
						// Add operand to the eqn
						postEqn.push(std::move(workingStack.top()));
						workingStack.pop();
					}
				}

				if (!matched) {
					std::cerr << "Unequal brackets!!" << std::endl;
				}
			}
		} else if (t->kind == oprtor) {
			auto temp = static_cast<Oprtor*>(t.release());
			auto o = std::unique_ptr<Oprtor>(temp);

			while(!workingStack.empty() &&
					workingStack.top()->kind != bracket &&
					(static_cast<Oprtor*>(workingStack.top().get()))->precedence >= o->precedence) {

				postEqn.push(std::move(workingStack.top()));
				workingStack.pop();
			}

			workingStack.push(std::move(o));
		}
	}

	while(!workingStack.empty()) {
		postEqn.push(std::move(workingStack.top()));
		workingStack.pop();
	}

	// This is where it's reversed to we can actually use it
	std::stack<std::unique_ptr<Token> > returnStack;
	while (!postEqn.empty()) {
		returnStack.push(std::move(postEqn.top()));
		postEqn.pop();
	}

	return returnStack;
}
