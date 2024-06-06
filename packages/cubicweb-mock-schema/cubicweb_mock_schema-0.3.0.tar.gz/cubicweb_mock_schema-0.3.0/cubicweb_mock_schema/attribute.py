from datetime import time, datetime, date
from yams.buildobjs import (
    EntityType,
    Boolean,
    Int,
    Float,
    String,
    Bytes,
    Time,
    Date,
    Datetime,
    TZDatetime,
)
from yams.constraints import (
    FormatConstraint,
    RegexpConstraint,
    IntervalBoundConstraint,
    BoundaryConstraint,
    SizeConstraint,
    Attribute,
    TODAY,
    NOW,
)
from pytz import UTC


MOON_TIME = time(2, 56, 20)
MOON_DATE = datetime(1969, 7, 21)
MOON_DATETIME = datetime(1969, 7, 21, 2, 56, 20)
MOON_TZDATE = datetime(1969, 7, 21, tzinfo=UTC)
MOON_TZDATETIME = datetime(1969, 7, 21, 2, 56, 20, tzinfo=UTC)


class BooleanConstraintEntity(EntityType):
    default_true = Boolean(default=True)
    default_false = Boolean(default=False)
    required_true = Boolean(required=True)
    required_false = Boolean(required=False)
    description = Boolean(description="This is a description")


class StringConstraintEntity(EntityType):
    default = String(default="default")
    unique_true = String(unique=True)
    required_true = String(required=True)
    required_false = String(required=False)
    description = String(description="This is a description")
    minsize = String(constraints=[SizeConstraint(min=2)])
    maxsize = String(constraints=[SizeConstraint(max=5)])
    boundedsize = String(constraints=[SizeConstraint(min=2, max=5)])
    vocabulary = String(vocabulary=["yes", "no"])
    formatted = String(constraints=[FormatConstraint()])
    regexp_is_int = String(constraints=[RegexpConstraint(r"\d+")])


class BytesConstraintEntity(EntityType):
    required_true = Bytes(required=True)
    required_false = Bytes(required=False)


class IntConstraintEntity(EntityType):
    default_to_1 = Int(default=1)
    unique_true = Int(unique=True)
    required_true = Int(required=True)
    required_false = Int(required=False)
    description = Int(description="This is a description")
    strict_positive = Int(constraints=[BoundaryConstraint(">", boundary=0)])
    positive = Int(constraints=[BoundaryConstraint(">=", boundary=0)])
    strict_negative = Int(
        constraints=[
            BoundaryConstraint("<", boundary=0),
        ]
    )
    negative = Int(constraints=[BoundaryConstraint("<=", boundary=0)])
    compare = Int(constraints=[BoundaryConstraint(">", Attribute("positive"))])
    interval = Int(
        constraints=[IntervalBoundConstraint(minvalue=0, maxvalue=10)]
    )


class FloatConstraintEntity(EntityType):
    default_to_1 = Float(default=1.0)
    unique_true = Float(unique=True)
    required_true = Float(required=True)
    required_false = Float(required=False)
    description = Float(description="This is a description")
    strict_positive = Float(
        constraints=[BoundaryConstraint(">", boundary=0.0)]
    )
    positive = Float(constraints=[BoundaryConstraint(">=", boundary=0.0)])
    strict_negative = Float(
        constraints=[BoundaryConstraint("<", boundary=0.0)]
    )
    negative = Float(constraints=[BoundaryConstraint("<=", boundary=0.0)])
    compare = Float(
        constraints=[BoundaryConstraint(">", Attribute("positive"))]
    )
    interval = Float(
        constraints=[IntervalBoundConstraint(minvalue=0.0, maxvalue=10.0)]
    )


class TimeConstraintEntity(EntityType):
    default_to_first_foot_on_moon = Time(default=MOON_TIME)
    unique_true = Time(unique=True)
    required_true = Time(required=True)
    required_false = Time(required=False)
    description = Time(description="This is a description")
    compare_after_unique_true = Time(
        constraints=[BoundaryConstraint(">", Attribute("unique_true"))]
    )
    after_moon = Time(
        constraints=[BoundaryConstraint(">", boundary=MOON_TIME)]
    )
    since_moon = Time(
        constraints=[BoundaryConstraint(">=", boundary=MOON_TIME)]
    )
    before_moon = Time(
        constraints=[BoundaryConstraint("<", boundary=MOON_TIME)]
    )
    until_moon = Time(
        constraints=[BoundaryConstraint("<=", boundary=MOON_TIME)]
    )
    interval = Time(
        constraints=[
            IntervalBoundConstraint(
                minvalue=time(0, 0, 0),
                maxvalue=time(1, 2, 3),
            )
        ]
    )


class DateConstraintEntity(EntityType):
    default_to_first_foot_on_moon = Date(default=MOON_DATE)
    unique_true = Date(unique=True)
    required_true = Date(required=True)
    required_false = Date(required=False)
    description = Date(description="This is a description")
    after_moon = Date(
        constraints=[BoundaryConstraint(">", boundary=MOON_DATE)]
    )
    since_moon = Date(
        constraints=[BoundaryConstraint(">=", boundary=MOON_DATE)]
    )
    before_moon = Date(
        constraints=[BoundaryConstraint("<", boundary=MOON_DATE)]
    )
    until_moon = Date(
        constraints=[BoundaryConstraint("<=", boundary=MOON_DATE)]
    )
    compare_after_moon = Date(
        constraints=[BoundaryConstraint(">", Attribute("after_moon"))]
    )
    compare_after_today = Date(
        constraints=[BoundaryConstraint(">", TODAY(type="Date"))]
    )
    interval = Date(
        constraints=[
            IntervalBoundConstraint(
                minvalue=date(2000, 1, 1), maxvalue=date(2010, 12, 31)
            )
        ]
    )


class DatetimeConstraintEntity(EntityType):
    default_to_first_foot_on_moon = Datetime(default=MOON_DATETIME)
    unique_true = Datetime(unique=True)
    required_true = Datetime(required=True)
    required_false = Datetime(required=False)
    description = Datetime(description="This is a description")
    after_moon = Datetime(
        constraints=[BoundaryConstraint(">", boundary=MOON_DATETIME)]
    )
    since_moon = Datetime(
        constraints=[BoundaryConstraint(">=", boundary=MOON_DATETIME)]
    )
    before_moon = Datetime(
        constraints=[BoundaryConstraint("<", boundary=MOON_DATETIME)]
    )
    until_moon = Datetime(
        constraints=[BoundaryConstraint("<=", boundary=MOON_DATETIME)]
    )
    compare_after_moon = Datetime(
        constraints=[BoundaryConstraint(">", Attribute("after_moon"))]
    )
    compare_after_today = Datetime(
        constraints=[BoundaryConstraint(">", TODAY(type="Datetime"))]
    )
    compare_after_now = Datetime(
        constraints=[BoundaryConstraint(">", NOW(type="Datetime"))]
    )
    interval = Datetime(
        constraints=[
            IntervalBoundConstraint(
                minvalue=datetime(2000, 1, 1, 0, 0, 0),
                maxvalue=datetime(2010, 12, 31, 0, 0, 0),
            )
        ]
    )


class TZDatetimeConstraintEntity(EntityType):
    default_to_first_foot_on_moon = TZDatetime(default=MOON_TZDATETIME)
    unique_true = TZDatetime(unique=True)
    required_true = TZDatetime(required=True)
    required_false = TZDatetime(required=False)
    description = TZDatetime(description="This is a description")
    after_moon = TZDatetime(
        constraints=[BoundaryConstraint(">", boundary=MOON_TZDATETIME)]
    )
    since_moon = TZDatetime(
        constraints=[BoundaryConstraint(">=", boundary=MOON_TZDATETIME)]
    )
    before_moon = TZDatetime(
        constraints=[BoundaryConstraint("<", boundary=MOON_TZDATETIME)]
    )
    until_moon = TZDatetime(
        constraints=[BoundaryConstraint("<=", boundary=MOON_TZDATETIME)]
    )
    compare_after_moon = TZDatetime(
        constraints=[BoundaryConstraint(">", Attribute("after_moon"))]
    )
    compare_after_today = TZDatetime(
        constraints=[BoundaryConstraint(">", TODAY(type="TZDatetime"))]
    )
    compare_after_now = TZDatetime(
        constraints=[BoundaryConstraint(">", NOW(type="TZDatetime"))]
    )
    interval = TZDatetime(
        constraints=[
            IntervalBoundConstraint(
                minvalue=datetime(2000, 1, 1, 0, 0, 0, tzinfo=UTC),
                maxvalue=datetime(2010, 12, 31, 0, 0, 0, tzinfo=UTC),
            )
        ]
    )
