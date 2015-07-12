#include <iostream>
#include <fstream>
#include <string>
#include <windows.h>
using namespace std;

/////////////////////////////////////////////////////////////////////////////////////////////////
// We will be reading the rooms from our World.txt file.  The file is set up so that we can add
// unlimited rooms to our game without ever having to touch a bit of code.
// We will be able to move around the rooms with
// collision detection and view the room descriptions.  
//
// The commands in this part are:	look north south east west help quit.  
// Below is an explanation of what each command does:
//	
// "look"  - This will display the room's description
// "north" - This will move the player north if there is a valid room
// "south" - This will move the player south if there is a valid room
// "east"  - This will move the player east if there is a valid room
// "west"  - This will move the player west if there is a valid room
// "help"  - This will display the list of available commands
// "quit"  - This will quit the game

#define GAME_FILE "World.txt"

// These defines are to make our return values from GetInput() more clear.  GetInput will return QUIT if we
// typed "quit", otherwise it will return STILL_PLAYING to let our main loop know to keep going.
#define STILL_PLAYING	1
#define QUIT			0

// This is our room structure.  This holds all the information about the current room.
struct tRoom
{										
	string strCurrentRoom;				// This stores the name of the current room we are in (I.E. "Hallway")
	string strRoomDescription;			// This holds the description of the current room
	string strRoomNorth;				// This holds the name of the room that is to the north
	string strRoomEast;					// This holds the name of the room that is to the east
	string strRoomSouth;				// This holds the name of the room that is to the south
	string strRoomWest;					// This holds the name of the room that is to the west
};


///////////////////////////////// DISPLAY ROOM \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\*
/////
/////	This function displays the current room description to the screen
/////
///////////////////////////////// DISPLAY ROOM \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\*

void DisplayRoom(tRoom &room)
{
	cout << room.strRoomDescription << endl << endl;		
}


///////////////////////////////// GET ROOM INFO \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\*
/////
/////	This function reads in the information for the desired room (strRoom) from the game file
/////
///////////////////////////////// GET ROOM INFO \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\*

void GetRoomInfo(ifstream &fin, tRoom &room)
{
	// Create some temporary strings for reading in data from world.txt
	string strLine = "";
	string strTemp = "";

	// Here we create a string that will store the room name with the '<' and '>' brackets around it.
	// We need to do this because in the text file we are reading from, it has the room blocks with
	// brackets around it.  This makes it more readable as a header.  You can take them off if you want.
	// So, by adding < and > to each side of room.strCurrentRoom, it would turn "Middle" into "<Middle>".
	string strRoom = "<" + room.strCurrentRoom + ">";

	// First we want to return the file pointer to the beginning of the file again.
	// This way we get a clean start for searching the file for the designed room block.

	// Set the file pointer at the beginning of the file and clear() the EOF (End of File) flag
	fin.seekg(NULL,ios::beg);						
	fin.clear();										

	// Next, we want to start looking for the room and read in it's data. Here is the plan:
	// Since we start at the beginning of the file each time, we want to read in each line
	// of the file, starting at the beginning, and then check if that line is equal to the
	// room block that we are looking for, for instance "<Middle>".  If it is, then we want
	// to read in the Middle room's description.  We do this by doing a getline() and stop
	// reading characters when we hit a '*' symbol, which should be placed at the end of
	// every room description in the text file.  This allows us to read in multiple lines
	// of text for the room description, but we needed a character to tell us when to stop reading.
	// We will store the room description paragraph in our room.strRoomDescription variable.
	// After we have the room description, we want to read in the rooms that are north, south,
	// east and west from the room being read in (I.E. <Middle>).  The room names are stored
	// after the direction block, like: <north> Top.   This tells us that to the north there is
	// a room called "Top".  Of course these rooms aren't good names, but in a game you can make
	// them more descriptive like "Hallway", "Library", etc...  
	// We want to store the room names in each of the associate variables, depending on the direction.
	// That means, for instance, that the "Top" in <north> Top should be stored in strRoomNorth.
	// Since we don't want the "<north>" string, we can't use getline(), otherwise it would read
	// in the whole line.  To get around this, we read in one word at a time.  When we read
	// in the first word, it will be "<north>".  Then, when can finally read in the next word
	// which will store the name of the room.  
	// This is coded below with:  fin >> strTemp >> room.strRoomNorth;
	// We use strTemp to read in the "<north>" string, and then store the next word in strRoomNorth.
	// We need to do this for every direction.  Once we finish reading in the last direction (west),
	// we return from the function because we no longer need to read from the file anymore.  We
	// then display the current room description (strRoomDescription) and we are now in the new room.

	// Here we want read in a line at a time from the file until we find the desired room
	while(getline(fin, strLine, '\n'))				
	{
		// If the current line is equal to the room that we are looking for (I.E. <Middle>), then read the room info
		if(strLine == strRoom)					
		{
			// Read in the room description until we hit the '*' symbol, telling us to stop
			getline(fin, room.strRoomDescription, '*');	

			// Read past the direction blocks (I.E. <north>) and store the room name for that direction
			fin >> strTemp >> room.strRoomNorth;				
			fin >> strTemp >> room.strRoomEast;				
			fin >> strTemp >> room.strRoomSouth;				
			fin >> strTemp >> room.strRoomWest;				

			// Stop reading from the file because we got everything we wanted; the room info was read in.
			return;									
		}
	}

}


///////////////////////////////// MOVE \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\*
/////
/////	This function checks if we can move, and if so, moves us to the desired room
/////
///////////////////////////////// MOVE \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\*

void Move(ifstream &fin, tRoom &room, string strRoom)
{
	// This function was created to reduce the amount of code in the GetInput() function.
	// Since each direction had to do the same checks and routines, I figured I would create this.
	// This takes the file pointer, the room data and the we are attempting to go too (I.E. "Middle").

	// Check if the room we are going to is valid. If it's not, then we want to 
	// display a message and return.  "None" is used as a room name in the text file to
	// indicate that there is NO room in that direction.  This is our simple, yet smart collision detection.
	if(strRoom == "None")					
	{
		// Display a message that we can't go in that direction, then leave this function
		cout << "You can't go that way!" << endl;	
		return;									
	}
		
	// If we get here the room name must be valid and we should move to that room.
	// First we want to set the current room we are in to the new room, then read in
	// the new room's data, then display it's room description to the screen.

	// Set the current room to the new room we are moving too
	room.strCurrentRoom = strRoom;

	// Pass in our file pointer, the room info so that we read in the new room's data
	GetRoomInfo(fin, room);		

	// Display the current room
	DisplayRoom(room);								
}


///////////////////////////////// GET INPUT \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\*
/////
/////	This function reads the input from the user and acts accordingly
/////
///////////////////////////////// GET INPUT \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\*

int GetInput(ifstream &fin, tRoom &room)
{
	// This is the main control function that is called every time in the game loop.
	// This displays a prompt, asks for the user's input, then handles the result of what they typed.
	// If we wanted to quit the game, we return QUIT, otherwise return STILL_PLAYING.

	// Create a variable to hold the user's input
	string strInput = "";

	// Display a simple prompt
	cout << endl << ": ";							

	// Read in the user's input
	cin >> strInput;									

	if(strInput == "look")									// Check if the user typed "look"
	{
		DisplayRoom(room);									// Display the current room's description
	}
	else if(strInput == "north")							// Check if the user typed "north"
	{
		Move(fin, room, room.strRoomNorth);					// Move to the room that is to the north (if it's a valid move)
	}
	else if(strInput == "east")								// Check if the user typed "east"
	{
		Move(fin, room, room.strRoomEast);					// Move to the room that is to the east (if it's a valid move)
	}
	else if(strInput == "south")							// Check if the user typed "south"
	{
		Move(fin, room, room.strRoomSouth);					// Move to the room that is to the south (if it's a valid move)
	}
	else if(strInput == "west")								// Check if the user typed "west"
	{
		Move(fin, room, room.strRoomWest);					// Move to the room that is to the west (if it's a valid move)
	}
	else if(strInput == "quit")								// Check if the user typed "quit"
	{
		cout << "Did you give up already?" << endl;			// Display a quit message
		return QUIT;										// Return QUIT to stop the game and end the program
	}
	else if(strInput == "help" || strInput == "?")			// Check if the user typed "help" or "?"			
	{														// Display a list of commands
		cout << endl << "Commands: look north south help quit" << endl;
	}
	else													// Otherwise we didn't recognize the command typed in
	{
		cout << endl << "Huh???" << endl;					// Display a message indicating we didn't understand what the user wants
	}

	// Return the default value saying that we still are playing
	return STILL_PLAYING;
}


///////////////////////////////// MAIN \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\*
/////
/////	This function is the start of our program
/////
///////////////////////////////// MAIN \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\*

int main()
{
	// Create our file pointer that will be opening and reading the file
	ifstream fin;
	// Create our room structure.  This will hold all of our room data.
	tRoom room;

	// Open the game file.  This will put the file pointer at the beginning of the file.
	fin.open(GAME_FILE);							

	// Check if the file was found.  If it wasn't, we want to quit the program
	if(fin.fail())									
	{												
		// Display a error message and return -1 (Quit the program)
		cout << "Unable to find World.txt" << endl;
		return -1;									
	}

	// Read in the starting room and store it in our strCurrentRoom variable. Twice to skip the <start> word
	fin >> room.strCurrentRoom >> room.strCurrentRoom;

	// Pass in our file point and our room data so that we can read in and store all the room data
	GetRoomInfo(fin, room);							

	// Once the room data is read, we want to display the current room description
	DisplayRoom(room);									

	// Start our main game loop
	while(1)										
	{
		// Call our GetInput() function to check the user input and make sure we didn't quit.
		// We pass in our file pointer and our room data so that we don't create any global variables.
		// These variables are passed by reference so that they can be passed to others functions inside
		// of GetInput().  If you can avoid using globals you should.
		if(GetInput(fin, room) == QUIT)			
			break;	// Quit the main loop
	}
	
	// If we get here the game is over and we must have quit.  We now want to do our clean up.
	// We need to close the file we have open and then do a little delay before the program quits.
	
	// Close the file
	fin.close();	
	
	// Delay the program for 3 seconds before quitting.
	Sleep(3000);

	// Return from main (Quit the program)
	return 0;										
}