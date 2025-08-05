survey_results = [
    ["Python","JavaScript","C++"],
    ["Python","JavaScript","C#"],
    ["Python","Java"],
    ["Python","C++","JavaScript"],
    ["Python","JavaScript","C++","Java"],
]




choices_sets = [set(p) for p in survey_results]
common_languages = set.intersection(*choices_sets)

all_survey = set.union(*choices_sets)

print("1.Laguages chosen by all perticipants", common_languages)

lang_counts = {}

for result in survey_results:
    unique_langs = set(result)
    for lang in unique_langs:
        if lang in lang_counts:
            lang_counts[lang] += 1
        else:
            lang_counts[lang] =1

unique_languages = [lang for lang in lang_counts if lang_counts[lang] == 1]
print("2.Languages only chosen by one participant:",unique_languages)

unique_languages_count = len(all_survey)
print("3.Number of unique languages:",unique_languages_count)


print("4.Languages chosen by exactly two participants::")

print("5.Participant with same set of languages:")