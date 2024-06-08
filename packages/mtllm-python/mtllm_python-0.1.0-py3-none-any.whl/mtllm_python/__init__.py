"""MTLLM - Meaning Typed Programming Tool."""

from typing import Any, Callable, Optional

from mtllm.tools import Tools

# from mttlm.base import BaseModel


class Function:
    """Function that uses the specified method to generate the output."""

    def __init__(
        self,
        fn: Callable,
        llm: Any,
        incl_info: list["DefinedVariable"],
        method: str = "Normal",
        tools: Optional[list[Tools]] = None,
        **kwargs: dict,
    ) -> None:
        """Initializes the Function object."""
        self.fn = fn
        self.llm = llm
        self.incl_info = incl_info
        self.method = method
        self.kwargs = kwargs

    def __call__(self, *args: list, **kwargs: dict) -> "Output":
        """Calls the function with the specified arguments."""
        pass


class ChainofThoughts(Function):
    """Function that uses the Chain of Thoughts method to generate the output."""

    def __init__(
        self,
        fn: Callable,
        llm: Any,
        incl_info: list["DefinedVariable"],
        **kwargs: dict,
    ) -> None:
        """Initializes the Chain of Thoughts Function."""
        super().__init__(fn, llm, incl_info, "ChainOfThought", None, **kwargs)


class BasicReasoning(Function):
    """Function that uses the Reason method to generate the output."""

    def __init__(
        self,
        fn: Callable,
        llm: Any,
        incl_info: list["DefinedVariable"],
        **kwargs: dict,
    ) -> None:
        """Initializes the Basic Reasoning Function."""
        super().__init__(fn, llm, incl_info, "Reason", None, **kwargs)


class ReAct(Function):
    """Function that uses the ReAct method to generate the output with the help of the tools."""

    def __init__(
        self,
        fn: Callable,
        llm: Any,
        incl_info: list["DefinedVariable"],
        tools: list[Tools],
        **kwargs: dict,
    ) -> None:
        """Initializes the ReAct Prompted Function."""
        assert len(tools) > 0, "Please provide at least one tool"
        super().__init__(fn, llm, incl_info, "ReAct", tools, **kwargs)


class DefinedVariable:
    """DefinedVariable object that contains the structured information of the variable."""

    def __init__(self, var: Any, desc: str) -> None:
        """Initializes the DefinedVariable object."""
        self.value = var
        self.desc = desc
        self.name = self.get_variable_name(var)
        self.type = self.get_type(var)

    def get_type(self, var: Any) -> str:
        """Returns the type of the variable."""
        pass

    def get_variable_name(self, var: Any) -> str:
        """Returns the name of the variable."""
        pass

    def __str__(self) -> str:
        """Returns the string representation of the variable."""
        return f"{self.desc} ({self.get_variable_name}) ({self.get_type}) = {str(self.value)}"

    def get_special_types(self) -> list[str]:
        """Returns the special types used in the variable."""
        pass


class Output:
    """Output object that contains the structured output of the function."""

    def __init__(self, llm_output: str, method: str) -> None:
        """Initializes the Output object."""
        self.llm_output = llm_output
        self.method = method

    @property
    def result(self) -> Any:
        """Returns the result of the output in the desired type."""
        pass

    @property
    def rationale(self) -> str:
        """Returns the rationale of the output."""
        assert self.method in [
            "ChainOfThought",
            "Reason",
        ], "Rationale is only available for ChainOfThought and Reason methods"
        pass
