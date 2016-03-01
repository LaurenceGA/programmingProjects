#ifndef GAME_OBJECT_HPP
#define GAME_OBJECT_HPP

#include <SFML/Graphics.hpp>
#include <SFML/System/Vector2.hpp>

class Object {
	public:
		int id;

		sf::Vector2f pos;
		sf::Vector2f velocity;
		double rotation;

		int depth;	// layer

		virtual void destroy();		// Destroy itself
		virtual void start() {}				// Called on initialisation
		virtual void update(float dt) {}	// Object logic
		virtual void draw(sf::RenderWindow& window, float dt) {}	// Draw calls

		bool operator<(const Object& obj) const;

		Object(sf::Vector2f position);
		virtual ~Object() {}
	
	protected:
		void setSprite(sf::Texture& texture);

		sf::Sprite sprite;
};

namespace GameObjects {
	Object *instantiate(Object *obj);
	void remove(int id);
	Object *get(int id);

	void drawAll(sf::RenderWindow& window, float dt);
	void updateAll(float dt);

	void removeAll();
}

#endif

