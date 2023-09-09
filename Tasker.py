import time
import inspect
import sys
import importlib
import subprocess
from datetime import datetime, timedelta
import os
#--------------------

def install_and_import(package):
    try:
        importlib.import_module(package)
    except ImportError:
        subprocess.check_call(["python", "-m", "pip", "install", package])
    finally:
        globals()[package] = importlib.import_module(package)

install_and_import('cachetools')
install_and_import('colorama')
from colorama import Fore, Style
from cachetools import TTLCache
#---------------
def format_time(seconds):
    if seconds < 1e-6:
        return f"{seconds * 1e9:.2f} ns" 
    elif seconds < 1e-3:
        return f"{seconds * 1e6:.2f} μs"  
    elif seconds < 1:
        return f"{seconds * 1e3:.2f} ms"  
    else:
        return f"{seconds:.2f} s"  


cache = TTLCache(maxsize=5, ttl=100)
def save_data(key, value):
    cache[key] = value

def get_data(key):
    return cache.get(key)


class t:
    def config(timer=False,filename=False):
        if filename is True:
            save_data("filename", True)
        else:
            save_data("filename", None)
        if timer is True:
            start_time = time.time()
            save_data("start", start_time)
        else:
            save_data("start",None)
        
    

    def print( message='None',code=1 , function_name=None):
        """
    ## t.print
    - print for you somthing with 4 code option
        - **0** = Start Code! use it when you start Somthing
        - **1** = Down Code! use it when down tasks
        - **2** = Error Code! For Just Showing Errors
            - .. note:: Error Code Most Run in Exceptions
        - **3** = Info Code! For showing somthing like stdout 
        - function_name = detect automatical but you can change to your chouse
    
    
    ### Example = `t.print('my test message',0,'TestNameFunctio')`

    `Help <https://t.me/dridop>`_
        """
        message = str(message)
        caller_frame = inspect.currentframe().f_back
        caller_line = caller_frame.f_lineno

        def get_error_line():
            exc_type, exc_value, exc_traceback = sys.exc_info()
            return exc_traceback.tb_lineno if exc_traceback else caller_line

        error_line = str(get_error_line() if code not in {0, 1, 3} else caller_line)
        outer_frames = inspect.getouterframes(caller_frame)
     

        if outer_frames is not None:
            outer_frame = outer_frames[0]
            function = outer_frame[3]
            function = "MainModule" if function == "<module>" else function

            if get_data('filename') == True:
                outer_frame = outer_frames[0]
                filename = os.path.basename(outer_frame[1])
                save_data('filename',f' {filename}')
            else : 
                save_data('filename','')
            if function_name is not None :
                if code == 0:
                    function = function_name
                if code == 1:
                    function = function_name
                if code == 2:
                    function = Fore.RED + function_name + Style.RESET_ALL
                if code == 3:
                    function = Fore.GREEN + function_name + Style.RESET_ALL


        else:
            function = "MainModule"
            
        if get_data("start"):
            start_time = get_data("start")
            counter = time.time() - start_time
            counter = f"[{format_time(counter)}]"
        else:
            counter = ""
            
        tag = ''
        if code == 0:
            tag = f'[{"S"}]'
        elif code == 1:
            tag = Fore.BLUE + f'[{"D"}]' + Style.RESET_ALL
        elif code == 2:
            tag = Fore.RED + Style.BRIGHT + f'[{"E"}]'
        elif code == 3:
            tag =  Fore.GREEN +  f'[{"I"}]' 

        print(
            f"[{error_line:^3}]"
            + Style.RESET_ALL
            + f"[{get_data('filename')} {function:^10} ]"
            + f"{tag}"
            + f"{counter}: {message} {Style.RESET_ALL}"
        )
