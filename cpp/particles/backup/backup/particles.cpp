#include "headers/particles.hpp"
#include "headers/logger.hpp"

#include <cstdlib>
#include <cmath>

Particle::Particle(sf::Vertex& v, sf::Color c, sf::Time lt) :
lifetime(lt),
vertex(v),
colour(c) {
	this->colour = this->colour;
	this->vertex.color = sf::Color::Transparent;
	this->timeToDeath = lt;
}

ParticleSystem::ParticleSystem(sf::Vector2f pos, int max_particles, sf::Color c, sf::Time lt) :
max_particles(max_particles),
vertices(sf::Points, max_particles) {
	for (int i=0; i < max_particles; i++) {
		this->deadParticles.push(new Particle(this->vertices[i], c, lt));
		if (!this->deadParticles.top()) {
			Logger::Log("FAILED TO ALLOCATE!!");
		}
	}
	this->setPosition(pos);
	this->gravity = true;
	this->gravStrength = 50;
	this->emmissionRate = 1000;
	this->emmissionCarry = 0;
	this->fadeParticle = true;
}

ParticleSystem::~ParticleSystem() {
	for (auto p : this->aliveParticles) {
		delete p.second;
		p.second = nullptr;
	}
	Particle* p;
	while (!this->deadParticles.empty()) {
		p = this->deadParticles.top();
		delete p;
		this->deadParticles.pop();
	}
}

void ParticleSystem::update(double dt) {
	float fdt = static_cast<float>(dt);

	// For all particles
	for (auto it=this->aliveParticles.begin(); it!=this->aliveParticles.end();) {
		auto p = it->second;

		p->timeToDeath -= sf::seconds(dt);
		if (p->timeToDeath < sf::Time::Zero) {
			p->vertex.color = sf::Color::Transparent;
			this->deadParticles.push(p);
			this->aliveParticles.erase(it++);
			continue;
		}

		float ratio = p->timeToDeath.asSeconds() / p->lifetime.asSeconds();
		p->vertex.color.a = static_cast<sf::Uint8>(ratio * 255);

		if (this->gravity) {
			p->velocity += sf::Vector2f(0, this->gravStrength);
		}
		p->vertex.position += p->velocity * fdt;
		it++;
	}

	// Emit particles
	float particlesToEmit = this->emmissionRate * (dt + this->emmissionCarry);
	int actualEmmission = static_cast<int>(particlesToEmit);
	this->emmissionCarry = (particlesToEmit - actualEmmission) / this->emmissionRate;
	for (int i=0; i < actualEmmission; i++) this->emit();
}

void ParticleSystem::emit() {
	if (!this->deadParticles.empty()) {
		Particle* p = this->deadParticles.top();
		this->aliveParticles[this->currentId++] = p;
		this->deadParticles.pop();

		this->resetParticle(p);
	}
}

void ParticleSystem::resetParticle(Particle *p) {
	p->vertex.position = sf::Vector2f(0, 0);
	p->velocity = sf::Vector2f(0, 0);
	p->vertex.color = p->colour;
	p->timeToDeath = p->lifetime;

	double angle = (std::rand() % 360) * 3.14 / 180;
	double speed = (std::rand() % 50) + 50;
	p->velocity = sf::Vector2f(std::cos(angle) * speed, std::sin(angle) * speed);
}

void ParticleSystem::draw(sf::RenderTarget& target, sf::RenderStates states) const {
	states.transform *= getTransform();
	states.texture = NULL;
	target.draw(this->vertices, states);
}
