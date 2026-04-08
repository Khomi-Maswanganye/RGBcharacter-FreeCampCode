
def create_character(character_name,strength,intelligence,charisma):

    
    full_dot = '●'
    empty_dot = '○'

    if not isinstance(character_name,str):
        return "The character name should be a string"
    elif character_name=="":
        return "The character should have a name"
    elif len(character_name)>10:
        return "The character name is too long"
    elif " " in character_name:
        return "The character name should not contain spaces"
                   

    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return "All stats should be integers"
    
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    
    if (strength + intelligence + charisma) != 7:
        return "The character should start with 7 points"

    s_line = "STR " + ( full_dot * strength) + (empty_dot * (10 - strength))
    i_line = "INT " + ( full_dot * intelligence) + (empty_dot * (10 - intelligence))
    c_line = "CHA " + (full_dot * charisma) + (empty_dot * (10 - charisma))    

    return f"{character_name}\n{s_line}\n{i_line}\n{c_line}"

create_character("Khomi",5,4,6)

