from marshmallow import Schema, fields, validate

from ebb_events.enums import EventType


TOPIC_MAX_LENGTH = 50
TOPIC_REGEX = r"^[a-z0-9-]+$"
SOURCE_REGEX = r"^([a-z0-9-]+\/){4}[a-z0-9-]+$"
SOURCE_MAX_LENGTH = 256


def remove_nones_helper(data):
    """
    Recursive helper returns the parameter dictionary with None key:values removed
    from top level and all nested dictionaries
    """
    if isinstance(data, dict):
        return {
            key: remove_nones_helper(value)
            for key, value in data.items()
            if value is not None and remove_nones_helper(value) is not None
        }
    return data


class EventEnvelopeSchema(Schema):
    """Schema for EventEnvelope class to validate fields follow requirements"""

    organization = fields.Str(
        validate=[
            validate.Length(max=TOPIC_MAX_LENGTH),
            validate.Regexp(regex=TOPIC_REGEX),
        ]
    )
    system_id = fields.Str(
        validate=[
            validate.Length(max=TOPIC_MAX_LENGTH),
            validate.Regexp(regex=TOPIC_REGEX),
        ]
    )
    subsystem_id = fields.Str(
        validate=[
            validate.Length(max=TOPIC_MAX_LENGTH),
            validate.Regexp(regex=TOPIC_REGEX),
        ]
    )
    device_id = fields.Str(
        validate=[
            validate.Length(max=TOPIC_MAX_LENGTH),
            validate.Regexp(regex=TOPIC_REGEX),
        ]
    )


class RawToStringField(fields.Raw):
    """
    Class for our EventPayloadSchema id field to accept any id but returns
    that id as a string value e.g. (str(id))
    """

    def _serialize(self, value, attr, obj, **kwargs):
        return str(value)


class DictConditionallyRemoveNone(fields.Dict):
    """
    Class for EventPayloadSchema data field to conditionally
    remove None fields
    """

    def _serialize(self, value, attr, obj, **kwargs):
        remove_nones = self.context.get("remove_nones", False)
        if remove_nones:
            # Filter out None values from the dictionary for top and second levels
            filtered_dict = remove_nones_helper(value)
            return filtered_dict
        else:
            return value


class EventPayloadSchema(Schema):
    """Schema for event payload json to validate fields follow requirements"""

    # id field could be uuid but doesn't have to be (could be string(int))
    id = RawToStringField(required=True)
    time = fields.DateTime(required=True, format="iso")
    source = fields.Str(
        required=True,
        validate=[
            validate.Length(max=SOURCE_MAX_LENGTH),
            validate.Regexp(regex=SOURCE_REGEX),
        ],
    )
    type = fields.Str(
        required=True,
        validate=[
            validate.OneOf([e.value for e in EventType]),
        ],
    )
    data = DictConditionallyRemoveNone(required=True)


class DataSchema(Schema):
    """Schema for event data entries to check expected structure"""

    value = fields.Float(required=True)
    units = fields.Str(required=False, allow_none=True)
