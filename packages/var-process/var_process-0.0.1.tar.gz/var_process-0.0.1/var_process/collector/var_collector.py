from typing import Union
from types import TracebackType


class VarCollector:
    def __init__(self, vars2collect: Union[tuple, list] = None, collect_all=False) -> None:
        """
        Initialize the VarCollector with a list of variable names.
        """

        if not collect_all:
            assert len(vars2collect) > 0, "The length of `vars` must be greater than 0"
        else:
            assert (
                vars2collect is None or len(vars2collect) == 0
            ), "`collect_all` is set to True, but `vars2collect` was not None or `[]`, which was conflict."

        self.collect_all = collect_all
        self.vars2collect = vars2collect
        self.local_vars = {}

    def collect_on_error(self, traceback: TracebackType):
        while traceback.tb_next:
            traceback = traceback.tb_next
            frame = traceback.tb_frame

            if self.collect_all:
                self.local_vars.update(frame.f_locals)
            elif self.vars2collect is not None or len(self.vars2collect) > 0:
                self.local_vars.update({name: val for name, val in frame.f_locals.items() if name in self.vars2collect})
            else:
                raise RuntimeError("Must set one of `collect_all` and `vars2collect`")

    @property
    def collected_vars(self):
        return self.local_vars
