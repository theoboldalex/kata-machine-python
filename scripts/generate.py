import sys

src_path = f"{sys.path[0]}/../src/" # TODO: update path depending on day generated

def create_function(name, item):
    f = open(f"{src_path}{name}.py", "w")
    f.write(f"def {item['fn_name']}({item['fn_args']}) -> {item['return_type']}:\n"
            f"    pass")
    f.close()
