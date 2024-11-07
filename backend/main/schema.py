import graphene
from graphene_django.types import DjangoObjectType
from .models import Blog, Contact, Quotation
from django.conf import settings

class BlogPostType(DjangoObjectType):
    image_url = graphene.String()

    class Meta:
        model = Blog
        fields = ("id", "title", "author", "content", "created_at", "updated_at", "published_at", "image")

    def resolve_image_url(self, info):
        if self.image:
            return f"{settings.MEDIA_URL}{self.image.name}"
        return None


class Query(graphene.ObjectType):
    all_blog_posts = graphene.List(BlogPostType)
    blog_post = graphene.Field(BlogPostType, id=graphene.Int(), slug=graphene.String())

    def resolve_all_blog_posts(root, info):
        # Récupère tous les posts de blog publiés
        return Blog.objects.all()

    def resolve_blog_post(root, info, id=None, slug=None):
        # Récupère les détails d'un post par ID ou par slug
        if id is not None:
            return Blog.objects.get(pk=id)
        if slug is not None:
            return Blog.objects.get(slug=slug)
        return None


class ContactType(DjangoObjectType):
    class Meta:
        model = Contact
        fields = ("id", "full_name", "email", "message", "created_at")

class QuotationType(DjangoObjectType):
    class Meta:
        model = Quotation
        fields = ("id", "full_name", "email", "phone", "address", "contract_type", "estimated_consumption", "message", "created_at")



class CreateContact(graphene.Mutation):
    contact = graphene.Field(ContactType)

    class Arguments:
        full_name = graphene.String(required=True)
        email = graphene.String(required=True)
        message = graphene.String(required=True)

    def mutate(self, info, full_name, email,message):
        contact = Contact(
            full_name=full_name,
            email=email,
            message=message,
        )
        contact.save()
        return CreateContact(contact=contact)

class CreateQuotation(graphene.Mutation):
    quotation = graphene.Field(QuotationType)

    class Arguments:
        full_name = graphene.String(required=True)
        email = graphene.String(required=True)
        phone = graphene.String(required=True)
        address = graphene.String(required=True)
        contract_type = graphene.String(required=True)
        estimated_consumption = graphene.Int(required=True)
        message = graphene.String(required=True)

    def mutate(self, info, full_name, email, phone, address, contract_type, estimated_consumption, message):
        quotation = Quotation(
            full_name=full_name,
            email=email,
            phone=phone,
            address=address,
            contract_type=contract_type,
            estimated_consumption=estimated_consumption,
            message=message,
        )
        quotation.save()
        return CreateQuotation(quotation=quotation)



class Mutation(graphene.ObjectType):
    create_contact = CreateContact.Field()
    create_quotation = CreateQuotation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
