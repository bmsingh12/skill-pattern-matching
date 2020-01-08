# from fuzzywuzzy import fuzz
#
# import Levenshtein
# import difflib
#
#
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#
# resume_skills = ["mssql 2005", "mssql 2008", "sql", "ms word", "visual recognition", "excel", "company analysis",
#                  "vb web", "apache", "php", "big data", "html", "selenium 3.141.59", "linux", "machine learning", "css",
#                  "team work", "git", "javascript ES5", "mysql", "assembly", "python", "M2001", "amazon EC2", "dallo",
#                  "biraj"]
#
#
# def lookupFileSkills():
#     lookupFile = open("/home/infotmt-user/PycharmProjects/KMPMatching/data/standard_skills.txt", "r")
#     lookup_list = map(lambda l: l.strip('\n'), lookupFile)
#     lis = list(lookup_list)
#     return lis
#
#
# def skill_from_db():
#     skills = open("/home/infotmt-user/PycharmProjects/KMPMatching/data/skills_db", "r")
#     skills_list = map(lambda l: l.strip("\n"), skills)
#     lis = list(skills_list)
#     return lis
#
#
# # print("Total Skills that need to be converted: ", len(skill_from_db()))
#
# i = 1
#
# check_list = []
# for x in skill_from_db():
#     for s in lookupFileSkills():
#         if fuzz.token_set_ratio(x, s) >= 90:
#             if x.lower() == s.lower():
#
#                 print(i, "\b.", bcolors.OKGREEN + "Perfect Match: " + bcolors.ENDC, x, " : ", s, " : ",
#                       fuzz.token_set_ratio(x, s))
#                 i += 1
#             else:
#                 check_list.append(s)
#             # print(i, "\b. ", x, " : ", s, " : ", fuzz.token_set_ratio(x, s))
#     # print("-" * 40)
#
# print(len(check_list))
# # print(difflib.get_close_matches("amazon", skill_from_db()))
#
#
# """
# [
# {"id":"123asdas", "name":"java", "type": "hard"},
# {"id":"123asdas", "name":"java", "type": "hard"},
# {"id":"123asdas", "name":"java", "type": "hard"},
# {"id":"123asdas", "name":"java", "type": "hard"},
# ]
# """
#
# # in_db = 'JavaScript'
# # a1 = ['javascript', 'javascript es6']
# # a2 = []
# # a3 = []
# # for s in a1:
# #     if s.lower() == in_db.lower():
# #         a2.append(s)
# #     else:
# #         a3.append(s)
# #
# # print("a2: ", a2)
# # print("a3: ", a3)
# #

# from difflib import  SequenceMatcher
#
# node = "node"
# node_list = ['Hewlett-Packard HP Network Node Manager', 'Node JS']
#
# for n in node_list:
#     seq = SequenceMatcher(None, node, n)
#     print(list(seq.get_matching_blocks()))
#     print(seq.ratio())
#
#
# x = ["asd","weq"]
# print(list(enumerate(x,2019)))
#
# for z in x:
#     print(enumerate(z,2019))