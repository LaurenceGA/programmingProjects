#ifndef PARTICLES_HPP
#define PARTICLES_HPP

#include <stack>
#include <map>

#include <SFML/Graphics.hpp>

class Particle {
	public:
		Particle(sf::Vertex& v, sf::Color c, sf::Time lt);

		sf::Time lifetime;
		sf::Time timeToDeath;
		sf::Vector2f velocity;
		sf::Vertex& vertex;
		sf::Color colour;
};

class ParticleSystem : public sf::Drawable, public sf::Transformable {
	public:
		ParticleSystem(sf::Vector2f pos, int max_particles, sf::Color c, sf::Time lt);
		~ParticleSystem();

		void update(double dt);
		void resetParticle(Particle* p);
	
	private:
		void draw(sf::RenderTarget& target, sf::RenderStates states) const;
		void emit();
		
		bool gravity;
		bool gravStrength;
		bool fadeParticle;

		int max_particles;
		sf::VertexArray vertices;
		std::stack<Particle*> deadParticles;

		std::map<int, Particle*> aliveParticles;
		int currentId;

		int  emmissionRate;		// Particles per second
		float emmissionCarry;
};

#endif
