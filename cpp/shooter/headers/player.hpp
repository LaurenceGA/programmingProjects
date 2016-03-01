#ifndef PLAYER_HPP
#define PLAYER_HPP

#include <SFML/Graphics.hpp>

#include "gameObject.hpp"

class Player : public Object {
	public:
		void update(float dt);
		void draw(sf::RenderWindow& window, float dt);

		Player(sf::Vector2f position, sf::Texture& texture);
	private:
		float moveSpeed = 150;	// Pixels per second

		float bulletSpeed = 400;
		bool canFire = true;
		sf::Time fireCooldown = sf::milliseconds(200);
		sf::Clock fireTimer;

		void fire(sf::Vector2f vel);
};

#endif
