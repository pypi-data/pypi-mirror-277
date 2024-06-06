from typing import Any, cast, Dict, Type, TypeVar, Union

import attr

from ..extensions import NotPresentError
from ..models.assembly_concatenation_method_polymer_type import AssemblyConcatenationMethodPolymerType
from ..models.assembly_concatenation_method_type import AssemblyConcatenationMethodType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AssemblyConcatenationMethod")


@attr.s(auto_attribs=True, repr=False)
class AssemblyConcatenationMethod:
    """  """

    _polymer_type: Union[Unset, AssemblyConcatenationMethodPolymerType] = UNSET
    _type: Union[Unset, AssemblyConcatenationMethodType] = UNSET

    def __repr__(self):
        fields = []
        fields.append("polymer_type={}".format(repr(self._polymer_type)))
        fields.append("type={}".format(repr(self._type)))
        return "AssemblyConcatenationMethod({})".format(", ".join(fields))

    def to_dict(self) -> Dict[str, Any]:
        polymer_type: Union[Unset, int] = UNSET
        if not isinstance(self._polymer_type, Unset):
            polymer_type = self._polymer_type.value

        type: Union[Unset, int] = UNSET
        if not isinstance(self._type, Unset):
            type = self._type.value

        field_dict: Dict[str, Any] = {}
        # Allow the model to serialize even if it was created outside of the constructor, circumventing validation
        if polymer_type is not UNSET:
            field_dict["polymerType"] = polymer_type
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any], strict: bool = False) -> T:
        d = src_dict.copy()

        def get_polymer_type() -> Union[Unset, AssemblyConcatenationMethodPolymerType]:
            polymer_type = UNSET
            _polymer_type = d.pop("polymerType")
            if _polymer_type is not None and _polymer_type is not UNSET:
                try:
                    polymer_type = AssemblyConcatenationMethodPolymerType(_polymer_type)
                except ValueError:
                    polymer_type = AssemblyConcatenationMethodPolymerType.of_unknown(_polymer_type)

            return polymer_type

        try:
            polymer_type = get_polymer_type()
        except KeyError:
            if strict:
                raise
            polymer_type = cast(Union[Unset, AssemblyConcatenationMethodPolymerType], UNSET)

        def get_type() -> Union[Unset, AssemblyConcatenationMethodType]:
            type = UNSET
            _type = d.pop("type")
            if _type is not None and _type is not UNSET:
                try:
                    type = AssemblyConcatenationMethodType(_type)
                except ValueError:
                    type = AssemblyConcatenationMethodType.of_unknown(_type)

            return type

        try:
            type = get_type()
        except KeyError:
            if strict:
                raise
            type = cast(Union[Unset, AssemblyConcatenationMethodType], UNSET)

        assembly_concatenation_method = cls(
            polymer_type=polymer_type,
            type=type,
        )

        return assembly_concatenation_method

    @property
    def polymer_type(self) -> AssemblyConcatenationMethodPolymerType:
        if isinstance(self._polymer_type, Unset):
            raise NotPresentError(self, "polymer_type")
        return self._polymer_type

    @polymer_type.setter
    def polymer_type(self, value: AssemblyConcatenationMethodPolymerType) -> None:
        self._polymer_type = value

    @polymer_type.deleter
    def polymer_type(self) -> None:
        self._polymer_type = UNSET

    @property
    def type(self) -> AssemblyConcatenationMethodType:
        if isinstance(self._type, Unset):
            raise NotPresentError(self, "type")
        return self._type

    @type.setter
    def type(self, value: AssemblyConcatenationMethodType) -> None:
        self._type = value

    @type.deleter
    def type(self) -> None:
        self._type = UNSET
