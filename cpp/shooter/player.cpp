#include <SFML/Graphics.hpp>
#include <SFML/System/Vector2.hpp>

#include "headers/player.hpp"
#include "headers/bullet.hpp"
#include "headers/gameObject.hpp"

Player::Player(sf::Vector2f position, sf::Texture& texture)
				: Object(position) {	// Superclass constructor
	setSprite(texture);
	sf::FloatRect bounds = sprite.getLocalBounds();
	sprite.setOrigin(bounds.width/2, bounds.height/2);
	sprite.setPosition(position);
	sprite.setRotation(rotation);

	depth = 1;
}

void Player::update(float dt) {
	velocity = sf::Vector2f(0, 0);
	if (sf::Keyboard::isKeyPressed(sf::Keyboard::A)) {
		velocity.x -= moveSpeed;
	}
	if (sf::Keyboard::isKeyPressed(sf::Keyboard::D)) {
		velocity.x += moveSpeed;
	}
	if (sf::Keyboard::isKeyPressed(sf::Keyboard::W)) {
		velocity.y -= moveSpeed;
	}
	if (sf::Keyboard::isKeyPressed(sf::Keyboard::S)) {
		velocity.y += moveSpeed;
	}

	if (canFire) {
		if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left)) {
			fire(sf::Vector2f(-bulletSpeed, 0));
			rotation = 180;
		} else if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right)) {
			fire(sf::Vector2f(bulletSpeed, 0));
			rotation = 0;
		} else if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up)) {
			fire(sf::Vector2f(0, -bulletSpeed));
			rotation = 270;
		} else if (sf::Keyboard::isKeyPressed(sf::Keyboard::Down)) {
			fire(sf::Vector2f(0, bulletSpeed));
			rotation = 90;
		}
	} else {
		if (fireTimer.getElapsedTime() > fireCooldown) {
			canFire = true;
		}
	}

	pos += velocity * dt;
	sprite.setRotation(rotation);
	sprite.setPosition(pos);
}

void Player::fire(sf::Vector2f vel) {
	sf::FloatRect r = sprite.getLocalBounds();
	sf::Vector2f bulletPos(0, 0);
	bulletPos.x = r.width/2 * ((vel.x < 0) ? -1 : (vel.x > 0));
	bulletPos.y = r.height/2 * ((vel.y < 0) ? -1 : (vel.y > 0));

	GameObjects::instantiate(new Bullet(sf::Vector2f(pos + bulletPos), vel));
	canFire = false;
	fireTimer.restart();
}

void Player::draw(sf::RenderWindow& window, float dt) {
	window.draw(sprite);
}
