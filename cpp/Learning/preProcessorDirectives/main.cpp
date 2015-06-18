/*
Preprocessor directives :
#define
#elif
#else
#endif
#error
#if
#ifdef
#ifndef
#import
#include
#line
#pragma
#undef
*/

#include <iostream>

#define NUM 1

#define TEXT "Preprocessor directives"

using namespace std;

int main()
{
	cout << NUM << endl;

	cout << TEXT << endl << endl;

#if NUM

	cout << "NUM is non-zero" << endl;

#else
	cout << "NUM is zero" << endl;
#endif

	return EXIT_SUCCESS;

}


/*	  
  Standard to begin the header file like this:

  #ifndef MAIN_H
  #define MAIN_H

  // The header file's contents

  #endif
  
  Preprocessor directives:
  #define
  #elif
  #else
  #endif
  #error
  #if
  #ifdef
  #ifndef
  #import
  #include
  #line
  #pragma
  #undef
*/