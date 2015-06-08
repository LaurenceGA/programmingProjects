#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "Question 2.py", "7/05/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")

import pickle   # Used to serialize the dictionary
import sys

cols = {
    'white':    "37",
    'yellow':   "33",
    'green':    "32",
    'blue':     "34",
    'red':      "31",
    'black':    "30"
}


def colour(string, col):
    """Adds colour character codes and returns the given string coloured"""
    if hasattr(sys.stdout, "isatty"):   # Check if supports colour
        return "\033[1;{}m".format(col) + string + "\033[0;0m"
    else:
        return string


def find_all(string, sub):
    start = 0
    strings = []
    while True:
        start = string.lower().find(sub.lower(), start)
        if start == -1:
            break
        strings.append(string[start:start+len(sub)])
        start += len(sub)
    return strings


def highlight(string, substr, col):
    # This will find all capitalized versions of the sub string in the string
    # This is important so the correctly capitalised string is replaced
    strings = find_all(string, substr)
    for s in set(strings):
        string = string.replace(s, colour(s, col))

    return string


def find(name_dict):
    found = False
    while not found:
        nickname = input("Nickname of contact to find: ")

        if not nickname.strip():
            print(colour("\nNothing was searched for.", cols['red']))
            break

        for nick in name_dict.keys():
            if nickname.lower() == nick.lower():
                print(colour("\n{:10}{:20}{:20}{:15}".format("Nickname", "Name", "Address", "Phone No."), cols['blue']))
                print(get_details(name_dict, nick))
                found = True
                break
        else:
            print(colour("No entry of name {}, try again.".format(nickname), cols['red']))


def search_all(name_dict):
    matches = []

    search = input("Search for: ")

    if search.strip():
        for nick, details in name_dict.items():
            dict_fields = [nick, details['name'], details['address'], details['phone_no']]
            for field in [item.lower() for item in dict_fields]:
                if search.lower() in field:
                    matches.append(nick)

        if matches:
            print(colour("\n     {:10}{:20}{:20}{:15}".format("Nickname",
                                                              "Name",
                                                              "Address",
                                                              "Phone No."), cols['blue']))
            for i, nick in enumerate(set(matches)):
                print("{:<5}".format(i+1) + highlight(get_details(name_dict, nick), search, cols['green']))
        else:
            print(colour("\nNo result for {}.".format(search), cols['red']))
    else:
        print(colour("\nNothing was searched for.", cols['red']))


def add(name_dict):
    nickname = ""
    got_nickname = False

    while not got_nickname:
        nickname = input("Nickname: ")

        if not nickname.strip():
            # Exit if nothing entered
            print(colour("\nNothing was added.", cols['red']))
            return
        else:
            got_nickname = True

            # Check if already in use, otherwise proceed
            for nick in name_dict.keys():
                if nickname.lower() == nick.lower():
                    print(colour("\nThe contact {} already exists!".format(nick), cols['red']))
                    got_nickname = False

                    # Overwrite details?
                    if input("Would you like to replace this contact's details? ").lower() in ['yes', 'y', 'yep']:
                        nickname = nick
                        got_nickname = True

    name = input("Full name: ")
    address = input("Address: ")
    phone = input("Phone number:")

    name_dict[nickname] = {
        'name': name,
        'address': address,
        'phone_no': phone
    }


def delete(name_dict):
    deleted = False

    while not deleted:
        nickname = input("Nickname of contact to delete: ")

        if not nickname.strip():
            # exit if nothing entered
            print(colour("\nNothing was deleted.", cols['red']))
            break

        for nick in name_dict.keys():
            if nickname.lower() == nick.lower():    # Case insensitive
                print(colour("\n{:10}{:20}{:20}{:15}".format("Nickname", "Name", "Address", "Phone No."), cols['blue']))
                print(get_details(name_dict, nick) + "\n")

                # Is this the right person?
                if input("Would you like to delete {}? ".format(nick)).lower() in ['yes', 'y', 'yep']:
                    del name_dict[nick]

                    print(colour("\n{} has been removed".format(nick), cols['green']))

                    deleted = True  # Break out of while loop
                    break           # Break out of for loop
                else:
                    print(colour("\nNothing was deleted.", cols['red']))
                    break
        else:
            print(colour("No entry of name {}, try again.".format(nickname), cols['red']))


def get_details(name_dict, nickname):
    details = name_dict[nickname]
    return "{:10}{:20}{:20}{:15}".format(nickname, details['name'], details['address'], details['phone_no'])


def list_all_across(name_dict):
    print(colour("{:5}{:10}{:20}{:20}{:15}".format("", "Nickname", "Name", "Address", "Phone No."), cols['blue']))
    if name_dict:
        i = 1
        for nick, _ in sorted(name_dict.items()):
            print("{:<5}{}".format(i, get_details(name_dict, nick)))

            i += 1
    else:
        print(colour("\t\tThere are no entries in this address book.", cols['red']))


def get_command():
    # Make all command letters a colour
    commands = [colour(com, cols['blue']) for com in ['F', 'S', 'A', 'D', 'L', 'Q']]
    print(colour("*** My Contacts ***", cols['blue']))
    # * unpacks tuple
    print("[{}]: find, [{}]: search, [{}]: add new entry, [{}]: delete, [{}]: list all, [{}]: quit".format(*commands))
    return input(colour("Enter a command: ", cols['blue']))


def save_dict(name_dict, filepath):
    # Save dictionary as external file
    pickle.dump(name_dict, open(filepath, "wb"))
    print(colour("Address book saved.", cols['green']))


def load_dict(filepath):
    try:
        # Load from external file if possible
        return pickle.load(open(filepath, "rb"))
    except IOError:
        return {}


def terminate():
    raise SystemExit

names = load_dict("addressBook")

while True:
    cmd = get_command().lower()
    print(colour("-----" * 15, cols['yellow']))

    if cmd == 'f':
        find(names)
    elif cmd == 's':
        search_all(names)
    elif cmd == 'a':
        add(names)
    elif cmd == 'd':
        delete(names)
    elif cmd == 'l':
        list_all_across(names)
    elif cmd == 'q':
        save_dict(names, "addressBook")
        terminate()

    else:
        print(colour("Please enter an appropriate command.", cols['red']))

    print(colour("-----" * 15, cols['yellow']))
