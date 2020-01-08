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


# Update records
def updateSkills(id, skill):
    psql_update_query = """ UPDATE skill_testing.skill SET name = %s WHERE id = %s """
    cursor.execute(psql_update_query, (skill, id))
    connection.commit()


# Insert to new table (testing table)
def insertToTestingTable(id, name, type):
    psql_insert_query = """ INSERT into skill_testing.skill(id, name, type) VALUES (%s,%s,%s) """
    rec_to_insert = (id, name, type)
    cursor.execute(psql_insert_query, rec_to_insert)
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
#     updateSkills(x[0], x[1])

#  this will insert data to new testing table (NOTE: use only after table is empty)
# for id, name, type in rec:
#     insertToTestingTable(id, name, type)

######################################################################################################
######################################################################################################
lfs = ['Oracle Java', 'Java', 'Oracle Java 2 Platform Enterprise Edition J2EE', 'Oracle Java EE JEE',
       'Oracle JavaServer Pages JSP',
       'Python', 'Cython',
       'SQL', 'Oracle SQL Developer', 'Oracle SQL Loader', 'Oracle SQL Plus', 'tSQL', 'T-SQL']

dic = {}
lis = []
d_t = {}

for id, skill, type in rec:
    list_of_matching_skills = []
    tup = tuple()
    for skills_lookup in lookupFileSkills():
        # print(skill)
        if fuzz.token_set_ratio(skill, skills_lookup) >= 90:
            list_of_matching_skills.append(skills_lookup)
            dic[skill] = list_of_matching_skills
            lis.append(dic)
            tup = (id, skill, type)
            d_t[tup] = list_of_matching_skills

# pprint.pprint(d_t)

i = 1
j = 1

for k, v in d_t.items():
    print("\n")
    # print(i, "\b.", bcolors.BOLD + k[0] + bcolors.ENDC, ":", v)
    print(i, "\b.", k, ":", v)
    i += 1
    seq_dict = {}
    for skill in v:
        # if k[1] == skill.lower():
        #     print(bcolors.OKGREEN + "Perfect Match: " + bcolors.ENDC, skill)
        #     j += 1
        # else:
        seq = SequenceMatcher(None, k[1].lower(), skill.lower())
        seq_dict[skill] = seq.ratio()
    None if seq_dict == {} else print(bcolors.FAIL + "Max Value" + bcolors.ENDC,
                                      max(seq_dict, key=seq_dict.get), " : ", max(seq_dict.values()))
    updateSkills(k[0], max(seq_dict, key=seq_dict.get))
    pprint.pprint(seq_dict)
