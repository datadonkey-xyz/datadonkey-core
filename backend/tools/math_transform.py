from latex2sympy2 import latex2sympy

def generate_func(latex_input: str) -> function:
    latex_clean = latex_input.replace('\ ', '')
    res: str
    try:
        res = latex2sympy(latex_clean)
    except Exception as e:
        print(e)

    def func(input: dict):
        return eval(res)


