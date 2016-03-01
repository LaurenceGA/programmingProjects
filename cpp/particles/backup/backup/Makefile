CC=g++
CFLAGS=-c -Wall -std=c++14
LDFLAGS=-lsfml-graphics -lsfml-window -lsfml-system
SOURCES=main.cpp particles.cpp
OBJECTS=$(SOURCES:.cpp=.o)
EXECUTABLE=particles
RM=rm -f

all: $(SOURCES) $(EXECUTABLE)
    
$(EXECUTABLE): $(OBJECTS) 
	$(CC) $(LDFLAGS) $(OBJECTS) -o $@

.cpp.o:
	$(CC) $(CFLAGS) $< -o $@

.PHONY : clean
clean:
	$(RM) $(OBJECTS) $(EXECUTABLE)
