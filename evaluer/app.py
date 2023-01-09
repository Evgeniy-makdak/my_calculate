import redis

print("начало")
red_client = redis.Redis(host="my_host_redis", port=6379, db=0)

user_input = ""
while user_input != "stop":
    user_input = input("введите выражение: ")
    if user_input != "stop":
        red_client.rpush("u_kommands", user_input)

print("конец ввода")
