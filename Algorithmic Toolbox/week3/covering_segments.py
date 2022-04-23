# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

'''
def optimal_points(segments):
    points = []
    #write your code here
    start =0
    end=0
    segments.sort()

    for i in range(len(segments)):
        start = segments[i].start
        end = segments[i].end
        for j in range(i+1,len(segments)):
            if ((segments[j].start >= start) and (segments[j].start <= end)):
                start = segments[j].start
                if segments[j].end <= end:
                    end = segments[j].end
            else:
                break

        if start not in points:
            points.append(start)

    return points
'''

def optimal_points2(segments):
    points = []
    segments.sort()
    current = segments[0].end
    points.append(current)
    for s in segments:
        if ((current < s.start) or (current > s.end)):
            current = s.end
            points.append(current)
    return points

if __name__ == '__main__':
    input = sys.stdin.readline()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    #points = optimal_points(segments)
    points = optimal_points2(segments)

    print(len(points))
    print(*points)
