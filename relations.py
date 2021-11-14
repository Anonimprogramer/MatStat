def find_relations(set1, set2):
    relation = "{"
    for k in set1:
        for q in set2:
            relation += "<" + str(k) + "," + str(q) + ">" + ","
    relation = relation[0:len(relation) - 1:1]
    relation += "}"
    print(relation)
