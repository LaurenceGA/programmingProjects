#ifndef LOGGER_HPP
#define LOGGER_HPP

#include <iostream>
#include <string>

namespace Logger {
	template <typename T>
	void Log(T out) {
		std::cout << out << std::endl;
	}
}

#endif
