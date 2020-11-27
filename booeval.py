class BooEval:

    def __init__(self, ast):
        self.ast = ast
        self.output = ''
        self.operators = {'+': 'add'}

    def run(self):
        for node in self.ast:
            n = node

            if node in self.operators:
                n = self.operators[node]

            getattr(self, n)(self.ast[node])


    def add(self, values):
        self.output = sum(map(int, values))