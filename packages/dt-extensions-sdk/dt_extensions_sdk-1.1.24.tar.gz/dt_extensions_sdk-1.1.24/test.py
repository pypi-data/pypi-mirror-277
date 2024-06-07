import json
import time

events = []
for i in range(5000):
    attributes = {}
    for j in range(150):
        attributes[f"attribute{j}"] = j
    events.append(attributes)

s = time.time()
print(len(json.dumps(events).encode("utf-8")))
print("json", time.time() - s)

s2 = time.time()
print(len(f"{events}".encode()))
print("f-string", time.time() - s2)
