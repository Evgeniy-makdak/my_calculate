import redis

red_client = redis.Redis(host="my_host_redis", port=6379, db=0)
u_examples = red_client.lrange("u_kommands", 0, -1)
for each in u_examples:
    examle = each.decode("utf-8")
    rez = eval(examle)
    print(examle, "=", rez)

print("конец")
