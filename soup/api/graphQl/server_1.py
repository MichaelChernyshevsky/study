import graphene

class User(graphene.ObjectType):
    id = graphene.ID()
    userName = graphene.String()


class Query(graphene.ObjectType):
    get_user =  graphene.Field(User)
    
    @staticmethod
    def resolve_get_user(root,indo):
        new_user = User()
        new_user.id = 0
        new_user.userName = "someName"
        return new_user


schema =  graphene.Schema(query=Query)
results = schema.execute("""
    query{
        getUser{
            userName
        }
    }
    """)
print(results.data)