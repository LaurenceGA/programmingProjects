#ifndef PARTICLES_HPP
#define PARTICLES_HPP

#include <stack>
#include <map>

#include <SFML/Graphics.hpp>

class Particle {
	public:
		Particle(sf::Vertex* v, sf::Color c, sf::Time lt, double size);
		void setColour(sf::Color c);
		void setAlpha(sf::Uint8 a);
		void addVelocity(sf::Vector2f v);
		void setPos(sf::Vector2f p);

		sf::Vertex* quad;	// Points to first of quad
		sf::Color colour;
		sf::Time lifetime;
		sf::Time timeToDeath;
		sf::Vector2f velocity;
		double size;
		sf::Vector2f position;

	private:
		void resetVerticies();
};

class ParticleSystem : public sf::Drawable, public sf::Transformable {
	public:
		ParticleSystem(sf::Vector2f pos, int max_particles, sf::Color c, sf::Time lt, sf::Texture* tex);
		~ParticleSystem();

		void update(double dt);
		void resetParticle(Particle* p);
	
	private:
		void draw(sf::RenderTarget& target, sf::RenderStates states) const;
		void emit();

		void setFade() { this->fadeParticle = true; }
		void setGrav(double str) { this->gravStrength = str; }
		void setMaxParticles(int m) { this->max_particles = m; }
		void setEmmissionRate(int e) { this->emmissionRate = e; }
		

		// Member variables
		bool gravity;
		double gravStrength;
		bool fadeParticle;

		int max_particles;
		sf::VertexArray vertices;
		std::stack<Particle*> deadParticles;

		std::map<int, Particle*> aliveParticles;
		int currentId;

		int  emmissionRate;		// Particles per second
		float emmissionCarry;

		sf::Texture* tex;
};

#endif
