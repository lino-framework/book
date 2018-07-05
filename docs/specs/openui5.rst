.. _book.specs.openui5:

===================
Openui5 specs tests
===================

.. to test only this document:
   
    $ doctest docs/specs/openui5.rst 
   
    doctest init:
    >>> import lino
    >>> lino.startup('lino_book.projects.ui5.settings.demo')
    >>> from lino.api.doctest import *

The :mod:`lino.modlib.openui5` plugin defines the openui5 front-end

.. currentmodule:: lino.modlib.openui5

>>> def soupyfiy(url):
...     r = test_client.get(url)
...     soup = BeautifulSoup(r.content, "lxml")
...     soup.body.hidden=True
...     return r,soup
>>> def pSoup(soup):
...     print(soup.body.prettify(formatter=None))
>>> test_client.force_login(rt.login('robin').user)
>>> r,s = soupyfiy("http://127.0.0.1:8000/ui/view/grid/tickets/AllTickets.view.xml")
>>> pSoup(s)
... #doctest: -ELLIPSIS -REPORT_UDIFF
 <mvc:view class="sapUiSizeCompact" controllername="lino.controller.table" height="100%" xmlns="sap.m" xmlns:core="sap.ui.core" xmlns:customdata="http://schemas.sap.com/sapui5/extension/sap.ui.core.CustomData/1" xmlns:editor="openui5" xmlns:html="http://www.w3.org/1999/xhtml" xmlns:m="sap.m" xmlns:mvc="sap.ui.core.mvc" xmlns:table="sap.ui.table" xmlns:tnt="sap.tnt" xmlns:u="sap.ui.unified" xmlns:ui="sap.ui">
  <table:table arialabelledby="title" cellcontextmenu="onProductIdCellContextMenu" class="sapUiSizeCondensed" columnselect="onColumnSelect" customdata:actor_id="tickets.AllTickets" customdata:content_type="44" customdata:is_slave="true" customdata:pk="0" customdata:url="/restful/tickets/AllTickets" enablecellfilter="{ui>/enableCellFilter}" enablecolumnfreeze="{ui>/showFreezeMenuEntry}" id="MAIN_TABLE" rowactioncount="1" rows="{/rows}" selectionmode="MultiToggle" showcolumnvisibilitymenu="true" visiblerowcountmode="Auto" xmlns:m="sap.m">
   <table:rowactiontemplate>
    <table:rowaction visible="true">
     <table:items>
      <table:rowactionitem press="onNavBack" type="Navigation" visible="true">
      </table:rowactionitem>
     </table:items>
    </table:rowaction>
   </table:rowactiontemplate>
   <table:extension>
    <m:toolbar>
     <m:title text="All tickets">
     </m:title>
     <m:toolbarspacer>
     </m:toolbarspacer>
     <m:togglebutton icon="sap-icon://resize-horizontal" pressed="{ui>/showFreezeMenuEntry}" tooltip="Enable / Disable Freezing Menu Entries">
     </m:togglebutton>
     <m:togglebutton icon="sap-icon://grid" pressed="{ui>/enableCellFilter}" tooltip="Enable / Disable Cell Filter">
     </m:togglebutton>
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
    </m:toolbar>
   </table:extension>
   <table:columns>
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
    <m:toolbar>
     <m:toolbarspacer>
     </m:toolbarspacer>
     <m:button icon="sap-icon://hint" press="showInfo" tooltip="Show information">
     </m:button>
    </m:toolbar>
   </table:footer>
  </table:table>
 </mvc:view>
