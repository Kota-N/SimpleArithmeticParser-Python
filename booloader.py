from boolexer import BooLexer
from booparser import BooParser
from booeval import BooEval

class BooLoader:

    def __init__(self, filename):
        prog = Program(open(filename, "r"))
        prog.run()

class Program:

    def __init__(self, fh):
        self.code = fh

    def run(self):
        for line in self.code:
            print(f"line: {line}")

            lexer = BooLexer()
            lexer.run(line)
            print(f"tokens: {lexer.tokens}")

            parser = BooParser(lexer.tokens)
            parser.run()
            print(f"ast: {parser.ast}")

            evaluator = BooEval(parser.ast)
            evaluator.run()
            print(f"output: {evaluator.output}")