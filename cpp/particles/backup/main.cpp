#include <SFML/Graphics.hpp>

#include "headers/particles.hpp"
#include "headers/logger.hpp"

int main() {
	sf::Clock clock;
	sf::RenderWindow window(sf::VideoMode(800, 600), "Particles!");
	window.setFramerateLimit(60);

	ParticleSystem rsys(sf::Vector2f(200, 150), 2000, sf::Color::Red, sf::seconds(2));
	ParticleSystem gsys(sf::Vector2f(400, 150), 2000, sf::Color::Green, sf::seconds(3));
	ParticleSystem bsys(sf::Vector2f(600, 150), 2000, sf::Color::Blue, sf::seconds(2));

	while (window.isOpen()) {
		sf::Time elapsed = clock.restart();
		double dt = elapsed.asSeconds();

		sf::Event event;
		while (window.pollEvent(event)) {
			if (event.type == sf::Event::Closed) {
				window.close();
			} else if (event.type == sf::Event::KeyPressed) {
				if (event.key.code == sf::Keyboard::Escape) {
					window.close();
				}
			}
		}

		rsys.update(dt);
		bsys.update(dt);
		gsys.update(dt);

		window.clear();

		window.draw(rsys);
		window.draw(gsys);
		window.draw(bsys);

		window.display();
		
	}


	return 0;
}