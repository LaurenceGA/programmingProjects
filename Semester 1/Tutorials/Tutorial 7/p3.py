#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "p3.py", "4/05/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")

from string import punctuation

misspellings= """abberration:aberration
accomodation:accommodation
acheive:achieve
adress:address
alot:a lot
alterior:ulterior
athiest:atheist
beggining:beginning
beleive:believe
Caucasion:Caucasian
cemetary:cemetery
committment:commitment
concieve:conceive
copywrite:copyright
Dalmation:Dalmatian
decaffinated:decaffeinated
decathalon:decathlon
definately:definitely
dependance:dependence
dessicate:desiccate
desireable:desirable
diarhea:diarrhoea
dissapoint:disappoint
dispell:dispel
embarass:embarrass
enviroment:environment
expresso:espresso
facist:fascist
Febuary:February
fivety:fifty
fluoroscent:fluorescent
flouride:fluoride
forteen:fourteen
fourty:forty
freind:friend
geneology:genealogy
goverment:government
grammer:grammar
hampster:hamster
harrass:harass
hemorage:haemorrhage
heros:heroes
hight:height
hygeine:hygiene
hypocracy:hypocricy
independance:independence
inate:innate
innoculate:inoculate
intresting:interesting
juge:judge
knowlege:knowledge
lazer:laser
libary:library
lightening:lightning
managable:manageable
millenium:millennium
mischievious:mischievous
mispell:misspell
missle:missile
monestary:monastery
monkies:monkeys
morgage:mortgage
mountian:mountain
neccessary:necessary
neice:niece
nickle:nickel
nineth:ninth
ninty:ninety
noone:no one
noticable:noticeable
occured:occurred
occurence:occurrence
oppurtunity:opportunity
opthamologist:ophthalmologist
paralell:parallel
pasttime:pastime
pavillion:pavilion
peice:piece
percieve:perceive
perserverance:perseverance
persue:pursue
posession:possession
potatoe:potato
preceeding:preceding
pronounciation:pronunciation
privelige:privilege
publically:publicly
quew:queue
rasberry:raspberry
recieve:receive
reccomend:recommend
rediculous:ridiculous
reguardless:regardless
rythm:rhythm
shedule:schedule
seige:siege
sentance:sentence
seperate:separate
sieze:seize
sincerly:sincerely
speach:speech
stragedy:strategy
supercede:supersede
suprise:surprise
thier:their
tommorrow:tomorrow
tounge:tongue
uneform:uniform
vaccuum:vacuum
vegeterian:vegetarian
Wendesday:Wednesday
wierd:weird
writen:written
writting:writing"""


def strip_punc(word):
    for char in punctuation:
        word = word.replace(char, "")
    return word


def check_word(word, c_list):
    for correction in c_list:
        if strip_punc(word.lower()) == correction[0].lower():
            correct = correction[1]
            correct += '.' if word[-1] == '.' else ''
            return correct
    return None

correction_list = misspellings.split("\n")
correction_list = [misspel.split(":") for misspel in correction_list]

while True:
    sentence = input("Type a sentence: ")
    if sentence.lower() in ['exit', 'quit']:
        break
    correct_sentence = ""

    for word in sentence.split():
        result = check_word(word, correction_list)

        if result:
            correct_sentence += result + " "
        else:
            correct_sentence += word + " "

    print("Original sentence: {}".format(sentence))
    print("Corrected sentence: {}".format(correct_sentence))