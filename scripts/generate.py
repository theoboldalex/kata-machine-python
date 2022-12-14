import os, glob, math, sys
from config import CONFIG
from dsa import DSA

src_path = f"{sys.path[0]}/../src/" # TODO: This probs won't work for everyone

day = 1

try:
    # TODO: this will die on generating day 11. FIx me please
    day = int(sorted(glob.glob(f"{src_path}day*"), reverse=True)[0][-1]) + 1

    if math.isnan(day):
        print("Day is not a number")
        day = 1
except:
    day = 1

day_name = f"day{day}"
day_path = os.path.join(src_path, day_name)
os.mkdir(day_path)

def create_class(name, item):
    pass

def create_function(name, item):
    f = open(f"{day_path}{name}.py", "w")
    f.write(f"def {item['fn_name']}({item['fn_args']}) -> {item['return_type']}:\n"
            f"    pass")
    f.close()

for ds in CONFIG["dsa"]:
    item = DSA[ds]
    if not item:
        raise Exception(f"algorithm {ds} could not be found")

    print(item)
    # TODO: we need to finish the config first before doing this
#    if item["type"] == "class":
#        create_class(ds, item)
#    else:
#        create_function(ds, item)
