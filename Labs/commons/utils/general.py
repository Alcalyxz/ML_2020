"""
Este archivo es generado automaticamente.

###### NO MODIFICAR #########

# cualquier alteración del archivo
# puede generar una mala calificación o configuracion
# que puede repercutir negativamente en la 
# calificación del laboratorio!!!!!

###### NO MODIFICAR #########
"""

import os
import functools
import traceback
import time
import pandas as pd

class Laboratory():

    def __init__ (self, data_paths, code_paths):

        self.data_path = [f"data/{data}" for data in data_paths]
        self.code_path = code_paths
        self.commons = ['imports.py']
        self.repo_path = "https://raw.githubusercontent.com/jdariasl/ML_2020/labs/Labs/commons/utils/"
        print("lab configuration started")


    def download_github_code(self, path):
        filename = path.rsplit("/")[-1]
        os.system(f"wget {self.repo_path}{path} -O {filename}")

    def download_files(self):
        for d in self.data_path + self.code_path+ self.commons:
            self.download_github_code(d)

    def install_libraries(self):
        os.system("pip install gspread")
        # for avoid a bug qith seaborn
        os.system("pip install matplotlib<3.3.1")
    
    def configure(self):
        print("installing libraries")
        self.install_libraries()
        print("downloading files")
        self.download_files()
        print("lab configured")

class Grader():

    def __init__(self, lab_name):
        self.tests = {}
        self.results = {}
        self.lab_name = lab_name

    def add_test(self, name, test_to_add):
        self.tests[name] = test_to_add

    def run_test(self, name, f_to_test):
        if name not in self.tests:
            print("verifica el orden de ejecucion de tu notebook!",  
                 "parece que no has ejecutado en el orden correcto",
                 "si tienes una duda, consultalo con el profesor, preguntando por",
                 f"FALLA en '{self.lab_name}-{name}'")
            return None

        self.results[name] = self.tests[name].run_test(f_to_test)

    def check_tests(self):
        if not( len(self.tests.keys()) == len(self.results.keys()) ):
            print("los tests estan incompletos! verifica el notebook")
            return None
    
        if (sum([res == 'nok' for res in self.results.values()]) >0 ):
            print("algunos de los test no estan ok. Verifica antes de enviar el formulario")
            return None

        print("Todo se ve ok. Asegurate de responder las preguntas en el formualario y envialo",
              "¡buen trabajo!")
    
    def grade(self):
        pass
        

class Tester():

    def __init__(self, func_for_testing):
        self.func_for_testing = func_for_testing
    
    def run_test(self, func_to_test):
        res = self.func_for_testing(func_to_test)
        if (res):
            print("TEST EXITOSO!")
            return ("ok")
        else:
            print("FALLIDO. revisa tu funcion. Sigue las instrucciones del notebook. Si tienes alguna duda pregunta!")
            return("nok")

### Utils
class Utils():

    def __init__(self):
            pass

    def is_func_tester(self, f):
        import types
        res = isinstance(f, types.FunctionType)
        if not (res):
            print("....¡Revisa tu codigo!....", 
                "parace ser que no creaste una funcion," , 
                "presta atención a las instrucciones, o pregunta al profesor")
        return (res)

    def is_dataframe_tester(self, df):
        test = isinstance(df, pd.DataFrame)
        if not (test):
            print("recuerda que debes devolver un pandas DataFrame")
            return(False)
        else:
            return(True)
        
    def test_columns_len(self, df, test_len):
        return (len(df.columns) == test_len)

    def test_conditions_and_methods(self, test_msgs):
        """ test the values of dict and return the msj (key) if the test is false """
        for msj,test in test_msgs.items():
            if not(test):
                print(msj)
                return(False)
        return (True)


### decorators
def unknow_error(func):
    """decorates functions to return the original error"""
    @functools.wraps(func)
    def wrapper (*args, **kwargs):
        ut = Utils()
        if not ut.is_func_tester(func):
            return False
        try:
            return (func(*args, **kwargs))
        except Exception as e: 
            print("...error inesperado....\n ", "es muy probable que tengas un error de sintaxis \n", 
            "...puedas que tengas una variable definida erroneamente dentro de la funcion... \n"
            "...este es el stack retornado...")
            traceback.print_exc()
            return False
    return (wrapper)


### -------------------------
### configuration for each lab
###---------------------------
## intro
def configure_intro():
    data = ['bank.csv']
    code = ["intro.py"]
    intro_lab_object = Laboratory(data, code)
    intro_lab_object.configure()
