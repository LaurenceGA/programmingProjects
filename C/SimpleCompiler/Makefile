CC=gcc
STD=c11
CFLAGS=-c -Wall -std=$(STD)
LDFLAGS=
SOURCES=comp.c
OBJECTS=$(SOURCES:.c=.o)
EXECUTABLE=lcomp
RM=rm -f

all: $(SOURCES) $(EXECUTABLE)
    
$(EXECUTABLE): $(OBJECTS) 
	$(CC) $(LDFLAGS) $(OBJECTS) -o $@

.cpp.o:
	$(CC) $(CFLAGS) $< -o $@

.PHONY : clean
clean:
	$(RM) $(OBJECTS) $(EXECUTABLE)
