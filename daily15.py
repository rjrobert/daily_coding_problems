"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
"""
import random


class RandomPicker:
    def __init__(self):
        self.result = 0
        self.count = 0
        self.reservoir = []

    def get_random_item(self, x):
        self.count += 1
        # print(f'count: {self.count}')

        if self.count == 1:
            self.result = x
        else:
            rand = random.randrange(self.count)
            # print(f'rand: {rand}')
            if rand == self.count - 1:
                self.result = x

        return self.result

    def select_num_items(self, stream, k):
        self.reservoir = [0] * k
        for i in range(len(stream)):
            rand = random.randrange(i + 1)
            if rand < k:
                self.reservoir[rand] = stream[i]

        return self.reservoir


stream = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# picker = RandomPicker()
# for i in range(len(stream)):
#     result = picker.get_random_item(stream[i])
#     print(f'result: {result}\n')

picker = RandomPicker()
print(f'results: {picker.select_num_items(stream, 5)}')
