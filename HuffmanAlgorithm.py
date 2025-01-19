class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanAlgorithm:
    def __init__(self):
        self.nodes = []

    def calculate_frequencies(self, text):
        frequencies = defaultdict(int)
        for char in text:
            frequencies[char] += 1
        return frequencies

    def build_tree(self, text):
        self.nodes = []
        frequencies = self.calculate_frequencies(text)

        heap = []
        for char, freq in frequencies.items():
            node = HuffmanNode(char, freq)
            heapq.heappush(heap, node)
            self.nodes.append(("leaf", node))

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)

            internal = HuffmanNode('*', left.freq + right.freq)
            internal.left = left
            internal.right = right

            heapq.heappush(heap, internal)
            self.nodes.append(("internal", internal))

        return self.nodes
