from fuzzywuzzy import fuzz
from string import ascii_lowercase
from collections import defaultdict

from src.KMPSearch import KMPSearch

resume_skills = ["mssql 2005", "mssql 2008", "sql", "ms word", "visual recognition", "excel", "company analysis",
                 "vb web", "apache", "php", "big data", "html", "selenium 3.141.59", "linux", "machine learning", "css",
                 "team work", "git", "javascript ES5", "mysql", "assembly", "python", "M2001", "amazon ec2"]

# tc = []
# for title_case in resume_skills:
#     tc.append(title_case.title())
alphabet_list = list(ascii_lowercase)


def lookupFileSkills():
    lookupFile = open("/home/infotmt-user/PycharmProjects/PatternMatching/data/skills", "r")
    lookup_list = map(lambda l: l.strip('\n'), lookupFile)
    lis = list(lookup_list)
    return lis


def createDictionary(lis):
    dict_a = defaultdict(list)
    # list_a = []

    for l in lis:
        for alpha in alphabet_list:
            if l.lower().startswith(alpha):
                dict_a[alpha].append(l)

    # print(dict_a)
    return dict_a


# print(createDictionary(lookupFileSkills()))

# print(dict(dict_a))


def refineSkillName(dict_a):
    refined_list_standard_name = set()
    refined_list_lowercase = set()
    final_list = []

    for skill in resume_skills:
        for alpha in alphabet_list:
            if skill.lower().startswith(alpha):
                for a in dict_a.get(alpha):
                    if fuzz.token_set_ratio(skill, a) >= 50 and len(a) > 2 and KMPSearch(a.lower(), skill):
                        # match = KMPSearch(a.lower(), skill)
                        # print(skill, ":", a, ":", fuzz.token_set_ratio(skill, a))
                        refined_list_standard_name.add(a)
                        refined_list_lowercase.add(skill)
                        remaining_list = set(resume_skills) - set(refined_list_lowercase)
                        final_list = list(map(lambda x: x.title(), remaining_list)) + list(refined_list_standard_name)
                        # print(refined_list_standard_name)

    return final_list


print("------OLD LIST:\n", resume_skills)
print("\n------NEW LIST:\n", refineSkillName(createDictionary(lookupFileSkills())))

# print(refined_list_standard_name, "\n")
# print("------NEW LIST:\n", final_list)

# s1 = "Assembly Language"
# s2 = "Assembly"

# if any(x in s2 for x in s1):
#     print("found")
