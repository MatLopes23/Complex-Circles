import os, pathlib, glob
import lizard
import pandas as pd


def get_files_project(project, language):
    files = []

    path = pathlib.Path(__file__).parents[1]

    if(language == "Python"):
        os.chdir(str(path) + '/repositories/' + project)
        files = glob.glob('**/*.py', recursive=True)
    
    elif(language == "Java"):
        os.chdir(root_path + '/repositories/versao_saner2021/' + project)
        files = glob.glob('**/*.java', recursive=True)
        #print(repo.name, len(files))
        
    elif(language == "JavaScript"):
        os.chdir(root_path + '/repositories/versao_saner2021/' + project)
        files = glob.glob('**/*.js', recursive=True)
        #print(repo.name, len(files))
            
    elif(language == "C++"):
        os.chdir(root_path + '/repositories/versao_saner2021/' + project)
        files = glob.glob('**/*.cpp', recursive=True)
        files+= glob.glob('**/*.h', recursive=True)
        files+= glob.glob('**/*.cc', recursive=True)
        #print(repo.name, len(files))
            
    elif(language == "C#"):
        os.chdir(root_path + '/repositories/versao_saner2021/' + project)
        files = glob.glob('**/*.cs', recursive=True)
        #print(repo.name, len(files))
    
    return files


def get_complexity(project, files):
    path = pathlib.Path(__file__).parents[1]

    dataset = []

    for file in files:
        lizard_analyze = lizard.analyze_file(str(path) + '/repositories/' + project + '/' + file)

        for function in lizard_analyze.function_list:

            f = function.__dict__
            dataset.append([f['name'], file, f['cyclomatic_complexity'], f['nloc'], f['top_nesting_level']])
    
    dataset = pd.DataFrame(dataset, columns=['name', 'filename', 'cyclomatic_complexity', 'nloc', 'top_nesting_level'])
    dataset.to_csv(str(path) + '/datasets/'+ project + '.csv')

repositories = [["youtube-dl", "Python"]]

for repo in repositories:
    files = get_files_project(repo[0], repo[1])
    get_complexity(repo[0], files)

