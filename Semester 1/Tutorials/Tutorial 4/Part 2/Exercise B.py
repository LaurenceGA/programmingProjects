def translate(word, language):
    translation = "unknown"
    if language.lower() == "german":
        if word.lower() == "dog":
            translation = "hund"
        elif word.lower() == "cat":
            translation = "katze"
    elif language.lower() == "french":
        if word.lower() == "dog":
            translation = "chien"
        elif word.lower() == "cat":
            translation = "chat"
    elif language.lower() == "spanish":
        if word.lower() == "dog":
            translation = "perro"
        elif word.lower() == "cat":
            translation = "gato"

    print("The translation of %s into %s is '%s'" % (word, language, translation))

translate("dog", "German")