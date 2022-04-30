import graphene
from graphene_django import DjangoObjectType
from graphene_file_upload.scalars import Upload
from compare.utils import are_similar
from graphene_django.rest_framework.mutation import SerializerMutation

from caches.models import Session, Cache, Clue

class SessionType(DjangoObjectType):
    class Meta:
        model = Session
        fields = ("id", "name", "date")

class CacheType(DjangoObjectType):
    class Meta:
        model = Cache
        fields = ("id", "session", "image", "name", "acomplished")

class ClueType(DjangoObjectType):
    class Meta:
        model = Clue
        fields = ("id", "cache", "clue") 

class SessionProgress(graphene.ObjectType):
    cache = graphene.Field(lambda : CacheType)
    current_index = graphene.Float()
    session_length = graphene.Float()

class Submmit(SerializerMutation):
    class Meta:
        serializer_class = MySerializer
    
    def mutate(root, info, id, cache, image):
        chache = Cache.objects.get(pk=id)
        if are_similar(image, cache.image):
            cache.acomplished = True
            cache.save()
    

class Query(graphene.ObjectType):
    all_sessions = graphene.List(SessionType)
    all_cahces = graphene.List(CacheType)
    all_clues = graphene.List(ClueType)
    session_by_id = graphene.Field(SessionType, id=graphene.Int(required=True))
    caches_by_id = graphene.Field(CacheType, id=graphene.Int(required=True))
    next_cache_by_session_id = graphene.Field(SessionProgress, id=graphene.Int(required=True))
    clues_by_id = graphene.Field(ClueType, id=graphene.Int(required=True))

    def resolve_all_sessions(root, info):
        return Session.objects.all()       

    def resolve_all_caches(root, info):
        return Cache.objects.all()    

    def resolve_all_clues(root, info):
        return Clue.objects.all()                                                                                        

    def resolve_session_by_id(root, info, id):
        try:
            return Session.objects.get(pk=id)
        except Session.DoesNotExist:
            return None

    def resolve_caches_by_id(root, info, id):
        try:
            return Cache.objects.get(pk=id)
        except Cache.DoesNotExist:
            return None

    def resolve_clues_by_id(root, info, id):
        try:
            return Clue.objects.get(id=id)
        except Clue.DoesNotExist:
            return None

    def resolve_next_cache_by_session_id(root, info, id):
        try:
            caches = Cache.objects.filter(session=id)
            currentIndex = len([cache for cache in caches if cache.acomplished])
            return SessionProgress(cache = caches[currentIndex], current_index = currentIndex, session_length=len(caches))
        except Clue.DoesNotExist:
            return None 

class CreateSession(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        date = graphene.Date()
    
    session = graphene.Field(lambda : SessionType)

    def mutate(root, info, name, date):
        session = Session(name=name, date=date)
        session.save()
        return CreateSession(session)

class UpdateSession(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        date = graphene.Date()
    
    session = graphene.Field(lambda : SessionType)

    def mutate(root, info, id, name, date):
        session = Session.objects.get(pk=id)
        session.name = name
        session.date = date
        session.save()
        return UpdateSession(session)

class DeleteSession(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    
    session = graphene.Field(lambda : SessionType)

    def mutate(root, info, id):
        session = Session.objects.get(pk=id)
        session.delete()
        return DeleteSession(session)

class CreateCache(graphene.Mutation):
    class Arguments:
        session_id = graphene.Int()
        name = graphene.String()
    
    session = graphene.Field(lambda : SessionType)
    cache = graphene.Field(lambda : CacheType)

    def mutate(root, info, session_id, date):
        session = Session.objects.get(pk=session_id)
        cache = Cache(session=session, name=name, acomplished=False)
        cache.save()
        return CreateCache(session)

class UpdateCache(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        acomplished = graphene.Boolean()
    
    cache = graphene.Field(lambda : CacheType)

    def mutate(root, info, id, name, acomplished):
        cache = Cache.objects.get(pk=id)
        cache.name = name
        cache.acomplished = acomplished
        cache.save()
        return UpdateCache(session)

class DeleteCache(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    
    cache = graphene.Field(lambda : CacheType)

    def mutate(root, info, id, name, acomplished):
        cache = Cache.objects.get(pk=id)
        cache.delete()
        return DeleteCache(session)

class CreateClue(graphene.Mutation):
    class Arguments:
        cache_id = graphene.Int()
        clue = graphene.String()
    
    cache = graphene.Field(lambda : CacheType)
    clue = graphene.Field(lambda : ClueType)

    def mutate(root, info, cache_id, clue):
        cache = Cache.objects.get(pk=cache_id)
        clue = Clue(cache=cache, clue=clue)
        clue.save()
        return CreateClue(session)

class UpdateClue(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        clue = graphene.String()
    
    clue = graphene.Field(lambda : ClueType)

    def mutate(root, info, id, clue):
        clue = Clue.objects.get(pk=id)
        clue.clue = clue
        clue.save()
        return UpdateClue(session)

class DeleteClue(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    
    clue = graphene.Field(lambda : ClueType)

    def mutate(root, info, id):
        clue = Clue.objects.get(pk=id)
        clue.delete()
        return DeleteClue(session)

class UploadMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        file = Upload(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id, file, **kwargs):
        #Do something with the file
        success = True
        return Verfy(cache_id = id, cerify = success )

class Mutations(graphene.ObjectType):
    create_session = CreateSession().Field()
    create_cache = CreateCache().Field()
    create_clue = CreateClue().Field()
    update_session = UpdateSession().Field()
    update_cache = UpdateCache().Field()
    update_clue = UpdateClue().Field()
    delete_session = DeleteSession().Field()
    delete_cache = DeleteCache().Field()
    delete_clue = DeleteClue().Field()

schema = graphene.Schema(query=Query, mutation=Mutations)