CC=g++
CFLAGS=-c -Wall -std=c++14
LDFLAGS=-lsfml-graphics -lsfml-window -lsfml-system
SOURCES=main.cpp game.cpp texture_manager.cpp gameObject.cpp player.cpp bullet.cpp
OBJECTS=$(SOURCES:.cpp=.o)
EXECUTABLE=shooter
RM=rm -f

all: $(SOURCES) $(EXECUTABLE)
    
$(EXECUTABLE): $(OBJECTS) 
	$(CC) $(LDFLAGS) $(OBJECTS) -o $@

.cpp.o:
	$(CC) $(CFLAGS) $< -o $@

.PHONY : clean
clean:
	$(RM) $(OBJECTS) $(EXECUTABLE)
