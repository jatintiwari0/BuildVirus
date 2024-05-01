import os
from rgbprint import gradient_print
import platform

logo = f"""
            
__________      .__.__       .___ ____   ____.__                     
\______   \__ __|__|  |    __| _/ \   \ /   /|__|______ __ __  ______
 |    |  _/  |  \  |  |   / __ |   \   Y   / |  \_  __ \  |  \/  ___/
 |    |   \  |  /  |  |__/ /_/ |    \     /  |  ||  | \/  |  /\___ \ 
 |______  /____/|__|____/\____ |     \___/   |__||__|  |____//____  >
        \/                    \/                                  \/ 
                 Author: JATIN TIWARI    (V4.0)
        =============================================================
                        [+] Github @jatintiwari0
                        [+] Linkedin @jatintiwari0                          
        =============================================================
"""




def banner():
    gradient_print(logo , start_color='cyan' , end_color='yellow')


def clear():
    os.system("cls") if 'Windows' in platform.platform() else os.system("clear")
