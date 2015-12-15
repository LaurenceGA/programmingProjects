CC=gcc
STD=c11
CFLAGS=-c -Wall -std=$(STD)
LDFLAGS=
SOURCES=main
OBJECTS=$(SOURCES:.c=.o)
EXECUTABLE=out
RM=rm -f

all: $(SOURCES) $(EXECUTABLE)
    
$(EXECUTABLE): $(OBJECTS) 
	$(CC) $(LDFLAGS) $(OBJECTS) -o $@

.cpp.o:
	$(CC) $(CFLAGS) $< -o $@

.PHONY : clean
clean:
	$(RM) $(OBJECTS) $(EXECUTABLE)
