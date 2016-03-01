#ifndef GAME_HPP
#define GAME_HPP

#include <SFML/Graphics.hpp>

#include "texture_manager.hpp"

class Game {
	private:
		void loadTextures();
	public:
		sf::RenderWindow window;
		TextureManager texmngr;

		void handleInput();
		void update(const float dt);
		void draw(const float dt);
		void gameLoop();

		Game();
		~Game();
};

#endif
