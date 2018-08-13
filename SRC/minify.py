import re

file_name = r"E:\WORK\ON_KORSCHFDOPPR_1_996_01_05_01_01.xsd"
with open(file_name, "r") as f:
     text = f.read()

text = text.replace("\t", "").replace("\n", "")

# pattern = "<xs:annotation>(.| |\s)+?\</xs:annotation>"
pattern = "<xs:annotation>(.|\s)+?\</xs:annotation>"
text = re.sub(pattern, "", text)

with open(r"E:\WORK\КСЧФ.xsd", "w") as f:
    # f.write(n_text.replace("\t", "").replace("\n", ""))
    f.write(text)
