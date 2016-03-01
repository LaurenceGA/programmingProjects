#ifndef BULLET_HPP
#define BULLET_HPP

#include <SFML/Graphics.hpp>

#include "gameObject.hpp"

class Bullet : public Object {
	public:
		void update(float dt);
		void draw(sf::RenderWindow& window, float dt);

		Bullet(sf::Vector2f position, sf::Vector2f velocity);
	private:
		float radius = 5;
		sf::Color col = sf::Color::Blue;
};

#endif
