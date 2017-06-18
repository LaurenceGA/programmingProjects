#include <cmath>
#include <iostream>
#include <stdexcept>
#include <random>
#include <functional>

#include "headers/board.hpp"

#include <SFML/Graphics.hpp>

Board::Board(int width, int height, int pixels) : pixels(pixels) {
	this->grid = new Grid(width, height);
	this->thickness = 2;
	this->boardThickness = 2;
	this->backCol = sf::Color::Blue;
	this->foreCol = sf::Color::Red;
	this->padding = 40;
	this->won = false;
	this->winLineLen = 0;
}

Board::~Board() {
	delete grid;
}

void Board::draw(sf::RenderWindow& window) {
	auto size = window.getSize();	// an sf vector

	int inc = size.x / this->getSize();
	sf::RectangleShape line(sf::Vector2f(this->boardThickness, size.y));
	line.setFillColor(this->backCol);
	for (int i=inc; i < static_cast<int>(size.y - inc); i+=inc) {
		line.setPosition(i, 0);
		window.draw(line);
	}

	inc = size.y / this->getSize();
	line = sf::RectangleShape(sf::Vector2f(size.x, this->boardThickness));
	line.setFillColor(this->backCol);
	for (int i=inc; i < static_cast<int>(size.x - inc); i+=inc) {
		line.setPosition(0, i);
		window.draw(line);
	}

	// Naughts and/or crosses
	for (int j=0; j < this->getSize(); j++) {
		for (int i=0; i < this->getSize(); i++) {
			int tileWidth = size.x / this->getSize();
			switch (this->get(i, j)) {
				case tile::naught:
					drawNaught(window,
							sf::Vector2f(	// Pos
								this->padding + i * tileWidth,	// x
								this->padding + j * tileWidth),	// y
							tileWidth / 2 - this->padding);					// radius
					break;
				case tile::cross:
					drawCross(window,
							sf::Vector2f(	// Pos
								this->padding + i * tileWidth,	// x
								this->padding + j * tileWidth),	// y
							tileWidth - this->padding*2);					// width
					break;
				default:
					break;
			}
		}
	}

	if (this->won) {
		sf::RectangleShape line(sf::Vector2f(this->winLineLen, this->thickness));
		line.setFillColor(this->foreCol);
		line.setRotation(this->winAngle);
		line.setOrigin(this->winLineLen/2, this->thickness/2);
		line.setPosition(this->winLineOrigin);
		window.draw(line);
	}
}

void Board::drawNaught(sf::RenderWindow& window, sf::Vector2f pos, int radius) {
	sf::CircleShape naught(radius);
	naught.setFillColor(sf::Color::Transparent);
	naught.setOutlineThickness(this->thickness);
	naught.setOutlineColor(this->foreCol);
	naught.setPosition(pos);
	window.draw(naught);
}

void Board::drawCross(sf::RenderWindow& window, sf::Vector2f pos, int width) {
	double length = std::sqrt(width*width + width*width);
	sf::RectangleShape line(sf::Vector2f(length, this->thickness));
	line.setFillColor(this->foreCol);
	line.setOrigin(sf::Vector2f(length/2, this->thickness/2));
	line.setPosition(pos + sf::Vector2f(width/2, width/2));

	line.rotate(45);
	window.draw(line);

	line.rotate(90);
	window.draw(line);
}

bool Board::setTile(int x, int y, tile type) {
	tile current = grid->get(x, y);
	if (current == tile::empty) {
		grid->set(x, y, type);
		return true;
	}
	return false;
}

bool Board::handleClick(float x, float y) {
	int h = static_cast<int>(x / pixels * this->getSize());
	int v = static_cast<int>(y / pixels * this->getSize());

	return setTile(h, v, tile::naught);
}

tile Board::checkWin() {
	tile type = tile::empty;
	// Rows
	for (int i=0; i < this->getSize(); i++) {
		if ((type = this->get(0, i)) != tile::empty) {
			if (rowSame(i, type) != tile::empty) {
				int inc = this->pixels / this->getSize();
				this->setWinLine(
						sf::Vector2f(this->pixels/2, i * inc + inc/2),	// Pos
						this->pixels - this->padding,
						0);	// Angle
				return type;
			}
		}
	}

	// Columns
	for (int i=0; i < this->getSize(); i++) {
		if ((type = this->get(i, 0)) != tile::empty) {
			if (colSame(i, type) != tile::empty) {
				int inc = this->pixels / this->getSize();
				this->setWinLine(
						sf::Vector2f(i * inc + inc/2, this->pixels/2),	// Pos
						this->pixels - this->padding,
						90);	// Angle
				return type;
			}
		}
	}

	// Diagonals
	if ((type = this->get(0, 0)) != tile::empty) {
		bool same = true;
		for (int i=1, j=1; i < this->getSize(); i++, j++) {
			if (this->get(i, j) != type) {
				same = false;
				break;
			}
		}
		if (same) {
			this->setWinLine(sf::Vector2f(this->pixels/2, this->pixels/2),
					std::sqrt(this->pixels*this->pixels + this->pixels*this->pixels) - this->padding,
					45);
			return type;
		}
	}

	if ((type = this->get(0, this->getSize()-1)) != tile::empty) {
		bool same = true;
		for (int i=1, j=this->getSize()-2; i < this->getSize(); i++, j--) {
			if (this->get(i, j) != type) {
				same = false;
				break;
			}
		}
		if (same) {
			this->setWinLine(sf::Vector2f(this->pixels/2, this->pixels/2),
					std::sqrt(this->pixels*this->pixels + this->pixels*this->pixels) - this->padding,
					-45);
			return type;
		}
	}

	return tile::empty;
}

tile Board::rowSame(int y, tile type) {
	for (int i=1; i < this->getSize(); i++) {
		if (this->get(i, y) != type) return tile::empty;
	}
	return type;
}

tile Board::colSame(int x, tile type) {
	for (int i=1; i < this->getSize(); i++) {
		if (this->get(x, i) != type) return tile::empty;
	}
	return type;
}

void Board::setWinLine(sf::Vector2f o, float length, int angle) {
	this->won = true;
	this->winLineOrigin = o;
	this->winLineLen = length;
	this->winAngle = angle;
}

bool Board::AITurn() {
        /*
        First we see if we can just straight up win. We do so if possible
        This isn't usually a common outcome.
        Next we try to block the player from winning. This happens often.
        If neither of those options work out, we just place a cross randomly
        */
	if (this->getSize() == 3) {		// Only for 3x3
	// Try to win
        // We go through each square and see if it provide a change to win
	for (int i=0; i < this->getSize(); i++) {
		for (int j=0; j < this->getSize(); j++) {
			if (this->get(i, j) == tile::cross) {
				if (this->makeMove(i, j, tile::cross)) {
					std::cout << "AI: win" << std::endl;
					return true;
				}
			}
		}
	}
	// Try to block
        // We go through each square, and see if we can block the player
	for (int i=0; i < this->getSize(); i++) {
		for (int j=0; j < this->getSize(); j++) {
			if (this->get(i, j) == tile::naught) {
				if (this->makeMove(i, j, tile::naught)) {
					std::cout << "AI: block" << std::endl;
					return true;
				}
			}
		}
	}
	}

	std::cout << "AI: random" << std::endl;

	std::random_device r;
	std::seed_seq seed{r(), r(), r(), r(), r(), r(), r(), r(), r()};

	std::default_random_engine generator(seed);
	std::uniform_int_distribution<int> dist(0, this->getSize()-1);
	auto rand_pos = std::bind(dist, generator);

	int cnt = 1;
	// int giveUp = 10000;

	int p_x = rand_pos(), p_y = rand_pos();
	while (this->get(p_x, p_y) != tile::empty) {
		p_x = rand_pos();
		p_y = rand_pos();
		//if (cnt > giveUp) return false;
		cnt++;
	}
	this->setTile(p_x, p_y, tile::cross);
	return true;
}

bool Board::makeMove(int i, int j, tile t) {
	switch (this->getType(i, j)) {
		case tileType::centre:	// CENTRE
			for (int ii=-1; ii < 2; ii++) {
				for (int jj=-1; jj < 2; jj++) {
					if (ii == 0 && jj == 0) continue;
					// one side is t and opposite empty, fill opposite
					if (this->get(i-ii, j-jj) == t && this->get(i+ii, j+jj) == tile::empty) {
						this->setTile(i+ii, j+jj, tile::cross);
						return true;
					}
				}
			}
		break;

		case tileType::corner:	// CORNERS
		{
			int rel_i = i - 1;
			int rel_j = j - 1;
			if (this->get(i-rel_i, j-rel_j) == t && this->get(i-rel_i*2, j-rel_j*2) == tile::empty) {
				this->setTile(i-rel_i*2, j-rel_j*2, tile::cross);
				return true;
			} else if (this->get(i-rel_i, j) == t && this->get(i-rel_i*2, j) == tile::empty) {
				this->setTile(i-rel_i*2, j, tile::cross);
				return true;
			} else if (this->get(i, j-rel_j) == t && this->get(i, j-rel_j*2) == tile::empty) {
				this->setTile(i, j-rel_j*2, tile::cross);
				return true;
			} else if (this->get(i-rel_i*2, j-rel_j*2) == t && this->get(i-rel_i, j-rel_j) == tile::empty) {
				this->setTile(i-rel_i, j-rel_j, tile::cross);
				return true;
			} else if (this->get(i-rel_i*2, j) == t && this->get(i-rel_i, j) == tile::empty) {
				this->setTile(i-rel_i, j, tile::cross);
				return true;
			} else if (this->get(i, j-rel_j*2) == t && this->get(i, j-rel_j) == tile::empty) {
				this->setTile(i, j-rel_j, tile::cross);
				return true;
			}
		}
		break;

		default:	// Note: purposefully catches tileType edges as it's covered by the others
		break;
	}
	return false;
}

tileType Board::getType(int x, int y) {
	if (x == (this->getSize()-1) / 2 && y == (this->getSize()-1) / 2) {
		return tileType::centre;
	} else if (x == 0) {
		if (y == 0 || y == this->getSize()-1) {
			return tileType::corner;
		}
	} else if (x == this->getSize()-1) {
		if (y == 0 || y == this->getSize()-1) {
			return tileType::corner;
		}
	}
	return tileType::edge;
}

Grid::Grid(int w, int h)
	: width(w), height(h) {
	this->tiles = std::vector<tile>(width * height, tile::empty);
}

tile Grid::get(int x, int y) {
	if (x < 0 || x >= this->width || y < 0 || y >= this->height) {
		throw std::out_of_range("can't get tile");
	}
	return this->tiles[y*width + x];
}

void Grid::set(int x, int y, tile type) {
	this->tiles[y*width + x] = type;
}

bool Grid::allFull() {
	for (auto x : this->tiles) {
		if (x == tile::empty) return false;
	}
	return true;
}

// For debugging
std::ostream& operator<<(std::ostream& os, const tile& t) {
	switch (t) {
		case tile::empty:
			os << "empty";
			break;
		case tile::naught:
			os << "naught";
			break;
		case tile::cross:
			os << "cross";
			break;
		default:
			os << "ERROR: unknwon tile type";
			break;
	}
	return os;
}

std::ostream& operator<<(std::ostream& os, const tileType& t) {
	switch (t) {
		case tileType::centre:
			os << "centre";
			break;
		case tileType::edge:
			os << "edge";
			break;
		case tileType::corner:
			os << "corner";
			break;
		default:
			os << "ERROR, unknown tile type";
			break;
	}
	return os;
}
