class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        mentions = 0
        res = [0] * numberOfUsers
        online = set(range(numberOfUsers))
        for event, timestamp, message in events:
            if event == "OFFLINE":
                events.append(["ONLINE", str(int(timestamp) + 60), message])
        events.sort(key=lambda x: x[0], reverse=True)
        events.sort(key=lambda x: int(x[1]))
        for event, timestamp, message in events:
            match event:
                case "MESSAGE":
                    if message == "ALL":
                        mentions += 1
                    elif message == "HERE":
                        for i in online:
                            res[i] += 1
                    else:
                        for x in message.split():
                            res[int(x[2:])] += 1
                case "OFFLINE":
                    online.remove(int(message))
                case "ONLINE":
                    online.add(int(message))
        for i in range(numberOfUsers): res[i] += mentions
        return res