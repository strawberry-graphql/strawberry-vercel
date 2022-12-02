from typing import Optional
import strawberry


@strawberry.type
class Query:
    @strawberry.field
    def hello_world(self, name: Optional[str] = None) -> str:
        return f"Hello {name or 'World'}"


schema = strawberry.Schema(Query)
