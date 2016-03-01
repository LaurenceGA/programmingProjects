#include <SFML/Graphics.hpp>

#include "headers/game.hpp"
#include "headers/gameObject.hpp"
#include "headers/player.hpp"

void Game::gameLoop() {
	sf::Clock clock;

	while (window.isOpen()) {
		sf::Time elapsed = clock.restart();
		float dt = elapsed.asSeconds();

		handleInput();
		update(dt);

		window.clear(sf::Color::Cyan);

		//Draw code
		draw(dt);

		window.display();
	}
	GameObjects::removeAll();
}

void Game::handleInput() {
	sf::Event event;
	// Poll events
	while (window.pollEvent(event)) {
		if (event.type == sf::Event::Closed) {
			// Close the window when the user wants to
			window.close();
		} else if (event.type == sf::Event::KeyPressed) {
			if (event.key.code == sf::Keyboard::Escape) {
				window.close();
			}
		}
	}
}

void Game::update(float dt) {
	GameObjects::updateAll(dt);
}

void Game::draw(float dt) {
	GameObjects::drawAll(window, dt);
}

Game::Game() {
	loadTextures();

	// Settings
	sf::ContextSettings settings;
	settings.antialiasingLevel = 4;

	window.create(sf::VideoMode(800, 600), "Pew! Pew!",
			sf::Style::Titlebar | sf::Style::Close, settings);	// Can't be resized
	window.setFramerateLimit(60);

	GameObjects::instantiate(new Player(sf::Vector2f(50, 50), texmngr.getRef("circle")));
}

Game::~Game() {
	// None
}

void Game::loadTextures() {
	texmngr.loadTexture("circle", "resources/sprites/circle.png");	
}
