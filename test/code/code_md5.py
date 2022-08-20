import hashlib


def before(context):
    context["before"] = hashlib.md5()
    return context


def transform(input_bytes, context):
    context["before"].update(input_bytes)


def after(context):
    return context["before"].hexdigest().encode()


def transform(input_bytes):
    md5 = hashlib.md5()
    md5.update(input_bytes)
    return md5.hexdigest().encode()


def filter(name, *args):
    return "0001" in name
