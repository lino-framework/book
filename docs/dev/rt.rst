====================================
The ``lino.api.rt`` module (runtime)
====================================

See also :mod:`lino.api`.


.. module:: lino.api.rt

.. data:: models

    Shortcut to :attr:`lino.core.site.Site.models`

.. data:: actors

    Deprecated alias for :attr:`models`

.. data:: modules

    Deprecated alias for :attr:`models`

.. function:: get_template(*args, **kw)
              
    Shortcut to :meth:`get_template` on the global `jinja2.Environment`
    (:attr:`jinja_env <lino.core.site.Site.jinja_env>`, see
    :mod:`lino.core.web`).

.. function:: show(*args, **kw)
              
    Calls :meth:`show <lino.core.requests.BaseRequest.show>` on a
    temporary anonymous session (created using
    :meth:`rt.login <lino.core.site.Site.login>`).

