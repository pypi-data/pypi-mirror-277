import traceback
import sys
import logging
import os

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("fairbench.log")],
)
from objwrap import Wrapper


class ExplainableError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.explain = message
        self.value = float("NaN")
        self.distribution = None
        self.desc = None
        self.__printed = False

    def __float__(self):
        return self.value

    def __int__(self):
        return self.value

    def __str__(self):
        return "---"

    def __repr__(self):
        return f"{type(self).__name__}: {self.explain}"

    def format_traceback(self):
        tb = traceback.extract_tb(self.__traceback__)
        tb = [frame for frame in traceback.extract_stack()[:-1]] + tb
        filtered_tb = [
            frame
            for frame in tb
            if not frame.filename.endswith(r"fairbench\core\compute\delegation.py")
            and not frame.filename.endswith(r"fairbench\core\fork.py")
            and not frame.filename.endswith(r"fairbench\core\explanation\error.py")
            and not frame.filename.endswith(r"fairbench\blocks\framework.py")
            and not frame.filename.startswith("<makefun-gen-")
        ]
        formatted_tb = traceback.format_list(filtered_tb)
        return (
            "".join(formatted_tb) + f"{type(self).__name__}: {self.explain}"
            f"\nThis error only appears because you requested dependent computations."
            f"\nOtherwise, it is normal for reports or other FairBench data to hold ExplainableError."
            f"\nYou need to check your data first for any errors (you will see --- when printing them)."
            f"\n- Issue tracker https://github.com/mever-team/FairBench/issues"
            f"\n- Full trace in ./{os.path.relpath('fairbench.log')}"
        )

    def caught(self):
        # this is what to return when catching explainable errors (e.g., raised within metric execution)
        return self

    def __add__(self, other):
        self.reraise()

    def __radd__(self, other):
        self.reraise()

    def __sub__(self, other):
        self.reraise()

    def __rsub__(self, other):
        self.reraise()

    def __mul__(self, other):
        self.reraise()

    def __rmul__(self, other):
        self.reraise()

    def __le__(self, other):
        self.reraise()

    def __ge__(self, other):
        self.reraise()

    def __lt__(self, other):
        self.reraise()

    def __gt__(self, other):
        self.reraise()

    def __eq__(self, other):
        self.reraise()

    def __neg__(self):
        self.reraise()

    def __ne__(self, other):
        self.reraise()

    def __pow__(self, power, modulo=None):
        self.reraise()

    def __rpow__(self, other):
        self.reraise()

    def reraise(self):
        if self.__printed:
            print("Repeated usage of " + repr(self), file=sys.stderr)
            raise self
        self.__printed = True
        stack_trace = "".join(traceback.format_stack())
        logging.error(
            "There was an attempt to call computations that encountered an ExplainabeError"
            "\nThis is the full stack trace of the ExplainableError that includes FairBench internals",
            exc_info=self,
        )
        logging.error(
            "This is the full stack trace of the computations where the ExplainableError was encountered"
            "\nTraceback (most recent call last):" + stack_trace + "-" * 120
        )
        # this is what happens when the explainable error creates another issue down the line
        print(self.format_traceback(), file=sys.stderr)
        # remove this to print full errors for fairbench's internal debugging
        raise self


def verify(condition, message):
    if not condition:
        raise ExplainableError(message)
