CC=gcc
STD=c11
CFLAGS=-c -Wall -std=$(STD) -lm
LDFLAGS=-lm
SOURCES=hoclang.c lexer.c
OBJECTS=$(SOURCES:.c=.o)
EXECUTABLE=hoc
RM=rm -f

all: $(SOURCES) $(EXECUTABLE)
    
$(EXECUTABLE): $(OBJECTS) 
	$(CC) $(LDFLAGS) $(OBJECTS) -o $@

.c.o:
	$(CC) $(CFLAGS) $< -o $@

.PHONY : clean
clean:
	$(RM) $(OBJECTS) $(EXECUTABLE)
