import time

activity_dict = {
    1: "Soccer",
    2: "Ice Skating",
    3: "Skeet Shooting",
    4: "Bear Wrasslin'"
}

while True:
    x = input("User enters an activity and a response is returned.")

    if x:
        response = len(activity_dict)

        with open("result_receiver.txt", "w") as result:
            result.write(str(response))

        time.sleep(1.0)

        with open("result_receiver.txt") as random_dig:
            value = random_dig.readline()
        with open("result_receiver.txt", "w") as clear:
            pass

        time.sleep(1.0)

        with open("random_activity.txt") as random_act:
            activity = random_act.readline()

        print(activity_dict[int(activity)])
