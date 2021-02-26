import json
import pathlib
import pandas as pd


class test_json:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

def add_path_to_json(path, filename):
    aux = test_json()
    aux.name = filename
    aux.children = []

    path.children.append(aux)
    return aux


def add_method_to_json(path, method, complexity):
    aux = test_json()
    aux.name = method
    aux.complexity = complexity

    path.children.append(aux)


def find_path(paths, name):
    for path in paths:
        if(path.name == name):
            return path
    return False

def csv_to_json(project):
    path_system = pathlib.Path(__file__).parents[1]
    df = pd.read_csv(str(path_system) + '/datasets/' + project + '.csv')

    tree = test_json()
    tree.name = "PROJECT - " + project
    tree.children = []
    
    for index, row in df.iterrows():
        filename = row['filename']
        list_filename = filename.split('/')
        
        current = tree
        for path in list_filename:
            path_exist = find_path(current.children, path)

            if(path_exist == False):
                novo_path = add_path_to_json(current, path)
                current = novo_path
            else:
                current = path_exist

        add_method_to_json(current, row['name'], row['cyclomatic_complexity'])

        #if(aux == 10):
        #    break
        #aux+=1

    with open(str(path_system) + project + '.json', 'w') as f:
        f.write(tree.toJSON())


csv_to_json('youtube-dl')