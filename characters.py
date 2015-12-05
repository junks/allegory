#!/usr/bin/python


characters = {

    # People
    "obama":"Bouba",
    "barack obama": "Bouba the Shapeshifter",
    "hillary":"Lucy",
    "hillary clinton": "Lucy the Fairy Godmother",
    "trump":"Nelson",
    "donald trump": "Nelson Muntz",
    "donald j. trump": "Nelson Muntz",
    "jeb": "Burt",
    "jeb bush": "Burt the Turtle",
    "john kerry": "Kiki the Sharpie",
    "john": "Kiki",
    "mr. xi": "Mr. Freeze",
    "xi": "Freeze",
    "jinping": "Cold",
    
    
    # Actors
    #"isis": "Sauron",
    "islamic state": "Sauron",

    # Places
    "the united states": "Middle-Earth",
    "united states": "Middle-Earth",
    "american": "Earthian",
    "russia": "Mars",
    "france": "the Moon",
    "parisian": "Moonian",
    "paris": "Moon Moon",
    "canada": "the Ice Kingdom",
    "canadian": "Icelandic",
    "morroco": "Marco Polo",
    "china": "Atlantis",
    "chinese": "Atlantean",
    "asia": "Oceania",
    
}


# Taken from: http://www.really-learn-english.com/list-of-pronouns.html
pronouns = [
    "I", "you", "he", "she", "it", "we", "they", "me", "him", "her", "us", "them",
    "what", "who"
    "me", "whom"
    "mine", "yours", "his", "hers", "ours", "theirs"
    "this", "that", "these", "those"
    "which", "what", "whose", "whoever", "whatever", "whichever", "whomever"
    "myself", "yourself", "himself", "herself", "itself", "ourselves", "themselves"
    "Anything", "everybody", "another", "each", "few", "many", "none", "some", "all", "any", "anybody", "anyone", "everyone", "everything", "no one", "nobody", "nothing", "none", "other", "others", "several", "somebody", "someone", "something", "most", "enough", "little", "more", "both", "either", "neither", "one", "much", "such"
]
pronouns = list(set([x.lower() for x in pronouns]))


def match_case(x, reference):
    if reference == reference.upper():
        return x.upper()
    if reference == reference.title():
        return x.title()
    if reference == reference.lower():
        return x.lower()
    return x

def coref_match(text, cluster):
    if text.lower() in pronouns:
        return text
    
    for item in cluster:
        longest_character = None
        for character in characters:
            if character.lower() in item.lower() and character.lower() in text.lower() and " "+character.lower()+" " in text.lower():
                
                if longest_character is None or len(character) > len(longest_character):
                    longest_character = character

        if not longest_character is None:            
            result = text.lower().replace(longest_character.lower(), characters[longest_character])

            return match_case(result, text)
    return text