#include "headers/particles.hpp"
#include "headers/logger.hpp"

#include <cstdlib>
#include <cmath>

Particle::Particle(sf::Vertex* v, sf::Color c, sf::Time lt, double size) :
quad(v),
colour(c),
lifetime(lt),
size(size) {
	this->setColour(sf::Color::Transparent);
	this->timeToDeath = lt;
}

void Particle::setColour(sf::Color c) {
	this->quad[0].color = c;
	this->quad[1].color = c;
	this->quad[2].color = c;
	this->quad[3].color = c;
}

void Particle::setAlpha(sf::Uint8 a) {
	// Bounds check
	this->quad[0].color.a = a;
	this->quad[1].color.a = a;
	this->quad[2].color.a = a;
	this->quad[3].color.a = a;
}

void Particle::addVelocity(sf::Vector2f v) {
	this->position += v;
	this->resetVerticies();
}

void Particle::resetVerticies() {
	this->quad[0].position = this->position + sf::Vector2f(-this->size/2, -this->size/2);
	this->quad[1].position = this->position + sf::Vector2f(this->size/2, -this->size/2);
	this->quad[2].position = this->position + sf::Vector2f(this->size/2, this->size/2);
	this->quad[3].position = this->position + sf::Vector2f(-this->size/2, this->size/2);
}

void Particle::setPos(sf::Vector2f p) {
	this->position = p;
	this->resetVerticies();
}

ParticleSystem::ParticleSystem(sf::Vector2f pos, int max_particles, sf::Color c, sf::Time lt, sf::Texture* tex) :
max_particles(max_particles),
vertices(sf::Quads, max_particles*4),	// 4 corners per quad
tex(tex) {
	sf::Vector2u texSize;
	if (tex != NULL)
		texSize = tex->getSize();
	for (int i=0; i < max_particles; i++) {
		// First set the texture cooirds
		if (tex != NULL) {
			this->vertices[i*4].texCoords = sf::Vector2f(0, 0);
			this->vertices[i*4 + 1].texCoords = sf::Vector2f(texSize.x, 0);
			this->vertices[i*4 + 2].texCoords = sf::Vector2f(texSize.x, texSize.y);
			this->vertices[i*4 + 3].texCoords = sf::Vector2f(0, texSize.y);
		}

		// Then give vertexes to particles we create
		this->deadParticles.push(new Particle(&(this->vertices[i*4]), c, lt, 4));
		if (!this->deadParticles.top()) {
			Logger::Log("FAILED TO ALLOCATE!!");
		}
	}
	this->setPosition(pos);
	this->gravity = true;
	this->gravStrength = 3;
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
			p->setColour(sf::Color::Transparent);
			this->deadParticles.push(p);
			this->aliveParticles.erase(it++);
			continue;
		}

		float ratio = p->timeToDeath.asSeconds() / p->lifetime.asSeconds();
		p->setAlpha(static_cast<sf::Uint8>(ratio * 255));

		if (this->gravity) {
			p->velocity += sf::Vector2f(0, this->gravStrength);
		}
		p->addVelocity(p->velocity * fdt);
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
	p->setPos(sf::Vector2f(0, 0));
	p->velocity = sf::Vector2f(0, 0);
	p->setColour(p->colour);
	p->timeToDeath = p->lifetime;

	double angle = (std::rand() % 360) * 3.14 / 180;
	double speed = (std::rand() % 50) + 50;
	p->velocity = sf::Vector2f(std::cos(angle) * speed, std::sin(angle) * speed);
}

void ParticleSystem::draw(sf::RenderTarget& target, sf::RenderStates states) const {
	states.transform *= getTransform();
	states.texture = this->tex;
	states.blendMode = sf::BlendAdd;
	target.draw(this->vertices, states);
}
