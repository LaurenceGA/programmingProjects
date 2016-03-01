#ifndef BOARD_HPP
#define BOARD_HPP

#include <vector>
#include <iostream>

#include <SFML/Graphics.hpp>

enum class tile { empty, naught, cross };
enum class tileType { centre, edge, corner };

std::ostream& operator<<(std::ostream& os, const tile& t);
std::ostream& operator<<(std::ostream& os, const tileType& t);

class Grid {	// Multi dimensional array class
	public:
		Grid(int w, int h);

		int getWidth() { return this->width; }
		int getHeight() { return this->height; }

		tile get(int x, int y);
		void set(int x, int y, tile type);

		bool allFull();

	private:
		int width, height;
		std::vector<tile> tiles;
};

class Board {
	public:
		Board(int width, int height, int pixels);
		~Board();

		int getSize() { return this->grid->getWidth(); }

		// Drawing
		void drawNaught(sf::RenderWindow& window, sf::Vector2f pos, int radius);
		void drawCross(sf::RenderWindow& window, sf::Vector2f pos, int width);
		void draw(sf::RenderWindow& window);

		// Get/set tiles
		tile get(int x, int y) { return grid->get(x, y); }
		bool setTile(int x, int y, tile type);

		bool handleClick(float x, float y);

		// Winning
		tile checkWin();
		bool allFull() { return this->grid->allFull(); }

		// AI
		bool AITurn();

	private:
		Grid* grid;
		int boardThickness;
		int thickness;	// Width of naught/Cross lines
		sf::Color backCol;	// Board colour
		sf::Color foreCol;	// naught/cross color
		int padding;		// Padding on naughts/crosses
		int pixels;

		bool won;
		sf::Vector2f winLineOrigin;
		float winLineLen;
		int winAngle;

		void setWinLine(sf::Vector2f o, float length, int angle);

		tile rowSame(int y, tile type);
		tile colSame(int x, tile type);

		tileType getType(int x, int y);
		bool makeMove(int i, int j, tile t);
};


#endif
