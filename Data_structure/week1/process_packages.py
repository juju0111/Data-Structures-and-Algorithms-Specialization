# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.max_buffer_size = size
        self.finish_time = []
        
    def process(self, request):
        # write your code here
        s = len(self.finish_time)
        if s == 0:
            self.finish_time.append(request.arrived_at)
            self.finish_time.append(request.time_to_process)
        else:
            if (request.arrived_at < self.finish_time[-1]):
                self.size -= 1
                if self.size <= 0:
                    return Response(False, -1)
                else:
                    self.finish_time.append(request.time_to_process + self.finish_time[-1])

            else:
                self.size += 1
                if self.size > self.max_buffer_size:
                    self.size = self.max_buffer_size
                self.finish_time.append(request.time_to_process + self.finish_time[-1])
        
        return Response(True,self.finish_time[-2] )


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if response.was_dropped else -1)


if __name__ == "__main__":
    main()
