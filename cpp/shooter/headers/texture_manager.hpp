#ifndef TEXTURE_MANAGER_HPP
#define TEXtURE_MANAGER_HPP

#include <string>
#include <map>

#include <SFML/Graphics.hpp>

class TextureManager {
	private:
		// Map of textures used
		std::map<std::string, sf::Texture> textures;

	public:
		void loadTexture(const std::string& name, const std::string& filename);
		sf::Texture& getRef(const std::string& texture);
		TextureManager() {}
};

#endif
