cat_accessing = ["find", "value", "put", "index", "request", "get", "set"]
cat_collections = ["collect", "append", "add", "select","filter", "remove", "delete", "list","next", "contains", "map", "size", "iterator", "accept", "visit"]
cat_condition = ["maybe","is","has","can","compare","should","equals"]
cat_conversion = ["from","format","wrap","for","of","as","with","convert","to"]
cat_coordination = ["wait","schedule","try","notify","update","await","send","start","handle","post","after","before","on"]
cat_creation = ["builder","build","create","new","make","allocate","copy","generate","assemble"]
cat_IO = ["show","log","save","open","refresh","print","record","flush","close","serialize","emit","write","read","end"]
cat_messages = ["invoke", "call"]
cat_proccessing = ["calculate","extract","resolve","process","prepare","compute","do","replace","decode","encode","parse","run","apply","execute","merge","hash","main"]
cat_release = ["shutdown","release","reset","stop","cancel","clear","dispose","tear"]
cat_setup = ["load","initialize","connect","init","register","bind","configure","setup"]
cat_test = ["mock","assert","test"]
cat_validation = ["ensure","verify","validate","check","error"]

colors = {
    "processing"  :     "rgb(255,255,255)",#white
    "accessing"   :     "rgb(255,99,71)",#"tomato"
    "collections" :     "rgb(255,165,0)",#"orange",
    "condition"   :     "rgb(240,230,140)",#"Khaki",
    "conversion"  :     "rgb(34,139,34)",#"green",
    "coordination":     "rgb(100,149,237)",#"blue",
    "creation"    :     "rgb(79,79,79)",#"grey31",
    "IO"          :     "rgb(0,191,255)",#"DeepSkyBlue",
    "messages"    :     "rgb(139, 0, 0)",#"DarkRed",
    "undefined"  :     "rgb(255,228,181)",#"Moccasin",
    "release"     :     "rgb(255,222,173)",#"NavajoWhite",
    "setup"       :     "rgb(128,0,128)",#"Purple",
    "test"        :     "rgb(255,182,193)",#"LightPink",
    "validation"  :     "rgb(255,228,225)",#"MistyRose"

}

def find_prefix(name):
    name = name.lower()
    category = ""
    position = 10000

    for cat in cat_accessing:
        p = name.find(cat)

        if p >= 0 and p < position:
            position = p
            category="accessing"
            break
    
    for cat in cat_collections:
        ip = name.find(cat)

        if p >= 0 and p < position:
            position = p
            category="collections"
            break
        
    for cat in cat_condition:
        p = name.find(cat)

        if p >= 0 and p < position:
            position = p
            category="condition"
            break
    
    for cat in cat_conversion:
        p = name.find(cat)

        if p >= 0 and p < position:
            position = p
            category="conversion"
            break
    
    for cat in cat_coordination:
        p = name.find(cat)

        if p >= 0 and p < position:
            position = p
            category="coordination"
            break
    
    for cat in cat_creation:
        p = name.find(cat)

        if p >= 0 and p < position:
            position = p
            category="creation"
            break
    
    for cat in cat_IO:
        p = name.find(cat)

        if p >= 0 and p < position:
            position = p
            category="IO"
            break
    
    for cat in cat_messages:
        p = name.find(cat)

        if p >= 0 and p < position:
            position = p
            category="messages"
            break
    
    for cat in cat_proccessing:
        p = name.find(cat)

        if p >= 0 and p < position:
            position = p
            category="processing"
            break
    
    for cat in cat_release:
        p = name.find(cat)

        if p >= 0 and p < position:
            position = p
            category="release"
            break
    
    for cat in cat_setup:
        p = name.find(cat)

        if p >= 0 and p < position:
            position = p
            category="setup"
            break

    for cat in cat_test:
        p = name.find(cat)

        if p >= 0 and p < position:
            position = p
            category="test"
            break
    
    for cat in cat_validation:
        p = name.find(cat)

        if p >= 0 and p < position:
            position = p
            category="validation"
            break
    
    if category == "":
        return "undefined"

    return category

def get_color(name):
    category = find_prefix(name)

    return colors[category]

if __name__ == "__main__":
    print(find_prefix(''))