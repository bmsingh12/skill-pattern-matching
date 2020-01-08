import pprint
import psycopg2
from fuzzywuzzy import fuzz
from difflib import SequenceMatcher

from src.test.match_to_standard import bcolors

connection = psycopg2.connect(
    user="infotmt",
    password="qwerty12345",
    host="localhost",
    port="5432",
    database="nobilis_ent_dev"
)
cursor = connection.cursor()

print("Table before updating records:")
postgres_select_query = """ SELECT * FROM sandbox12.skill"""
cursor.execute(postgres_select_query)
rec = cursor.fetchall()


# pprint.pprint(rec)


# Update to old records
def updateToOldSkills(id, skill):
    psql_update_query = """ UPDATE sandbox12.skill SET name = %s WHERE id = %s """
    cursor.execute(psql_update_query, (skill, id))
    connection.commit()


# list of sample db skills (unfiltered)
def skill_from_db():
    skills = open("/home/infotmt-user/PycharmProjects/KMPMatching/data/skills_db", "r")
    skills_list = map(lambda l: l.strip("\n"), skills)
    lisz = list(skills_list)
    return lisz


# lookup skills file
def lookupFileSkills():
    lookupFile = open("/home/infotmt-user/PycharmProjects/KMPMatching/data/standard_skills.txt", "r")
    lookup_list = map(lambda l: l.strip('\n'), lookupFile)
    lisz = list(lookup_list)
    return lisz


# list of id from skill table
list_id = [x[0] for x in rec]

# zip id and old db skill name
zip_data = [(x, y) for x, y in zip(list_id, skill_from_db())]

# this will update to old skills w.r.to id
# for x in zip_data:
#     updateToOldSkills(x[0], x[1])

######################################################################################################
######################################################################################################
lfs = ['Oracle Java', 'Java', 'Oracle Java 2 Platform Enterprise Edition J2EE', 'Oracle Java EE JEE',
       'Oracle JavaServer Pages JSP',
       'Python', 'Cython',
       'SQL', 'Oracle SQL Developer', 'Oracle SQL Loader', 'Oracle SQL Plus', 'tSQL', 'T-SQL']

dic = {}
lis = []

for id, skill, type in rec:
    list_of_matching_skills = []
    for skills_lookup in lfs:
        # print(skill)
        if fuzz.token_set_ratio(skill, skills_lookup) >= 90:
            list_of_matching_skills.append(skills_lookup)
            dic[skill] = list_of_matching_skills
            lis.append(dic)

# print(lis[0])

t = ("ff8081816ec604ae016ec63ad676001c", "sql", "hard")
# d1 = {
#     t: ['SQL', 'Oracle SQL Developer', 'Oracle SQL Loader', 'Oracle SQL Plus', 'T-SQL']
# }
d1 = {}
d1[t] = ['SQL', 'Oracle SQL Developer', 'Oracle SQL Loader', 'Oracle SQL Plus', 'T-SQL']
print(d1)

i = 1
j = 1

for k, v in lis[0].items():
    print("\n")
    print(i, "\b.", bcolors.BOLD + k + bcolors.ENDC, ":", v)
    i += 1
    # if len(v) == 1:
    #     print(bcolors.OKBLUE + "Only Match: " + bcolors.ENDC, v[0])
    seq_dict = {}
    for skill in v:
        if k == skill.lower():
            print(bcolors.OKGREEN + "Perfect Match: " + bcolors.ENDC, skill)
            j += 1
        else:
            seq = SequenceMatcher(None, k.lower(), skill.lower())
            seq_dict[skill] = seq.ratio()
    None if seq_dict == {} else print(bcolors.FAIL + "Max Value" + bcolors.ENDC,
                                      max(seq_dict, key=seq_dict.get), " : ", max(seq_dict.values()))
    pprint.pprint(seq_dict)
