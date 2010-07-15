=============
infrae.layout
=============

``infrae.layout`` defines a way to write view that can reuse an
existing defined layout in Zope 2. It is similar to `megrok.layout`_,
and work the same way, with some additions.


API
===

You can define a *Layout* that are after used by a *Page*. A *Page* is
basically a view and behave the same way. But before rendering it
self, it look for a *Layout* to include its content in it.

A *Layout* is found by adapting the request and the content you are
on: you can register layouts for your skin, and after for a specific
content.

If this is not sufficient, a page can use the Grok directive
``layout`` to directly specify its type of Layout to use. While
defining your layout, you can use the same directive to declare this
layout belongs to this type::


  from infae.layout import layout, Layout, ILayout, Page
  from five import grok

  from corp.skin import ICorpSkin

  grok.skin(ICorpSkin)


  class ViewLayout(Layout):

     def render(self):
         return u'View %s' % self.view.content()

  class Index(Page):

     def render(self):
         return self.context.title()


And now if on the same content you want an edition layout for instance::

   class IEditionLayout(ILayout)
       """Layout to edit content
       """

   class EditionLayout(Layout):
       layout(IEditionLayout)

       def render(self):
           return u'Edit %s' % self.view.content()

   class Edit(Page):
      layout(IEditionLayout)

      def render(self):
           return self.context.title()


If that modularity is not enough for your application, you can write
an adapter on the request and your content that provides
``ILayoutFactory``, where you can yourself select the layout you want,
with the criteria you wish.


.. _megrok.layout: http://pypi.python.org/pypi/megrok.layout
