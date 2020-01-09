from fuzzywuzzy import fuzz
from difflib import SequenceMatcher

import csv



def lookupFileSkills():
    lookupFile = open("/home/infotmt-user/PycharmProjects/KMPMatching/data/standard_skills.txt", "r")
    lookup_list = map(lambda l: l.strip('\n'), lookupFile)
    lisz = list(lookup_list)
    return lisz


with open("skill.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['SN', 'Skill', 'related-1', 'related-2'])

    for skill in lookupFileSkills():
        if SequenceMatcher(None, "java", skill.lower()).ratio() >= 0.7:
        # if fuzz.token_set_ratio("java", skill.lower()) >= 70:
            print(skill)
