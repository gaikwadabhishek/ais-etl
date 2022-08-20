from urllib import request
from aistore import Client

client = Client("http://192.168.49.2:8080")

for obj in client.bucket("caltech256").list_all_objects():
    req = request.Request(
        f"http://0.0.0.0:50051/caltech256/{obj.name}",
        client.bucket("caltech256").object(obj.name).get().read_all(),
        {"Content-Type": "application/octet-stream"},
        method="PUT",
    )
    try:
        request.urlopen(req).read()
    except:
        pass
# req = request.Request(
#         "http://0.0.0.0:50051/caltech256/999.ak47/001_0098.jpg",
#         client.bucket("caltech256").object("999.ak47/001_0098.jpg").get().read_all(),
#         {
#             "Content-Type": "application/octet-stream",
#             "Name": "ais://caltech256/999.ak47/001_0098.jpg",
#         },
#         method="PUT",
#     )
# try:
#     string = request.urlopen(req).read()
#     for i in string:
#         print(i)
# except ConnectionResetError:
#     print("==> ConnectionResetError")
#     pass
