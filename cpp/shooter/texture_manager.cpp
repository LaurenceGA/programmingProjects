#include <map>
#include <string>

#include <SFML/Graphics.hpp>

#include "headers/texture_manager.hpp"

void TextureManager::loadTexture(const std::string& name, const std::string& filename) {
	sf::Texture tex;
	tex.loadFromFile(filename);

	this->textures[name] = tex;
}

sf::Texture& TextureManager::getRef(const std::string& texture) {
	return this->textures.at(texture);
}
