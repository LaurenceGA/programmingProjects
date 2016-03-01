#include <map>
#include <stdexcept>
#include <stack>

#include <SFML/Graphics.hpp>
#include <SFML/System/Vector2.hpp>

#include "headers/gameObject.hpp"

Object::Object(sf::Vector2f position) {
	pos = position;
	velocity.x = 0;
	velocity.y = 0;
	rotation = 0;
	depth = 0;
}

void Object::setSprite(sf::Texture& texture) {
	sprite.setTexture(texture);
}

bool Object::operator<(const Object& obj) const {
	return (depth < obj.depth);
}

void Object::destroy() {
	GameObjects::remove(id);
}

namespace GameObjects {
	// Private variables of the namespace
	namespace {
		std::map<int, Object*> instances;
		int currentId = 0;
		std::stack<int> removals;

		// Actual physical removal of the object, seperate to the interface version
		void __remove(int r) {
			delete instances[r];
			instances.erase(r);
		}

		void clearRemovals() {
			while (!removals.empty()) {
				int r = removals.top();
				__remove(r);
				removals.pop();
			}
		}
	}

	Object *instantiate(Object *obj) {
		obj->id = currentId;
		instances[currentId++] = obj;
		obj->start();

		return obj;
	}

	// Public version simply sets object to be removed
	void remove(int id) {
		removals.push(id);
	}

	void removeAll() {
		for (auto x : instances) {
			delete x.second;
		}
		instances.clear();
	}

	Object *get(int id) {
		if (instances.at(id) != nullptr) {
			return instances[id];
		} else {
			throw std::out_of_range("Instance id not found.");
		}
		return instances[id];
	}

	void drawAll(sf::RenderWindow& window, float dt) {
		// We need to sort by depth for drawing,
		// this is done using a depth map
		// Effectively iterate through objects twice
		std::map<int, std::vector<Object*> > depthMap;
		for (auto x : instances) {
			depthMap[x.second->depth].push_back(x.second);
		}

		// Actual draw calls
		for (auto x : depthMap) {
			for (auto y : x.second) {
				y->draw(window, dt);
			}
		}
	}

	void updateAll(float dt) {
		for (auto x : instances) {
			x.second->update(dt);

		}
		clearRemovals();
	}
}
