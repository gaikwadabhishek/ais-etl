import hashlib
# from itertools import cycle
def transform(input_bytes):
    md5 = hashlib.md5()
    md5.update(input_bytes)
    return md5.hexdigest().encode()

def filter(name, obj):
    return "backpack" in name


# def before(context):
#     context["key"] = b"AISTORE"


# def transform(input_bytes, context):
#     return bytes([_a ^ _b for _a, _b in zip(input_bytes, cycle(context["key"]))])
