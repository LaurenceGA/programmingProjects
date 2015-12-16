CC=g++
CFLAGS=-c -Wall -std=c++14
LDFLAGS=
SOURCES=exprType.cpp
OBJECTS=$(SOURCES:.cpp=.o)
EXECUTABLE=exprType
RM=rm -f

all: $(SOURCES) $(EXECUTABLE)
    
$(EXECUTABLE): $(OBJECTS) 
	$(CC) $(LDFLAGS) $(OBJECTS) -o $@

.cpp.o:
	$(CC) $(CFLAGS) $< -o $@

.PHONY : clean
clean:
	$(RM) $(OBJECTS) $(EXECUTABLE)
