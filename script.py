import re
def echap_french_caracters(sentence, space_caracter="-"):
    """This function transform sentence with some french caracters
    by english term acceptable for variable or fileNames"""
    CARACTERS = ["à", "â", "ä", "é", "è", "ê", "ë", "ï", "î",\
                  "ô", "ö", "ù", "û", "ü", "ÿ" ,"ç"]
    u_list = ["ù", "û", "ü"]
    a_list = ["à", "â", "ä"]
    e_list = ["é", "è", "ê", "ë"]
    o_list = ["ô", "ö"]
    i_list = ["ï", "î"]
    # name_normal = "Maéè est îcî-tr"
    # img_link = entry['img_link']
    name_normal = sentence.strip()
    name_list = list(name_normal)
    name_found = []
    for item in name_list:
        letter = item
        if item in CARACTERS:
            if item in u_list:
                letter = "u"
            elif item in a_list:
                letter = "a"
            elif item in e_list:
                letter = "e"
            elif item in o_list:
                letter = "o"
            elif item in i_list:
                letter = "i"
            elif item == "ÿ":
                letter = "y"
            elif item == "ç":
                letter = "c"
        elif re.match('[^a-zA-Z1-9\.]', item):
            letter = space_caracter
        name_found.append(letter)
    final_name = "".join(name_found)

    return final_name
