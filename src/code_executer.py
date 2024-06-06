def execute_code(code, variables={}):
    exec_locals = {}
    exec(code, variables, exec_locals)
    return exec_locals

# Example usage
# code = "def calculate_average(data):\n    return sum(data) / len(data)\nresult = calculate_average([1, 2, 3, 4, 5])"
# output = execute_code(code)
# print(output['result'])
