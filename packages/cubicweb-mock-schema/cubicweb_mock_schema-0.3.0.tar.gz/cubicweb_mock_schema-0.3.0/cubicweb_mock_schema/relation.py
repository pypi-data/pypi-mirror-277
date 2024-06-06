from yams.buildobjs import EntityType, SubjectRelation, String


class TestSubject(EntityType):
    name = String()

    relation_one_one = SubjectRelation("TestObject", cardinality="11")
    relation_question_one = SubjectRelation("TestObject", cardinality="?1")
    relation_plus_one = SubjectRelation("TestObject", cardinality="+1")
    relation_star_one = SubjectRelation("TestObject", cardinality="*1")

    relation_one_question = SubjectRelation("TestObject", cardinality="1?")
    relation_question_question = SubjectRelation(
        "TestObject", cardinality="??"
    )
    relation_plus_question = SubjectRelation("TestObject", cardinality="+?")
    relation_star_question = SubjectRelation("TestObject", cardinality="*?")

    relation_one_plus = SubjectRelation("TestObject", cardinality="1+")
    relation_question_plus = SubjectRelation("TestObject", cardinality="?+")
    relation_plus_plus = SubjectRelation("TestObject", cardinality="++")
    relation_star_plus = SubjectRelation("TestObject", cardinality="*+")

    relation_one_star = SubjectRelation("TestObject", cardinality="1*")
    relation_question_star = SubjectRelation("TestObject", cardinality="?*")
    relation_plus_star = SubjectRelation("TestObject", cardinality="+*")
    relation_star_star = SubjectRelation("TestObject", cardinality="**")

    relation_one_one_composite = SubjectRelation(
        "TestObject", cardinality="11", composite="object"
    )
    relation_one_one_two_objects = SubjectRelation(
        ("TestObject", "OtherTestObject"), cardinality="11"
    )
    relation_star_star_two_objects = SubjectRelation(
        ("TestObject", "OtherTestObject"), cardinality="**"
    )


class TestObject(EntityType):
    name = String()


class OtherTestObject(EntityType):
    name = String()
