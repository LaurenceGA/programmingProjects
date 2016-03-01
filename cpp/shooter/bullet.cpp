#include <SFML/Graphics.hpp>
#include <SFML/System/Vector2.hpp>

#include "headers/bullet.hpp"

Bullet::Bullet(sf::Vector2f position, sf::Vector2f vel)
				: Object(position) {
	velocity = vel;
}

void Bullet::update(float dt) {
	pos += velocity * dt;
	if (pos.x < 0 || pos.x > 800 || pos.y < 0 || pos.y > 600) {
		destroy();
	}
	// if (pos.x - radius > 800) pos.x = -radius;
	// if (pos.x + radius < 0) pos.x = 800 + radius;
	// if (pos.y - radius > 600) pos.y = -radius;
	// if (pos.y + radius < 0) pos.y = 600 + radius;
}

void Bullet::draw(sf::RenderWindow& window, float dt) {
	sf::CircleShape shape(radius);
	shape.setOrigin(radius, radius);
	shape.setFillColor(col);
	shape.setPosition(pos);
	window.draw(shape);
}
