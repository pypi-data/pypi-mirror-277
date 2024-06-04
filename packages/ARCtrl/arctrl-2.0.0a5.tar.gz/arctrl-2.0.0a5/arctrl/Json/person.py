from __future__ import annotations
from collections.abc import Callable
from typing import Any
from ..fable_modules.fable_library.array_ import map
from ..fable_modules.fable_library.list import (choose, of_array, FSharpList)
from ..fable_modules.fable_library.option import default_arg
from ..fable_modules.fable_library.result import FSharpResult_2
from ..fable_modules.fable_library.seq import try_pick
from ..fable_modules.fable_library.string_ import (replace, split, join, to_text, printf)
from ..fable_modules.fable_library.types import Array
from ..fable_modules.fable_library.util import (equals, to_enumerable)
from ..fable_modules.thoth_json_core.decode import (object, IOptionalGetter, string, IGetters, IRequiredGetter, map as map_1, array as array_2)
from ..fable_modules.thoth_json_core.types import (Json, Decoder_1)
from ..fable_modules.thoth_json_python.decode import Decode_fromString
from ..fable_modules.thoth_json_python.encode import to_string
from ..Core.comment import Comment
from ..Core.conversion import (Person_setCommentFromORCID, Person_setOrcidFromComments)
from ..Core.ontology_annotation import OntologyAnnotation
from ..Core.person import Person
from .comment import (Comment_encoder, Comment_decoder, Comment_ROCrate_encoderDisambiguatingDescription, Comment_ROCrate_decoderDisambiguatingDescription)
from .context.rocrate.isa_organization_context import context_jsonvalue
from .context.rocrate.isa_person_context import (context_jsonvalue as context_jsonvalue_1, context_minimal_json_value)
from .decode import (Decode_resizeArray, Decode_objectNoAdditionalProperties)
from .encode import (try_include, try_include_seq, default_spaces)
from .ontology_annotation import (OntologyAnnotation_encoder, OntologyAnnotation_decoder, OntologyAnnotation_ROCrate_encoderDefinedTerm, OntologyAnnotation_ROCrate_decoderDefinedTerm)

def Person_encoder(person: Person) -> Json:
    def chooser(tupled_arg: tuple[str, Json], person: Any=person) -> tuple[str, Json] | None:
        v: Json = tupled_arg[1]
        if equals(v, Json(3)):
            return None

        else: 
            return (tupled_arg[0], v)


    def _arrow1184(value: str, person: Any=person) -> Json:
        return Json(0, value)

    def _arrow1185(value_2: str, person: Any=person) -> Json:
        return Json(0, value_2)

    def _arrow1186(value_4: str, person: Any=person) -> Json:
        return Json(0, value_4)

    def _arrow1187(value_6: str, person: Any=person) -> Json:
        return Json(0, value_6)

    def _arrow1188(value_8: str, person: Any=person) -> Json:
        return Json(0, value_8)

    def _arrow1189(value_10: str, person: Any=person) -> Json:
        return Json(0, value_10)

    def _arrow1190(value_12: str, person: Any=person) -> Json:
        return Json(0, value_12)

    def _arrow1191(value_14: str, person: Any=person) -> Json:
        return Json(0, value_14)

    def _arrow1192(value_16: str, person: Any=person) -> Json:
        return Json(0, value_16)

    def _arrow1193(oa: OntologyAnnotation, person: Any=person) -> Json:
        return OntologyAnnotation_encoder(oa)

    def _arrow1194(comment: Comment, person: Any=person) -> Json:
        return Comment_encoder(comment)

    return Json(5, choose(chooser, of_array([try_include("firstName", _arrow1184, person.FirstName), try_include("lastName", _arrow1185, person.LastName), try_include("midInitials", _arrow1186, person.MidInitials), try_include("orcid", _arrow1187, person.ORCID), try_include("email", _arrow1188, person.EMail), try_include("phone", _arrow1189, person.Phone), try_include("fax", _arrow1190, person.Fax), try_include("address", _arrow1191, person.Address), try_include("affiliation", _arrow1192, person.Affiliation), try_include_seq("roles", _arrow1193, person.Roles), try_include_seq("comments", _arrow1194, person.Comments)])))


def _arrow1206(get: IGetters) -> Person:
    def _arrow1195(__unit: None=None) -> str | None:
        object_arg: IOptionalGetter = get.Optional
        return object_arg.Field("orcid", string)

    def _arrow1196(__unit: None=None) -> str | None:
        object_arg_1: IOptionalGetter = get.Optional
        return object_arg_1.Field("lastName", string)

    def _arrow1197(__unit: None=None) -> str | None:
        object_arg_2: IOptionalGetter = get.Optional
        return object_arg_2.Field("firstName", string)

    def _arrow1198(__unit: None=None) -> str | None:
        object_arg_3: IOptionalGetter = get.Optional
        return object_arg_3.Field("midInitials", string)

    def _arrow1199(__unit: None=None) -> str | None:
        object_arg_4: IOptionalGetter = get.Optional
        return object_arg_4.Field("email", string)

    def _arrow1200(__unit: None=None) -> str | None:
        object_arg_5: IOptionalGetter = get.Optional
        return object_arg_5.Field("phone", string)

    def _arrow1201(__unit: None=None) -> str | None:
        object_arg_6: IOptionalGetter = get.Optional
        return object_arg_6.Field("fax", string)

    def _arrow1202(__unit: None=None) -> str | None:
        object_arg_7: IOptionalGetter = get.Optional
        return object_arg_7.Field("address", string)

    def _arrow1203(__unit: None=None) -> str | None:
        object_arg_8: IOptionalGetter = get.Optional
        return object_arg_8.Field("affiliation", string)

    def _arrow1204(__unit: None=None) -> Array[OntologyAnnotation] | None:
        arg_19: Decoder_1[Array[OntologyAnnotation]] = Decode_resizeArray(OntologyAnnotation_decoder)
        object_arg_9: IOptionalGetter = get.Optional
        return object_arg_9.Field("roles", arg_19)

    def _arrow1205(__unit: None=None) -> Array[Comment] | None:
        arg_21: Decoder_1[Array[Comment]] = Decode_resizeArray(Comment_decoder)
        object_arg_10: IOptionalGetter = get.Optional
        return object_arg_10.Field("comments", arg_21)

    return Person(_arrow1195(), _arrow1196(), _arrow1197(), _arrow1198(), _arrow1199(), _arrow1200(), _arrow1201(), _arrow1202(), _arrow1203(), _arrow1204(), _arrow1205())


Person_decoder: Decoder_1[Person] = object(_arrow1206)

def Person_ROCrate_genID(p: Person) -> str:
    def chooser(c: Comment, p: Any=p) -> str | None:
        matchValue: str | None = c.Name
        matchValue_1: str | None = c.Value
        (pattern_matching_result, n, v) = (None, None, None)
        if matchValue is not None:
            if matchValue_1 is not None:
                pattern_matching_result = 0
                n = matchValue
                v = matchValue_1

            else: 
                pattern_matching_result = 1


        else: 
            pattern_matching_result = 1

        if pattern_matching_result == 0:
            if True if (True if (n == "orcid") else (n == "Orcid")) else (n == "ORCID"):
                return v

            else: 
                return None


        elif pattern_matching_result == 1:
            return None


    orcid: str | None = try_pick(chooser, p.Comments)
    if orcid is None:
        match_value_1: str | None = p.EMail
        if match_value_1 is None:
            matchValue_2: str | None = p.FirstName
            matchValue_3: str | None = p.MidInitials
            matchValue_4: str | None = p.LastName
            (pattern_matching_result_1, fn, ln, mn, fn_1, ln_1, ln_2, fn_2) = (None, None, None, None, None, None, None, None)
            if matchValue_2 is None:
                if matchValue_3 is None:
                    if matchValue_4 is not None:
                        pattern_matching_result_1 = 2
                        ln_2 = matchValue_4

                    else: 
                        pattern_matching_result_1 = 4


                else: 
                    pattern_matching_result_1 = 4


            elif matchValue_3 is None:
                if matchValue_4 is None:
                    pattern_matching_result_1 = 3
                    fn_2 = matchValue_2

                else: 
                    pattern_matching_result_1 = 1
                    fn_1 = matchValue_2
                    ln_1 = matchValue_4


            elif matchValue_4 is not None:
                pattern_matching_result_1 = 0
                fn = matchValue_2
                ln = matchValue_4
                mn = matchValue_3

            else: 
                pattern_matching_result_1 = 4

            if pattern_matching_result_1 == 0:
                return (((("#" + replace(fn, " ", "_")) + "_") + replace(mn, " ", "_")) + "_") + replace(ln, " ", "_")

            elif pattern_matching_result_1 == 1:
                return (("#" + replace(fn_1, " ", "_")) + "_") + replace(ln_1, " ", "_")

            elif pattern_matching_result_1 == 2:
                return "#" + replace(ln_2, " ", "_")

            elif pattern_matching_result_1 == 3:
                return "#" + replace(fn_2, " ", "_")

            elif pattern_matching_result_1 == 4:
                return "#EmptyPerson"


        else: 
            return match_value_1


    else: 
        return orcid



def Person_ROCrate_Affiliation_encoder(affiliation: str) -> Json:
    return Json(5, to_enumerable([("@type", Json(0, "Organization")), ("@id", Json(0, replace(("#Organization_" + affiliation) + "", " ", "_"))), ("name", Json(0, affiliation)), ("@context", context_jsonvalue)]))


def _arrow1207(get: IGetters) -> str:
    object_arg: IRequiredGetter = get.Required
    return object_arg.Field("name", string)


Person_ROCrate_Affiliation_decoder: Decoder_1[str] = object(_arrow1207)

def Person_ROCrate_encoder(oa: Person) -> Json:
    def chooser(tupled_arg: tuple[str, Json], oa: Any=oa) -> tuple[str, Json] | None:
        v: Json = tupled_arg[1]
        if equals(v, Json(3)):
            return None

        else: 
            return (tupled_arg[0], v)


    def _arrow1208(value_2: str, oa: Any=oa) -> Json:
        return Json(0, value_2)

    def _arrow1209(value_4: str, oa: Any=oa) -> Json:
        return Json(0, value_4)

    def _arrow1210(value_6: str, oa: Any=oa) -> Json:
        return Json(0, value_6)

    def _arrow1211(value_8: str, oa: Any=oa) -> Json:
        return Json(0, value_8)

    def _arrow1212(value_10: str, oa: Any=oa) -> Json:
        return Json(0, value_10)

    def _arrow1213(value_12: str, oa: Any=oa) -> Json:
        return Json(0, value_12)

    def _arrow1214(value_14: str, oa: Any=oa) -> Json:
        return Json(0, value_14)

    def _arrow1215(value_16: str, oa: Any=oa) -> Json:
        return Json(0, value_16)

    def _arrow1216(affiliation: str, oa: Any=oa) -> Json:
        return Person_ROCrate_Affiliation_encoder(affiliation)

    def _arrow1217(oa_1: OntologyAnnotation, oa: Any=oa) -> Json:
        return OntologyAnnotation_ROCrate_encoderDefinedTerm(oa_1)

    def _arrow1218(comment: Comment, oa: Any=oa) -> Json:
        return Comment_ROCrate_encoderDisambiguatingDescription(comment)

    return Json(5, choose(chooser, of_array([("@id", Json(0, Person_ROCrate_genID(oa))), ("@type", Json(0, "Person")), try_include("orcid", _arrow1208, oa.ORCID), try_include("firstName", _arrow1209, oa.FirstName), try_include("lastName", _arrow1210, oa.LastName), try_include("midInitials", _arrow1211, oa.MidInitials), try_include("email", _arrow1212, oa.EMail), try_include("phone", _arrow1213, oa.Phone), try_include("fax", _arrow1214, oa.Fax), try_include("address", _arrow1215, oa.Address), try_include("affiliation", _arrow1216, oa.Affiliation), try_include_seq("roles", _arrow1217, oa.Roles), try_include_seq("comments", _arrow1218, oa.Comments), ("@context", context_jsonvalue_1)])))


def _arrow1230(get: IGetters) -> Person:
    def _arrow1219(__unit: None=None) -> str | None:
        object_arg: IOptionalGetter = get.Optional
        return object_arg.Field("orcid", string)

    def _arrow1220(__unit: None=None) -> str | None:
        object_arg_1: IOptionalGetter = get.Optional
        return object_arg_1.Field("lastName", string)

    def _arrow1221(__unit: None=None) -> str | None:
        object_arg_2: IOptionalGetter = get.Optional
        return object_arg_2.Field("firstName", string)

    def _arrow1222(__unit: None=None) -> str | None:
        object_arg_3: IOptionalGetter = get.Optional
        return object_arg_3.Field("midInitials", string)

    def _arrow1223(__unit: None=None) -> str | None:
        object_arg_4: IOptionalGetter = get.Optional
        return object_arg_4.Field("email", string)

    def _arrow1224(__unit: None=None) -> str | None:
        object_arg_5: IOptionalGetter = get.Optional
        return object_arg_5.Field("phone", string)

    def _arrow1225(__unit: None=None) -> str | None:
        object_arg_6: IOptionalGetter = get.Optional
        return object_arg_6.Field("fax", string)

    def _arrow1226(__unit: None=None) -> str | None:
        object_arg_7: IOptionalGetter = get.Optional
        return object_arg_7.Field("address", string)

    def _arrow1227(__unit: None=None) -> str | None:
        object_arg_8: IOptionalGetter = get.Optional
        return object_arg_8.Field("affiliation", Person_ROCrate_Affiliation_decoder)

    def _arrow1228(__unit: None=None) -> Array[OntologyAnnotation] | None:
        arg_19: Decoder_1[Array[OntologyAnnotation]] = Decode_resizeArray(OntologyAnnotation_ROCrate_decoderDefinedTerm)
        object_arg_9: IOptionalGetter = get.Optional
        return object_arg_9.Field("roles", arg_19)

    def _arrow1229(__unit: None=None) -> Array[Comment] | None:
        arg_21: Decoder_1[Array[Comment]] = Decode_resizeArray(Comment_ROCrate_decoderDisambiguatingDescription)
        object_arg_10: IOptionalGetter = get.Optional
        return object_arg_10.Field("comments", arg_21)

    return Person(_arrow1219(), _arrow1220(), _arrow1221(), _arrow1222(), _arrow1223(), _arrow1224(), _arrow1225(), _arrow1226(), _arrow1227(), _arrow1228(), _arrow1229())


Person_ROCrate_decoder: Decoder_1[Person] = object(_arrow1230)

def Person_ROCrate_encodeAuthorListString(author_list: str) -> Json:
    def encode_single(name: str, author_list: Any=author_list) -> Json:
        def chooser(tupled_arg: tuple[str, Json], name: Any=name) -> tuple[str, Json] | None:
            v: Json = tupled_arg[1]
            if equals(v, Json(3)):
                return None

            else: 
                return (tupled_arg[0], v)


        def _arrow1231(value_1: str, name: Any=name) -> Json:
            return Json(0, value_1)

        return Json(5, choose(chooser, of_array([("@type", Json(0, "Person")), try_include("name", _arrow1231, name), ("@context", context_minimal_json_value)])))

    def mapping(s: str, author_list: Any=author_list) -> str:
        return s.strip()

    return Json(6, map(encode_single, map(mapping, split(author_list, ["\t" if (author_list.find("\t") >= 0) else (";" if (author_list.find(";") >= 0) else ",")], None, 0), None), None))


def ctor(v: Array[str]) -> str:
    return join(", ", v)


def _arrow1233(get: IGetters) -> str:
    def _arrow1232(__unit: None=None) -> str | None:
        object_arg: IOptionalGetter = get.Optional
        return object_arg.Field("name", string)

    return default_arg(_arrow1232(), "")


Person_ROCrate_decodeAuthorListString: Decoder_1[str] = map_1(ctor, array_2(object(_arrow1233)))

Person_ISAJson_allowedFields: FSharpList[str] = of_array(["@id", "firstName", "lastName", "midInitials", "email", "phone", "fax", "address", "affiliation", "roles", "comments", "@type", "@context"])

def Person_ISAJson_encoder(person: Person) -> Json:
    person_1: Person = Person_setCommentFromORCID(person)
    def chooser(tupled_arg: tuple[str, Json], person: Any=person) -> tuple[str, Json] | None:
        v: Json = tupled_arg[1]
        if equals(v, Json(3)):
            return None

        else: 
            return (tupled_arg[0], v)


    def _arrow1235(value: str, person: Any=person) -> Json:
        return Json(0, value)

    def _arrow1236(value_2: str, person: Any=person) -> Json:
        return Json(0, value_2)

    def _arrow1237(value_4: str, person: Any=person) -> Json:
        return Json(0, value_4)

    def _arrow1238(value_6: str, person: Any=person) -> Json:
        return Json(0, value_6)

    def _arrow1239(value_8: str, person: Any=person) -> Json:
        return Json(0, value_8)

    def _arrow1240(value_10: str, person: Any=person) -> Json:
        return Json(0, value_10)

    def _arrow1241(value_12: str, person: Any=person) -> Json:
        return Json(0, value_12)

    def _arrow1242(value_14: str, person: Any=person) -> Json:
        return Json(0, value_14)

    def _arrow1243(oa: OntologyAnnotation, person: Any=person) -> Json:
        return OntologyAnnotation_encoder(oa)

    def _arrow1244(comment: Comment, person: Any=person) -> Json:
        return Comment_encoder(comment)

    return Json(5, choose(chooser, of_array([try_include("firstName", _arrow1235, person_1.FirstName), try_include("lastName", _arrow1236, person_1.LastName), try_include("midInitials", _arrow1237, person_1.MidInitials), try_include("email", _arrow1238, person_1.EMail), try_include("phone", _arrow1239, person_1.Phone), try_include("fax", _arrow1240, person_1.Fax), try_include("address", _arrow1241, person_1.Address), try_include("affiliation", _arrow1242, person_1.Affiliation), try_include_seq("roles", _arrow1243, person_1.Roles), try_include_seq("comments", _arrow1244, person_1.Comments)])))


def _arrow1255(get: IGetters) -> Person:
    def _arrow1245(__unit: None=None) -> str | None:
        object_arg: IOptionalGetter = get.Optional
        return object_arg.Field("lastName", string)

    def _arrow1246(__unit: None=None) -> str | None:
        object_arg_1: IOptionalGetter = get.Optional
        return object_arg_1.Field("firstName", string)

    def _arrow1247(__unit: None=None) -> str | None:
        object_arg_2: IOptionalGetter = get.Optional
        return object_arg_2.Field("midInitials", string)

    def _arrow1248(__unit: None=None) -> str | None:
        object_arg_3: IOptionalGetter = get.Optional
        return object_arg_3.Field("email", string)

    def _arrow1249(__unit: None=None) -> str | None:
        object_arg_4: IOptionalGetter = get.Optional
        return object_arg_4.Field("phone", string)

    def _arrow1250(__unit: None=None) -> str | None:
        object_arg_5: IOptionalGetter = get.Optional
        return object_arg_5.Field("fax", string)

    def _arrow1251(__unit: None=None) -> str | None:
        object_arg_6: IOptionalGetter = get.Optional
        return object_arg_6.Field("address", string)

    def _arrow1252(__unit: None=None) -> str | None:
        object_arg_7: IOptionalGetter = get.Optional
        return object_arg_7.Field("affiliation", string)

    def _arrow1253(__unit: None=None) -> Array[OntologyAnnotation] | None:
        arg_17: Decoder_1[Array[OntologyAnnotation]] = Decode_resizeArray(OntologyAnnotation_decoder)
        object_arg_8: IOptionalGetter = get.Optional
        return object_arg_8.Field("roles", arg_17)

    def _arrow1254(__unit: None=None) -> Array[Comment] | None:
        arg_19: Decoder_1[Array[Comment]] = Decode_resizeArray(Comment_decoder)
        object_arg_9: IOptionalGetter = get.Optional
        return object_arg_9.Field("comments", arg_19)

    return Person_setOrcidFromComments(Person(None, _arrow1245(), _arrow1246(), _arrow1247(), _arrow1248(), _arrow1249(), _arrow1250(), _arrow1251(), _arrow1252(), _arrow1253(), _arrow1254()))


Person_ISAJson_decoder: Decoder_1[Person] = Decode_objectNoAdditionalProperties(Person_ISAJson_allowedFields, _arrow1255)

def ARCtrl_Person__Person_fromJsonString_Static_Z721C83C5(s: str) -> Person:
    match_value: FSharpResult_2[Person, str] = Decode_fromString(Person_decoder, s)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        return match_value.fields[0]



def ARCtrl_Person__Person_toJsonString_Static_71136F3F(spaces: int | None=None) -> Callable[[Person], str]:
    def _arrow1256(obj: Person, spaces: Any=spaces) -> str:
        value: Json = Person_encoder(obj)
        return to_string(default_spaces(spaces), value)

    return _arrow1256


def ARCtrl_Person__Person_fromROCrateJsonString_Static_Z721C83C5(s: str) -> Person:
    match_value: FSharpResult_2[Person, str] = Decode_fromString(Person_ROCrate_decoder, s)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        return match_value.fields[0]



def ARCtrl_Person__Person_toROCrateJsonString_Static_71136F3F(spaces: int | None=None) -> Callable[[Person], str]:
    def _arrow1257(obj: Person, spaces: Any=spaces) -> str:
        value: Json = Person_ROCrate_encoder(obj)
        return to_string(default_spaces(spaces), value)

    return _arrow1257


def ARCtrl_Person__Person_toISAJsonString_Static_71136F3F(spaces: int | None=None) -> Callable[[Person], str]:
    def _arrow1258(obj: Person, spaces: Any=spaces) -> str:
        value: Json = Person_ISAJson_encoder(obj)
        return to_string(default_spaces(spaces), value)

    return _arrow1258


def ARCtrl_Person__Person_fromISAJsonString_Static_Z721C83C5(s: str) -> Person:
    match_value: FSharpResult_2[Person, str] = Decode_fromString(Person_ISAJson_decoder, s)
    if match_value.tag == 1:
        raise Exception(to_text(printf("Error decoding string: %O"))(match_value.fields[0]))

    else: 
        return match_value.fields[0]



__all__ = ["Person_encoder", "Person_decoder", "Person_ROCrate_genID", "Person_ROCrate_Affiliation_encoder", "Person_ROCrate_Affiliation_decoder", "Person_ROCrate_encoder", "Person_ROCrate_decoder", "Person_ROCrate_encodeAuthorListString", "Person_ROCrate_decodeAuthorListString", "Person_ISAJson_allowedFields", "Person_ISAJson_encoder", "Person_ISAJson_decoder", "ARCtrl_Person__Person_fromJsonString_Static_Z721C83C5", "ARCtrl_Person__Person_toJsonString_Static_71136F3F", "ARCtrl_Person__Person_fromROCrateJsonString_Static_Z721C83C5", "ARCtrl_Person__Person_toROCrateJsonString_Static_71136F3F", "ARCtrl_Person__Person_toISAJsonString_Static_71136F3F", "ARCtrl_Person__Person_fromISAJsonString_Static_Z721C83C5"]

