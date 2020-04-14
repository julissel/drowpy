import os.path


filename = "file/not/found"

# 1
try:
    if not os.path.exists(filename):
        raise ValueError("file doesn't exists", filename)
except ValueError as err:
    message, filename = err.args[0], err.args[1]
    print('# 1: ', message, filename)
finally:
    # 2
    try:
        raw = input("input the number: ")
        if not raw.isdigit():
            raise ValueError("bad number", raw)
    except ValueError as err:
        print("irregular value!", err)