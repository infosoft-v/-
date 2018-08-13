import re
# import json
from xml.etree import ElementTree as ET

def get_table_coll(table_text: object) -> list:
    row_coll = table_text.split("\n")
    row_coll = list(r.lstrip() for r in row_coll)
    row_coll = list(re.sub(r"[ ]+", " ", r) for r in row_coll)
    return row_coll


file_name = r"E:\WORK\database.txt"
# file_name = r"E:\WORK\database.txt"
with open(file_name, "r") as f:
    text = f.read()

pattern = r"Table [\w.*\\\s]+?\n\n"
text_m = re.findall(pattern, text)

dict_tables = dict()

root = ET.Element("Database")

if text_m is not None:
    for table_text in text_m:
        desc_rows = get_table_coll(table_text)
        dict_tbl = dict()
        dict_flds = dict()
        dict_tbl.setdefault("Fields", dict_flds)
        dict_idxs = dict()
        dict_tbl.setdefault("Indexes", dict_idxs)
        table_name = desc_rows[0].split(" ")[1]
        table_path = desc_rows[1].split(" ")[1]
        dict_tbl.setdefault("PATH", table_path)
        dict_tables.setdefault(table_name, dict_tbl)
        e_table = ET.SubElement(root, table_name)
        e_path = ET.SubElement(e_table, "Path")
        e_path.text = table_path
        e_fields = ET.SubElement(e_table, "Fields")
        e_indexes = ET.SubElement(e_table, "Indexes")

        for cnt in range(2, len(desc_rows)):
            first_word = desc_rows[cnt].split(" ")[0]
            if first_word.upper() == "FIELD":
                field_name = desc_rows[cnt].split(" ")[1]
                dict_flds.setdefault(field_name, "")
                e_field = ET.SubElement(e_fields, "Field")
                e_field.text = field_name
            elif first_word.upper() == "INDEX":
                index_name = desc_rows[cnt].split(" ")[1]
                e_index = ET.SubElement(e_indexes, "Index")
                e_index.text = index_name
                dict_idx_info = dict()
                cnt += 1
                params = desc_rows[cnt].split(" ")
                par = dict_idx_info.setdefault("Unique", bool(params[1]))
                dict_idxs.setdefault(index_name, dict_idx_info)


# print(dict_tables)
ET.ElementTree(root).write('E:\WORK\db.xml')
# with open(r"E:\WORK\db_out.xsd", "w") as f:
#     # f.write(n_text.replace("\t", "").replace("\n", ""))
#     f.write(text)
