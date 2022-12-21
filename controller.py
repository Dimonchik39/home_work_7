import functions as fu
import simple_calc as si
import rational as ra
import complex as co

def start_calc():
    calc_mode = fu.menu_select()
    if calc_mode == 3:
        result = si.work_calc()
    if calc_mode == 2:
        result = co.comp()
    if calc_mode == 1:
        result = ra.comp2()
    result
    
