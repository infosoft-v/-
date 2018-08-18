import sys
import re
from xml.etree import ElementTree as ET

#r = sys.stdin.buffer.read(16).decode('cp1251')
def get_table_coll(table_text: object) -> list:
    row_coll = table_text.split("\n")
    row_coll = list(r.lstrip() for r in row_coll)
    row_coll = list(re.sub(r"[ ]+", " ", r) for r in row_coll)
    return row_coll


if len(sys.argv) > 1:
    file_data_name = sys.argv[1]
    file_xml_name = re.sub("\.\w+", ".xml", file_data_name)

    with open(file_data_name, "r") as f:
        text = f.read()

    pattern = r"Table [\w.*\\\s]+?\n\n"
    text_m = re.findall(pattern, text)

    root = ET.Element("Database")

    if text_m is not None:
        for table_text in text_m:
            desc_rows = get_table_coll(table_text)
            table_name = desc_rows[0].split(" ")[1]
            table_path = desc_rows[1].split(" ")[1]
            e_table = ET.SubElement(root, table_name)
            e_path = ET.SubElement(e_table, "Path")
            e_path.text = table_path
            e_fields = ET.SubElement(e_table, "Fields")
            e_indexes = ET.SubElement(e_table, "Indexes")
            for cnt in range(2, len(desc_rows)):
                first_word = desc_rows[cnt].split(" ")[0]
                if first_word.upper() == "FIELD":
                    field_name = desc_rows[cnt].split(" ")[1]
                    e_field = ET.SubElement(e_fields, "Field")
                    e_field.text = field_name
                elif first_word.upper() == "INDEX":
                    index_name = desc_rows[cnt].split(" ")[1]
                    e_index = ET.SubElement(e_indexes, "Index")
                    e_index.text = index_name
                    cnt += 1

    ET.ElementTree(root).write(file_xml_name)

else:
    print ("Формат запуска: analize_to_xml.exe имя_файла.txt")
