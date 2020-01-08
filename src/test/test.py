import pprint

from fuzzywuzzy import fuzz
from src.test.match_to_standard import bcolors
from difflib import SequenceMatcher

i = 1
j = 1
lis = []
dic = {}


def lookupFileSkills():
    lookupFile = open("/home/infotmt-user/PycharmProjects/KMPMatching/data/standard_skills.txt", "r")
    lookup_list = map(lambda l: l.strip('\n'), lookupFile)
    lisz = list(lookup_list)
    return lisz


def skill_from_db():
    skills = open("/home/infotmt-user/PycharmProjects/KMPMatching/data/skills_db", "r")
    skills_list = map(lambda l: l.strip("\n"), skills)
    lisz = list(skills_list)
    return lisz


sfd = ['java', 'python', 'sql']
lfs = ['Oracle Java', 'Java', 'Oracle Java 2 Platform Enterprise Edition J2EE', 'Oracle Java EE JEE',
       'Oracle JavaServer Pages JSP',
       'Python', 'Cython',
       'SQL', 'Oracle SQL Developer', 'Oracle SQL Loader', 'Oracle SQL Plus', 'tSQL', 'T-SQL']

# for skills_db in skill_from_db():
#     list_of_matching_skills = []
#     for skills_lookup in lookupFileSkills():
#         if skills_db.lower() == skills_lookup.lower():
#             print(i, "\b.", bcolors.OKGREEN + "Perfect Match: " + bcolors.ENDC, skills_db, " : ", skills_lookup, " : ",
#                   fuzz.token_set_ratio(skills_db, skills_lookup))
#             i += 1
#         elif fuzz.token_set_ratio(skills_db, skills_lookup) >= 90:
#             # if skills_db:  # apache
#             list_of_matching_skills.append(skills_lookup)
#             dic[skills_db] = list_of_matching_skills
#             lis.append(dic)

# print(skills_db)

for skills_db in skill_from_db():
    list_of_matching_skills = []
    for skills_lookup in lookupFileSkills():
        if fuzz.token_set_ratio(skills_db, skills_lookup) >= 90:
            # if skills_db:  # apache
            list_of_matching_skills.append(skills_lookup)
            dic[skills_db] = list_of_matching_skills
            lis.append(dic)
        # elif skills_db.lower() == skills_lookup.lower():
        #     print(i, "\b.", bcolors.OKGREEN + "Perfect Match: " + bcolors.ENDC, skills_db, " : ", skills_lookup, " : ",
        #           fuzz.token_set_ratio(skills_db, skills_lookup))
        #     i += 1

filtered_dict = lis[0]

for k, v in filtered_dict.items():
    print("\n")
    print(i, "\b.", bcolors.BOLD + k + bcolors.ENDC, ":", v)
    i += 1
    if len(v) == 1:
        print(bcolors.OKBLUE + "Only Match: " + bcolors.ENDC, v[0])
    seq_dict = {}
    for skill in v:
        if k == skill.lower():
            print(bcolors.OKGREEN + "Perfect Match: " + bcolors.ENDC, skill)
            # print(j, "\b.", bcolors.OKGREEN + "Perfect Match: " + bcolors.ENDC, skill)
            j += 1
        else:
            seq = SequenceMatcher(None, k.lower(), skill.lower())
            seq_dict[skill] = seq.ratio()
            # print("---> ", skill, " : ", seq.ratio())

    None if seq_dict == {} else print(bcolors.FAIL + "Max Value" + bcolors.ENDC,
                                      max(seq_dict, key=seq_dict.get), " : ", max(seq_dict.values()))

    # print(bcolors.FAIL + "Else Match: " + bcolors.ENDC, v[0])
    pprint.pprint(seq_dict)

print("-" * 80)
