from django.template import Library, loader
from ..models import Post
from ..models import Portfolio, Category
from taggit.models import Tag
from _data.herobizdental import CATEGORY
from ..forms import SearchForm
from _data import herobizdental


import logging
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(levelname)s: [%(name)s] %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(logging.ERROR)


register = Library()

# https://localcoder.org/django-inclusion-tag-with-configurable-template


template_name = herobizdental.context['template_name']


@register.simple_tag(takes_context=True)
def seo(context):
    t = loader.get_template(template_name + "/seo.html")
    context.update({
        'template_name': template_name,
    })
    logger.info(context)
    return t.render(context.flatten())


@register.simple_tag(takes_context=True)
def header(context):
    t = loader.get_template(template_name + "/header.html")
    context.update({
        'template_name': template_name,
    })
    logger.info(context)
    return t.render(context.flatten())


@register.simple_tag(takes_context=True)
def hero(context):
    t = loader.get_template(template_name + f"/_hero-{context['hero_type']}.html")
    context.update({
        'template_name': template_name,
    })
    logger.info(context)
    return t.render(context.flatten())


@register.simple_tag(takes_context=True)
def featured_services(context):
    t = loader.get_template(template_name + "/_featured-services.html")
    context.update({
        'template_name': template_name,
    })
    logger.info(context)
    return t.render(context.flatten())


@register.simple_tag(takes_context=True)
def about(context):
    t = loader.get_template(template_name + "/_about.html")
    context.update({
        'template_name': template_name,
    })
    logger.info(context)
    return t.render(context.flatten())


@register.simple_tag(takes_context=True)
def clients(context):
    t = loader.get_template(template_name + "/_clients.html")
    context.update({
        'template_name': template_name,
    })
    logger.info(context)
    return t.render(context.flatten())


@register.simple_tag(takes_context=True)
def cta(context):
    t = loader.get_template(template_name + "/_cta.html")
    context.update({
        'template_name': template_name,
    })
    logger.info(context)
    return t.render(context.flatten())


@register.simple_tag(takes_context=True)
def onfocus(context):
    t = loader.get_template(template_name + "/_onfocus.html")
    context.update({
        'template_name': template_name,
    })
    logger.info(context)
    return t.render(context.flatten())


@register.simple_tag(takes_context=True)
def features(context):
    t = loader.get_template(template_name + "/_features.html")
    context.update({
        'template_name': template_name,
    })
    logger.info(context)
    return t.render(context.flatten())


@register.simple_tag(takes_context=True)
def services(context):
    t = loader.get_template(template_name + "/_services.html")
    context.update({
        'template_name': template_name,
    })
    logger.info(context)
    return t.render(context.flatten())


@register.simple_tag(takes_context=True)
def testimonials(context):
    t = loader.get_template(template_name + "/_testimonials.html")
    context.update({
        'template_name': template_name,
    })
    logger.info(context)
    return t.render(context.flatten())


@register.simple_tag(takes_context=True)
def pricing(context):
    t = loader.get_template(template_name + "/_pricing.html")
    context.update({
        'template_name': template_name,
    })
    logger.info(context)
    return t.render(context.flatten())


@register.simple_tag(takes_context=True)
def faq(context):
    t = loader.get_template(template_name + "/_faq.html")
    context.update({
        'template_name': template_name,
    })
    logger.info(context)
    return t.render(context.flatten())


@register.simple_tag(takes_context=True)
def portfolio(context):
    t = loader.get_template(template_name + "/_portfolio.html")
    context.update({
        'template_name': template_name,
        'categories': Category.objects,
        'items': Portfolio.objects,
    })
    logger.info(context)
    return t.render(context.flatten())


@register.simple_tag(takes_context=True)
def team(context):
    t = loader.get_template(template_name + "/_team.html")
    context.update({
        'template_name': template_name,
    })
    logger.info(context)
    return t.render(context.flatten())


@register.simple_tag(takes_context=True)
def recent_blog_posts(context):
    t = loader.get_template(template_name + "/_recent-blog-posts.html")
    objects = Post.objects.filter(status=1).filter(remarkable=True).order_by('-updated_on')
    context.update({
        'template_name': template_name,
        'top3': objects[:3],
    })
    logger.info(context)
    return t.render(context.flatten())


@register.simple_tag(takes_context=True)
def contact(context):
    t = loader.get_template(template_name + "/_contact.html")
    context.update({
        'template_name': template_name,
    })
    logger.info(context)
    return t.render(context.flatten())


@register.simple_tag(takes_context=True)
def sidebar(context):
    t = loader.get_template(template_name + "/_sidebar.html")
    tags = Tag.objects.all()
    category = []
    for category_int, name in CATEGORY:
        category.append([category_int, name, Post.objects.filter(status=1).filter(category=category_int).count()])
    context.update({
        'template_name': template_name,
        'form': SearchForm(),
        'category': category,
        'all_tags': tags,
        'latest': Post.objects.filter(status=1).order_by('-updated_on')[:6],
    })
    logger.info(context)
    return t.render(context.flatten())


@register.simple_tag(takes_context=True)
def footer(context):
    t = loader.get_template(template_name + "/footer.html")
    context.update({
        'template_name': template_name,
        'latest': Post.objects.filter(status=1).order_by('-updated_on')[:5],
    })
    logger.info(context)
    return t.render(context.flatten())