#include <SFML/Graphics.hpp>

#include "headers/board.hpp"

const int SIZE = 800, FPS = 60;

int main() {
	sf::RenderWindow window(sf::VideoMode(SIZE, SIZE), "Tic Tac Toe!");
	window.setFramerateLimit(FPS);

	Board* board = new Board(3, 3, SIZE);
	bool p1Turn = true;
	bool waiting = false;
	sf::Clock clock;
	sf::Time waitTime = sf::seconds(1);

	sf::Font font;
	if (!font.loadFromFile("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf")) return 1;
	sf::Text endMessage;
	endMessage.setFont(font);
	endMessage.setFillColor(sf::Color::Red);
	endMessage.setPosition(SIZE/2, SIZE/4);

	while (window.isOpen()) {
		sf::Event event;
		while (window.pollEvent(event)) {
			if (event.type == sf::Event::Closed) {
				window.close();
			} else if (event.type == sf::Event::KeyPressed) {
				if (event.key.code == sf::Keyboard::Escape) {
					window.close();
				}
			} else if (event.type == sf::Event::MouseButtonReleased ) {
				if (event.mouseButton.button == sf::Mouse::Left) {
					if (p1Turn && !waiting) {
						if (board->handleClick(event.mouseButton.x,
									event.mouseButton.y)) {
							p1Turn = !p1Turn;
						}
					}
				}
			}
		}

		if (waiting && clock.getElapsedTime() > waitTime) {
				window.close();
		}

		tile winner;
		if (!waiting && (((winner = board->checkWin()) != tile::empty) || board->allFull())) {
			switch (winner) {
				case tile::empty:
					std::cout << "It's a tie!" << std::endl;
					endMessage.setString("It's a tie!");
					break;
				case tile::cross:
					std::cout << "AI wins!" << std::endl;
					endMessage.setString("AI wins!");
					break;
				case tile::naught:
					std::cout << "You win!" << std::endl;
					endMessage.setString("You win!");
					break;
				default:
					break;
			}
			endMessage.setOrigin(endMessage.getLocalBounds().width / 2, 0);
			waiting = true;
			clock.restart();
		}

		if (!waiting && !p1Turn) {
			if (!board->AITurn()) {
				waiting = true;
				clock.restart();
			}
			p1Turn = !p1Turn;
		}

		window.clear(sf::Color::White);

		board->draw(window);

		if (waiting) {
			window.draw(endMessage);
		}

		window.display();
	}

	delete board;

	return 0;
}
