from yams.buildobjs import (
    EntityType,
    String,
    RichString,
    SubjectRelation,
)


class Blog(EntityType):
    title = String(maxsize=50, required=True)
    description = RichString()
    rss_url = String(
        maxsize=128,
        description=(
            "blog's RSS url "
            "(useful for when using external site such as feedburner)"
        ),
    )


class BlogEntry(EntityType):
    __permissions__ = {
        "read": (
            "managers",
            "users",
        ),
        "add": ("managers", "users"),
        "update": ("managers", "owners"),
        "delete": ("managers", "owners"),
    }
    title = String(required=True, fulltextindexed=True, maxsize=256)
    content = RichString(required=True, fulltextindexed=True)
    entry_of = SubjectRelation("Blog")
    creator = SubjectRelation("UserAccount")


class UserAccount(EntityType):
    name = String(required=True)
    avatar = String()
