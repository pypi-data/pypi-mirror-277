"""Module for callable ASTx."""

from __future__ import annotations

from typing import Optional, cast

from public import public

from astx.base import (
    NO_SOURCE_LOCATION,
    ASTKind,
    ASTNodes,
    DataType,
    ExprType,
    SourceLocation,
    StatementType,
)
from astx.blocks import Block
from astx.modifiers import ScopeKind, VisibilityKind
from astx.types import ReprStruct
from astx.variables import Arguments


@public
class FunctionCall(DataType):
    """AST class for function call."""

    fn: Function
    args: tuple[DataType, ...]

    def __init__(
        self,
        fn: Function,
        args: tuple[DataType, ...],
        loc: SourceLocation = NO_SOURCE_LOCATION,
        parent: Optional[ASTNodes] = None,
    ) -> None:
        """Initialize the Call instance."""
        super().__init__(loc=loc, parent=parent)
        self.fn = fn
        self.args = args
        self.kind = ASTKind.CallKind

    def __str__(self) -> str:
        """Return a string representation of the object."""
        args = [str(arg) for arg in self.args]
        return f"Call[{self.fn}: {', '.join(args)}]"

    def get_struct(self, simplified: bool = False) -> ReprStruct:
        """Return the AST structure of the object."""
        call_args = []

        for node in self.args:
            call_args.append(node.get_struct(simplified))

        key = f"FUNCTION-CALL[{self.fn}]"
        value = cast(ReprStruct, {"args": call_args})

        return self._prepare_struct(key, value, simplified)


@public
class FunctionPrototype(StatementType):
    """AST class for function prototype declaration."""

    name: str
    args: Arguments
    return_type: ExprType
    scope: ScopeKind
    visibility: VisibilityKind

    def __init__(
        self,
        name: str,
        args: Arguments,
        return_type: ExprType,
        scope: ScopeKind = ScopeKind.global_,
        visibility: VisibilityKind = VisibilityKind.public,
        loc: SourceLocation = NO_SOURCE_LOCATION,
        parent: Optional[ASTNodes] = None,
    ) -> None:
        """Initialize the FunctionPrototype instance."""
        super().__init__(loc=loc, parent=parent)
        self.name = name
        self.args = args
        self.return_type = return_type
        self.loc = loc
        self.kind = ASTKind.PrototypeKind
        self.scope = scope
        self.visibility = visibility

    def get_struct(self, simplified: bool = False) -> ReprStruct:
        """Get the AST structure that represent the object."""
        raise Exception("Visitor method not necessary")


@public
class FunctionReturn(StatementType):
    """AST class for function `return` statement."""

    value: DataType

    def __init__(
        self,
        value: DataType,
        loc: SourceLocation = NO_SOURCE_LOCATION,
        parent: Optional[ASTNodes] = None,
    ) -> None:
        """Initialize the Return instance."""
        super().__init__(loc=loc, parent=parent)
        self.value = value
        self.kind = ASTKind.ReturnKind

    def __str__(self) -> str:
        """Return a string representation of the object."""
        return f"Return[{self.value}]"

    def get_struct(self, simplified: bool = False) -> ReprStruct:
        """Return the AST structure of the object."""
        key = "RETURN"
        value = self.value.get_struct(simplified)
        return self._prepare_struct(key, value, simplified)


@public
class Function(StatementType):
    """AST class for function definition."""

    prototype: FunctionPrototype
    body: Block

    def __init__(
        self,
        prototype: FunctionPrototype,
        body: Block,
        loc: SourceLocation = NO_SOURCE_LOCATION,
        parent: Optional[ASTNodes] = None,
    ) -> None:
        """Initialize the Function instance."""
        super().__init__(loc=loc, parent=parent)
        self.prototype = prototype
        self.body = body
        self.kind = ASTKind.FunctionKind

    @property
    def name(self) -> str:
        """Return the function prototype name."""
        return self.prototype.name

    def __str__(self) -> str:
        """Return a string that represent the object."""
        return f"Function[{self.name}]"

    def __call__(
        self,
        args: tuple[DataType, ...],
        loc: SourceLocation = NO_SOURCE_LOCATION,
        parent: Optional[ASTNodes] = None,
    ) -> FunctionCall:
        """Initialize the Call instance."""
        return FunctionCall(fn=self, args=args, loc=loc, parent=parent)

    def get_struct(self, simplified: bool = False) -> ReprStruct:
        """Get the AST structure that represent the object."""
        fn_args = self.prototype.args.get_struct(simplified)
        fn_body = self.body.get_struct(simplified)

        key = f"FUNCTION[{self.prototype.name}]"
        args_struct = self._prepare_struct("args", fn_args, simplified)
        body_struct = self._prepare_struct("body", fn_body, simplified)

        if not isinstance(args_struct, dict):
            raise Exception("`args` struct is not a valid object.")

        if not isinstance(body_struct, dict):
            raise Exception("`body` struct is not a valid object.")

        value: ReprStruct = {**args_struct, **body_struct}
        return self._prepare_struct(key, value, simplified)
