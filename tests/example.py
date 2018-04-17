from aide_document import convert

# [yaml_to_md] takes three file names:
# <input>, <output>, <template>
# convert.yaml_to_md("input.yml", "output.md", "template.md")

convert.docx_to_md("data/EtFlocSedFiEnglish.docx", "data/EtFlocSedFiEnglish")

# [translate] takes four arguments:
# <input>, <source_language>, <target_language>, <output>
# Notice: the output file will be created.
# If there is a file with the same name, it gets replaced.
#translate.translate("output.md", "en", "es", "translated.md")
#translate.translate("output.md", "en", "hi", "translated2.md")