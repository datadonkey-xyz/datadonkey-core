from typing import List
from latex2sympy2 import latex2sympy

def transform_func_from_latex(
    latex_input: str,
    arg_names: List[str]
):
    latex_clean = latex_input.replace('\ ', '')
    try:
        expr = latex2sympy(latex_clean)
        arg_list_string = ""
        subst_dict_string = "{"
        for i in range(len(arg_names)):
            name = arg_names[i]
            arg_list_string += f"{name}"
            subst_dict_string += f'"{name}":{name}'
            if i < len(arg_names) - 1:
                arg_list_string += ","
                subst_dict_string += ","
        subst_dict_string += "}"
        f: function = eval(f"""
lambda {arg_list_string}: expr.subs({subst_dict_string}).evalf()
""", {"expr": expr})
        return f

    except Exception as e:
        print(e)
