# -*- coding: utf-8 -*-

import martian
import zope.component
import grokcore.component
from infrae.layout import ILayout, Layout, layout
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from grokcore.view.meta.views import TemplateGrokker


class LayoutTemplateGrokker(TemplateGrokker):
    martian.component(Layout)

    def has_render(self, factory):
        render = getattr(factory, 'render', None)
        base_method = getattr(render, 'base_method', False)
        return render and not base_method

    def has_no_render(self, factory):
        render = getattr(factory, 'render', None)
        base_method = getattr(render, 'base_method', False)
        return render is None or base_method


class LayoutGrokker(martian.ClassGrokker):
    martian.component(Layout)
    martian.directive(grokcore.component.context)
    martian.directive(grokcore.view.layer, default=IDefaultBrowserLayer)
    martian.directive(layout, default=ILayout)

    def grok(self, name, factory, module_info, **kw):
        factory.module_info = module_info
        return super(LayoutGrokker, self).grok(name, factory, module_info, **kw)

    def execute(self, factory, config, context, layer, layout, **kw):
        adapts = (layer, context)
        config.action(
            discriminator=('adapter', adapts, layout),
            callable=zope.component.provideAdapter,
            args=(factory, adapts, layout))
        return True
