def solution(members, messages):
    count = 0

    member_hashmap = {}

    for member in members:
        member_hashmap[member] = 0

    for message in messages:
        local = {}

        if "@all" in message:
            count += 1
        else:
            words = message.split(" ")

            for word in words:
                if (
                    word[0] == "@"
                    and word[1:] in member_hashmap
                    and word[1:] not in local
                ):
                    local[word[1:]] = 1

        for key, value in local.items():
            member_hashmap[key] += 1

    for key, value in member_hashmap.items():
        member_hashmap[key] += count

    sorted_items = sorted(member_hashmap.items(), key=lambda x: [-x[1], x[0]])

    answer = []

    for item in sorted_items:
        answer.append("{}={}".format(item[0], item[1]))

    return answer
