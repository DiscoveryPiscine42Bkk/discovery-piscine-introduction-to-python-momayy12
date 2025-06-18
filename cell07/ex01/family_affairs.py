def genopum(family):
    return list(filter(lamba name: family[name] == "pum", family.keys()))

dupont_family = {
    "pum": "pum",
    "geno": "geno",
    "mairu": "tem",
    "chutinun": "pum",
    "yungmak": "pum"
}

print(genopum(dupont_family))