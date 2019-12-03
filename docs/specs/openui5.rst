.. doctest docs/specs/openui5.rst
.. _specs.openui5:

=====================
The OpenUI5 front-end
=====================

Note: This page is deprecated because the :ref:`openui5` for Lino isn't
currently maintained.


The :mod:`lino_openui5` package defines a front end which
uses the `OpenUI5 <https://openui5.org/>`__ JavaScript UI library and
is meant to fully replace the :mod:`lino.modlib.extjs` front end.

It uses and includes a static version of the `zlib.js
<https://github.com/imaya/zlib.js>`__ library by Imaya Yuta and the
`openui5-ckeditor <https://github.com/jasper07/openui5-ckeditor>`__ by
John Patterson.

The index.html file
===================

.. xfile:: openui5/main.html

The :xfile:`openui5/main.html` is a Jinja template used to generate
the main index file used by Lino applications when they have
:mod:`lino.modlib.openui5` as :attr:`default_ui
<lino.core.site.Site.default_ui>`.

It is rendered by the :class:`lino.modlib.openui5.views.App` view.
See also the SAP documentation `Step 1: Create an HTML Page
<https://help.sap.com/doc/saphelp_nw751abap/7.51.0/de-DE/85/1bde42e4e1410c96abbe402fa9128c/frameset.htm>`__.

The index page loads the `sap-ui-bootstrap` script.  The `src`
parameter says that we currently use the latest OpenUI5 core
(`resources/sap-ui-core.js`) from
https://openui5nightly.hana.ondemand.com which is okay as long as we
don't use it on a production site.

The `data-sap-ui-resourceroots` parameter specifies rules for
resolving namespaces.

The index file defines an empty `<body id="content"
class="sapUiBody">` tag which will be populated by the init function.

The file defines an inline `<script>` which registers an init function
(using :func:`sap.ui.getCore().attachInit`) to be executed once when
the bootstrap is done.

The init function does only one thing: it calls :func:`sap.ui.require`
which basically instantiates a `app.m.Shell` control and places it to
the body.

The `app` of that Shell control is a `sap.ui.core.ComponentContainer`

.. currentmodule:: lino.modlib.openui5

Examples in this document use the :mod:`lino_openui5.projects.teamUi5` demo
project.

>>> import lino
>>> lino.startup('lino_openui5.projects.teamUi5.settings.demo')
>>> from lino.api.doctest import *

Define a utility function:

>>> def soupyfiy(url, Print=False):
...     r = test_client.get(url)
...     soup = BeautifulSoup(r.content, "lxml")
...     soup.body.hidden=True
...     if Print:
...         pSoup(soup)
...     return r,soup
>>> def pSoup(soup):
...     print(soup.body.prettify(formatter=None))
>>> test_client.force_login(rt.login('robin').user)

The following test is currently skipped

>>> r,s = soupyfiy("http://127.0.0.1:8000/ui/view/grid/tickets/AllTickets.view.xml", Print=True)
... #doctest: -ELLIPSIS -REPORT_UDIFF +SKIP
     <mvc:view class="sapUiSizeCompact" controllername="lino.controller.table" height="100%" xmlns="sap.m" xmlns:core="sap.ui.core" xmlns:customdata="http://schemas.sap.com/sapui5/extension/sap.ui.core.CustomData/1" xmlns:editor="openui5" xmlns:html="http://www.w3.org/1999/xhtml" xmlns:m="sap.m" xmlns:mvc="sap.ui.core.mvc" xmlns:table="sap.ui.table" xmlns:tnt="sap.tnt" xmlns:u="sap.ui.unified" xmlns:ui="sap.ui">
      <page class="sapUiContentPadding" enablescrolling="true" navbuttonpress="onNavBack" showfooter="true" showheader="true" shownavbutton="true">
       <content>
        <table:table arialabelledby="title" cellcontextmenu="onProductIdCellContextMenu" class="sapUiSizeCondensed" columnselect="onColumnSelect" customdata:actor_id="tickets.AllTickets" customdata:pk="0" customdata:url="/restful/tickets/AllTickets" enablecellfilter="{ui>/enableCellFilter}" enablecolumnfreeze="{ui>/showFreezeMenuEntry}" id="MAIN_TABLE" rowactioncount="1" rows="{/rows}" selectionmode="MultiToggle" showcolumnvisibilitymenu="true" visiblerowcountmode="Auto">
         <table:rowactiontemplate>
          <table:rowaction visible="true">
           <table:items>
            <table:rowactionitem press="onRowNavPress" type="Navigation" visible="true">
            </table:rowactionitem>
           </table:items>
          </table:rowaction>
         </table:rowactiontemplate>
         <table:extension>
          <toolbar>
           <title text="All tickets">
           </title>
           <button press="onPressAction" text="HTML">
            <customdata>
             <core:customdata key="action_name" value="HTML">
             </core:customdata>
            </customdata>
           </button>
           <button press="onPressAction" text="Table (landscape)">
            <customdata>
             <core:customdata key="action_name" value="Table (landscape)">
             </core:customdata>
            </customdata>
           </button>
           <button press="onPressAction" text="Table (portrait)">
            <customdata>
             <core:customdata key="action_name" value="Table (portrait)">
             </core:customdata>
            </customdata>
           </button>
           <button press="onPressAction" text="Export to .xls">
            <customdata>
             <core:customdata key="action_name" value="Export to .xls">
             </core:customdata>
            </customdata>
           </button>
           <button press="onPressAction" text="New">
            <customdata>
             <core:customdata key="action_name" value="New">
             </core:customdata>
            </customdata>
           </button>
           <button press="onPressAction" text="Detail">
            <customdata>
             <core:customdata key="action_name" value="Detail">
             </core:customdata>
            </customdata>
           </button>
           <button press="onPressAction" text="Delete">
            <customdata>
             <core:customdata key="action_name" value="Delete">
             </core:customdata>
            </customdata>
           </button>
           <button press="onPressAction" text="Merge">
            <customdata>
             <core:customdata key="action_name" value="Merge">
             </core:customdata>
            </customdata>
           </button>
           <button press="onPressAction" text="Changes">
            <customdata>
             <core:customdata key="action_name" value="Changes">
             </core:customdata>
            </customdata>
           </button>
           <button press="onPressAction" text="Commits">
            <customdata>
             <core:customdata key="action_name" value="Commits">
             </core:customdata>
            </customdata>
           </button>
           <button press="onPressAction" text="Check data">
            <customdata>
             <core:customdata key="action_name" value="Check data">
             </core:customdata>
            </customdata>
           </button>
           <button press="onPressAction" text="Fix data problems">
            <customdata>
             <core:customdata key="action_name" value="Fix data problems">
             </core:customdata>
            </customdata>
           </button>
           <toolbarspacer>
           </toolbarspacer>
           <button icon="sap-icon://close-command-field" press="onFirstPress" tooltip="First page">
           </button>
           <button icon="sap-icon://navigation-left-arrow" press="onPrevPress" tooltip="Previous page">
           </button>
           <input align="center" fieldwidth="60%" livechange="onPagerInputChange" value="{meta>/page}" width="4ch"/>
           <label text="of {meta>/page_total}">
           </label>
           <button icon="sap-icon://navigation-right-arrow" press="onNextPress" tooltip="Next page">
           </button>
           <button icon="sap-icon://open-command-field" press="onLastPress" tooltip="Last page">
           </button>
           <toolbarspacer>
           </toolbarspacer>
           <searchfield id="searchField" search="onSearch" tooltip="{i18n>worklistSearchTooltip}" width="auto">
           </searchfield>
           <togglebutton icon="sap-icon://resize-horizontal" pressed="{ui>/showFreezeMenuEntry}" tooltip="Enable / Disable Freezing Menu Entries">
           </togglebutton>
           <togglebutton icon="sap-icon://grid" pressed="{ui>/enableCellFilter}" tooltip="Enable / Disable Cell Filter">
           </togglebutton>
          </toolbar>
         </table:extension>
         <table:columns press="onPress">
          <table:column showsortmenuentry="true" sortproperty="id" visible="true">
           <label text="ID">
           </label>
           <table:template>
            <m:text text="{0}" wrapping="false">
            </m:text>
           </table:template>
          </table:column>
          <table:column showsortmenuentry="true" sortproperty="summary" visible="true" width="50ch">
           <label text="Summary">
           </label>
           <table:template>
            <m:text text="{1}" wrapping="false">
            </m:text>
           </table:template>
          </table:column>
          <table:column visible="true">
           <label text="Priority">
           </label>
           <table:template>
            <m:text text="{2}" wrapping="false">
            </m:text>
           </table:template>
          </table:column>
          <table:column visible="true" width="30ch">
           <label text="Workflow">
           </label>
           <table:template>
            <core:html content="<span>{4}</span>" wrapping="false" xmlns="sap.ui.core">
            </core:html>
           </table:template>
          </table:column>
          <table:column visible="true" width="10ch">
           <label text="Site">
           </label>
           <table:template>
            <m:text text="{5}" wrapping="false">
            </m:text>
           </table:template>
          </table:column>
         </table:columns>
         <table:footer>
          <toolbar>
           <toolbarspacer>
           </toolbarspacer>
           <button icon="sap-icon://hint" press="showInfo" tooltip="Show information">
           </button>
          </toolbar>
         </table:footer>
        </table:table>
       </content>
      </page>
     </mvc:view>
