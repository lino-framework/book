/*
 Copyright 2009-2015 Luc Saffre
 License: BSD (see file COPYING for details)
*/

// lino.js --- generated Mon May 16 03:07:18 2016 by Lino Belref 0.1 for Anonyme.
Ext.BLANK_IMAGE_URL = '/static/ext-3.3.1/resources/images/default/s.gif';
LANGUAGE_CHOICES = [ [ "fr", "Fran\u00e7ais" ], [ "nl", "Hollandais" ], [ "de", "Allemand" ] ];
MEDIA_URL = "/media/";

// hack to add a toCamel function, inspired by
// http://jamesroberts.name/blog/2010/02/22/string-functions-for-javascript-trim-to-camel-case-to-dashed-and-to-underscore/
String.prototype.toCamel = function(){
  //~ return this.replace(/(\-[a-z])/g, function($1){return $1.toUpperCase().replace('-','');});
  //~ return this;
  return this.replace(/([A-Z])([A-Z]+)/g, function(match,p1,p2,offset,string){
      //~ console.log("20131005 got ",arguments);
      return p1 + p2.toLowerCase();});
};


// 20151126 hack to modify Ext.EventObjectImpl.isSpecialKey() which
// returned false for Ctrl-S when called from a keyup handler (namely
// ComboBox.onLoad)

Ext.EventObjectImpl.prototype.isSpecialKey = function(){
    // same as original except for one line
    var k = this.normalizeKey(this.keyCode);
    // return (this.type == 'keypress' && this.ctrlKey) ||
    return (this.ctrlKey) ||
        this.isNavKeyPress() ||
        (k == this.BACKSPACE) || 
        (k >= 16 && k <= 20) || 
        (k >= 44 && k <= 46);   
};





/* MonthPickerPlugin: thanks to keypoint @ sencha forum
   http://www.sencha.com/forum/showthread.php?74002-3.x-Ext.ux.MonthMenu&p=356860#post356860
*/
Ext.namespace('Ext.ux'); 

Ext.ux.MonthPickerPlugin = function() { 
    var picker; 
    var oldDateDefaults; 

    this.init = function(pk) { 
        picker = pk; 
        picker.onTriggerClick = picker.onTriggerClick.createSequence(onClick); 
        picker.getValue = picker.getValue.createInterceptor(setDefaultMonthDay).createSequence(restoreDefaultMonthDay); 
        picker.beforeBlur = picker.beforeBlur.createInterceptor(setDefaultMonthDay).createSequence(restoreDefaultMonthDay); 
    }; 

    function setDefaultMonthDay() { 
        oldDateDefaults = Date.defaults.d; 
        Date.defaults.d = 1; 
        return true; 
    } 

    function restoreDefaultMonthDay(ret) { 
        Date.defaults.d = oldDateDefaults; 
        return ret; 
    } 

    function onClick(e, el, opt) { 
        var p = picker.menu.picker; 
        p.activeDate = p.activeDate.getFirstDateOfMonth(); 
        if (p.value) { 
            p.value = p.value.getFirstDateOfMonth(); 
        } 

        p.showMonthPicker(); 
         
        if (!p.disabled) { 
            p.monthPicker.stopFx(); 
            p.monthPicker.show(); 

            p.mun(p.monthPicker, 'click', p.onMonthClick, p); 
            p.mun(p.monthPicker, 'dblclick', p.onMonthDblClick, p); 
            p.onMonthClick = p.onMonthClick.createSequence(pickerClick); 
            p.onMonthDblClick = p.onMonthDblClick.createSequence(pickerDblclick); 
            p.mon(p.monthPicker, 'click', p.onMonthClick, p); 
            p.mon(p.monthPicker, 'dblclick', p.onMonthDblClick, p); 
        } 
    } 

    function pickerClick(e, t) { 
        var el = new Ext.Element(t); 
        if (el.is('button.x-date-mp-cancel')) { 
            picker.menu.hide(); 
        } else if(el.is('button.x-date-mp-ok')) { 
            var p = picker.menu.picker; 
            p.setValue(p.activeDate); 
            p.fireEvent('select', p, p.value); 
        } 
    } 

    function pickerDblclick(e, t) { 
        var el = new Ext.Element(t); 
        if (el.parent() 
            && (el.parent().is('td.x-date-mp-month') 
            || el.parent().is('td.x-date-mp-year'))) { 

            var p = picker.menu.picker; 
            p.setValue(p.activeDate); 
            p.fireEvent('select', p, p.value); 
        } 
    } 
}; 

Ext.preg('monthPickerPlugin', Ext.ux.MonthPickerPlugin);  


/**
JC Watsons solution (adapted to ExtJS 3.3.1 by LS) is elegant and simple:
`A "fix" for unchecked checkbox submission  behaviour
<http://www.sencha.com/forum/showthread.php?28449>`_

Added special handling for checkbox inputs. 
ExtJS defines disabled checkboxes `readonly`, not `disabled` as for other inputs.

*/
Ext.lib.Ajax.serializeForm = function(form) {
    //~ console.log('20120203 linolib.js serializeForm',form);
    var fElements = form.elements || (document.forms[form] || Ext.getDom(form)).elements, 
        hasSubmit = false, 
        encoder = encodeURIComponent, 
        name, 
        data = '', 
        type, 
        hasValue;

    Ext.each(fElements, function(element){
        name = element.name;
        type = element.type;

        if (!element.disabled && name && !(type == 'checkbox' && element.readonly)) {
            if (/select-(one|multiple)/i.test(type)) {
                Ext.each(element.options, function(opt){
                    if (opt.selected) {
                        hasValue = opt.hasAttribute ? opt.hasAttribute('value') : opt.getAttributeNode('value').specified;
                        data += String.format("{0}={1}&", encoder(name), encoder(hasValue ? opt.value : opt.text));
                    }
                });
            } else if (!(/file|undefined|reset|button/i.test(type))) {
                //~ if (!(/radio|checkbox/i.test(type) && !element.checked) && !(type == 'submit' && hasSubmit)) {
                if (!(type == 'submit' && hasSubmit)) {
                    if (type == 'checkbox') {
                        //~ console.log('20111001',element,'data += ',encoder(name) + '=' + (element.checked ? 'on' : 'off') + '&');
                        data += encoder(name) + '=' + (element.checked ? 'on' : 'off') + '&';
                    } else {
                        //~ console.log('20111001',element,'data += ',encoder(name) + '=' + encoder(element.value) + '&');
                        data += encoder(name) + '=' + encoder(element.value) + '&';
                    }
                    hasSubmit = /submit/i.test(type);
                }
            }
        //~ } else {
            //~ console.log(name,type,element.readonly);
        }
    });
    return data.substr(0, data.length - 1);
};



/*
Set a long timeout of fifteen minutes. 
See /blog/2012/0307
*/
Ext.Ajax.timeout = 15 * 60 * 1000; 

/*
 * Thanks to 
 * `huuze <http://stackoverflow.com/users/10040/huuuze>`_ for the question
 * and to 
 * `chrisv <http://stackoverflow.com/users/683808/chrisv>`_
 * for the answer on
 * http://stackoverflow.com/questions/3764589/how-do-i-include-django-1-2s-csrf-token-in-a-javascript-generated-html-form/5485616#5485616
 * 
 * */
 
Ext.Ajax.on('beforerequest', function (conn, options) {
   if (!(/^http:.*/.test(options.url) || /^https:.*/.test(options.url))) {
     if (typeof(options.headers) == "undefined") {
       options.headers = {'X-CSRFToken': Ext.util.Cookies.get('csrftoken')};
     } else {
       options.headers.extend({'X-CSRFToken': Ext.util.Cookies.get('csrftoken')});
     }                        
   }
}, this);


/*
My fix for the "Cannot set QuickTips dismissDelay to 0" bug,
see http://www.sencha.com/forum/showthread.php?183515 
*/
Ext.override(Ext.QuickTip,{
  showAt : function(xy){
        var t = this.activeTarget;
        //~ console.log("20120224 QuickTip.showAt",this.title,this.dismissDelay,t.dismissDelay);
        if(t){
            if(!this.rendered){
                this.render(Ext.getBody());
                this.activeTarget = t;
            }
            if(t.width){
                this.setWidth(t.width);
                this.body.setWidth(this.adjustBodyWidth(t.width - this.getFrameWidth()));
                this.measureWidth = false;
            } else{
                this.measureWidth = true;
            }
            this.setTitle(t.title || '');
            this.body.update(t.text);
            this.autoHide = t.autoHide;
            // bugfix by Luc 20120226
            if (t.dismissDelay != undefined) this.dismissDelay = t.dismissDelay;
            //~ this.dismissDelay = t.dismissDelay || this.dismissDelay;
            if(this.lastCls){
                this.el.removeClass(this.lastCls);
                delete this.lastCls;
            }
            if(t.cls){
                this.el.addClass(t.cls);
                this.lastCls = t.cls;
            }
            if(this.anchor){
                this.constrainPosition = false;
            }else if(t.align){ 
                xy = this.el.getAlignToXY(t.el, t.align);
                this.constrainPosition = false;
            }else{
                this.constrainPosition = true;
            }
        }
        Ext.QuickTip.superclass.showAt.call(this, xy);
    }
});

/*
Another hack. See /docs/blog/2012/0228
*/
Ext.Element.addMethods(
    function() {
        var VISIBILITY      = "visibility",
            DISPLAY         = "display",
            HIDDEN          = "hidden",
            NONE            = "none",
            XMASKED         = "x-masked",
            XMASKEDRELATIVE = "x-masked-relative",
            data            = Ext.Element.data;

        return {
            
            mask : function(msg, msgCls) {
                var me  = this,
                    dom = me.dom,
                    dh  = Ext.DomHelper,
                    EXTELMASKMSG = "ext-el-mask-msg",
                    el,
                    mask;
                // removed the following lines. See /docs/blog/2012/0228
                //~ if (!(/^body/i.test(dom.tagName) && me.getStyle('position') == 'static')) {
                    //~ console.log(20120228,dom.tagName,me);
                    //~ me.addClass(XMASKEDRELATIVE); 
                //~ }
                if (el = data(dom, 'maskMsg')) {
                    el.remove();
                }
                if (el = data(dom, 'mask')) {
                    el.remove();
                }

                mask = dh.append(dom, {cls : "ext-el-mask"}, true);
                data(dom, 'mask', mask);

                me.addClass(XMASKED);
                mask.setDisplayed(true);
                
                if (typeof msg == 'string') {
                    var mm = dh.append(dom, {cls : EXTELMASKMSG, cn:{tag:'div'}}, true);
                    data(dom, 'maskMsg', mm);
                    mm.dom.className = msgCls ? EXTELMASKMSG + " " + msgCls : EXTELMASKMSG;
                    mm.dom.firstChild.innerHTML = msg;
                    mm.setDisplayed(true);
                    mm.center(me);
                }
                
                
                if (Ext.isIE && !(Ext.isIE7 && Ext.isStrict) && me.getStyle('height') == 'auto') {
                    mask.setSize(undefined, me.getHeight());
                }
                
                return mask;
            }

            
        };
    }()
);



Ext.namespace('Lino');
    
    

//~ Lino.subst_user_field = new Ext.form.ComboBox({});
//~ Lino.subst_user = null;
Lino.insert_subst_user = function(p){
    //~ console.log('20120714 insert_subst_user',Lino.subst_user,p);
    //~ if (Lino.subst_user_field.getValue()) {
    if (p.su) return;
    if (Lino.subst_user) {
        //~ p.su = Lino.subst_user_field.getValue();
        p.su = Lino.subst_user;
    //~ } else {
        //~ delete p.su;
    }
    //~ console.log('20120714 insert_subst_user -->',Lino.subst_user,p);
}

Lino.login_window = null;

Lino.autorefresh = function() {
  if (Lino.current_window == null) {
      Lino.viewport.refresh();
      Lino.autorefresh.defer(60000);
  }
}

Lino.show_login_window = function(on_login, username, password) {
  // console.log('20121103 show_login_window',arguments);
  //~ var current_window = Lino.current_window;
  if (typeof username != 'string') username = '';
  if (typeof password != 'string') password = '';
  if (Lino.login_window == null) {
    
      function do_login() { 
            Lino.viewport.loadMask.show()
            login_panel.getForm().submit({ 
                method:'POST', 
                waitTitle:'Connecting', 
                waitMsg:'Sending data...',
                success:function(){ 
                  Lino.login_window.hide();
                  Lino.handle_home_button();
                  Lino.viewport.loadMask.hide();
                  if (typeof on_login == 'string') {
                      Lino.load_url(on_login);
                  } 
                },
                failure: function(form,action) { 
                  Lino.on_submit_failure(form, action);
                  Lino.viewport.loadMask.hide()
                }
            }); 
      };
    
      var login_button = new Ext.Button({ 
        text:"Se connecter",
        formBind: true,	 
        // Function that fires when user clicks the button 
        handler: do_login});
    
      var login_panel = new Ext.FormPanel({ 
        //~ inspired by http://www.sencha.com/learn/a-basic-login/
        autoHeight:true,
        labelWidth:90,
        url:'/auth', 
        frame:true, 
        defaultType:'textfield',
        monitorValid:true,
        items:[{ 
            fieldLabel:"Nom d'utilisateur", 
            id: 'username',
            name:'username', 
            value: username, 
            autoHeight:true,
            allowBlank:false 
        },{ 
            fieldLabel:"Mot de passe", 
            id:'password', 
            name:'password', 
            value: password, 
            inputType:'password', 
            autoHeight:true,
            allowBlank:false 
        }],        
        buttons:[ login_button ]});
        
      Lino.login_window = new Ext.Window({
          layout:'fit',
          defaultButton: 'username',
          width:300,
          title:"Se connecter", 
          autoHeight:true,
          modal: true,
          closeAction: "hide",
          keys: {
            key: Ext.EventObject.ENTER,
            fn: function() { do_login()}
          },
          items: [login_panel] });
  } else {
      var fld = Lino.login_window.items.first().form.findField('username');
      fld.setValue(username);
      var fld = Lino.login_window.items.first().form.findField('password');
      fld.setValue(password);
  };
  Lino.login_window.show();
};

Lino.logout = function(id,name) {
    Lino.call_ajax_action(
        Lino.viewport, 'GET', 
        '/auth',
        {}, 'logout', undefined, undefined,
        function(){Lino.reload();})
}

Lino.set_subst_user = function(id, name) {
    //~ console.log(20130723,'Lino.set_subst_user',id,name,Lino.current_window,Lino.viewport);
    Lino.subst_user = id;
    if (Lino.current_window) 
        Lino.current_window.main_item.set_base_param("su",id);
    if (Lino.viewport) 
        Lino.permalink_handler(Lino.current_window)();
}



//~ Lino.select_subst_user = function(cmp,rec,value){
    //~ Lino.subst_user=value;
    //~ console.log(20120713,rec);
//~ }
    
Lino.current_window = null;
Lino.window_history = Array();
    
Lino.chars2width = function(cols) {  return cols * 9; }
Lino.rows2height = function(cols) {  return cols * 20; }
Lino.perc2width = function(perc) {  
    // var w = Math.max(document.documentElement.clientWidth, window.innerWidth);
    // console.log("20151226", document, window, w);
    var w = Lino.viewport.getWidth();
    return w * perc / 100; 
}



Lino.MainPanel = {
  is_home_page : false,
  setting_param_values : false,
  config_containing_window : function(wincfg) { }
  ,init_containing_window : function(win) { }
  ,is_loading : function() { 
      if (!this.rendered) return true;
      //~ return (Ext.select('.x-loading-msg').elements.length > 0);
      return true; 
    } 
  ,do_when_clean : function(auto_save,todo) { todo() }
  ,get_master_params : function() {
    var p = {}
    p['mt'] = this.content_type; 
    rec = this.get_current_record()
    if (rec) {
      if (rec.phantom) {
          p['mk'] = undefined; 
      }else{
          p['mk'] = rec.id; 
      }
    } else {
      p['mk'] = undefined;
    }
    //~ console.log('get_master_params returns',p,'using record',rec);
    return p;
  }
  ,get_permalink : function() {
    var p = Ext.apply({}, this.get_base_params());
    delete p.fmt;
    Ext.apply(p, this.get_permalink_params());
    
    if (this.toggle_params_panel_btn) {
        p.sp = this.toggle_params_panel_btn.pressed;
        //~ if (this.toggle_params_panel_btn.pressed == this.params_panel_hidden) {
          //~ p.sp = true;
        //~ }
    }
    
    //~ Lino.insert_subst_user(p);
     //~ p.fmt = 'html';
    //~ console.log('get_permalink',p,this.get_permalink_params());
    if (this.is_home_page)
        //~ var url = '';
        var url = '/';
    else 
        var url = this.get_permalink_url();
    if (p.su == null) 
        delete p.su;
    if (Ext.urlEncode(p)) url = url + "?" + Ext.urlEncode(p);
    return url;
  }
  ,get_record_url : function(record_id) {
      var url = '/api' + this.ls_url
      //~ var url = this.containing_window.config.url_data; // ls_url;
      url += '/' + (record_id === undefined ? '-99999' : String(record_id));
      //~ if (record_id !== undefined) url += '/' + String(record_id);
      //~ url += '/' + String(record_id);
      return url;
  }
  ,get_permalink_url : function() {
      return '/api' + this.ls_url;
  }
  ,get_permalink_params : function() {
      //~ return {an:'grid'};
      var p = {};
      if (this.action_name)
          p.an = this.action_name;
      this.add_param_values(p,false)
      return p;
  }
  /*

  Lino.MainPanel.set_status() : the status can have the following keys:

  - param_values : values of parameter fields
  - field_values : values of action parameter fields
  - base_params
  - record_id
  - active_tab
  - data_record
  - show_params_panel
  - current_page

   */
  ,set_status : function(status, requesting_panel) {}
  ,get_status : function() { return {}}
  ,refresh : function() {}
  ,get_base_params : function() {  // Lino.MainPanel
    var p = {};
    Lino.insert_subst_user(p);
    return p;
  }
  ,add_params_panel : function (tbar) {
      if (this.params_panel) {
        //~  20130923b
        //~ this.params_panel.autoHeight = true; // 20130924
        var t = this;
        var update = function() {
            var p = t.params_panel;
            //~ console.log("update", p.getSize().height,p.forceLayout,p.autoHeight);
            var w = t.get_containing_window();
            Lino.do_when_visible(w, function() {
                //~ p.doLayout(true); // doLayout(shallow, force)
                w.doLayout(true); // doLayout(shallow, force)
                //~ t.params_panel.on('afterlayout',update,t,{single:true});
            });
        };
        Lino.do_when_visible(this.params_panel, update);
        this.params_panel.on('show',update);
        this.params_panel.on('hide',update);
        //~ this.params_panel.on('bodyresize',update);
        this.params_panel.on('afterlayout',update);
        //~ this.params_panel.on('afterlayout',update,this,{single:true});
        //~ this.params_panel.on('bodyresize',update,this,{single:true});
        //~ this.params_panel.on('resize',update,this,{single:true});
        //~ this.params_panel.on('render',update,this,{single:true});
        
        // this.params_panel.on('render',
        //~ this.params_panel.on('afterlayout',update,this,{single:true,delay:200});
        //~ this.params_panel.on('bodyresize',update,this,{single:true,delay:200});
        this.toggle_params_panel_btn = new Ext.Button({ scope:this, 
          //~ text: "$_("[parameters]")", // gear
          iconCls: 'x-tbar-database_gear',
          tooltip:"Show or hide the table parameters panel",
          enableToggle: true,
          //~ pressed: ! this.params_panel.hidden,
          pressed: ! this.params_panel_hidden,
          toggleHandler: function(btn,state) { 
            //~ console.log("20120210 add_params_panel",state,this.params_panel);
            if (state) {
                this.params_panel.show();
            } else {
                this.params_panel.hide();
            }
            //~ this.params_panel.on('afterlayout',update,this,{single:true});
            //~ t.get_containing_window().doLayout();
            //~ this.params_panel.on('afterlayout',function() {
                //~ console.log("20130918 afterlayout");
                //~ t.get_containing_window().doLayout(); // doLayout(shallow, force)
            //~ },this,{single:true});
          }
        }); 
        tbar = tbar.concat([this.toggle_params_panel_btn]);
        var refresh = function() {
            if (!t.setting_param_values) {
                t._force_dirty = true; 
                t.refresh();
            }
        }
        Ext.each(this.params_panel.fields,function(f) {
          //~ f.on('valid',function() {t.refresh()});
          if (f instanceof Ext.form.Checkbox) {
              f.on('check',refresh);
          } else if (f instanceof Ext.DatePicker) {
              f.on('select',refresh);
          } else if (f instanceof Ext.form.TriggerField) {
              f.on('select',refresh);
              //~ f.on('change',refresh);
              //~ f.on('valid',refresh);
          } else {
              if (! f.on) 
                  console.log("20121010 no method 'on'",f);
              else
                  f.on('change',refresh);
            }
          });
      }
      return tbar;
  }
  ,add_param_values : function (p,force_dirty) {
    if (this.params_panel) {
      /* 
      * 20120918 add param_values to the request string 
      * *only if the params_form is dirty*.
      * Otherwise Actor.default_params() would never be used.
      *
      * 20121023 But IntegClients.params_default has non-empty default values. 
      * Users must have the possibility to make them empty.
      * 
      * 20130605 : added `force_dirty` parameter because Checkbox fields don't 
      * mark their form as dirty when check is fired.
      * 
      * 20130721 : `force_dirty` not as a parameter but as 
      * `this._force_dirty` because
      * 
      * 20130915 : both _force_dirty and force_dirty parameter are needed.
      * 
      */
      if (force_dirty || this._force_dirty || this.params_panel.form.isDirty()) {
      //~ if (this._force_dirty || this.params_panel.form.isDirty()) {
        p.pv = this.get_param_values();
        //~ console.log("20130923 form is dirty (",force_dirty,this._force_dirty,this.params_panel.form.isDirty(),")");
        //~ console.log("20130923 form is dirty",p);
      }else{
        //~ console.log("20130923 form not dirty:",this.params_panel.form);
        if (this.status_param_values) 
          p.pv = Lino.fields2array(
            this.params_panel.fields,this.status_param_values);
      }
      //~ if (!this.params_panel.form.isDirty()) return;
      //~ p.pv = this.get_param_values();
      //~ console.log("20120203 add_param_values added pv",p.pv,"to",p);
    }
  },
  get_param_values : function() { // similar to get_field_values()
      return Lino.fields2array(this.params_panel.fields);
  },
  set_param_values : function(pv) {
    if (this.params_panel) {
      //~ console.log('20120203 MainPanel.set_param_values', pv);
      this.status_param_values = pv;
      //~ this.params_panel.form.suspendEvents(false);
      this.setting_param_values = true;
      if (pv) { 
          this.params_panel.form.my_loadRecord(pv);
      } else { 
        this.params_panel.form.reset(); 
      }
      this.setting_param_values = false;
      this._force_dirty = false; 
      //~ this.params_panel.form.resumeEvents();
    }
  }
};




Lino.Viewport = Ext.extend(Ext.Viewport, Lino.MainPanel);
Lino.Viewport = Ext.extend(Lino.Viewport, {
  layout : "fit"
  ,is_home_page : true
  ,initComponent : function(){
    Lino.Viewport.superclass.initComponent.call(this);
    this.on('render',function(){
      this.loadMask = new Ext.LoadMask(this.el,{msg:"Veuillez patienter..."});
      //~ console.log("20121118 Lino.viewport.loadMask",this.loadMask);
    },this);
  }
  ,refresh : function() {
      var caller = this;
      // console.log("20140829 Lino.Viewport.refresh()");
      if (caller.loadMask) caller.loadMask.show();
      var success = function(response) {
        if (caller.loadMask) caller.loadMask.hide();
        if (response.responseText) {
          var result = Ext.decode(response.responseText);
          //~ console.log('Lino.do_action()',action.name,'result is',result);
          if (result.html) {
              var cmp = Ext.getCmp('dashboard');
              // cmp.removeAll(true);  // 20140829
              cmp.update(result.html, true);
          }
          if (result.message) {
              if (result.alert) {
                  //~ Ext.MessageBox.alert('Alert',result.alert_msg);
                  Ext.MessageBox.alert('Alert',result.message);
              } else {
                  Lino.notify(result.message);
              }
          }
          
          if (result.notify_msg) Lino.notify(result.notify_msg);
          if (result.js_code) { 
            var jsr = result.js_code(caller);
            //~ console.log('Lino.do_action()',action,'returned from js_code in',result);
          };
        }
      };
      var action = {
        url : '/api/main_html',
        waitMsg: "Veuillez patienter...",
        failure: Lino.ajax_error_handler(caller),
        success: success,
        method: 'GET',
        params: {}
      };
      Lino.insert_subst_user(action.params);
      Ext.Ajax.request(action);
    
  }
});




Lino.open_window = function(win, st, requesting_panel) {
  // console.log("20140831 Lino.open_window()", win, win.el.getBox());
  var cw = Lino.current_window;
  if (cw) {
    // console.log("20140829 Lino.open_window() save current status",
    //             cw.main_item.get_status());
    Lino.window_history.push({
      window:cw,
      status:cw.main_item.get_status()
    });
  }
  Lino.current_window = win;
  //~ if (st.su) 
      //~ Lino.subst_user_field.setValue(st.su);
  win.main_item.set_status(st, requesting_panel);
  // win.toFront();
  win.show();
};

Lino.load_url = function(url) {
    //~ foo.bar.baz = 2; 
    //~ console.log("20121120 Lino.load_url()");
    //~ Lino.body_loadMask.show();
    Lino.viewport.loadMask.show();
    //~ location.replace(url);
    document.location = url;
}

Lino.close_window = function(status_update, norestore) {
  // norestore is used when called by handle_action_result() who 
  // will call set_status itself later
  var cw = Lino.current_window;
  var ww = Lino.window_history.pop();
  var retval = cw.main_item.requesting_panel;
  // console.log(
  //     "20150514 Lino.close_window() going to close", cw.title,
  //     "previous is", ww, 
  //     "norestore is", norestore,
  //     "retval is", retval);
  if (ww) {
    //~ if (status_update) Ext.apply(ww.status,status_update);
    if(!norestore) {
        if (status_update) status_update(ww);
        ww.window.main_item.set_status(ww.status , cw.id);
    }
    Lino.current_window = ww.window;
  } else {
      Lino.current_window = null;
      // new since 20140829:
      if(!norestore) { Lino.viewport.refresh(); }
  }
  if (cw) cw.hide_really();
  return retval;
};

Lino.kill_current_window = function() {
  // console.log("20140418 Lino.kill_current_window()");
  var cw = Lino.current_window;
  Lino.current_window = null;
  if (cw) cw.hide_really();
};

Lino.reload = function() {
    // First close all windows to ensure all changes are saved
    Lino.close_all_windows();

    // Then reload current view
    var url =  "/"

    var p = {};
    Lino.insert_subst_user(p)
    if (Ext.urlEncode(p))
        url = url + "?" + Ext.urlEncode(p);

    Lino.load_url(url);
}

Lino.handle_home_button = function() {
  if (Lino.window_history.length == 0)
      Lino.reload();
  else
      Lino.close_all_windows();
}

Lino.close_all_windows = function() {
    while (Lino.window_history.length > 0) {
        Lino.close_window();
    }
}

Lino.calling_window = function() {
    if (Lino.window_history.length) 
        return Lino.window_history[Lino.window_history.length-1];
}

//~ Lino.WindowAction = function(mainItemClass,windowConfig,mainConfig,ppf) {
Lino.WindowAction = function(windowConfig,main_item_fn) {
    //~ if(!mainConfig) mainConfig = {};
    //~ mainConfig.is_main_window = true;
    this.windowConfig = windowConfig;
    this.main_item_fn = main_item_fn;
    //~ if (ppf) mainConfig.params_panel.fields = ppf;
    //~ this.mainConfig = mainConfig;
    //~ this.mainItemClass = mainItemClass;
};

Lino.WindowAction = Ext.extend(Lino.WindowAction,{
    window : null,
    //~ mainItemClass: null,
    get_window : function() {
      //~ if(mainConfig) Ext.apply(this.mainConfig,mainConfig);
      // if (this.window == null || this.window.isDestroyed)  { // 20140829
      // if (this.window == null || this.window.getBox().width == 0)  { // 20140829
      if (this.window == null)  {
      // if (true)  {
          //~ this.windowConfig.main_item = new this.mainItemClass(this.mainConfig);
          this.windowConfig.main_item = this.main_item_fn();
          this.window = new Lino.Window(this.windowConfig);
      }
      return this.window;
    },
    run : function(requesting_panel, status) {
      // console.log('20140829 window_action.run()', this)
      Lino.open_window(this.get_window(), status, requesting_panel);
    }
  
});


Lino.PanelMixin = {
  get_containing_window : function (){
      if (this.containing_window) return this.containing_window;
      return this.containing_panel.get_containing_window();
  }
  ,set_window_title : function(title) {
    //~ this.setTitle(title);
    var cw = this.get_containing_window();

    //~ if (cw) {
    //~ if (cw && cw.closable) {
    if (cw && !cw.main_item.hide_window_title) {
      //~ console.log('20111202 set_window_title(',title,') for',this.containing_window);
      //~ if (! this.containing_window.rendered) console.log("WARNING: not rendered!");
      cw.setTitle(title);
    //~ } else {
      //~ document.title = title;
    }
    //~ else console.log('20111202 not set_window_title(',title,') for',this);
  }
  
};


// Lino.status_bar = new Ext.ux.StatusBar({defaultText:'Lino version 1.7.0.'});






/* 
  Originally copied from Ext JS Library 3.3.1
  Modifications by Luc Saffre : 
  - rendering of phantom records
  - fire afteredit event
  - react on dblclcik, not on single click

 */
Lino.CheckColumn = Ext.extend(Ext.grid.Column, {

    processEvent : function(name, e, grid, rowIndex, colIndex){
        //~ console.log('20110713 Lino.CheckColumn.processEvent',name)
        if (name == 'click') {
        //~ if (name == 'mousedown') {
        //~ if (name == 'dblclick') {
            return this.toggleValue(grid, rowIndex, colIndex);
        } else {
            return Ext.grid.ActionColumn.superclass.processEvent.apply(this, arguments);
        }
    },
    
    toggleValue : function (grid,rowIndex,colIndex) {
        var record = grid.store.getAt(rowIndex);
        var dataIndex = grid.colModel.getDataIndex(colIndex);
        // 20120514
        //~ if(record.data.disabled_fields && record.data.disabled_fields[dataIndex]) {
          //~ Lino.notify("This field is disabled");
          //~ return false;
        //~ }
      
        //~ if (dataIndex in record.data['disabled_fields']) {
            //~ Lino.notify("This field is disabled.");
            //~ return false;
        //~ }
        var startValue = record.data[dataIndex];
        var value = !startValue;
        //~ record.set(this.dataIndex, value);
        var e = {
            grid: grid,
            record: record,
            field: dataIndex,
            originalValue: startValue,
            value: value,
            row: rowIndex,
            column: colIndex,
            cancel: false
        };
        if(grid.fireEvent("beforeedit", e) !== false && !e.cancel){
        //~ if(grid.fireEvent("validateedit", e) !== false && !e.cancel){
            record.set(dataIndex, value);
            delete e.cancel;
            grid.fireEvent("afteredit", e);
        }
        return false; // Cancel event propagation
    },

    renderer : function(v, p, record){
        if (record.phantom) return '';
        p.css += ' x-grid3-check-col-td'; 
        return String.format('<div class="x-grid3-check-col{0}">&#160;</div>', v ? '-on' : '');
    }

    // Deprecate use as a plugin. Remove in 4.0
    // init: Ext.emptyFn
});

// register ptype. Deprecate. Remove in 4.0
// Ext.preg('checkcolumn', Lino.CheckColumn);

// backwards compat. Remove in 4.0
// Ext.grid.CheckColumn = Lino.CheckColumn;

// register Column xtype
Ext.grid.Column.types.checkcolumn = Lino.CheckColumn;


/* 20110725 : 
Lino.on_tab_activate is necessary 
in contacts.Person.2.dtl 
(but don't ask me why...)
*/
Lino.on_tab_activate = function(item) {
  //~ console.log('activate',item); 
  if (item.rendered && item.doLayout) item.doLayout();
  //~ if (item.rendered) item.doLayout();
}

Lino.TimeField = Ext.extend(Ext.form.TimeField,{
  format: 'H:i',
  increment: 15
  });
Lino.DateField = Ext.extend(Ext.form.DateField,{
  //~ boxMinWidth: Lino.chars2width(15), // 20131005 changed from 11 to 15
  format: 'd.m.Y',
  altFormats: 'd/m/Y|Y-m-d'
  });
Lino.DatePickerField = Ext.extend(Ext.DatePicker,{
  //~ boxMinWidth: Lino.chars2width(11),
  format: 'd.m.Y',
  //~ altFormats: 'd/m/Y|Y-m-d'
  formatDate : function(date){
      //~ console.log("20121203 formatDate",this.name,date);
      return Ext.isDate(date) ? date.dateFormat(this.format) : date;
  }
  });
Lino.DateTimeField = Ext.extend(Ext.ux.form.DateTime,{
  dateFormat: 'd.m.Y',
  timeFormat: 'H:i'
  //~ ,hiddenFormat: 'd.m.Y H:i'
  });
Lino.URLField = Ext.extend(Ext.form.TriggerField,{
  triggerClass : 'x-form-search-trigger',
  //~ triggerClass : 'x-form-world-trigger',
  vtype: 'url',
  onTriggerClick : function() {
    //~ console.log('Lino.URLField.onTriggerClick',this.value)
    //~ document.location = this.value;
    window.open(this.getValue(),'_blank');
  }
});
Lino.IncompleteDateField = Ext.extend(Ext.form.TextField,{
  //~ regex: /^-?\d+-[01]\d-[0123]\d$/,
  //~ regex: /^[0123]\d\.[01]\d\.-?\d+$/,
  maxLength: 10,
  boxMinWidth: Lino.chars2width(10),
  regex: /^[0123]?\d\.[01]?\d\.-?\d+$/,
  regexText: 'Enter a date in format YYYY-MM-DD (use zeroes for unknown parts).'
  });


//~ Lino.make_dropzone = function(cmp) {
    //~ cmp.on('render', function(ct, position){
      //~ ct.el.on({
        //~ dragenter:function(event){
          //~ event.browserEvent.dataTransfer.dropEffect = 'move';
          //~ return true;
        //~ }
        //~ ,dragover:function(event){
          //~ event.browserEvent.dataTransfer.dropEffect = 'move';
          //~ event.stopEvent();
          //~ return true;
        //~ }
        //~ ,drop:{
          //~ scope:this
          //~ ,fn:function(event){
            //~ event.stopEvent();
            //~ console.log(20110516);
            //~ var files = event.browserEvent.dataTransfer.files;
            //~ if(files === undefined){
              //~ return true;
            //~ }
            //~ var len = files.length;
            //~ while(--len >= 0){
              //~ console.log(files[len]);
              //~ // this.processDragAndDropFileUpload(files[len]);
            //~ }
          //~ }
        //~ }
      //~ });
    //~ });
//~ };

//~ Lino.FileUploadField = Ext.ux.form.FileUploadField;

Lino.FileUploadField = Ext.extend(Ext.ux.form.FileUploadField,{
    unused_onRender : function(ct, position){
      Lino.FileUploadField.superclass.onRender.call(this, ct, position);
      this.el.on({
        dragenter:function(event){
          event.browserEvent.dataTransfer.dropEffect = 'move';
          return true;
        }
        ,dragover:function(event){
          event.browserEvent.dataTransfer.dropEffect = 'move';
          event.stopEvent();
          return true;
        }
        ,drop:{
          scope:this
          ,fn:function(event){
            event.stopEvent();
            //~ console.log(20110516);
            var files = event.browserEvent.dataTransfer.files;
            if(files === undefined){
              return true;
            }
            var len = files.length;
            while(--len >= 0){
              console.log(files[len]);
              //~ this.processDragAndDropFileUpload(files[len]);
            }
          }
        }
      });
    }
});

Lino.FileField = Ext.extend(Ext.form.TriggerField,{
  triggerClass : 'x-form-search-trigger',
  editable: false,
  onTriggerClick : function() {
    //~ console.log('Lino.URLField.onTriggerClick',this.value)
    //~ document.location = this.value;
    if (this.getValue()) window.open(MEDIA_URL + '/'+this.getValue(),'_blank');
  }
});

Lino.file_field_handler = function(panel,config) {
  if (panel.action_name == 'insert') {
      panel.has_file_upload = true;


      // config.value = '<br/><br/>';

      var f = new Lino.FileUploadField(config);
      //~ Lino.make_dropzone(f);
      return f;
      //~ return new Ext.ux.form.FileUploadField(config);
      //~ return new Lino.FileField(config);
      
  } else {
      //~ return new Lino.URLField(config);
      return new Lino.FileField(config);
  }
}

Lino.VBorderPanel = Ext.extend(Ext.Panel,{
    constructor : function(config) {
      config.layout = 'border';
      delete config.layoutConfig;
      Lino.VBorderPanel.superclass.constructor.call(this,config);
      for(var i=0; i < this.items.length;i++) {
        var item = this.items.get(i);
        if (this.isVertical(item) && item.collapsible) {
          item.on('collapse',this.onBodyResize,this);
          item.on('expand',this.onBodyResize,this);
        }
      }
    },
    isVertical : function(item) {
       return (item.region == 'north' || item.region == 'south' || item.region == 'center');
    },
    onBodyResize: function(w, h){
        //~ console.log('VBorderPanel.onBodyResize',this.title)
      if (this.isVisible()) { // to avoid "Uncaught TypeError: Cannot call method 'getHeight' of undefined."
        var sumflex = 0;
        var availableHeight = this.getInnerHeight();
        var me = this;
        this.items.each(function(item){
          if (me.isVertical(item)) {
              if (item.collapsed || item.flex == 0 || item.flex === undefined) {
                  if (item.rendered) availableHeight -= item.getHeight();
              } else {
                  sumflex += item.flex;
              }
          } 
          
        });
        //~ for(var i=0; i < this.items.length;i++) {
          //~ var item = this.items.get(i);
          //~ // if (this.isVertical(item) && item.getResizeEl()) {
          //~ if (this.isVertical(item)) {
              //~ if (item.collapsed || item.flex == 0 || item.flex === undefined) {
                  //~ // item.syncSize()
                  //~ // item.doLayout()
                  //~ // if (item.region == "north") console.log('region north',item.getHeight(),item.id, item);
                  //~ // if (item.getHeight() == 0) console.log(20100921,'both flex and getHeight() are 0!');
                  //~ availableHeight -= item.getHeight();
              //~ } else {
                  //~ sumflex += item.flex;
                  //~ // console.log(item.flex);
              //~ }
          //~ } 
          //~ // else console.log('non-vertical item in VBoderPanel:',item)
        //~ }
        var hunit = availableHeight / sumflex;
        //~ console.log('sumflex=',sumflex,'hunit=',hunit, 'availableHeight=',availableHeight);
        for(var i=0; i < this.items.length;i++) {
          var item = this.items.get(i);
          if (this.isVertical(item)) {
              if (item.flex != 0 && ! item.collapsed) {
                  item.setHeight(hunit * item.flex);
                  //~ console.log(item.region,' : height set to',item.getHeight());
              }
          }
          //~ else console.log('non-vertical item in VBoderPanel:',item)
        }
      }
      Lino.VBorderPanel.superclass.onBodyResize.call(this, w, h);
    }
});


/*
  modifications to the standard behaviour of a CellSelectionModel:
  
*/
Ext.override(Ext.grid.CellSelectionModel, {
//~ var dummy = {

    handleKeyDown : function(e){
        /* removed because F2 wouldn't pass
        if(!e.isNavKeyPress()){
            return;
        }
        */
        //~ console.log('handleKeyDown',e)
        var k = e.getKey(),
            g = this.grid,
            s = this.selection,
            sm = this,
            walk = function(row, col, step){
                return g.walkCells(
                    row,
                    col,
                    step,
                    g.isEditor && g.editing ? sm.acceptsNav : sm.isSelectable, 
                    sm
                );
            },
            cell, newCell, r, c, ae;

        switch(k){
            case e.ESC:
            case e.PAGE_UP:
            case e.PAGE_DOWN:
                break;
            default:
                // e.stopEvent(); // removed because Browser keys like Alt-Home, Ctrl-R wouldn't work
                break;
        }

        if(!s){
            cell = walk(0, 0, 1); 
            if(cell){
                this.select(cell[0], cell[1]);
            }
            return;
        }

        cell = s.cell;  
        r = cell[0];    
        c = cell[1];    
        
        switch(k){
            case e.TAB:
                if(e.shiftKey){
                    newCell = walk(r, c - 1, -1);
                }else{
                    newCell = walk(r, c + 1, 1);
                }
                break;
            case e.HOME:
                if (! (g.isEditor && g.editing)) {
                  if (!e.hasModifier()){
                      newCell = [r, 0];
                      //~ console.log('home',newCell);
                      break;
                  }else if(e.ctrlKey){
                      var t = g.getTopToolbar();
                      var activePage = Math.ceil((t.cursor + t.pageSize) / t.pageSize);
                      if (activePage > 1) {
                          e.stopEvent();
                          t.moveFirst();
                          return;
                      }
                      newCell = [0, c];
                      break;
                  }
                }
            case e.END:
                if (! (g.isEditor && g.editing)) {
                  c = g.colModel.getColumnCount()-1;
                  if (!e.hasModifier()) {
                      newCell = [r, c];
                      //~ console.log('end',newCell);
                      break;
                  }else if(e.ctrlKey){
                      var t = g.getTopToolbar();
                      var d = t.getPageData();
                      if (d.activePage < d.pages) {
                          e.stopEvent();
                          var self = this;
                          t.on('change',function(tb,pageData) {
                              var r = g.store.getCount()-2;
                              self.select(r, c);
                              //~ console.log('change',r,c);
                          },this,{single:true});
                          t.moveLast();
                          return;
                      } else {
                          newCell = [g.store.getCount()-1, c];
                          //~ console.log('ctrl-end',newCell);
                          break;
                      }
                  }
                }
            case e.DOWN:
                newCell = walk(r + 1, c, 1);
                break;
            case e.UP:
                newCell = walk(r - 1, c, -1);
                break;
            case e.RIGHT:
                newCell = walk(r, c + 1, 1);
                break;
            case e.LEFT:
                newCell = walk(r, c - 1, -1);
                break;
            case e.F2:
                if (!e.hasModifier()) {
                    if (g.isEditor && !g.editing) {
                        g.startEditing(r, c);
                        e.stopEvent();
                        return;
                    }
                    break;
                }
            case e.INSERT:
                if (!e.hasModifier()) {
                    if (g.ls_insert_handler && !g.editing) {
                        e.stopEvent();
                        Lino.show_insert(g);
                        return;
                    }
                    break;
                }
            // case e.DELETE:
            //     if (!e.hasModifier()) {
            //         if (!g.editing) {
            //             e.stopEvent();
            //             Lino.delete_selected(g);
            //             return;
            //         }
            //         break;
            //     }

            case e.ENTER:
                e.stopEvent();
                g.onCellDblClick(r,c);
                break;

            default:
                g.handle_key_event(e);
                
        }
        

        if(newCell){
          e.stopEvent();
          r = newCell[0];
          c = newCell[1];
          this.select(r, c); 
          if(g.isEditor && g.editing){ 
            ae = g.activeEditor;
            if(ae && ae.field.triggerBlur){
                ae.field.triggerBlur();
            }
            g.startEditing(r, c);
          }
        //~ } else if (g.isEditor && !g.editing && e.charCode) {
        //~ // } else if (!e.isSpecialKey() && g.isEditor && !g.editing) {
            //~ g.set_start_value(String.fromCharCode(e.charCode));
            //~ // g.set_start_value(String.fromCharCode(k));
            //~ // g.set_start_value(e.charCode);
            //~ g.startEditing(r, c);
            //~ // e.stopEvent();
            //~ return;
        // } else {
          // console.log('20120513',e,g);
        }
        
    }


//~ };
});

 

function PseudoConsole() {
    this.log = function() {};
};
if (typeof(console) == 'undefined') console = new PseudoConsole();

Lino.notify = function(msg) {
  if (msg == undefined) msg = ''; else console.log(msg);
  
    if (msg == undefined) return;
    // Lino.alert(msg);
  
};

Lino.alert = function(msg) {
  Ext.MessageBox.alert('Notify',msg);
};


//~ Lino.show_about = function() {
  //~ new Ext.Window({
    //~ width: 400, height: 400,
    //~ title: "About",
    //~ html: '<a href="http://www.extjs.com" target="_blank">ExtJS</a> version ' + Ext.version
  //~ }).show();
//~ };

function obj2str(o) {
  if (typeof o != 'object') return String(o);
  var s = '';
  for (var p in o) {
    s += p + ': ' + obj2str(o[p]) + '\n';
  }
  return s;
}

Lino.on_store_exception = function (store,type,action,options,response,arg) {
  //~ throw response;
  console.log("on_store_exception: store=",store,
    "type=",type,
    "action=",action,
    "options=",options,
    "response=",response,
    "arg=",arg);
  if (arg) { console.log(arg.stack)};
};

//~ Lino.on_submit_success = function(form, action) {
   //~ Lino.notify(action.result.message);
   //~ this.close();
//~ };

Lino.on_submit_failure = function(form, action) {
    //~ Lino.notify();
  // action may be undefined
    switch (action.failureType) {
        case Ext.form.Action.CLIENT_INVALID:
            Ext.Msg.alert('Client-side failure', 'Form fields may not be submitted with invalid values');
            break;
        case Ext.form.Action.CONNECT_FAILURE:
            Ext.Msg.alert('Connection failure', 'Ajax communication failed');
            break;
        case Ext.form.Action.SERVER_INVALID:
            Ext.Msg.alert('Server-side failure', action.result.message);
   }
};



/*
Lino.save_wc_handler = function(ww) {
  return function(event,toolEl,panel,tc) {
    var pos = panel.getPosition();
    var size = panel.getSize();
    wc = ww.get_window_config();
    Ext.applyIf(wc,{ 
      x:pos[0],y:pos[1],height:size.height,width:size.width,
      maximized:panel.maximized});
    Lino.do_action(ww,{url:'/window_configs/'+ww.config.permalink_name,params:wc,method:'POST'});
  }
};

*/

Lino.show_in_own_window_button = function(handler) {
  return {
    qtip: "Montrer ce panneau dans une fenêtre à part.", 
    id: "up",
    handler: function(event,toolEl,panel, tc) {
      //~ console.log('20111206 report_window_button',panel,handler);
      handler.run(null,{base_params:panel.containing_panel.get_master_params()});
    }
  }
}

Lino.action_handler = function (panel, on_success, on_confirm) {
  return function (response) {
      if (!panel) { 
          if (Lino.current_window) 
              panel = Lino.current_window.main_item;
          else panel = Lino.viewport;
      }
      
    if (panel.loadMask) panel.loadMask.hide(); // 20120211
    if (!response.responseText) return ;
    var result = Ext.decode(response.responseText);
    Lino.handle_action_result(panel, result, on_success, on_confirm);
  }
};

Lino.handle_action_result = function (panel, result, on_success, on_confirm) {

    // console.log('20150514 Lino.handle_action_result()', result);
    
    // if (panel instanceof Lino.GridPanel) {
    //     gridmode = true;
    // } else {
    //     gridmode = false;
    // }

    //~ if (result.goto_record) {
        //~ var js = "Lino." + result.goto_record[0] + '.detail.run';
        //~ var h = eval(js);
        //~ h(panel,{record_id:result.goto_record[1]});
    //~ }
    
    if (result.xcallback) {
        //~ var config = {title:"Confirmation"};
        var config = {title:result.xcallback.title};
        //~ config.buttons = Ext.MessageBox.YESNOCANCEL;
        //~ config.buttons = Ext.MessageBox.YESNO;
        var p = {};
        Lino.insert_subst_user(p);
        config.buttons = result.xcallback.buttons;
        config.msg = result.message;
        config.fn = function(buttonId, text, opt) {
          panel.loadMask.show(); 
          //~ Lino.insert_subst_user(p);
          Ext.Ajax.request({
            method: 'GET',
            url: '/callbacks/'
                  + result.xcallback.id + '/' + buttonId,
            params: p,
            success: Lino.action_handler(panel, on_success, on_confirm)
          });
        }
        Ext.MessageBox.show(config);
        return;
    }

    // `record_id` and/or `data_record` both mean "display the detail
    // of this record". 
    
    if(result.detail_handler_name) {
        // TODO: make sure that result.detail_handler_name is secure
        var detail_handler = eval("Lino." + result.detail_handler_name);
    }
    var ns = {};  // new status
    if (result.close_window) {
        
        // Subsequent processing expects that `panel` is "the current
        // panel". But if we close the window, `panel` must point
        // to the previous window. Note the case of an insert window
        // that has been invoked by double-clicking on the phantom row
        // of a slave table in a detail window. In that case we want
        // `panel` to become the grid panel of the slave table who
        // called the insert window, not the master's detail form
        // panel.  When the insert window has been called by an action
        // link (e.g. generated using ar.insert_button), then
        // Lino.close_window can return `undefined`.

        if(result.record_id || result.data_record) {
            var ww = Lino.calling_window();
            if (ww && ww.window.main_item instanceof Lino.FormPanel) {
                if (ww.window.main_item.ls_detail_handler == detail_handler) {
                    ns.record_id = result.record_id;
                    ns.data_record = result.data_record;
                    // console.log("20150514 use new status.");
                }
            }
        }

        panel = Lino.close_window(
            function(ww) { Ext.apply(ww.status, ns) }); 
        if (!panel) 
            // console.log("20150514 close_window returned no panel.");
            if (Lino.current_window)
                panel = Lino.current_window.main_item;

    }

    if(result.record_id || result.data_record) {
        if (! (ns.record_id || ns.data_record)) {
          // no close_window, so we must update record data in current
          // panel (if it is the detail_handler for this record) or
          // open the detail handler.
          var st = {
              record_id: result.record_id,
              data_record: result.data_record
          };
          if (result.active_tab) st.active_tab = result.active_tab;
          if (panel instanceof Lino.FormPanel 
              && panel.ls_detail_handler == detail_handler) 
            {
              // console.log("20150514 use panel.set_status().");
              panel.set_status(st);
          } else {
              // console.log("20150514 run detail_handler.");
              st.base_params = panel.get_base_params();
              detail_handler.run(null, st);
          }

          // if (panel instanceof Lino.FormPanel 
          //     && panel.ls_url == result.actor_url) {
          //     // console.log("20140506 case 2 it's a FormPanel:", panel);
          //     panel.set_status({
          //         record_id: result.record_id,
          //         data_record: result.data_record});
          // } else if (panel.ls_detail_handler 
          //            && panel.ls_url == result.actor_url) {
          //     // console.log("20140506 case 4");
          //     panel.ls_detail_handler.run(null, {
          //         record_id: result.record_id,
          //         data_record: result.data_record,
          //         base_params: panel.get_base_params()});
          // } else {
          //     result.refresh_all = true;
          //     console.log("20140604 case 6", result.actor_url);
          // }
        }
    }

    // `eval_js` must get handled after `close_window` because it
    // might ask to open a new window (and we don't want to close that
    // new window).  It must execute *before* any MessageBox,
    // otherwise the box would get hidden by a window that opens
    // afterwards.

    if (result.eval_js) {
        //~ console.log(20120618,result.eval_js);
        eval(result.eval_js);
    }
    
    if (on_success && result.success) {
        // console.log("20140430 handle_action_result calls on_success", 
        //             on_success);
        on_success(result);
    }
    
    if (result.info_message) {
        console.log(result.info_message);
    }
    
    if (result.warning_message) {
        if (!result.alert) result.alert = "Avertissement";
        Ext.MessageBox.alert(result.alert, result.warning_message);
    }
    
    if (result.message) {
        //~ if (result.alert && ! gridmode) {
        if (result.alert) { // 20120628b 
            //~ Ext.MessageBox.alert('Alert',result.alert_msg);
            if (result.alert === true) result.alert = "Alerte";
            Ext.MessageBox.alert(result.alert, result.message);
        } else {
            Lino.notify(result.message);
        }
    }

    if(result.record_deleted && panel.ls_detail_handler == detail_handler) {
        panel.after_delete();
    }
    
    if (result.refresh_all) {
        var cw = Lino.current_window;
        // var cw = panel.get_containing_window();
        if (cw) {
            // console.log("20140917 refresh_all calls refresh on", cw.main_item);
            cw.main_item.refresh();
        }
        // else console.log("20140917 cannot refresh_all because ",
        //                  "there is no current_window");
    } else {
        if (result.refresh) {
            // console.log("20140917 Gonna call panel.refresh()", panel);
            panel.refresh();
        }
    }if (result.open_url) {
        //~ console.log(20111126,result.open_url);
        //~ if (!result.message)
            //~ Lino.notify('Open new window <a href="'+result.open_url+'" target="_blank">'+result.open_url+'</a>');
        window.open(result.open_url,'foo',"");
        //~ document.location = result.open_url;
    }
};

// obsolete but still used for deleting records.
Lino.do_action = function(caller,action) { 
  action.success = function(response) {
    if (caller.loadMask) caller.loadMask.hide();
    //~ console.log('Lino.do_action()',action,'action success',response);
    if (action.after_success) {
        //~ console.log('Lino.do_action() calling after_success');
        action.after_success();
    }
    if (response.responseText) {
      var result = Ext.decode(response.responseText);
      //~ console.log('Lino.do_action()',action.name,'result is',result);
      if (result.message) {
          if (result.alert) {
              //~ Ext.MessageBox.alert('Alert',result.alert_msg);
              Ext.MessageBox.alert('Alert',result.message);
          } else {
              Lino.notify(result.message);
          }
      }
      
      //~ if (result.alert_msg) Ext.MessageBox.alert('Alert',result.alert_msg);
      //~ if (result.message) Lino.notify(result.message);
      if (result.notify_msg) Lino.notify(result.notify_msg);
      if (result.js_code) { 
        //~ console.log('Lino.do_action()',action,'gonna call js_code in',result);
        var jsr = result.js_code(caller);
        //~ console.log('Lino.do_action()',action,'returned from js_code in',result);
        if (action.after_js_code) {
          //~ console.log('Lino.do_action()',action,'gonna call after_js_code');
          action.after_js_code(jsr);
          //~ console.log('Lino.do_action()',action,'returned from after_js_code');
        //~ } else {
          //~ console.log('Lino.do_action()',action,' : after_js_code is false');
        }
      };
    }
  };
  Ext.applyIf(action,{
    waitMsg: "Veuillez patienter...",
    failure: Lino.ajax_error_handler(caller),
    params: {}
  });
  //~ action.params.su = Lino.subst_user;
  Lino.insert_subst_user(action.params);
  
  Ext.Ajax.request(action);
};

//~ Lino.gup = function( name )
//~ {
  //~ // Thanks to http://www.netlobo.com/url_query_string_javascript.html
  //~ name = name.replace(/[\[]/,"\\\[").replace(/[\]]/,"\\\]");
  //~ var regexS = "[\\?&]"+name+"=([^&#]*)";
  //~ var regex = new RegExp( regexS );
  //~ var results = regex.exec( window.location.href );
  //~ if( results == null )
    //~ return "";
  //~ else
    //~ return results[1];
//~ };

//~ Lino.refresh_handler = function (ww) {
  //~ return function() { 
      //~ console.log('refresh',ww);
      //~ ww.main_item.doLayout(false,true);
      //~ ww.main_item.syncSize();
  //~ }
//~ };

//~ Lino.tools_close_handler = function (ww) {
  //~ return function() { 
      //~ ww.close();
  //~ }
//~ };
Lino.permalink_handler = function (ww) {
  return function() { 
    //~ document.location = ww.main_item.get_permalink();
    //~ console.log('20130723 Lino.permalink_handler',ww);
    
    /* Uncaught TypeError: Cannot read property 'main_item' of null  */
    if (ww) {
        var url = ww.main_item.get_permalink();
    } else {
        var url = Lino.viewport.get_permalink();
    }
    Lino.load_url(url);
  }
};
//~ Lino.run_permalink = function() {
  //~ var plink = Lino.gup('permalink');
  //~ if(plink) { eval('Lino.'+plink); }
//~ }


Lino.ajax_error_handler = function(panel) {
  return function(response,options) {
    console.log('Ajax failure:', response, options);
    if (panel.loadMask) panel.loadMask.hide();
    if (response.responseText) {
      var lines = response.responseText.split('\n');
      if (lines.length > 10) {
          line = lines.splice(5, lines.length-10, "(...)");
      }
      //~ console.log(20131005, response.statusText.toCamel());
      Ext.MessageBox.alert(
        response.statusText.toCamel(),
        lines.join('<br/>')
        //~ response.responseText.replace(/\n/g,'<br/>'))
      )
    } else {
      Ext.MessageBox.alert('Action failed',
        'Lino server did not respond to Ajax request');
    }
  }
}
// Ext.Ajax.on('requestexception',Lino.ajax_error_handler)
 


Ext.QuickTips.init();

/* setting QuickTips dismissDelay to 0 */
// Apply a set of config properties to the singleton
//~ Ext.apply(Ext.QuickTips.getQuickTip(), {
//~ Ext.apply(Ext.ToolTip, {
    //~ dismissDelay: 0
    //~ autoHide: false,
    //~ closable: true,
    //~ maxWidth: 200,
    //~ minWidth: 100,
    //~ showDelay: 50      // Show 50ms after entering target
    //~ ,trackMouse: true
//~ });


//~ Ext.apply(Ext.QuickTip, {
    //~ dismissDelay: 0,
//~ });
  
Lino.quicktip_renderer = function(title,body) {
  return function(c) {
    //~ if (c instanceof Ext.Panel) var t = c.bwrap; else // 20130129
    if (c instanceof Ext.Panel) var t = c.header; else // 20130129
    var t = c.getEl();
    //~ console.log(20130129,t,title,body);
    //~ t.dismissDelay = 0;
    Ext.QuickTips.register({
      target: t,
      //~ cls: 'lino-quicktip-classical',
      dismissDelay: 0,
      //~ autoHide: false,
      showDelay: 50,      // Show 50ms after entering target
      //~ title: title,
      text: body
    });
  }
};


  
Lino.help_text_editor = function() {
  //~ var bp = {
      //~ mk:this.content_type,
      //~ mt:1
    //~ };
    //~ console.log(20120202,bp);
  //~ Lino.lino.ContentTypes.detail({},{base_params:bp});
  //~ Lino.lino.ContentTypes.detail.run(null,{record_id:this.content_type});
  Lino.lino.ContentTypes.detail.run(null,{record_id:this.content_type});
}

// Path to the blank image should point to a valid location on your server
//~ Ext.BLANK_IMAGE_URL = MEDIA_URL + '/extjs/resources/images/default/s.gif'; 


// used as Ext.grid.Column.renderer for id columns in order to hide the special id value -99999
Lino.id_renderer = function(value, metaData, record, rowIndex, colIndex, store) {
  //~ if (record.phantom) return '';
  return value;
}

Lino.raw_renderer = function(value, metaData, record, rowIndex, colIndex, store) {
  return value;
}

Lino.text_renderer = function(value, metaData, record, rowIndex, colIndex, store) {
  //~ return "not implemented"; 
  return value;
}

Lino.NullNumberColumn = Ext.extend(Ext.grid.Column, {
    align : 'right', 
    format : '0,00/i', 
    renderer : function(value, metaData, record, rowIndex, colIndex, store) {
        //~ console.log(20130128,"NullNumberColumn.renderer",value);
        if (value === null) return '';
        return Ext.util.Format.number(value, this.format);
    }
});


Lino.link_button = function(url) {
    // return '<a href="' + url + '"><img src="/media/lino/extjs/images/xsite/link.png" alt="link_button"></a>'
    return '<a href="' + url + '" style="text-decoration:none;">&#10138;</a>'
}

Lino.fk_renderer = function(fkname,handlername) {
  //~ console.log('Lino.fk_renderer handler=',handler);
  return function(value, metaData, record, rowIndex, colIndex, store) {
    //~ console.log('Lino.fk_renderer',fkname,rowIndex,colIndex,record,metaData,store);
    //~ if (record.phantom) return '';
    if (value) {
        return Lino.link_button('javascript:'+handlername + '.run(null,{record_id:\'' + String(record.data[fkname]) + '\'})")') + value;
        // until 20140822 (clickable foreign keys):
        // var s = '<a href="javascript:' ;
        // s += handlername + '.run(null,{record_id:\'' + String(record.data[fkname]) + '\'})">';
        // s += value + '</a>';
        // return s
    }
    return '';
  }
};

Lino.lfk_renderer = function(panel,fkname) {
  //~ console.log('Lino.fk_renderer handler=',handler);
  var handlername = 'console.log';
  return function(value, metaData, record, rowIndex, colIndex, store) {
    //~ console.log('Lino.fk_renderer',fkname,rowIndex,colIndex,record,metaData,store);
    if (record.phantom) return '';
    if (value) {
        var s = '<a href="javascript:' ;
        s += handlername + '({},{record_id:\'' + String(record.data[fkname]) + '\'})">';
        s += value + '</a>';
        //~ console.log('Lino.fk_renderer',value,'-->',s);
        return s
    }
    return '';
  }
};

//~ Lino.gfk_renderer = function() {
  //~ return function(value, metaData, record, rowIndex, colIndex, store) {
    //~ if (record.phantom) return '';
    //~ console.log('Lino.gfk_renderer',value,colIndex,record,metaData,store);
    //~ return value;
  //~ }
//~ };


Lino.build_buttons = function(panel,actions) {
  //~ console.log("20121006 Lino.build_buttons",actions);
  if (actions) {
    var buttons = Array(actions.length);
    var cmenu = Array(actions.length);
    var keyhandlers = {};
    for (var i=0; i < actions.length; i++) { 
      var a = actions[i];
      if (a.menu) a.menu = Lino.build_buttons(panel,a.menu).bbar;
      buttons[i] = a;
      cmenu[i] = {
            text : a.menu_item_text,
            iconCls : a.iconCls,
            menu : a.menu
          };
      if (a.panel_btn_handler) {
          var h = a.panel_btn_handler.createCallback(panel);
          if (a.auto_save == true) {
              h = panel.do_when_clean.createDelegate(panel,[true,h]);
          } else if (a.auto_save == null) {
              h = panel.do_when_clean.createDelegate(panel,[false,h]);
          } else if (a.auto_save == false) {
              // h = h;
          } else {
              console.log("20120703 unhandled auto_save value",a)
          }
          buttons[i].handler = h;
          cmenu[i].handler = h;
          if (a.keycode) {
              keyhandlers[a.keycode] = h;
          }
          //~ if (buttons[i].xtype == 'splitbutton') {
              //~ cmenu[i].menu = a.menu;
          //~ } else {
              //~ cmenu[i].handler = h;
          //~ }
      } else {
          console.log("action without panel_btn_handler",a)
          // cmenu[i].handler = a.handler;
      }
    }
    return {
        bbar:buttons, 
        cmenu:new Ext.menu.Menu(cmenu),
        keyhandlers: keyhandlers
    };
  }
}

Lino.do_when_visible = function(cmp,todo) {
  //~ if (cmp.el && cmp.el.dom) 
  if (cmp.isVisible()) { 
    // 'visible' means 'rendered and not hidden'
    //~ console.log(cmp.title,'-> cmp is visible now');
    todo(); 
  //~ } else {
      //~ cmp.on('resize',todo,cmp,{single:true});
  //~ }
  //~ if (false) { // 20120213
  } else { 
    //~ console.log('Lino.do_when_visible() must defer because not isVisible()',todo,cmp);
    if (cmp.rendered) {
      //~ console.log(cmp,'-> cmp is rendered but not visible: and now?');
      //~ console.log(cmp.title,'-> cmp is rendered but not visible: try again in a moment...');
      //~ var fn = function() {Lino.do_when_visible(cmp,todo)};
      //~ fn.defer(100);
      
      Lino.do_when_visible.defer(50,this,[cmp,todo]);
      //~ Lino.do_when_visible.defer(100,this,[cmp,todo]);
      
    } else {
      //~ console.log(cmp.title,'-> after render');
      cmp.on('afterrender',todo,cmp,{single:true});
    }
  }
  
};    

/*
*/
Lino.do_on_current_record = function(panel, fn, phantom_fn) {
  // console.log('20140930 do_on_current_record', arguments);
  var rec = panel.get_current_record();
  if (rec == undefined) {
    Lino.notify("There's no selected record.");
    return;
  }
  // 20120307 A VirtualTable with a Detail (lino.Models) has only "phantom" records.
  if (rec.phantom) {
    //~ if (!panel.editable) { console.log("20120312 not editable:",panel)}
    if (phantom_fn) {
      phantom_fn(panel);
    } else {
      Lino.notify("Action not available on phantom record.");
    }
    return;
  }
  return fn(rec);
};


Lino.call_ajax_action = function(
    panel, method, url, p, actionName, step, on_confirm, on_success) {
  p.an = actionName;
  if (!panel || !panel.isVisible()) {
  //~ if (true) { // 20131026 : workflow_actions of a newly created record detail executed but did't refresh the screen because their requesting panel was the insert (not the detail) formpanel.
      if (Lino.current_window) 
          panel = Lino.current_window.main_item;
      else panel = Lino.viewport;
  }
  // console.log("20150130 a", p.pv);
  // Ext.apply(p, panel.get_base_params());
  // console.log("20150130 b", p.pv);

  if (panel.get_selected) {
      var selected_recs = panel.get_selected();
      //~ console.log("20130831",selected_recs);
      var rs = Array(selected_recs.length);
      for(var i=0; i < selected_recs.length;i++) {
          rs[i] = selected_recs[i].data.id;
      };
      p.sr = rs;
  }
  
  // console.log("20140516 Lino.call_ajax_action", p, actionName, step);
  
  if (panel.loadMask) panel.loadMask.show(); 
    
  Ext.Ajax.request({
    method: method
    ,url: url
    ,params: p
    ,success: Lino.action_handler(panel, on_success, on_confirm)
    ,failure: Lino.ajax_error_handler(panel)
  });
};




Lino.row_action_handler = function(actionName, hm, pp) {
  var p = {};
  var fn = function(panel, btn, step) {
      // console.log('20150514 row_action_handler');
      if (pp) { p = pp(panel); if (! p) return; }
      
      if (!panel || panel.get_current_record == undefined) { // AFTER_20130725
        // console.log('20140930 row_action_handler 2', panel);
        panel = Ext.getCmp(panel);
        if (panel == undefined) {
          console.log("20160410 Invalid panel spec.", actionName, hm, pp);
          Lino.notify("Invalid panel spec.");
          return;
        }
      }
      
      Lino.do_on_current_record(panel, function(rec) {
          //~ console.log(panel);
          panel.add_param_values(p, true);
          Ext.apply(p, panel.get_base_params());
          Lino.call_ajax_action(
              panel, hm, panel.get_record_url(rec.id), 
              p, actionName, step, fn);
      });
  };
  return fn;
};

Lino.list_action_handler = function(ls_url,actionName,hm,pp) {
  var p = {};
  var url = '/api' + ls_url
  var fn = function(panel,btn,step) {
      //~ console.log("20121210 Lino.list_action_handler",arguments);
      if (pp) { p = pp(panel);  if (! p) return; }
      if (panel) { // may be undefined when called e.g. from quicklink
          panel.add_param_values(p, true);
          Ext.apply(p, panel.get_base_params());
      }
      Lino.call_ajax_action(panel, hm,url, p, actionName, step, fn);
  };
  return fn;
};

Lino.param_action_handler = function(window_action) { // 20121012
  var fn = function(panel,btn,step) {
    Lino.do_on_current_record(panel,function(rec) {
      window_action.run(panel.getId(),{}); 
    });
  };
  return fn;
};


Lino.run_row_action = function(
    requesting_panel, url, meth, pk, actionName, params, preprocessor) {
  //~ var panel = action.get_window().main_item;
  // console.log("20140930 Lino.run_row_action", params);
  url = '/api' + url  + '/' + pk;
  var panel = Ext.getCmp(requesting_panel);
  if (!params) params = {};
  if (preprocessor) {
      var p = preprocessor(); 
      Ext.apply(params, p);
  }
  if (panel) 
      Ext.apply(params, panel.get_base_params());
  var fn = function(panel, btn, step) {
    Lino.call_ajax_action(panel, meth, url, params, actionName, step, fn);
  }
  fn(panel, null, null);
}

Lino.put = function(requesting_panel, pk, data) {
    var panel = Ext.getCmp(requesting_panel);
    //~ var panel = null; // 20131026
    var p = {};
    p.an = 'put'; // SubmitDetail.action_name

    Ext.apply(p,data);
    var req = {
        params:p
        ,waitMsg: 'Saving your data...'
        ,scope: panel
        ,success: Lino.action_handler( panel, function(result) { 
            panel.refresh();
        })
        ,failure: Lino.ajax_error_handler(panel)
    };
    req.method = 'PUT';
    req.url = '/api' + panel.ls_url + '/' + pk;
    if (panel.loadMask) panel.loadMask.show(); 
    Ext.Ajax.request(req);
}



Lino.show_detail = function(panel, btn) {
  Lino.do_on_current_record(panel, 
    function(rec) {
      //~ panel.loadMask.show();
      Lino.run_detail_handler(panel, rec.id);
    },
    Lino.show_insert
  );
};

Lino.run_detail_handler = function(panel,pk) {
  var bp = panel.get_base_params();
  panel.add_param_values(bp); // 20120918
  var status = {
    record_id:pk,
    base_params:bp
  }
  //~ console.log("20120918 Lino.show_detail",status);
  panel.ls_detail_handler.run(null,status);
}

Lino.show_fk_detail = function(combo,detail_action,insert_action) {
    //~ console.log("Lino.show_fk_detail",combo,handler);
    pk = combo.getValue();
    if (pk) {
        detail_action.run(null,{record_id: pk})
      } else {
        insert_action.run(null,{record_id:-99999});
        //~ Lino.notify("Cannot show detail for empty foreign key.");
      }
};

Lino.show_insert = function(panel,btn) {
  var bp = panel.get_base_params();
  //~ console.log('20120125 Lino.show_insert',bp)
  //~ panel.ls_insert_handler.run(null,{record_id:-99999,base_params:bp});
  panel.ls_insert_handler.run(panel.getId(),{record_id:-99999,base_params:bp});
};



if (Ext.ux.grid !== undefined) {
    Lino.GridFilters = Ext.extend(Ext.ux.grid.GridFilters,{
      encode:true,
      local:false
    });
} else {
    Lino.GridFilters = function() {}; // dummy
    Ext.override(Lino.GridFilters,{
      init : function() {}
    });
};



Lino.FieldBoxMixin = {
  before_init : function(config,params) {
    if (params) Ext.apply(config,params);
    var actions = Lino.build_buttons(this, config.ls_bbar_actions);
    if (actions) config.bbar = actions.bbar;
  },
  //~ constructor : function(ww,config,params){
    //~ this.containing_window = ww;
    //~ if (params) Ext.apply(config,params);
    //~ var actions = Lino.build_buttons(this,config.ls_bbar_actions);
    //~ if (actions) config.bbar = actions.bbar;
    //~ Lino.FieldBoxMixin.superclass.constructor.call(this, config);
  //~ },
  do_when_clean : function(auto_save,todo) { todo() },
  //~ format_data : function(html) { return '<div class="htmlText">' + html + '</div>' },
  format_data : function(html) { return html },
  get_base_params : function() {
    // needed for insert action
    var p = Ext.apply({}, this.base_params);
    Lino.insert_subst_user(p);
    return p;
  },
  set_base_params : function(p) {
    this.base_params = Ext.apply({},p);
    //~ if (p.param_values) this.set_param_values(p.param_values);  
  },
  clear_base_params : function() {
      this.base_params = {};
      Lino.insert_subst_user(this.base_params);
  },
  set_base_param : function(k,v) {
    this.base_params[k] = v;
  }
};



Lino.HtmlBoxPanel = Ext.extend(Ext.Panel, Lino.PanelMixin);
Lino.HtmlBoxPanel = Ext.extend(Lino.HtmlBoxPanel, Lino.FieldBoxMixin);
Lino.HtmlBoxPanel = Ext.extend(Lino.HtmlBoxPanel, {
  disabled_in_insert_window : true,
  constructor : function(config,params) {
    this.before_init(config,params);
    Lino.HtmlBoxPanel.superclass.constructor.call(this, config);
  },
  //~ constructor : function(ww,config,params){
    //~ this.ww = ww;
    //~ if (params) Ext.apply(config,params);
    //~ var actions = Lino.build_buttons(this,config.ls_bbar_actions);
    //~ if (actions) config.bbar = actions.bbar;
    //~ Lino.FieldBoxMixin.constructor.call(this, ww,config,params);
  //~ },
  //~ constructor : function(ww,config,params){
    //~ this.ww = ww;
    //~ if (params) Ext.apply(config,params);
    //~ var actions = Lino.build_buttons(this,config.ls_bbar_actions);
    //~ if (actions) config.bbar = actions.bbar;
    //~ Lino.FieldBoxMixin.superclass.constructor.call(this, config);
  //~ },
  //~ disable : function() { var tb = this.getBottomToolbar(); if(tb) tb.disable()},
  //~ enable : function() { var tb = this.getBottomToolbar(); if(tb) tb.enable()},
  onRender : function(ct, position){
    Lino.HtmlBoxPanel.superclass.onRender.call(this, ct, position);
    //~ console.log(20111125,this.containing_window);
    if (this.containing_panel) {
      this.containing_panel.on('enable',this.enable,this);
      this.containing_panel.on('disable',this.disable,this);
    }
    this.el.on({
      dragenter:function(event){
        event.browserEvent.dataTransfer.dropEffect = 'move';
        return true;
      }
      ,dragover:function(event){
        event.browserEvent.dataTransfer.dropEffect = 'move';
        event.stopEvent();
        return true;
      }
      ,drop:{
        scope:this
        ,fn:function(event){
          event.stopEvent();
          //~ console.log(20110516);
          var files = event.browserEvent.dataTransfer.files;
          if(files === undefined){
            return true;
          }
          var len = files.length;
          while(--len >= 0){
            console.log(files[len]);
            //~ this.processDragAndDropFileUpload(files[len]);
          }
          Lino.show_insert(this);
        }
      }
    });
  },
  refresh : function(unused) { 
      // this.containing_panel.refresh();
      this.refresh_with_after();
  },
  /* HtmlBoxPanel */
  refresh_with_after : function(after) {
      // var todo = this.containing_panel.refresh();
      var box = this.items.get(0);
      var todo = function() {
        if (this.disabled) { return; }
        this.set_base_params(this.containing_panel.get_master_params());

        var el = box.getEl();
        if (el) {
            var record = this.containing_panel.get_current_record();
            var newcontent = record ? 
                this.format_data(record.data[this.name]) : '';
            // console.log('20140917 HtmlBox.refresh()',
            //             this.name, record.data.LinksByHuman);
            el.update(newcontent, true);
        // } else {
        //     console.log('20140502 cannot HtmlBox.refresh()',this.name);
        }
      };

      Lino.do_when_visible(box, todo.createDelegate(this));
  }
});
//~ Ext.override(Lino.HtmlBoxPanel,Lino.FieldBoxMixin);


Lino.ActionFormPanel = Ext.extend(Ext.form.FormPanel,Lino.MainPanel);
Lino.ActionFormPanel = Ext.extend(Lino.ActionFormPanel, Lino.PanelMixin);
Lino.ActionFormPanel = Ext.extend(Lino.ActionFormPanel, Lino.FieldBoxMixin);
Lino.ActionFormPanel = Ext.extend(Lino.ActionFormPanel, {
  //~ layout:'fit'
  //~ ,autoHeight: true
  //~ ,frame: true
  window_title : "Action Parameters",
  constructor : function(config){
    config.bbar = [
        {text: 'OK', handler: this.on_ok, scope: this},
        {text: 'Cancel', handler: this.on_cancel, scope: this}
    ];
    Lino.ActionFormPanel.superclass.constructor.call(this, config);
  }
  //~ ,initComponent : function(){
    //~ Lino.ActionFormPanel.superclass.initComponent.call(this);
  //~ }
  ,on_cancel : function() { 
    this.get_containing_window().close();
  }
  ,on_ok : function() { 
    var panel = this.requesting_panel;
    // var panel = this.get_containing_window().main_item;
    // console.log("20131004 on_ok",this,panel,arguments);
    var actionName = this.action_name;
    var pk = this.record_id;
    if (pk == undefined && this.base_params) { pk = this.base_params.mk; }
    if (pk == undefined && panel) {
        pk = panel.get_current_record().id;
    }
    if (pk == undefined) {
        Lino.alert("Sorry, dialog action without base_params.mk");
        return;
    }
    var self = this;
    // function on_success() { self.get_containing_window().close(); };
    // see 20131004 and 20140430
    var url = '/api';

    // 20150119 : The OK button on AgentsByClient.create_visit went to
    // /api/pcsw/Clients/ instead of /api/pcsw/Coachings/
    // if (panel) 
    //     url += panel.ls_url;
    // else 
    //     url += this.ls_url;

    if (this.ls_url) 
        url += this.ls_url;
    else 
        url += panel.ls_url;
    url += '/' + pk;
    // wrap into function to prepare possible recursive call
    var fn = function(panel, btn, step) {
      var p = {};
      self.add_field_values(p)
      if (panel) Ext.apply(p, panel.get_base_params());
      delete p.pv;
      // console.log("20150130", p.pv);

      Lino.call_ajax_action(
          panel, 'GET', url, p, actionName, step, fn); //  , on_success);
    }
    fn(panel, null, null);
    
    
  }
  /* ActionFormPanel*/
  ,set_status : function(status, rp){
    this.requesting_panel = Ext.getCmp(rp);
    //~ console.log('20120918 ActionFormPanel.set_status()',status,rp,this.requesting_panel);
    this.clear_base_params();
    if (status == undefined) status = {};
    //~ if (status.param_values) 
    this.set_field_values(status.field_values);
    if (status.base_params) this.set_base_params(status.base_params);
    this.record_id = status.record_id;
  }
  
  ,before_row_edit : function(record) {}
  ,add_field_values : function (p) { // similar to add_param_values()
      //~ 20121023 
      if (this.form.isDirty()) {
        p.fv = this.get_field_values();
      }else{
        if (this.status_field_values) 
          p.fv = Lino.fields2array(this.fields,this.status_field_values);
      }
      //~ if (!this.form.isDirty()) return;
      //~ p.$constants.URL_PARAM_FIELD_VALUES = this.get_field_values();
      //~ console.log("20120203 add_param_values added pv",pv,"to",p);
  }
  ,get_field_values : function() {
      return Lino.fields2array(this.fields);
  }
  ,set_field_values : function(pv) {
      //~ console.log('20120203 MainPanel.set_param_values', pv);
      this.status_field_values = pv;
      if (pv) {
          this.form.my_loadRecord(pv);
          var record = { data: pv };
          this.before_row_edit(record);
      } else {
          this.form.reset(); 
          this.before_row_edit();
      }
  }
  ,config_containing_window : function(wincfg) { 
      wincfg.title = this.window_title;
      wincfg.keys = [
        { key: Ext.EventObject.ENTER, fn: this.on_ok }
      ]
      
      if (!wincfg.defaultButton) this.getForm().items.each(function(f){
          if(f.isFormField){ 
              wincfg.defaultButton = f;
              return false;
          }
      });

  }
});

    
Lino.fields2array = function(fields,values) {
    //~ console.log('20130605 fields2array gonna loop on', fields,values);
    var pv = Array(fields.length);
    for(var i=0; i < fields.length;i++) {
        var f = fields[i]
        if (values) 
          var v = values[f.name];
        else 
          var v = f.getValue();
        if (f.formatDate) {
            pv[i] = f.formatDate(v); 
        } else {
            pv[i] = v; // f.getValue(); 
        }
    }
    return pv;
}


Lino.FormPanel = Ext.extend(Ext.form.FormPanel,Lino.MainPanel);
Lino.FormPanel = Ext.extend(Lino.FormPanel,Lino.PanelMixin);
Lino.FormPanel = Ext.extend(Lino.FormPanel,{
  params_panel_hidden : false,
  save_action_name : null, 
  //~ base_params : {},
  //~ trackResetOnLoad : true,
  //~ query_params : {},
  //~ 20110119b quick_search_text : '',
  constructor : function(config,params){
    if (params) Ext.apply(config,params);
    this.base_params = {};
    //~ ww.config.base_params.query = ''; // 20111018
    //~ console.log(config);
    //~ console.log('FormPanel.constructor() 1',config)
    //~ Ext.applyIf(config,{base_params:{}});
    //~ console.log('FormPanel.constructor() 2',config)
      
    config.trackResetOnLoad = true;
    
    Lino.FormPanel.superclass.constructor.call(this, config);
      
    //~ this.set_base_param('$URL_PARAM_FILTER',null); // 20111018
    //~ this.set_base_param('$URL_PARAM_FILTER',''); // 20111018
      
  },
  initComponent : function(){
    
    this.containing_panel = this;

    //~ console.log("20111201 containing_window",this.containing_window,this);


    var actions = Lino.build_buttons(this, this.ls_bbar_actions);
    if (actions) {
        this.bbar = actions.bbar;
    //~ } else {
        //~ this.bbar = [];
    }
    //~ Ext.apply(config,Lino.build_buttons(this,config.ls_bbar_actions));
    //~ config.bbar = Lino.build_buttons(this,config.ls_bbar_actions);
    //~ var config = this;
    
    //~ if (this.containing_window instanceof Lino.DetailWrapper) {
    
    //~ console.log('20120121 initComponent', this.action_name);
    //~ if (this.action_name == 'detail' | this.action_name == 'show') {
    //~ if (this.action_name != 'insert') {
    if (! this.hide_top_toolbar) {
      this.tbar = [];
      // 20111015    
      if (! this.hide_navigator) {
        this.record_selector = new Lino.RemoteComboFieldElement({
          store: new Lino.ComplexRemoteComboStore({
            //~ baseParams: this.containing_window.config.base_params,
            baseParams: this.get_base_params(),
            //~ value: this.containing_window.config.base_params.query,
            proxy: new Ext.data.HttpProxy({
              url: '/choices' + this.ls_url,
              method:'GET'
            })
          }),
          pageSize:25,
          listeners: { 
            scope:this, 
            select:function(combo,record,index) {
              //~ console.log('jumpto_select',arguments);
              this.goto_record_id(record.id);
            }
          },
          emptyText: "Go to record"
        })
        this.tbar = this.tbar.concat([this.record_selector]);
        
        this.tbar = this.tbar.concat([
          this.first = new Ext.Toolbar.Button({
              tooltip:"Premier",disabled:true,
              handler:this.moveFirst,scope:this,iconCls:'x-tbar-page-first'}),
          this.prev = new Ext.Toolbar.Button({
              tooltip:"Previous",disabled:true,
              handler:this.movePrev,scope:this,iconCls:'x-tbar-page-prev'}),
          this.next = new Ext.Toolbar.Button({
              tooltip:"Next",disabled:true,
              handler:this.moveNext,scope:this,iconCls:'x-tbar-page-next'}),
          this.last = new Ext.Toolbar.Button({
              tooltip:"Last",disabled:true,
              handler:this.moveLast,scope:this,iconCls:'x-tbar-page-last'})
        ]);
      }
      this.tbar = this.add_params_panel(this.tbar);
      
      //~ console.log(20101117,this.containing_window.refresh);
      this.tbar = this.tbar.concat([
        {
          //~ text:'Refresh',
          handler:function(){ this.do_when_clean(false,this.refresh.createDelegate(this)) },
          iconCls: 'x-tbar-loading',
          tooltip:"Relire les données et actualiser l'écran",
          scope:this}
      ]);
          
      if (this.bbar) { // since 20121016
        if (this.tbar) {
            this.tbar = this.tbar.concat(['-']) ;
        } else {
          this.tbar = [];
        }
        this.tbar = this.tbar.concat(this.bbar) ;
        this.bbar = undefined;
      }
    
      this.tbar = this.tbar.concat([
          '->',
          this.displayItem = new Ext.Toolbar.TextItem({})
      ]);
          
    }
    //~ if (this.content_type && this.action_name != 'insert') {
      //~ this.bbar = this.bbar.concat([
        //~ '->',
        //~ { text: "[$_('Help Text Editor')]",
          //~ handler: Lino.help_text_editor,
          //~ qtip: "$_('Edit help texts for fields on this model.')",
          //~ scope: this}
      //~ ])
    //~ }
    //~ this.before_row_edit = config.before_row_edit.createDelegate(this);
      
    //~ if (this.master_panel) {
        //~ this.set_base_params(this.master_panel.get_master_params());
    //~ }
      
    Lino.FormPanel.superclass.initComponent.call(this);

    // this.on('show',
    //         function(){ this.init_focus();}, 
    //         this);
    
    this.on('render',function(){
      this.loadMask = new Ext.LoadMask(this.bwrap,{msg:"Veuillez patienter..."});
    },this);
    
    
    if (this.action_name == 'insert') {
      this.cascade(function(cmp){
        // console.log('20110613 cascade',cmp);
        if (cmp.disabled_in_insert_window) {
            //~ cmp.disable();
            cmp.hide();
        }
      });
      
    }
    
  },
  
  unused_init_focus : function(){ 
    // set focus to the first field
    console.log("20140205 Lino.FormPanel.init_focus");
    // Lino.FormPanel.superclass.focus.call(this);
    this.getForm().items.each(function(f){
        if(f.isFormField && f.rendered){ 
            f.focus();
            console.log("20140205 focus", f);
            return false;
        }
    });
  },

  /* FormPanel */
  get_status : function(){
      var st = {
        base_params: this.get_base_params(),
        // data_record : this.get_current_record()
        }
      st.record_id = this.get_current_record().id;
      // 20140917 : get_status must not store the whole data_record
      // because that would prevent the form to actually reload
      // when set_status is called after a child window closed.
      
      var tp = this.items.get(0);
      if (tp instanceof Ext.TabPanel) {
        st.active_tab = tp.getActiveTab();
      }
      st.param_values = this.status_param_values;
      return st;
  },

  /* FormPanel */
  set_status : function(status, rp){
    this.requesting_panel = Ext.getCmp(rp);
    // console.log('20140917 FormPanel.set_status()', status);
    this.clear_base_params();
    if (status == undefined) status = {};
    //~ if (status.param_values) 
    this.set_param_values(status.param_values);
    if (status.base_params) this.set_base_params(status.base_params);
    var tp = this.items.get(0);
    if (tp instanceof Ext.TabPanel) {
      if (status.active_tab) {
        //~ console.log('20111201 active_tab',this.active_tab,this.items.get(0));
        //~ tp.activeTab = status.active_tab;
        tp.setActiveTab(status.active_tab);
        //~ this.main_item.items.get(0).activate(status.active_tab);
      } else {
        if (! status.data_record) {  // 20141206
            tp.setActiveTab(0);
        }
      }
    }
    
    if (status.data_record) {
      /* defer because set_window_title() didn't work otherwise */
      // 20140421 removed defer for bughunting to simplify side effects
      // this.set_current_record.createDelegate(
      //     this, [status.data_record]).defer(100);
      this.set_current_record(status.data_record);
      //~ return;
    } else if (status.record_id != undefined) { 
      /* possible values include 0 and null, 0 being a valid record id, 
      null the equivalent of undefined
      */
      this.load_record_id(status.record_id);
    } else {
      this.set_current_record(undefined);
    }
    // this.init_focus()
  }
  ,get_base_params : function() {  /* FormPanel */
    // needed for insert_action
    var p = Ext.apply({}, this.base_params);
    Lino.insert_subst_user(p);
    return p;
  }
  ,set_base_params : function(p) {
    //~ this.base_params = Ext.apply({},this.base_params); // make sure it is an instance variable
    delete p['query'] // 20120725
    Ext.apply(this.base_params,p);
    if (this.record_selector) {
        var store = this.record_selector.getStore();
        for (k in p) store.setBaseParam(k,p[k]);
        delete this.record_selector.lastQuery;
        //~ console.log("20120725 record_selector.setBaseParam",p)
    }
  }
  ,clear_base_params : function() {
      this.base_params = {};
      Lino.insert_subst_user(this.base_params);
  }
  ,set_base_param : function(k,v) {
    this.base_params[k] = v;
  }
  ,after_delete : function() {
    if (this.current_record.navinfo.next)
      this.moveNext();
    else if (this.current_record.navinfo.prev)
      this.movePrev();
    else 
      this.abandon();
  }
  ,moveFirst : function() {this.goto_record_id(
      this.current_record.navinfo.first)}
  ,movePrev : function() {this.goto_record_id(
      this.current_record.navinfo.prev)}
  ,moveNext : function() {this.goto_record_id(
      this.current_record.navinfo.next)}
  ,moveLast : function() {this.goto_record_id(
      this.current_record.navinfo.last)}
  
  ,refresh : function(unused) { 
      this.refresh_with_after();
  }
  /* FormPanel */
  ,refresh_with_after : function(after) { 
    // console.log('20140917 Lino.FormPanel.refresh_with_after()',this);
    if (this.current_record) {
        this.load_record_id(this.current_record.id, after);
    } else {
        this.set_current_record(undefined, after);
    }
  }
  
  ,do_when_clean : function(auto_save, todo) {
    var this_ = this;
    if (this.form.isDirty()) {
        // console.log('20140421 do_when_clean : form is dirty')
        if (auto_save) {
            this_.save(todo);
        } else {
          //~ console.log('20111217 do_when_clean() form is dirty',this.form);
          var config = {title:"Confirmation"};
          config.buttons = Ext.MessageBox.YESNOCANCEL;
          config.msg = " Sauvegarder les modifications?";
          config.fn = function(buttonId,text,opt) {
            //~ console.log('do_when_clean',buttonId)
            if (buttonId == "yes") {
                //~ Lino.submit_detail(this_,undefined,todo);
                //~ this_.containing_window.save(todo);
                this_.save(todo);
            } else if (buttonId == "no") { 
              todo();
            }
          }
          Ext.MessageBox.show(config);
        }
    }else{
      // console.log('20140421 do_when_clean : now!')
      todo();
    }
  }
  
  ,goto_record_id : function(record_id) {
    // console.log('20140917 Lino.FormPanel.goto_record_id()',record_id);
    //~ var this_ = this;
    //~ this.do_when_clean(function() { this_.load_record_id(record_id) }
    this.do_when_clean(
        true, this.load_record_id.createDelegate(this, [record_id]));
  }
  
  ,load_record_id : function(record_id, after) {
    var this_ = this;
    var p = Ext.apply({}, this.get_base_params());
    if (this.action_name)
        p.an = this.action_name;
    p.rp = this.getId();
    p.fmt = 'json';
    this.add_param_values(p);
    if (this.loadMask) this.loadMask.show();
    Ext.Ajax.request({ 
      waitMsg: 'Loading record...',
      method: 'GET',
      params: p,
      scope: this,
      url: this.get_record_url(record_id),
      success: function(response) {   
        // todo: convert to Lino.action_handler.... but result 
        if (this.loadMask) this.loadMask.hide();
        if (response.responseText) {
          var rec = Ext.decode(response.responseText);
          // console.log('20150905 load_record_id success', rec);
          this.set_param_values(rec.param_values);
          this.set_current_record(rec, after);
        }
      },
      failure: Lino.ajax_error_handler(this)
    });
  }

  ,abandon : function () {
    Ext.MessageBox.alert('Note',
      "No more records to display. Detail window has been closed.");
    Lino.close_window();
  }
  
  ,set_current_record : function(record, after) {
    // console.log('20150905 set_current_record', record);
    if (this.record_selector) {
        this.record_selector.clearValue();
        // e.g. InsertWrapper FormPanel doesn't have a record_selector
    }
    this.current_record = record;
    if (record && record.data) {
      this.enable();
      this.form.my_loadRecord(record.data);
      this.set_window_title(record.title);
      //~ this.getBottomToolbar().enable();
      var da = record.data.disabled_actions;
      if (da) {
          //~ console.log('20120528 disabled_actions =',da,this.getBottomToolbar());
          //~ 20121016 this.getBottomToolbar().items.each(function(item,index,length){
          var tb = this.getTopToolbar();
          if (tb) tb.items.each(function(item,index,length){
              //~ console.log('20120528 ',item.itemId,'-->',da[item.itemId]);
              if (da[item.itemId]) item.disable(); else item.enable();
          });
      };
      if (this.disable_editing | record.data.disable_editing) {
          //~ console.log("20120202 disable_editing",record.title);
          this.form.items.each(function(cmp){
            if (!cmp.always_enabled) cmp.disable();
          },this);
      } else {
          this.form.items.each(function(cmp){
            //~ console.log("20120202",cmp);
            if (record.data.disabled_fields[cmp.name]) cmp.disable();
            else cmp.enable();
          },this);
        
          //~ if (record.data.disabled_fields) {
              //~ for (i = 0; i < record.data.disabled_fields.length; i++) {
                  //~ var flds = this.find('name',record.data.disabled_fields[i]);
                  //~ if (flds.length == 1) { 
                    //~ flds[0].disable(); 
                  //~ }
              //~ }
          //~ }
      };
      if (this.first) {
        if (record.navinfo  && ! this.hide_navigator) {
          this.first.setDisabled(!record.navinfo.first);
          this.prev.setDisabled(!record.navinfo.prev);
          this.next.setDisabled(!record.navinfo.next);
          this.last.setDisabled(!record.navinfo.last);
          this.displayItem.setText(record.navinfo.message);
        } else {
          this.first.setDisabled(true);
          this.prev.setDisabled(true);
          this.next.setDisabled(true);
          this.last.setDisabled(true);
        }
      }
    } else {
      if (this.form.rendered) 
        this.form.reset(); /* FileUploadField would fail when resetting a non-rendered form */
      //~ this.disable();
      //~ this.getBottomToolbar().disable();
      this.form.items.each(function(cmp){
        cmp.disable();
      },this);
      this.set_window_title(this.empty_title);
      //~ this.containing_window.window.setTitle(this.empty_title);
      if (!this.hide_navigator) {
        this.first.disable();
        this.prev.disable();
        this.next.disable();
        this.last.disable();
      }
    }
    // console.log('20140917 gonna call before_row_edit', record);
    this.before_row_edit(record);
    // console.log('20140917 gonna call after', after);
    if (after) after();
  },
  
  /* FormPanel */
  before_row_edit : function(record) {},
  search_change : function(field,oldValue,newValue) {
    //~ console.log('search_change',field.getValue(),oldValue,newValue)
    this.set_base_param('query',field.getValue()); 
    this.refresh();
  },
  
  get_selected : function() { return [ this.current_record ] },
  get_current_record : function() {  
    //~ console.log(20100714,this.current_record);
    return this.current_record 
  },
  
  get_permalink_url : function() {
      var rec = this.get_current_record();
      if (rec && ! rec.phantom && rec.id != -99998)
          return '/api' 
              + this.ls_url + '/' + rec.id;
      return '/api' + this.ls_url;
    
  },
  add_param_tab : function(p) {
    var main = this.items.get(0);
    if (main.activeTab) {
      var tab = main.items.indexOf(main.activeTab);
      // console.log('20150130 main.activeTab', tab, main.activeTab);
      if (tab) p.tab = tab;
    // } else {
    //   console.log('20150130 no main.activeTab');
    }
  },
  get_permalink_params : function() {
    var p = {};
    //~ var p = {an:'detail'};
    if (this.action_name)
        p.an = this.action_name;
    this.add_param_tab(p)
    this.add_param_values(p)
    return p;
  }
  
  ,validate_form : function() {  // not used. see actions.ValidateForm
      // var ov = {};
      // this.form.items.each(function(f){
      //     ov[f.name] = f.originalValue
      // });

      // console.log('20140509 FormPanel.validate_form', ov);
      // var after = function() { 
      //     this.form.items.each(function(f){
      //         f.originalValue = ov[f.name];
      //     });
      // }
      // this.save2(null, 'validate', after);
      this.save2(null, 'validate');
  }

  /* Lino.FormPanel */
  ,save : function(after) {
    var action_name = this.save_action_name;
    if (!action_name) 
        action_name = this.action_name;
    // console.log('20140503 FormPanel.save', action_name);
    this.save2(after, action_name);
  }

  ,save2 : function(after, action_name) {
    var rec = this.get_current_record();
    if (!rec) { 
        Lino.notify("Sorry, no current record."); 
        return; 
    }
    var panel = this;
    if (this.has_file_upload) this.form.fileUpload = true;
    this.loadMask.show();
    var p = {};
    Ext.apply(p, this.get_base_params());
    p.rp = this.getId();
    p.an = action_name;
    this.add_param_tab(p)
    // console.log('20150216 FormPanel.save()', rec, this.form);
    var submit_config = {
        params: p, 
        scope: this,
        success: function(form, action) {
          this.loadMask.hide();
          Lino.notify(action.result.message);
          Lino.handle_action_result(this, action.result, after);
        },
        failure: function(form,action) { 
          this.loadMask.hide();
          Lino.on_submit_failure(form, action);
        },
        clientValidation: true
    };
    if (rec.phantom) {  // it's a new record
      Ext.apply(submit_config, {
        url: '/api' + this.ls_url,
        method: 'POST'
      });
      // panel.refresh();
      // temporarily disabled. See 20151002
    } else {  // submit on existing row
      Ext.apply(submit_config, {
        url: '/api' 
              + this.ls_url + '/' + rec.id,
        method: 'PUT'
      })
    }
    this.form.submit(submit_config);
  }
  
  ,on_cancel : function() { 
    this.get_containing_window().close();
  }
  ,on_ok : function() { 
      // console.log("20140424");
      // this.save(null, true, this.save_action_name);
      this.save();
  }
  ,config_containing_window : function(wincfg) { 

      // Note that defaultButton means: which component should receive
      // focus when Window is focussed.  If no defaultButton set,
      // specify the first form field.

      if (!wincfg.defaultButton) this.getForm().items.each(function(f){
          if(f.isFormField){ 
              wincfg.defaultButton = f;
              // console.log("20140205 defaultButton", f);
              return false;
          }
      });

      wincfg.keys = [];

      wincfg.keys.push({
          key: Ext.EventObject.ESCAPE, 
          handler: this.on_cancel, scope:this });
      wincfg.keys.push({
          key: 's', ctrl: true, 
             stopEvent: true, handler: this.on_ok, scope:this });
  }
  
});



Lino.getRowClass = function(record, rowIndex, rowParams, store) {
    //~ console.log(20130816,record);
    //~ return 'x-grid3-row-green';
    //~ return record.data.row_class + ' auto-height';
    return record.data.row_class;
  //~ if (true) {
      //~ return 'x-grid3-row-red';
  //~ }
  //~ if (record.phantom) {
    //~ console.log(20101009,record);
    //~ rowParams.bodyStyle = "color:red;background-color:blue";
    //~ return 'lino-phantom-row';
    //~ }
  //~ console.log('20101009 not a phantom:',record);
  //~ return '';
}

//~ FOO = 0;



Lino.GridStore = Ext.extend(Ext.data.ArrayStore,{ 
  autoLoad: false
  ,load: function(options) {
    //~ foo.bar = baz; // 20120213
    if (!options) options = {};
    if (!options.params) options.params = {};
    options.params.fmt = 'json';
    options.params.rp = this.grid_panel.getId();
    Lino.insert_subst_user(options.params); // since 20121016
      
    var start = this.grid_panel.start_at_bottom ? -1 : 0;
    if (this.grid_panel.hide_top_toolbar) {
        //~ console.log("20120206 GridStore.load() toolbar is hidden");
        options.params.start = start;
        if (this.grid_panel.preview_limit) {
          options.params.limit = this.grid_panel.preview_limit;
        }
    } else {
        var ps = this.grid_panel.calculatePageSize();
        if (!ps) {
          // console.log("GridStore.load() failed to calculate pagesize");
          return false;
        } 
        options.params.limit = ps;
      
        this.grid_panel.getTopToolbar().pageSize =  ps;
        if (options.params.start == undefined)
            // if (start != -1) 
            //     start = this.grid_panel.getTopToolbar().cursor
            options.params.start = start;
      
        // console.log("20141108 GridStore.load() ", options.params);
    }
      
    this.grid_panel.add_param_values(options.params);
    //~ Lino.insert_subst_user(options.params);
    //~ console.log("20120814 GridStore.load()",options.params,this.baseParams);
    return Lino.GridStore.superclass.load.call(this, options);
  }
  // ,insert : function(index, records) {
  //   return Ext.data.Store.prototype.insert.call(this, index, records)
    // return Lino.GridStore.superclass.insert.call(this, index, records);
  // }
});

Lino.get_current_grid_config = function(panel) {
    return panel.get_current_grid_config();
}


// Like the default value for GridView.cellTpl but adds a class "lino-auto-height"
Lino.auto_height_cell_template = new Ext.Template(
'<td class="x-grid3-col x-grid3-cell x-grid3-td-{id} {css}" style="{style}" tabIndex="0" {cellAttr}>',
    '<div class="lino-auto-height x-grid3-cell-inner x-grid3-col-{id}" unselectable="on" {attr}>{value}</div>',
'</td>'
);

Lino.GridPanel = Ext.extend(Ext.grid.EditorGridPanel, Lino.MainPanel);
Lino.GridPanel = Ext.extend(Lino.GridPanel, Lino.PanelMixin);
Lino.GridPanel = Ext.extend(Lino.GridPanel, {
  quick_search_text : '',
  start_at_bottom : false,
  is_searching : false,
  disabled_in_insert_window : true,
  clicksToEdit:2,
  enableColLock: false,
  autoHeight: false,
  params_panel_hidden : false,
  preview_limit : undefined, 
  //~ loadMask: true,
  //~ viewConfig: {
          //~ getRowClass: Lino.getRowClass,
          //~ emptyText:"$_('No data to display.')"
        //~ },
        
        
  loadMask: {msg:"Veuillez patienter..."},
  
  constructor : function(config){

    config.plugins = [new Lino.GridFilters()];
    
    
    Lino.GridPanel.superclass.constructor.call(this,config);
    
    //~ if (this.containing_window) {
        //~ console.log("20111206 install refresh");
        //~ this.containing_window.on('show',this.refresh,this);
    //~ }
    
  },
  
  init_containing_window : function(win) { 
    //~ console.log("20111206 install refresh");
    //~ win.on('show',this.refresh,this);
  }

  ,handle_key_event : function(e) { 
    // console.log("20140514 handle_key_event", e, this.keyhandlers);
    var h = this.keyhandlers[e.keyCode];
    if (h) {
      h(this);
      e.stopEvent();
    }
  }
  
  ,initComponent : function(){
    
    /* 
    Problem 20111206:
    When a GridPanel is the main item of the window, then it doesn't 
    have it's own header but uses the window's header bar.
    We must do this in initComponent because e.g. in beforerender 
    it's already to late: a header element has been created because 
    there was a title.
    But Lino.Window adds itself as `this.containing_window` 
    only after the GridPanel has been initialized.
    Workaround is to generate a line "params.containing_window = true;" 
    in the handler function.
    */ 
    if (this.is_main_window) {
        //~ console.log(20111206, 'delete title',this.title,'from',this);
        this.tools = undefined;  
        this.title = undefined;  /* simply deleting it 
          isn't enough because that would only 
          unhide the title defined in some base class. */
    } 
    //~ else console.log(20111206, 'dont delete title',this.title,'from',this);
    
    /* e.g. when slave gridwindow called from a permalink */
    //~ if (this.base_params) Ext.apply(bp,this.base_params);  
    
    var proxy = new Ext.data.HttpProxy({ 
      // 20120814 
      url: '/api' + this.ls_url
      ,method: "GET"
      //~ ,url: ADMIN_URL + '/restful' + this.ls_url
      //~ ,restful: true 
      //~ ,listeners: {load:on_proxy_load} 
      //~ ,listeners: {write:on_proxy_write} 
    });
    //~ config.store = new Ext.data.JsonStore({ 
    //~ this.store = new Ext.data.ArrayStore({ 
    this.store = new Lino.GridStore({ 
      grid_panel: this
      ,listeners: { exception: Lino.on_store_exception }
      ,remoteSort: true
      ,totalProperty: "count"
      ,root: "rows"
      //~ ,id: "id" 
      ,proxy: proxy
      //~ autoLoad: this.containing_window ? true : false
      ,idIndex: this.pk_index
      //~ ,baseParams: bp
      ,fields: this.ls_store_fields
      ,idProperty: this.ls_id_property 
      // 20120814
      //~ ,writer : new Ext.data.JsonWriter({
        //~ writeAllFields: false
        //~ ,listful: true
      //~ })
      //~ ,restful : true
    });
      
    //~ console.log('config.pk_index',config.pk_index,config.store),
    delete this.ls_store_fields;
      
    var this_ = this;
    //~ var grid = this;
    this.store.on('load', function() {
        //~ console.log('20120814 GridStore.on(load)',this_.store);
        this_.set_param_values(this_.store.reader.arrayData.param_values);
        //~ this_.set_status(this_.store.reader.arrayData.status);
        //~ 20120918
        this.getView().getRowClass = Lino.getRowClass;
        
        if (this_.store.reader.arrayData.no_data_text) {
            //~ this.viewConfig.emptyText = this_.store.reader.arrayData.no_data_text;
            this.getView().emptyText = this_.store.reader.arrayData.no_data_text;
            this.getView().refresh();
        }
        if (this_.containing_window)
            this_.set_window_title(this_.store.reader.arrayData.title);
            //~ this_.containing_window.setTitle(this_.store.reader.arrayData.title);
        if (!this.is_searching) { // disabled 20121025: quick_search_field may not lose focus
          this.is_searching = false;
          if (this_.selModel.getSelectedCell){
              if (this_.getStore().getCount()) // there may be no data
                  this_.selModel.select(0,0); 
          } else {
              this_.selModel.selectFirstRow();
              this_.getView().focusEl.focus();
          }
        } 
        //~ else console.log("is_searching -> no focussing");
        //~ var t = this.getTopToolbar();
        //~ var activePage = Math.ceil((t.cursor + t.pageSize) / t.pageSize);
        //~ this.quick_search_field.focus(); // 20121024
      }, this
    );
    var actions = Lino.build_buttons(this, this.ls_bbar_actions);
    //~ Ext.apply(config,Lino.build_buttons(this,config.ls_bbar_actions));
    //~ config.bbar, this.cmenu = Lino.build_buttons(this,config.ls_bbar_actions);
    //~ this.cmenu = new Ext.menu.Menu({items: config.bbar});
    delete this.ls_bbar_actions
    if (actions) {
        this.cmenu = actions.cmenu;
        this.keyhandlers = actions.keyhandlers;
    }
    
    if (!this.hide_top_toolbar) {  
      var tbar = [ 
        this.quick_search_field = new Ext.form.TextField({ 
          //~ fieldLabel: "Search"
          listeners: { 
            scope:this_
            //~ ,change:this_.search_change
            
            ,render: Lino.quicktip_renderer("Quick Search","Enter a text to use as quick search filter")
            
            //~ ,keypress: this.search_keypress 
            ,blur: function() { this.is_searching = false}
          }
          ,validator:function(value) { return this_.search_validate(value) }
          //~ ,tooltip: "Enter a quick search text, then press TAB"
          //~ value: text
          //~ scope:this, 
          //~ ,enableKeyEvents: true
          //~ listeners: { keypress: this.search_keypress }, 
          //~ id: "seachString" 
      })];
      tbar = this.add_params_panel(tbar);
      var menu = [];
      var set_gc = function(index) {
        return function() {
          //~ console.log('set_gc() 20100812');
          this.getColumnModel().setConfig(
              this.apply_grid_config(index,this.ls_grid_configs,this.ls_columns));
        }
      }
      for (var i = 0; i < this.ls_grid_configs.length;i++) {
        var gc = this.ls_grid_configs[i];
        menu.push({text:gc.label,handler:set_gc(i),scope:this})
      }
      if(menu.length > 1) {
        tbar = tbar.concat([
          { text:"View",
            menu: menu,
            tooltip:"Select another view of this report"
          }
        ]);
      }
      
      if (actions) {
        tbar = tbar.concat(actions.bbar);
          //~ this.bbar = actions.bbar;
      }
      
      this.tbar = new Ext.PagingToolbar({ 
        store: this.store, 
        prependButtons: true, 
        //~ pageSize: this.page_length, 
        pageSize: 1, 
        displayInfo: true, 
        beforePageText: "Page",
        afterPageText: "de {0}",
        displayMsg: "Enregistrements {0} - {1} de {2}",
        firstText: "Première page",
        lastText: "Dernière page",
        prevText: "Page précédente",
        nextText: "Page suivante",
        items: tbar
      });
    }
      
    if (this.cell_edit) {
      this.selModel = new Ext.grid.CellSelectionModel()
      this.get_selected = function() {
        //~ console.log(this.getSelectionModel().selection);
        if (this.selModel.selection)
            return [ this.selModel.selection.record ];
        return [this.store.getAt(0)];
      };
      this.get_current_record = function() { 
        if (this.getSelectionModel().selection) 
          return this.selModel.selection.record;
        return this.store.getAt(0);
      };
    } else { 
      this.selModel = new Ext.grid.RowSelectionModel() 
      this.get_selected = function() {
        var sels = this.selModel.getSelections();
        if (sels.length == 0) sels = [this.store.getAt(0)];
        return sels
      };
      this.get_current_record = function() { 
        var rec = this.selModel.getSelected();
        if (rec == undefined) rec = this.store.getAt(0);
        return rec
      };
    };
    this.columns  = this.apply_grid_config(this.gc_name,this.ls_grid_configs,this.ls_columns);
    
    Lino.GridPanel.superclass.initComponent.call(this);
    
    this.on('resize', function(){
      //~ console.log("20120213 resize",arguments)
      this.refresh();
      },this);
    this.on('viewready', function(){
      //~ console.log("20120213 resize",arguments);
      this.view_is_ready = true;
      this.refresh(); // removed 20130911
      },this);
    this.on('afteredit', this.on_afteredit); // 20120814
    this.on('beforeedit', this.on_beforeedit);
    this.on('beforeedit',function(e) { this.before_row_edit(e.record)},this);
    if (this.cell_edit) {
        this.on('cellcontextmenu', Lino.cell_context_menu, this);
    } else {
        this.on('rowcontextmenu', Lino.row_context_menu, this);
    }
    //~ this.on('contextmenu', Lino.grid_context_menu, this);
    
    delete this.cell_edit;
    
  },
  
  //~ onResize : function(){
      //~ console.log("20120206 GridPanel.onResize",arguments);
      //~ Lino.GridPanel.superclass.onResize.apply(this, arguments);
      //~ this.refresh();
  //~ },
  
  
  get_status : function(){
    var st = { base_params : this.get_base_params()};
    if (!this.hide_top_toolbar) {
        // #866
        var totalLength = this.getStore().totalLength;
        if (this.getStore().lastOptions != undefined && this.getStore().lastOptions.params != undefined){
            st.current_page = Math.round(this.getStore().lastOptions.params.start / totalLength ) + 1 ;
        }
    }
    st.param_values = this.status_param_values;
    //~ console.log("20120213 GridPanel.get_status",st);
    return st;
  },
  
  /* 
  Lino.GridPanel.set_status() 
  */
  set_status : function(status, rp){
    this.requesting_panel = Ext.getCmp(rp);
    // console.log("20140527 GridPanel.set_status", status);
    this.clear_base_params();
    if (status == undefined) status = {base_params:{}};
    this.set_param_values(status.param_values);
    if (status.base_params) { 
      this.set_base_params(status.base_params);
    }
    if (status.show_params_panel != undefined) {
        if (this.toggle_params_panel_btn) {
            //~ this.toggle_params_panel_btn.toggle(status.show_params_panel=='true');
            this.toggle_params_panel_btn.toggle(status.show_params_panel);
        }
    }
    if (!this.hide_top_toolbar) {
      //~ console.log("20120213 GridPanel.getTopToolbar().changePage",
          //~ status.current_page || 1);
      this.getTopToolbar().changePage(status.current_page || 1);
    }
    //~ this.fireEvent('resize');
    //~ this.refresh.defer(100,this); 
    //~ this.onResize.defer(100,this); 
    //~ this.refresh(); 
    //~ this.doLayout(); 
    //~ this.onResize(); 
    //~ this.store.load();
  },
  
  refresh : function(unused) { 
    this.refresh_with_after();
  },
  /* GridPanel */
  refresh_with_after : function(after) { 
    // console.log('20140504 Lino.GridPanel.refresh '+ this.store.proxy.url);
    //~ var bp = { fmt:'json' }
    if (! this.view_is_ready) return;
    
    if (this.containing_panel) {
        //~ Ext.apply(p,this.master_panel.get_master_params());
        //~ Ext.apply(options.params,this.containing_panel.get_master_params());
        this.set_base_params(this.containing_panel.get_master_params());
        // 20130911
        if (!this.store.baseParams.mk) {  
            return;
        }
    }
    
    //~ console.log('20130911 Lino.GridPanel.refresh_with_after',this.containing_panel.get_master_params());
    
    var options = {};
    if (after) {
        options.callback = function(r,options,success) {if(success) after()}
    }
      
    //~ if (!this.rendered) {
        //~ console.log("20120206 GridPanel.refresh() must wait until rendered",options);
        //~ this.grid_panel.on('render',this.load.createDelegate(this,options))
        //~ return;
    //~ }
    // Ticket 802
    if (this.store.lastOptions != undefined){
        var params = {};
        params.limit = this.store.lastOptions.params.limit;
        params.start = this.store.lastOptions.params.start;
        options.params = params;
    }
    this.store.load(options);
  },
  
  /* pageSize depends on grid height (Trying to remove scrollbar)
  Thanks to 
  - Christophe Badoit on http://www.sencha.com/forum/showthread.php?82647
  - http://www.sencha.com/forum/archive/index.php/t-37231.html
  */
  calculatePageSize : function(second_attempt) {
    //~ if (!this.rendered) { 
    if (!this.view_is_ready) { 
      //~ console.log('Cannot calculatePageSize() : not rendered');
      return false; }
    //~ if (!this.isVisible()) { 
      //~ console.log('calculatePageSize : not visible');
      //~ return false; }
      
    //~ console.log('getFrameHeight() is',this.getFrameHeight());
    //~ console.log('getView().scroller.getHeight() is',this.getView().scroller.getHeight());
    //~ console.log('mainBody.getHeight() is',this.getView().mainBody.getHeight());
    //~ console.log('getInnerHeight() is',this.getInnerHeight());
    //~ console.log('getHeight() is',this.getHeight());
    //~ console.log('el.getHeight() is',this.getEl().getHeight());
    //~ console.log('getGridEl().getHeight() is',this.getGridEl().getHeight());
    //~ console.log('getOuterSize().height is',this.getOuterSize().height);
    //~ console.log('getBox().height is',this.getBox().height);
    //~ console.log('getResizeEl.getHeight() is',this.getResizeEl().getHeight());
    //~ console.log('getLayoutTarget().getHeight() is',this.getLayoutTarget().getHeight());
      
    //~ var rowHeight = 52; // experimental value
    var row = this.view.getRow(0);
    if (row) {
      //~ console.log('20120213 yes');
      var rowHeight = Ext.get(row).getHeight();
    } else {
        //~ var rowHeight = this.getFrameHeight();
        //~ var rowHeight = 10; // reasonably smallest approximative value
        //~ There is no data yet. Construct a fake row and get its height
        var Element = Ext.Element;
        var gv = this.view;
        var fakeBody = new Element(Element.fly(gv.scroller).child('div.x-grid3-body'));
        var rowTemplate = gv.templates.row;
        var cellTemplate = gv.templates.cell;
        var tstyle  = 'width:' + gv.getGridInnerWidth() + 'px;';
        var cells = cellTemplate.apply({value:'&#160;'});
        var markup = rowTemplate.apply({
                tstyle: tstyle,
                cols  : 1,
                cells : cells,
                alt   : ''
            });        
        fakeBody.dom.innerHTML = gv.templates.body.apply({rows: markup});
        var row = fakeBody.dom.childNodes[0];
        var rowHeight = Ext.get(row).getHeight();
    }
    //~ console.log('rowHeight is ',rowHeight,this,caller);
    //~ this.getView().syncScroll();
    //~ this.getView().initTemplates();
    var height = this.getView().scroller.getHeight();
    //~ console.log('getView().scroller.getHeight() is',this.getView().scroller.getHeight());
    //~ console.log('getInnerHeight() - getFrameHeight() is',
      //~ this.getInnerHeight(), '-',
      //~ this.getFrameHeight(), '=',
      //~ this.getInnerHeight() - this.getFrameHeight());
    //~ var height = this.getView().mainBody.getHeight();
    //~ var height = this.getView().mainWrap.getHeight();
    //~ var height = this.getView().resizeMarker.getHeight();
    //~ this.syncSize();
    //~ var height = this.getInnerHeight() - this.getFrameHeight();
    //~ var height = this.getHeight() - this.getFrameHeight();
    height -= Ext.getScrollBarWidth(); // leave room for a possible horizontal scrollbar... 
    //~ height -= this.getView().scrollOffset;
    var ps = Math.floor(height / rowHeight);
    //~ console.log('20130816 calculatePageSize():',height,'/',rowHeight,'->',ps);
    ps -= 1; // leave room for a possible phantom row
    //~ return (ps > 1 ? ps : false);
    if (ps > 1) return ps;
    //~ console.log('calculatePageSize() found less than 1 row:',height,'/',rowHeight,'->',ps);
    //~ foo.bar = baz; // 20120213
    return 5; // preview_limit
    //~ if (second_attempt) {
        //~ console.log('calculatePageSize() abandons after second attempt:',
          //~ height,'/',rowHeight,'->',ps);
      //~ return 5;
    //~ }
    //~ return this.calculatePageSize.defer(500,this,[true]);
  },
  
  onCellDblClick : function(grid, row, col){
      //~ console.log("20120307 onCellDblClick",this,grid, row, col);
      if (this.ls_detail_handler) {
          //~ Lino.notify('show detail');
          Lino.show_detail(this);
          return false;
      }else{
        //~ console.log('startEditing');
        this.startEditing(row,col);
      }
  },
  get_base_params : function() {  /* Lino.GridPanel */
    var p = Ext.apply({}, this.store.baseParams);
    Lino.insert_subst_user(p);
    // if (this.quick_search_field)
    //     if (this.quick_search_field.getValue())
    //         p.query = this.quick_search_field.getValue();
    return p;
  },
  set_base_params : function(p) {
    //~ console.log('20130911 GridPanel.set_base_params',p)
    for (k in p) this.store.setBaseParam(k,p[k]);
    //~ this.store.baseParams = p;
    if (this.quick_search_field)
      this.quick_search_field.setValue(p.query || "");
    //~ if (p.param_values) 
        //~ this.set_param_values(p.param_values);  
  },
  clear_base_params : function() {
      this.store.baseParams = {};
      Lino.insert_subst_user(this.store.baseParams);
  },
  set_base_param : function(k,v) {
    this.store.setBaseParam(k,v);
  },
  
  //~ get_permalink_params : function() {
    //~ var p = {};
    //~ return p;
  //~ },
  
  before_row_edit : function(record) {},
    
  //~ search_keypress : function(){
    //~ console.log("2012124 search_keypress",arguments);
  //~ },
  search_validate : function(value) {
    if (value == this.quick_search_text) return true;
    this.is_searching = true;
    //~ console.log('search_validate',value)
    this.quick_search_text = value;
    this.set_base_param('query',value); 
    //~ this.getTopToolbar().changePage(1);
    this.getTopToolbar().moveFirst();
    //~ this.refresh();
    return true;
  },
  
  search_change : function(field,oldValue,newValue) {
    //~ console.log('search_change',field.getValue(),oldValue,newValue)
    this.set_base_param('query',field.getValue()); 
    this.getTopToolbar().moveFirst();
    //~ this.refresh();
  },
  
  apply_grid_config : function(index,grid_configs,rpt_columns) {
    //~ var rpt_columns = this.ls_columns;
    var gc = grid_configs[index];    
    //~ console.log('apply_grid_config() 20100812',name,gc);
    this.gc_name = index;
    if (gc == undefined) {
      return rpt_columns;
      //~ config.columns = config.ls_columns;
      //~ return;
    } 
    //~ delete config.ls_filters
    
    //~ console.log(20100805,config.ls_columns);
    var columns = Array(gc.columns.length);
    for (var j = 0; j < rpt_columns.length;j++) {
      var col = rpt_columns[j];
      for (var i = 0; i < gc.columns.length; i++) {
        if (col.dataIndex == gc.ci[i]) {
          col.width = gc.cw[i];
          col.hidden = gc.ch[i];
          columns[i] = col;
          break;
        }
      }
    }
    
    //~ var columns = Array(rpt_columns.length);
    //~ for (var i = 0; i < rpt_columns.length; i++) {
      //~ columns[i] = rpt_columns[gc.columns[i]];
      //~ columns[i].width = gc.widths[i];
    //~ }
    
    //~ if (gc.hidden_cols) {
      //~ for (var i = 0; i < gc.hidden_cols.length; i++) {
        //~ var hc = gc.hidden_cols[i];
        //~ for (var j = 0; j < columns.length;j++) {
          //~ var col = columns[j];
          //~ if (col.dataIndex == hc) {
            //~ col.hidden = true;
            //~ break
          //~ }
        //~ }
      //~ }
    //~ }
    if (gc.filters) {
      //~ console.log(20100811,'config.ls_filters',config.ls_filters);
      //~ console.log(20100811,'config.ls_grid_config.filters',config.ls_grid_config.filters);
      for (var i = 0; i < gc.filters.length; i++) {
        var fv = gc.filters[i];
        for (var j = 0; j < columns.length;j++) {
          var col = columns[j];
          if (col.dataIndex == fv.field) {
            //~ console.log(20100811, f,' == ',fv);
            if (fv.type == 'string') {
              col.filter.value = fv.value;
              //~ if (fv.comparison !== undefined) f.comparison = fv.comparison;
            } else {
              //~ console.log(20100811, fv);
              col.filter.value = {};
              col.filter.value[fv.comparison] = fv.value;
            }
            break;
          }
        };
      }
    }
    
    return columns;
    //~ config.columns = cols;
    //~ delete config.ls_columns
  },
  
  get_current_grid_config : function () {
    var cm = this.getColumnModel();
    var widths = Array(cm.config.length);
    var hiddens = Array(cm.config.length);
    //~ var hiddens = Array(cm.config.length);
    var columns = Array(cm.config.length);
    //~ var columns = Array(cm.config.length);
    //~ var hidden_cols = [];
    //~ var filters = this.filters.getFilterValues();
    var p = this.filters.buildQuery(this.filters.getFilterData())
    for (var i = 0; i < cm.config.length; i++) {
      var col = cm.config[i];
      columns[i] = col.dataIndex;
      //~ hiddens[i] = col.hidden;
      widths[i] = col.width;
      hiddens[i] = col.hidden;
      //~ if (col.hidden) hidden_cols.push(col.dataIndex);
    }
    //~ p['hidden_cols'] = hidden_cols;
    p.cw = widths;
    p.ch = hiddens;
    p.ci = columns;
    //~ p['widths'] = widths;
    //~ p['hiddens'] = hiddens;
    //~ p['columns'] = columns;
    p['name'] = this.gc_name;
    //~ var gc = this.ls_grid_configs[this.gc_name];
    //~ if (gc !== undefined) 
        //~ p['label'] = gc.label
    //~ console.log('20100810 save_grid_config',p);
    return p;
  },
  
  unused_manage_grid_configs : function() {
    var data = [];
    for (k in this.ls_grid_configs) {
      var v = this.ls_grid_configs[k];
      var i = [k,String(v.columns),String(v.hidden_cols),String(v.filters)];
      data.push(i)
    }
    if (this.ls_grid_configs[this.gc_name] == undefined) {
      var v = this.get_current_grid_config();
      var i = [k,String(v.columns),String(v.hidden_cols),String(v.filters)];
      data.push(i);
    }
    //~ console.log(20100811, data);
    var main = new Ext.grid.GridPanel({
      store: new Ext.data.ArrayStore({
        idIndex:0,
        fields:['name','columns','hidden_cols','filters'],
        autoDestroy:true,
        data: data}),
      //~ autoHeight:true,
      selModel: new Ext.grid.RowSelectionModel(),
      listeners: { 
        rowdblclick: function(grid,rowIndex,e) {
          console.log('row doubleclicked',grid, rowIndex,e);
        },
        rowclick: function(grid,rowIndex,e) {
          console.log('row clicked',grid, rowIndex,e);
        }
      },
      columns: [ 
        {dataIndex:'name',header:'Name'}, 
        {dataIndex:'columns',header:'columns'}, 
        {dataIndex:'hidden_cols',header:'hidden columns'}, 
        {dataIndex:'filters',header:'filters'} 
      ]
    });
    var win = new Ext.Window({title:'GridConfigs Manager',layout:'fit',items:main,height:200});
    win.show();
  },
  
  unused_edit_grid_config : function(name) {
    gc = this.ls_grid_configs[name];
    var win = new Ext.Window({
      title:'Edit Grid Config',layout:'vbox', 
      //~ layoutConfig:'stretch'
      items:[
        {xtype:'text', value: gc.name},
        {xtype:'text', value: gc.columns},
        {xtype:'text', value: gc.hidden_cols},
        {xtype:'text', value: gc.filters}
      ]
    });
    win.show();
  },
  
  unused_save_grid_config : function () {
    //~ console.log('TODO: save_grid_config',this);
    //~ p.column_widths = Ext.pluck(this.colModel.columns,'width');
    var a = { 
      params:this.get_current_grid_config(), 
      method:'PUT',
      url:'/grid_config' + this.ls_url,
      success: Lino.action_handler(this),
      scope: this,
      failure: Lino.ajax_error_handler(this)
    };
    this.loadMask.show(); // 20120211
    Ext.Ajax.request(a);
    //~ Lino.do_action(this,a);
  },
  
  on_beforeedit : function(e) {
    //~ console.log('20130128 GridPanel.on_beforeedit()',e,e.record.data.disable_editing);
    if(this.disable_editing | e.record.data.disable_editing) {
      e.cancel = true;
      Lino.notify("This record is disabled");
      return;
    }
    if(e.record.data.disabled_fields && e.record.data.disabled_fields[e.field]) {
      e.cancel = true;
      Lino.notify("This field is disabled");
      return;
    }
    //~ if (e.record.data.disabled_fields) {
      //~ for (i in e.record.data.disabled_fields) {
        //~ if(e.record.data.disabled_fields[i] == e.field) {
          //~ e.cancel = true;
          //~ Lino.notify(String.format('Field "{0}" is disabled for this record',e.field));
          //~ return
        //~ }
      //~ }
    //~ }
  },
  save_grid_data : function() {
      //~ console.log("20120814 save_grid_data");
      this.getStore().commitChanges();
  },
  on_afteredit : function(e) {
    /*
    e.grid - The grid that fired the event
    e.record - The record being edited
    e.field - The field name being edited
    e.value - The value being set
    e.originalValue - The original value for the field, before the edit.
    e.row - The grid row index
    e.column - The grid column index
    */
    var p = {};
    // console.log('20140403 afteredit: ',e.record);
    //~ console.log('20101130 value: ',e.value);
    //~ var p = e.record.getChanges();
    //~ console.log('20101130 getChanges: ',e.record.getChanges());
    //~ this.before_row_edit(e.record);

    for(k in e.record.getChanges()) {
        var v = e.record.get(k);
    //~ for(k in e.record.modified) {
        //~ console.log('20101130',k,'=',v);
        //~ var cm = e.grid.getColumnModel();
        //~ var di = cm.getDataIndex(k);
        var f = e.record.fields.get(k);
        //~ console.log('20101130 f = ',f);
        //~ var v = e.record.get(di);
        if (f.type.type == 'date') {
            p[k] = Ext.util.Format.date(v, f.dateFormat);
        }else{
            p[k] = v;
            var v = e.record.get(k+'Hidden');
            if (v !== undefined) {
              p[k+'Hidden'] = v;
            }
        }
    }
    // add value used by ForeignKeyStoreField CHOICES_HIDDEN_SUFFIX
    // not sure whether this is still needed:
    p[e.field+'Hidden'] = e.value;
    //~ p.su = Lino.subst_user;
    Lino.insert_subst_user(p);
    // this one is needed so that this field can serve as choice context:
    e.record.data[e.field+'Hidden'] = e.value;
    // p[pk] = e.record.data[pk];
    // console.log("grid_afteredit:",e.field,'=',e.value);
    Ext.apply(p, this.get_base_params()); // needed for POST, ignored for PUT
    //~ Ext.apply(p,this.containing_window.config.base_params);
    //~ 20121109 p['$constants.URL_PARAM_ACTION_NAME'] = 'grid';
    var self = this;
    var req = {
        params:p,
        waitMsg: 'Saving your data...',
        success: Lino.action_handler( this, function(result) {
          // console.log("20140728 afteredit.success got ", result);
          //~ if (result.data_record) {
          if (result.refresh_all) {
              var cw = self.get_containing_window();
              if (cw) {
                  cw.main_item.refresh();
              }
              else console.log("20120123 cannot refresh_all",self);
          } else if (result.rows) {
              //~ self.getStore().loadData(result,true);
              var r = self.getStore().reader.readRecords(result);
              if (e.record.phantom) {
                  // console.log("20140728 gonna call Store.insert()", self.getStore(), e.row, r.records);
                  self.getStore().insert(e.row, r.records);
              }else{
                  // console.log("20140728 afteredit.success doUpdate", r.records[0]);
                  self.getStore().doUpdate(r.records[0]);
              }
              self.getStore().rejectChanges(); 
              /* 
              get rid of the red triangles without saving the record again
              */
              //~ self.getStore().commitChanges(); // get rid of the red triangles
          } else {
              self.getStore().commitChanges(); // get rid of the red triangles
              self.getStore().reload();        // reload our datastore.
          }
          }),
        scope: this,
        failure: Lino.ajax_error_handler(this)
    };
    if (e.record.phantom) {
      req.params.an = 'grid_post'; // CreateRow.action_name
      Ext.apply(req,{
        method: 'POST',
        url: '/api' + this.ls_url
      });
    } else {
      req.params.an = 'grid_put'; // SaveRow.action_name
      Ext.apply(req,{
        method: 'PUT',
        url: '/api' + this.ls_url + '/' + e.record.id
      });
    }
    //~ console.log('20110406 on_afteredit',req);
    this.loadMask.show(); // 20120211
    Ext.Ajax.request(req);
  },

  afterRender : function() {
    Lino.GridPanel.superclass.afterRender.call(this);
    // this.getView().mainBody.focus();
    // console.log(20100114,this.getView().getRows());
    // if (this.getView().getRows().length > 0) {
    //  this.getView().focusRow(1);
    // }
    //~ this.my_load_mask = new Ext.LoadMask(this.getEl(), {
        //~ msg:'$_("Please wait...")',
        //~ store:this.store});
      
    var tbar = this.getTopToolbar();
    // tbar.on('change',function() {this.getView().focusRow(1);},this);
    // tbar.on('change',function() {this.getSelectionModel().selectFirstRow();this.getView().mainBody.focus();},this);
    // tbar.on('change',function() {this.getView().mainBody.focus();},this);
    // tbar.on('change',function() {this.getView().focusRow(1);},this);
    this.nav = new Ext.KeyNav(this.getEl(),{
      pageUp: function() {tbar.movePrevious(); },
      pageDown: function() {tbar.moveNext(); },
      home: function() {tbar.moveFirst(); },
      end: function() {tbar.moveLast(); },
      scope: this
    });

  },
  after_delete : function() {
    //~ console.log('Lino.GridPanel.after_delete');
    this.refresh();
  },
  add_row_listener : function(fn,scope) {
    this.getSelectionModel().addListener('rowselect',fn,scope);
  },
  postEditValue : function(value, originalValue, r, field){
    value = Lino.GridPanel.superclass.postEditValue.call(this,value,originalValue,r,field);
    //~ console.log('GridPanel.postEdit()',value, originalValue, r, field);
    return value;
  },
  
  set_start_value : function(v) {
      this.start_value = v;
  },
  preEditValue : function(r, field){
      if (this.start_value) {
        var v = this.start_value;
        delete this.start_value;
        this.activeEditor.selectOnFocus = false;
        return v;
      }
      var value = r.data[field];
      return this.autoEncode && Ext.isString(value) ? Ext.util.Format.htmlDecode(value) : value;
  },
  
  on_master_changed : function() {
    //~ if (! this.enabled) return;
    //~ cmp = this;
    //~ console.log('20130911 Lino.GridPanel.on_master_changed()',this.title,this.rendered);
    if (! this.rendered) return; // 20120213
    var todo = function() {
      if (this.disabled) return;
      //~ if (this.disabled) return;
      //~ if (this.enabled) {
          //~ var src = caller.config.url_data + "/" + record.id + ".jpg"
          //~ console.log(20111125, this.containing_window);
          //~ for (k in p) this.getStore().setBaseParam(k,p[k]);
          //~ console.log('Lino.GridPanel.on_master_changed()',this.title,p);
          this.refresh();
          //~ this.set_base_params(this.master_panel.get_master_params());
          //~ this.getStore().load(); 
      //~ }
    };
    Lino.do_when_visible(this,todo.createDelegate(this));
  },
  load_record_id : function(record_id,after) {
      Lino.run_detail_handler(this,record_id)
  }
  
});
  

//~ Lino.MainPanelMixin = {
  //~ tbar_items : function() {
      //~ return ;
  //~ }
//~ };

//~ Ext.override(Lino.GridPanel,Lino.MainPanelMixin);
//~ Ext.override(Lino.FormPanel,Lino.MainPanelMixin);

//~ Lino.grid_context_menu = function(e) {
  //~ console.log('contextmenu',arguments);
//~ }

Lino.row_context_menu = function(grid,row,col,e) {
  console.log('20130927 rowcontextmenu',grid,row,col,e,grid.store.reader.arrayData.rows[row]);
}

Lino.cell_context_menu = function(grid,row,col,e) {
  //~ console.log('20120531 cellcontextmenu',grid,row,col,e,grid.store.reader.arrayData.rows[row]);
  e.stopEvent();
  //~ grid.getView().focusCell(row,col);
  grid.getSelectionModel().select(row,col);
  //~ console.log(grid.store.getAt(row));
  //~ grid.getView().focusRow(row);
  //~ return;
  if(!grid.cmenu.el){grid.cmenu.render(); }
  //~ if(e.record.data.disabled_fields) {
  
  var da = grid.store.reader.arrayData.rows[row][grid.disabled_actions_index];
  if (da) {
      this.cmenu.cascade(function(item){ 
        //~ console.log(20120531, item.itemId, da[item.itemId]);
        if (da[item.itemId]) item.disable(); else item.enable();
      });
  };
  
  var xy = e.getXY();
  xy[1] -= grid.cmenu.el.getHeight();
  grid.cmenu.showAt(xy);
}


Lino.chooser_handler = function(combo,name) {
  return function(cmp, newValue, oldValue) {
    //~ console.log('Lino.chooser_handler()',cmp,oldValue,newValue);
    combo.setContextValue(name, newValue);
  }
};



Lino.ComboBox = Ext.extend(Ext.form.ComboBox,{
  forceSelection: "yes but select on tab",
  // forceSelection: true,
  triggerAction: 'all',
  minListWidth:280, // 20131022
  autoSelect: false,
  selectOnFocus: true, // select any existing text in the field immediately on focus.
  submitValue: true,
  displayField: 'text', // 'text', 
  valueField: 'value', // 'value',
  
  //~ initComponent : Ext.form.ComboBox.prototype.initComponent.createSequence(function() {
  initComponent : function(){
      this.contextParams = {};
      //~ Ext.form.ComboBox.initComponent(this);
      Lino.ComboBox.superclass.initComponent.call(this);
  },
  setValue : function(v, record_data){
      /*
      Based on feature request developed in http://extjs.net/forum/showthread.php?t=75751
      */
      /* `record_data` is used to get the text corresponding to this value */
      //~ if(this.name == 'city') 
      //~ console.log('20120203', this.name,'.setValue(', v ,') this=', this,'record_data=',record_data);
      var text = v;
      if(this.valueField){
        if(v == null || v == '') { 
            //~ if (this.name == 'birth_country') 
                //~ console.log(this.name,'.setValue',v,'no lookup needed, value is empty');
            //~ v = undefined;
            v = '';
            //~ text = '';
        } else if (Ext.isDefined(record_data)) {
          text = record_data[this.name];
          //~ if (this.name == 'birth_country') 
            //~ console.log(this.name,'.setValue',v,'got text ',text,' from record ',record);
        } else {
          // if(this.mode == 'remote' && !Ext.isDefined(this.store.totalLength)){
          if(this.mode == 'remote' && ( this.lastQuery === null || (!Ext.isDefined(this.store.totalLength)))){
              //~ if (this.name == 'birth_country') console.log(this.name,'.setValue',v,'store not yet loaded');
              this.store.on('load', this.setValue.createDelegate(this, arguments), null, {single: true});
              if(this.store.lastOptions === null || this.lastQuery === null){
                  var params;
                  if(this.valueParam){
                      params = {};
                      params[this.valueParam] = v;
                  }else{
                      var q = this.allQuery;
                      this.lastQuery = q;
                      this.store.setBaseParam(this.queryParam, q);
                      params = this.getParams(q);
                  }
                  //~ if (this.name == 'birth_country') 
                    //~ console.log(this.name,'.setValue',v,' : call load() with params ',params);
                  this.store.load({params: params});
              //~ }else{
                  //~ if (this.name == 'birth_country') 
                    //~ console.log(this.name,'.setValue',v,' : but store is loading',this.store.lastOptions);
              }
              return;
          //~ }else{
              //~ if (this.name == 'birth_country') 
                //~ console.log(this.name,'.setValue',v,' : store is loaded, lastQuery is "',this.lastQuery,'"');
          }
          var r = this.findRecord(this.valueField, v);
          if(r){
              text = r.data[this.displayField];
          }else if(this.valueNotFoundText !== undefined){
              text = this.valueNotFoundText;
          }
        }
      }
      this.lastSelectionText = text;
      //~ this.lastSelectionText = v;
      if(this.hiddenField){
          //~ this.hiddenField.originalValue = v;
          this.hiddenField.value = v;
      }
      Ext.form.ComboBox.superclass.setValue.call(this, text);
      this.value = v; // needed for grid.afteredit
  },
  
  getParams : function(q){
    // p = Ext.form.ComboBox.superclass.getParams.call(this, q);
    // causes "Ext.form.ComboBox.superclass.getParams is undefined"
    var p = {};
    if(this.pageSize){
        p['start'] = 0;
        p['limit'] = this.pageSize;
    }
    // now my code:
    if(this.contextParams) Ext.apply(p, this.contextParams);
    return p;
  },
  setContextValue : function(name,value) {
    //~ console.log('setContextValue',this,this.name,':',name,'=',value);
    //~ if (this.contextValues === undefined) {
        //~ this.contextValues = Array(); // this.contextParams.length);
    //~ }
    if (this.contextParams[name] != value) {
      //~ console.log('setContextValue 1',this.contextParams);
      this.contextParams[name] = value;
      this.lastQuery = null;
      //~ console.log('setContextValue 2',this.contextParams);
    }
  }
});

Lino.ChoicesFieldElement = Ext.extend(Lino.ComboBox,{
  mode: 'local'
});


Lino.SimpleRemoteComboStore = Ext.extend(Ext.data.JsonStore,{
  // forceSelection: true,  20140206 why was this here?
  constructor: function(config){
      Lino.SimpleRemoteComboStore.superclass.constructor.call(this, Ext.apply(config, {
          totalProperty: 'count',
          root: 'rows',
          id: 'value', // 'value'
          fields: ['value' ], 
          listeners: { exception: Lino.on_store_exception }
      }));
  }
});

Lino.ComplexRemoteComboStore = Ext.extend(Ext.data.JsonStore,{
  constructor: function(config){
      Lino.ComplexRemoteComboStore.superclass.constructor.call(this, Ext.apply(config, {
          totalProperty: 'count',
          root: 'rows',
          id: 'value', // constants.CHOICES_VALUE_FIELD
          fields: ['value','text'], // constants.CHOICES_VALUE_FIELD, // constants.CHOICES_TEXT_FIELD
          listeners: { exception: Lino.on_store_exception }
      }));
  }
});

Lino.RemoteComboFieldElement = Ext.extend(Lino.ComboBox,{
  mode: 'remote',
  //~ forceSelection:false,
  minChars: 2, // default 4 is too much
  queryDelay: 300, // default 500 is maybe slow
  queryParam: 'query', 
  //~ typeAhead: true,
  //~ selectOnFocus: true, // select any existing text in the field immediately on focus.
  resizable: true
  ,initList : function() {
      Lino.RemoteComboFieldElement.superclass.initList.call(this);
      if (this.pageTb) {
          
          var me = this;
          this.pageTb.on("beforechange", function(toolbar, o){
              if(me.contextParams)
                  Ext.apply(o, me.contextParams);
          });
          
          //~ 
          //~ var btn = ls_buttons
          //~ this.pageTb.items = this.pageTb.items.concat([btn]);
          //~ console.log("20131022 pageTb.items is", this.pageTb.items)
      }
  }
});

/*
Thanks to Animal for posting the basic idea:
http://www.sencha.com/forum/showthread.php?15842-2.0-SOLVED-Combobox-twintrigger-clear&p=76130&viewfull=1#post76130

*/
Lino.TwinCombo = Ext.extend(Lino.RemoteComboFieldElement,{
    trigger2Class : 'x-form-search-trigger',
    //~ trigger2Class : 'x-tbar-detail',
    initComponent : function() {
        //~ Lino.TwinCombo.superclass.initComponent.call(this);
        Lino.ComboBox.prototype.initComponent.call(this);
        Ext.form.TwinTriggerField.prototype.initComponent.call(this);
    },
    onTrigger2Click : function() {
        //~ console.log('onTrigger2Click',this,arguments);
    }
  });
//~ Lino.TwinCombo.prototype.initComponent = Ext.form.TwinTriggerField.prototype.initComponent;
Lino.TwinCombo.prototype.getTrigger = Ext.form.TwinTriggerField.prototype.getTrigger;
Lino.TwinCombo.prototype.getOuterSize = Ext.form.TwinTriggerField.prototype.getOuterSize;
Lino.TwinCombo.prototype.initTrigger = Ext.form.TwinTriggerField.prototype.initTrigger;
Lino.TwinCombo.prototype.onTrigger1Click = Ext.form.ComboBox.prototype.onTriggerClick;
//~ Lino.TwinCombo.prototype.onTrigger2Click = function() {
    //~ console.log('onTrigger2Click',arguments);
//~ };



Lino.SimpleRemoteComboFieldElement = Ext.extend(Lino.RemoteComboFieldElement,{
  displayField: 'value', 
  valueField: null,
  forceSelection: false
});




Lino.Window = Ext.extend(Ext.Window,{
  //~ layout: "fit", 
  closeAction : 'hide',
  renderTo: 'main_area', 
  constrain: true,
  maximized: true,
  draggable: false,
  width: 700,
  height: 500,
  maximizable: false,
  constructor : function (config) {
    if (config.main_item.params_panel) {
        config.layout = 'border';
        config.main_item.region = 'center';
        config.main_item.params_panel.region = 'north';
        //~ config.main_item.params_panel.autoHeight = false; // 20130924
        config.main_item.params_panel.hidden = config.main_item.params_panel_hidden;
        config.items = [config.main_item.params_panel, config.main_item];
        //~ 20130923b
    } else {
        config.layout = 'fit';
        config.items = config.main_item;
    }
    this.main_item = config.main_item; 

    if (typeof config.width == "string" && config.width.slice(-1) == "%") {
        config.width = Lino.perc2width(parseInt(config.width.slice(0, -1)));
    }
    
    delete config.main_item;
    //~ delete config.params_item;
    
    //~ this.main_item = config.items.get(0);
    this.main_item.containing_window = this;
    
    //~ console.log('20120110 Lino.Window.constructor() 1');
    //~ if (Lino.current_window) { // all windows except the top are closable
    if (this.main_item.hide_window_title) { 
      config.closable = false;
      config.frame = false;
      config.shadow = false;
      //~ config.border = true;
      //~ config.title = undefined;
      //~ config.tools = null;
      delete config.title;
      delete config.tools;
    } else {
      config.title = this.main_item.empty_title;
      config.closable = true;
      config.tools = [ 
        { qtip: 'permalink', handler: Lino.permalink_handler(this), id: "pin" }
      ];
      if (this.main_item.content_type && this.main_item.action_name != 'insert') {
        config.tools = [ {
          handler: Lino.help_text_editor,
          qtip: "Edit help texts for fields on this model.",
          scope: this.main_item,
          id: "gear"
        }].concat(config.tools);
      }
        
    //~ { qtip: '', handler: Lino.save_wc_handler(this), id: "save" }, 
    //~ { qtip: this.config.qtip, handler: Lino.save_wc_handler(this), id: "save" }, 
    //~ { qtip: 'Call doLayout() on main Container.', handler: Lino.refresh_handler(this), id: "refresh" },
    //~ if (this.main_item.params_panel) {
        //~ config.tools = config.tools.concat([ 
          //~ { qtip: 'Show/hide parameter panel', handler: this.toggle_params_panel, id: "gear", scope:this } 
        //~ ]);
    //~ }
    //~ if (config.closable !== false) {
      // if undefined, will take default behaviour
      //~ config.tools = config.tools.concat([ 
        //~ { qtip: 'close', handler: this.hide, id: "close", scope:this } 
      //~ ]);
    }
    
    this.main_item.config_containing_window(config);
    
    // console.log('20150514 Lino.Window.constructor() 2');
    Lino.Window.superclass.constructor.call(this, config);
    
    //~ console.log('20120110 Lino.Window.constructor() 3');
    
  },
  initComponent : function() {
    this.main_item.init_containing_window(this);
    Lino.Window.superclass.initComponent.call(this);
  
  },
  hide : function() { 
      this.main_item.do_when_clean(false,function() { 
        Lino.close_window(); });
  },
  hide_really : function() { 
    Lino.Window.superclass.hide.call(this);
  },
  onRender : function(ct, position){
    // console.log('20140829 Lino.Window.onRender() 1');
    Lino.Window.superclass.onRender.call(this, ct, position);
    var main_area = Ext.getCmp('main_area')
    //~ console.log('20120110 Lino.Window.onRender() 2');
  
    this.on('show', function(win) {
        // console.log('20140829 Lino.Window.on(show) : add resize handler');
        main_area.on('resize', win.onWindowResize, win);
    });
    this.on('hide', function(win) {
        // console.log('20140829 Lino.Window.on(hide) : remove resize handler');
        main_area.un('resize', win.onWindowResize, win);
    });
    // console.log('20140829 Lino.Window.onRender() 3');
  }
});


Ext.override(Ext.form.BasicForm,{
    my_loadRecord : function(record_data){
    //~ loadRecord : function(record){
        /* Same as ExtJS's loadRecord() (setValues()), except that we
        forward also the record_data to field.setValue(). This second
        parameter is used by Lino.Combobox.
        */
        //~ console.log('20120918 my_loadRecord', record_data)
        if(Ext.isArray(record_data)){ 
            for(var i = 0, len = record_data.length; i < len; i++){
                var v = record_data[i];
                var f = this.findField(v.id);
                if(f){
                    f.setValue(v.value, record_data);
                    if(this.trackResetOnLoad){
                        f.originalValue = f.getValue();
                    }
                }
            }
        }else{ 
            var field, id;
            for(id in record_data){
                if(!Ext.isFunction(record_data[id]) && (field = this.findField(id))){
                    field.setValue(record_data[id], record_data);
                    if(this.trackResetOnLoad){
                        field.originalValue = field.getValue();
                        //~ if (field.hiddenField) {
                          //~ field.hiddenField.originalValue = field.hiddenField.value;
                        //~ }
                    }
                }
            }
        }
        return this;
    }
});




function initializeFooBarDropZone(cmp) {
    //~ console.log('initializeFooBarDropZone',cmp);
    cmp.dropTarget = new Ext.dd.DropTarget(cmp.bwrap, {
      //~ ddGroup     : 'gridDDGroup',
      notifyEnter : function(ddSource, e, data) {
        console.log('notifyEnter',ddSource,e,data);
        //Add some flare to invite drop.
        cmp.body.stopFx();
        cmp.body.highlight();
      },
      notifyDrop  : function(ddSource, e, data){
        console.log('notifyDrop',ddSource,e,data);
        // Reference the record (single selection) for readability
        //~ var selectedRecord = ddSource.dragData.selections[0];


        // Load the record into the form
        //~ formPanel.getForm().my_loadRecord(selectedRecord);


        // Delete record from the grid.  not really required.
        //~ ddSource.grid.store.remove(selectedRecord);

        return(true);
      }
    })
}



Lino.show_mti_child = function(fieldname,detail_handler) {
  //~ console.log('show_mti_child',this);
  //~ console.log('show_mti_child',panel.find("main_area"));
  rec = Lino.current_window.main_item.get_current_record();
  //~ rec = panel.get_current_record();
  if (rec) {
    //~ console.log('show_mti_child',Lino.current_window,rec);
    if (rec.phantom) {
      Lino.notify('Not allowed on phantom record.');
    }else if (rec.data[fieldname]) {
      //~ console.log('show_mti_child',rec.id);
      //~ detail_handler(Lino.current_window.main_item,{},{record_id:rec.id});
      detail_handler.run(null,{record_id:rec.id});
      //~ window.open(urlroot + '/' + rec.id);
      //~ document.location = urlroot + '/' + rec.id;
      //~ window.open(urlroot + '/' + rec.id,'_blank');
    } else {
      Lino.alert("Cannot show MTI child if checkbox is off.");
    }
  } else {
    Lino.notify('No current record.');
  }
};


/*
captureEvents utility by Aaron Conran
<http://www.sencha.com/learn/grid-faq/>

Ext.onReady(function(){
    var grid = new Ext.grid.GridPanel({
        ... 
    });
    captureEvents(grid);
});
*/
function captureEvents(observable) {
    Ext.util.Observable.capture(
        observable,
        function(eventName) {
            console.info(eventName);
        },
        this
    );		
}

// settings.SITE.get_plugin_snippets()



Lino.main_menu = [ { "menu": { "items": [ { "handler": function() {Lino.concepts.Concepts.grid.run(null)}, "text": "Concepts " }, { "handler": function() {Lino.countries.Countries.grid.run(null)}, "listeners": { "render": Lino.quicktip_renderer("Foo","\n    A country is a geographic entity considered a \"nation\".\n    ") }, "text": "Pays" }, { "handler": function() {Lino.countries.Places.grid.run(null)}, "listeners": { "render": Lino.quicktip_renderer("Foo","\n    The table of known geographical places.\n    A geographical place can be a city, a town, a suburb,\n    a province, a lake... any named geographic entity,\n    except for countries because these have their own table.\n    ") }, "text": "Endroits" } ] }, "text": "Concepts " }, { "handler": function() {Lino.handle_home_button()}, "text": "D\u00e9part" } ];
Ext.namespace('Lino.system.SiteConfigs')
Ext.namespace('Lino.countries.Countries')
Ext.namespace('Lino.countries.Places')
Ext.namespace('Lino.concepts.Concepts')
Ext.namespace('Lino.concepts.TopLevelConcepts')
Ext.namespace('Lino.concepts.Links')
Ext.namespace('Lino.belref.Main')
Ext.namespace('Lino.countries.PlacesByPlace')
Ext.namespace('Lino.countries.PlacesByCountry')
Ext.namespace('Lino.concepts.Parents')
Ext.namespace('Lino.concepts.Children')
Ext.namespace('Lino.about.Models')
Ext.namespace('Lino.about.FieldsByModel')
Ext.namespace('Lino.about.Inspector')
Ext.namespace('Lino.about.SourceFiles')
Ext.namespace('Lino.about.About')
Ext.namespace('Lino.system.PeriodEvents')
Ext.namespace('Lino.concepts.LinkTypes')
Ext.namespace('Lino.system.YesNo')
Ext.namespace('Lino.system.Genders')
Ext.namespace('Lino.countries.PlaceTypes')
Ext.namespace('Lino.printing.BuildMethods')

// ChoiceLists: 
Lino.system.PeriodEvents = [ [ "10", "D\u00e9bute" ], [ "20", "Est active" ], [ "30", "Termine" ] ];
Lino.concepts.LinkTypes = [ [ "10", "Jargon" ], [ "20", "Obsoletes" ] ];
Lino.system.YesNo = [ [ "y", "Oui" ], [ "n", "Non" ] ];
Lino.system.Genders = [ [ "M", "Masculin" ], [ "F", "F\u00e9minin" ] ];
Lino.countries.PlaceTypes = [ [ "10", "Member State" ], [ "11", "Division" ], [ "12", "Region" ], [ "13", "Community" ], [ "14", "Territory" ], [ "20", "County" ], [ "21", "Province" ], [ "22", "Shire" ], [ "23", "Subregion" ], [ "24", "Department" ], [ "25", "Arrondissement" ], [ "26", "Prefecture" ], [ "27", "District" ], [ "28", "Sector" ], [ "50", "Ville" ], [ "51", "Ville" ], [ "52", "Municipality" ], [ "54", "Parish" ], [ "55", "Township" ], [ "56", "Quartier" ], [ "61", "Borough" ], [ "62", "Small borough" ], [ "70", "Village" ] ];
Lino.printing.BuildMethods = [ [ "latex", "LatexBuildMethod" ], [ "pisa", "PisaBuildMethod" ], [ "rtf", "RtfBuildMethod" ] ];

Lino.about.Inspector.ParamsPanel = Ext.extend(Ext.form.FormPanel, {
  autoHeight: true,
  frame: true,
  layoutConfig: { "align": "stretchmax" },
  hideCheckBoxLabels: true,
  autoScroll: false,
  labelWidth: 153,
  border: false,
  bodyBorder: false,
  labelAlign: "top",
  layout: 'hbox',
  autoHeight: true,
  initComponent : function() {
    var inspected1 = new Ext.form.TextField({ "anchor": "-20", "autoHeight": true, "fieldLabel": "Inspected object", "listeners": { "render": Lino.quicktip_renderer("Inspected object","(about.Inspector.inspected) ") }, "maxLength": 100, "name": "inspected", "selectOnFocus": true });
    var show_callables2 = new Ext.form.Checkbox({ "anchor": "-20", "autoHeight": true, "boxLabel": "show callables", "checked": false, "hideLabel": true, "listeners": { "render": Lino.quicktip_renderer("show callables","(about.Inspector.show_callables) ") }, "name": "show_callables", "selectOnFocus": true });
    this.items = [ { "autoHeight": true, "flex": 67, "items": inspected1, "labelAlign": "top", "layout": "form", "xtype": "panel" }, { "autoHeight": true, "flex": 32, "items": show_callables2, "labelAlign": "top", "layout": "form", "xtype": "panel" } ];
    this.fields = [ inspected1, show_callables2 ];
    Lino.about.Inspector.ParamsPanel.superclass.initComponent.call(this);
  }
});


Lino.countries.Countries.InsertFormPanel = Ext.extend(Lino.FormPanel,{
  layout: 'fit',
  auto_save: true,
  autoHeight: true,
  initComponent : function() {
    var isocode6 = new Ext.form.TextField({ "allowBlank": false, "anchor": "-20", "autoHeight": true, "boxMinWidth": Lino.chars2width(4), "fieldLabel": "<span style=\"border-bottom: 1px dotted #000000;\">ISO code</span>", "listeners": { "render": Lino.quicktip_renderer("ISO code","(countries.Countries.isocode)         The two-letter code for this country as defined by ISO 3166-1.\n        For countries that no longer exist it may be a 4-letter code.") }, "maxLength": 4, "name": "isocode", "selectOnFocus": true });
    var inscode7 = new Ext.form.TextField({ "anchor": "-20", "autoHeight": true, "boxMinWidth": Lino.chars2width(3), "fieldLabel": "<span style=\"border-bottom: 1px dotted #000000;\">INS code</span>", "listeners": { "render": Lino.quicktip_renderer("INS code","(countries.Countries.inscode) The official code for this country used by statbel.fgov.be") }, "maxLength": 3, "name": "inscode", "selectOnFocus": true });
    var main_1_panel8 = new Ext.Panel({ "anchor": "-20", "autoHeight": true, "autoScroll": false, "border": false, "frame": false, "hideCheckBoxLabels": true, "items": [ { "autoHeight": true, "flex": 50, "items": isocode6, "labelAlign": "top", "layout": "form", "xtype": "panel" }, { "autoHeight": true, "flex": 50, "items": inscode7, "labelAlign": "top", "layout": "form", "xtype": "panel" } ], "labelAlign": "top", "labelWidth": 81, "layout": "hbox", "layoutConfig": { "align": "stretchmax" } });
    var name11 = new Ext.form.TextField({ "allowBlank": false, "anchor": "-20", "autoHeight": true, "fieldLabel": "D\u00e9signation", "listeners": { "render": Lino.quicktip_renderer("D\u00e9signation","(countries.Countries.name) ") }, "maxLength": 200, "name": "name", "selectOnFocus": true });
    var name_nl12 = new Ext.form.TextField({ "anchor": "-20", "autoHeight": true, "fieldLabel": "D\u00e9signation (nl)", "listeners": { "render": Lino.quicktip_renderer("D\u00e9signation (nl)","(countries.Countries.name_nl) ") }, "maxLength": 200, "name": "name_nl", "selectOnFocus": true });
    var name_de13 = new Ext.form.TextField({ "anchor": "-20", "autoHeight": true, "fieldLabel": "D\u00e9signation (de)", "listeners": { "render": Lino.quicktip_renderer("D\u00e9signation (de)","(countries.Countries.name_de) ") }, "maxLength": 200, "name": "name_de", "selectOnFocus": true });
    var main_2_panel14 = new Ext.Panel({ "anchor": "-20", "autoHeight": true, "autoScroll": false, "border": false, "frame": false, "hideCheckBoxLabels": true, "items": [ { "autoHeight": true, "flex": 33, "items": name11, "labelAlign": "top", "layout": "form", "xtype": "panel" }, { "autoHeight": true, "flex": 33, "items": name_nl12, "labelAlign": "top", "layout": "form", "xtype": "panel" }, { "autoHeight": true, "flex": 33, "items": name_de13, "labelAlign": "top", "layout": "form", "xtype": "panel" } ], "labelAlign": "top", "labelWidth": 153, "layout": "hbox", "layoutConfig": { "align": "stretchmax" } });
    var main_panel18 = new Ext.Panel({ "autoHeight": true, "autoScroll": false, "bodyBorder": false, "border": false, "frame": true, "hideCheckBoxLabels": true, "items": [ main_1_panel8, main_2_panel14 ], "labelAlign": "top", "layout": "form" });
    this.items = main_panel18;
    this.before_row_edit = function(record) {
    }
    Lino.countries.Countries.InsertFormPanel.superclass.initComponent.call(this);
  }
});


Lino.system.SiteConfigs.DetailFormPanel = Ext.extend(Lino.FormPanel,{
  layout: 'fit',
  auto_save: true,
  initComponent : function() {
    var default_build_method19 = new Lino.ChoicesFieldElement({ "anchor": "-20", "autoHeight": true, "fieldLabel": "M\u00e9thode de constuction par d\u00e9fault", "forceSelection": true, "hiddenName": "default_build_methodHidden", "listeners": { "render": Lino.quicktip_renderer("M\u00e9thode de constuction par d\u00e9fault","(system.SiteConfigs.default_build_method) ") }, "name": "default_build_method", "selectOnFocus": true, "store": [['','<br>']].concat(Lino.printing.BuildMethods) });
    var main_panel20 = new Ext.Panel({ "autoScroll": false, "bodyBorder": false, "border": false, "frame": true, "hideCheckBoxLabels": true, "items": [ { "autoHeight": true, "items": default_build_method19, "labelAlign": "top", "layout": "form", "xtype": "panel" } ], "labelAlign": "top", "labelWidth": 315, "layout": "fit" });
    this.items = main_panel20;
    this.before_row_edit = function(record) {
    }
    Lino.system.SiteConfigs.DetailFormPanel.superclass.initComponent.call(this);
  }
});


Lino.countries.Countries.DetailFormPanel = Ext.extend(Lino.FormPanel,{
  layout: 'fit',
  auto_save: true,
  initComponent : function() {
    var isocode22 = new Ext.form.TextField({ "allowBlank": false, "anchor": "-20", "autoHeight": true, "boxMinWidth": Lino.chars2width(4), "fieldLabel": "<span style=\"border-bottom: 1px dotted #000000;\">ISO code</span>", "listeners": { "render": Lino.quicktip_renderer("ISO code","(countries.Countries.isocode)         The two-letter code for this country as defined by ISO 3166-1.\n        For countries that no longer exist it may be a 4-letter code.") }, "maxLength": 4, "name": "isocode", "selectOnFocus": true });
    var name23 = new Ext.form.TextField({ "allowBlank": false, "anchor": "-20", "autoHeight": true, "fieldLabel": "D\u00e9signation", "listeners": { "render": Lino.quicktip_renderer("D\u00e9signation","(countries.Countries.name) ") }, "maxLength": 200, "name": "name", "selectOnFocus": true });
    var name_nl24 = new Ext.form.TextField({ "anchor": "-20", "autoHeight": true, "fieldLabel": "D\u00e9signation (nl)", "listeners": { "render": Lino.quicktip_renderer("D\u00e9signation (nl)","(countries.Countries.name_nl) ") }, "maxLength": 200, "name": "name_nl", "selectOnFocus": true });
    var name_de25 = new Ext.form.TextField({ "anchor": "-20", "autoHeight": true, "fieldLabel": "D\u00e9signation (de)", "listeners": { "render": Lino.quicktip_renderer("D\u00e9signation (de)","(countries.Countries.name_de) ") }, "maxLength": 200, "name": "name_de", "selectOnFocus": true });
    var short_code26 = new Ext.form.TextField({ "anchor": "-20", "autoHeight": true, "boxMinWidth": Lino.chars2width(4), "fieldLabel": "<span style=\"border-bottom: 1px dotted #000000;\">Short code</span>", "listeners": { "render": Lino.quicktip_renderer("Short code","(countries.Countries.short_code) A short abbreviation for regional usage. Obsolete.") }, "maxLength": 4, "name": "short_code", "selectOnFocus": true });
    var inscode27 = new Ext.form.TextField({ "anchor": "-20", "autoHeight": true, "boxMinWidth": Lino.chars2width(3), "fieldLabel": "<span style=\"border-bottom: 1px dotted #000000;\">INS code</span>", "listeners": { "render": Lino.quicktip_renderer("INS code","(countries.Countries.inscode) The official code for this country used by statbel.fgov.be") }, "maxLength": 3, "name": "inscode", "selectOnFocus": true });
    var main_1_panel28 = new Ext.Panel({ "autoHeight": true, "autoScroll": false, "border": false, "frame": false, "hideCheckBoxLabels": true, "items": [ { "autoHeight": true, "flex": 10, "items": isocode22, "labelAlign": "top", "layout": "form", "xtype": "panel" }, { "autoHeight": true, "flex": 22, "items": name23, "labelAlign": "top", "layout": "form", "xtype": "panel" }, { "autoHeight": true, "flex": 22, "items": name_nl24, "labelAlign": "top", "layout": "form", "xtype": "panel" }, { "autoHeight": true, "flex": 22, "items": name_de25, "labelAlign": "top", "layout": "form", "xtype": "panel" }, { "autoHeight": true, "flex": 10, "items": short_code26, "labelAlign": "top", "layout": "form", "xtype": "panel" }, { "autoHeight": true, "flex": 10, "items": inscode27, "labelAlign": "top", "layout": "form", "xtype": "panel" } ], "labelAlign": "top", "labelWidth": 153, "layout": "hbox", "layoutConfig": { "align": "stretchmax" } });
    var countries_PlacesByCountry_grid99 = new Lino.countries.PlacesByCountry.GridPanel({ "containing_panel": this, "flex": 83, "hide_top_toolbar": true, "listeners": { "render": Lino.quicktip_renderer("Endroits","(countries.countries.PlacesByCountry) ") }, "master_panel": this, "preview_limit": 15, "tools": [ Lino.show_in_own_window_button(Lino.countries.PlacesByCountry.grid) ] });
    var main_panel100 = new Ext.Panel({ "autoScroll": false, "bodyBorder": false, "border": false, "frame": true, "hideCheckBoxLabels": true, "items": [ main_1_panel28, countries_PlacesByCountry_grid99 ], "labelAlign": "top", "layout": "vbox", "layoutConfig": { "align": "stretch" } });
    this.items = main_panel100;
    this.before_row_edit = function(record) {
      countries_PlacesByCountry_grid99.on_master_changed();
    }
    Lino.countries.Countries.DetailFormPanel.superclass.initComponent.call(this);
  }
});


Lino.concepts.Concepts.DetailFormPanel = Ext.extend(Lino.FormPanel,{
  layout: 'fit',
  auto_save: true,
  initComponent : function() {
    var name101 = new Ext.form.TextField({ "allowBlank": false, "anchor": "-20", "autoHeight": true, "fieldLabel": "D\u00e9signation", "listeners": { "render": Lino.quicktip_renderer("D\u00e9signation","(concepts.Concepts.name) ") }, "maxLength": 200, "name": "name", "selectOnFocus": true });
    var name_nl102 = new Ext.form.TextField({ "anchor": "-20", "autoHeight": true, "fieldLabel": "D\u00e9signation (nl)", "listeners": { "render": Lino.quicktip_renderer("D\u00e9signation (nl)","(concepts.Concepts.name_nl) ") }, "maxLength": 200, "name": "name_nl", "selectOnFocus": true });
    var name_de103 = new Ext.form.TextField({ "anchor": "-20", "autoHeight": true, "fieldLabel": "D\u00e9signation (de)", "listeners": { "render": Lino.quicktip_renderer("D\u00e9signation (de)","(concepts.Concepts.name_de) ") }, "maxLength": 200, "name": "name_de", "selectOnFocus": true });
    var main_1_panel104 = new Ext.Panel({ "autoHeight": true, "autoScroll": false, "border": false, "frame": false, "hideCheckBoxLabels": true, "items": [ { "autoHeight": true, "flex": 33, "items": name101, "labelAlign": "top", "layout": "form", "xtype": "panel" }, { "autoHeight": true, "flex": 33, "items": name_nl102, "labelAlign": "top", "layout": "form", "xtype": "panel" }, { "autoHeight": true, "flex": 33, "items": name_de103, "labelAlign": "top", "layout": "form", "xtype": "panel" } ], "labelAlign": "top", "labelWidth": 153, "layout": "hbox", "layoutConfig": { "align": "stretchmax" } });
    var abbr108 = new Ext.form.TextField({ "anchor": "-20", "autoHeight": true, "fieldLabel": "Abbr\u00e9viation", "listeners": { "render": Lino.quicktip_renderer("Abbr\u00e9viation","(concepts.Concepts.abbr) ") }, "maxLength": 30, "name": "abbr", "selectOnFocus": true });
    var abbr_nl109 = new Ext.form.TextField({ "anchor": "-20", "autoHeight": true, "fieldLabel": "Abbr\u00e9viation (nl)", "listeners": { "render": Lino.quicktip_renderer("Abbr\u00e9viation (nl)","(concepts.Concepts.abbr_nl) ") }, "maxLength": 30, "name": "abbr_nl", "selectOnFocus": true });
    var abbr_de110 = new Ext.form.TextField({ "anchor": "-20", "autoHeight": true, "fieldLabel": "Abbr\u00e9viation (de)", "listeners": { "render": Lino.quicktip_renderer("Abbr\u00e9viation (de)","(concepts.Concepts.abbr_de) ") }, "maxLength": 30, "name": "abbr_de", "selectOnFocus": true });
    var main_2_panel111 = new Ext.Panel({ "autoHeight": true, "autoScroll": false, "border": false, "frame": false, "hideCheckBoxLabels": true, "items": [ { "autoHeight": true, "flex": 33, "items": abbr108, "labelAlign": "top", "layout": "form", "xtype": "panel" }, { "autoHeight": true, "flex": 33, "items": abbr_nl109, "labelAlign": "top", "layout": "form", "xtype": "panel" }, { "autoHeight": true, "flex": 33, "items": abbr_de110, "labelAlign": "top", "layout": "form", "xtype": "panel" } ], "labelAlign": "top", "labelWidth": 162, "layout": "hbox", "layoutConfig": { "align": "stretchmax" } });
    var definition115 = new Ext.form.TextArea({ "anchor": "-20 -10", "fieldLabel": "D\u00e9finition", "growMax": 2000, "listeners": { "render": Lino.quicktip_renderer("D\u00e9finition","(concepts.Concepts.definition) ") }, "name": "definition", "selectOnFocus": true });
    var definition_nl116 = new Ext.form.TextArea({ "anchor": "-20 -10", "fieldLabel": "D\u00e9finition (nl)", "growMax": 2000, "listeners": { "render": Lino.quicktip_renderer("D\u00e9finition (nl)","(concepts.Concepts.definition_nl) ") }, "name": "definition_nl", "selectOnFocus": true });
    var definition_de117 = new Ext.form.TextArea({ "anchor": "-20 -10", "fieldLabel": "D\u00e9finition (de)", "growMax": 2000, "listeners": { "render": Lino.quicktip_renderer("D\u00e9finition (de)","(concepts.Concepts.definition_de) ") }, "name": "definition_de", "selectOnFocus": true });
    var main_3_panel118 = new Ext.Panel({ "autoScroll": false, "border": false, "flex": 38, "frame": false, "hideCheckBoxLabels": true, "items": [ { "flex": 33, "items": definition115, "labelAlign": "top", "layout": "form", "xtype": "panel" }, { "flex": 33, "items": definition_nl116, "labelAlign": "top", "layout": "form", "xtype": "panel" }, { "flex": 33, "items": definition_de117, "labelAlign": "top", "layout": "form", "xtype": "panel" } ], "labelAlign": "top", "labelWidth": 144, "layout": "hbox", "layoutConfig": { "align": "stretch" } });
    var wikipedia122 = new Ext.form.TextField({ "anchor": "-20", "autoHeight": true, "fieldLabel": "Wikipedia", "listeners": { "render": Lino.quicktip_renderer("Wikipedia","(concepts.Concepts.wikipedia) ") }, "maxLength": 200, "name": "wikipedia", "selectOnFocus": true });
    var wikipedia_nl123 = new Ext.form.TextField({ "anchor": "-20", "autoHeight": true, "fieldLabel": "Wikipedia (nl)", "listeners": { "render": Lino.quicktip_renderer("Wikipedia (nl)","(concepts.Concepts.wikipedia_nl) ") }, "maxLength": 200, "name": "wikipedia_nl", "selectOnFocus": true });
    var wikipedia_de124 = new Ext.form.TextField({ "anchor": "-20", "autoHeight": true, "fieldLabel": "Wikipedia (de)", "listeners": { "render": Lino.quicktip_renderer("Wikipedia (de)","(concepts.Concepts.wikipedia_de) ") }, "maxLength": 200, "name": "wikipedia_de", "selectOnFocus": true });
    var main_4_panel125 = new Ext.Panel({ "autoHeight": true, "autoScroll": false, "border": false, "frame": false, "hideCheckBoxLabels": true, "items": [ { "autoHeight": true, "flex": 33, "items": wikipedia122, "labelAlign": "top", "layout": "form", "xtype": "panel" }, { "autoHeight": true, "flex": 33, "items": wikipedia_nl123, "labelAlign": "top", "layout": "form", "xtype": "panel" }, { "autoHeight": true, "flex": 33, "items": wikipedia_de124, "labelAlign": "top", "layout": "form", "xtype": "panel" } ], "labelAlign": "top", "labelWidth": 135, "layout": "hbox", "layoutConfig": { "align": "stretchmax" } });
    var Parents_grid136 = new Lino.concepts.Parents.GridPanel({ "containing_panel": this, "flex": 50, "hide_top_toolbar": true, "listeners": { "render": Lino.quicktip_renderer("Concepts subordonn\u00e9s","(concepts.concepts.Parents) ") }, "master_panel": this, "preview_limit": 15, "tools": [ Lino.show_in_own_window_button(Lino.concepts.Parents.grid) ] });
    var Children_grid144 = new Lino.concepts.Children.GridPanel({ "containing_panel": this, "flex": 50, "hide_top_toolbar": true, "listeners": { "render": Lino.quicktip_renderer("Concepts sous-jacents","(concepts.concepts.Children) ") }, "master_panel": this, "preview_limit": 15, "tools": [ Lino.show_in_own_window_button(Lino.concepts.Children.grid) ] });
    var main_5_panel145 = new Ext.Panel({ "autoScroll": false, "border": false, "flex": 38, "frame": false, "hideCheckBoxLabels": true, "items": [ Parents_grid136, Children_grid144 ], "labelAlign": "top", "layout": "hbox", "layoutConfig": { "align": "stretch" } });
    var main_panel146 = new Ext.Panel({ "autoScroll": false, "bodyBorder": false, "border": false, "frame": true, "hideCheckBoxLabels": true, "items": [ main_1_panel104, main_2_panel111, main_3_panel118, main_4_panel125, main_5_panel145 ], "labelAlign": "top", "layout": "vbox", "layoutConfig": { "align": "stretch" } });
    this.items = main_panel146;
    this.before_row_edit = function(record) {
      Parents_grid136.on_master_changed();
      Children_grid144.on_master_changed();
    }
    Lino.concepts.Concepts.DetailFormPanel.superclass.initComponent.call(this);
  }
});


Lino.about.About.DetailFormPanel = Ext.extend(Lino.FormPanel,{
  layout: 'fit',
  auto_save: true,
  disable_editing: true,
  initComponent : function() {
    var server_status_disp148 = new Ext.form.DisplayField({ "always_enabled": true, "anchor": "-20", "autoHeight": true, "disabled": true, "fieldLabel": "Server status", "listeners": { "render": Lino.quicktip_renderer("Server status","(about.About.server_status) ") }, "name": "server_status", "value": "<br/>" });
    var main_panel149 = new Ext.Panel({ "autoScroll": false, "bodyBorder": false, "border": false, "frame": true, "hideCheckBoxLabels": true, "items": [ { "flex": 25, "html": "<div class=\"htmlText\"><span>Ceci est <a href=\"http://www.lino-framework.org/examples/belref.html\" target=\"_blank\">Lino Belref</a> 0.1 utilisant <a href=\"http://www.lino-framework.org\" target=\"_blank\">Lino</a> 1.7.0, <a href=\"http://www.djangoproject.com\" target=\"_blank\">Django</a> 1.9.5, <a href=\"http://www.python.org/\" target=\"_blank\">Python</a> 2.7.6, <a href=\"http://babel.edgewall.org/\" target=\"_blank\">Babel</a> 2.2.0, <a href=\"http://jinja.pocoo.org/\" target=\"_blank\">Jinja</a> 2.8, <a href=\"http://sphinx-doc.org/\" target=\"_blank\">Sphinx</a> 1.4a1, <a href=\"http://labix.org/python-dateutil\" target=\"_blank\">python-dateutil</a> 2.5.2, <a href=\"http://pypi.python.org/pypi/odfpy\" target=\"_blank\">OdfPy</a> ODFPY/1.3.2, <a href=\"http://docutils.sourceforge.net/\" target=\"_blank\">docutils</a> 0.12, <a href=\"https://fedorahosted.org/suds/\" target=\"_blank\">suds</a> 0.4, <a href=\"http://pyyaml.org/\" target=\"_blank\">PyYaml</a> 3.11, <a href=\"http://appyframework.org/pod.html\" target=\"_blank\">Appy</a> 0.9.2 (2015/04/30 15:00), <a href=\"http://getbootstrap.com\" target=\"_blank\">Bootstrap</a> 3.3.4, <a href=\"http://www.sencha.com\" target=\"_blank\">ExtJS</a> <a href=\"#\" onclick=\"alert('ExtJS client version is ' + Ext.version);\" title=\"Click to see ExtJS client version\">(version)</a>, <a href=\"http://www.famfamfam.com/lab/icons/silk/\" target=\"_blank\">Silk Icons</a> 1.3</span><p>Langues: fr, nl, de</p><p>Ce serveur tourne depuis : <b>lundi 16 mai 2016 at 03:07:18.344229</b></p><p>Ceci est un site de d&#233;monstration Lino.</p><p>Source timestamps:</p><ul><li>lino : <b>lundi 16 mai 2016 at 02:45:58.231031</b></li><li>django : <b>vendredi 13 mai 2016 at 22:34:32.263605</b></li><li>atelier : <b>mercredi 20 avril 2016 at 12:24:08.578869</b></li></ul></div>", "xtype": "label" }, { "autoHeight": true, "items": server_status_disp148, "labelAlign": "top", "layout": "form", "xtype": "panel" } ], "labelAlign": "top", "labelWidth": 126, "layout": "vbox", "layoutConfig": { "align": "stretch" } });
    this.items = main_panel149;
    this.before_row_edit = function(record) {
    }
    Lino.about.About.DetailFormPanel.superclass.initComponent.call(this);
  }
});


Lino.about.Models.DetailFormPanel = Ext.extend(Lino.FormPanel,{
  layout: 'fit',
  auto_save: true,
  disable_editing: true,
  initComponent : function() {
    var app_disp151 = new Ext.form.DisplayField({ "always_enabled": true, "anchor": "-20", "autoHeight": true, "disabled": true, "fieldLabel": "app_label", "listeners": { "render": Lino.quicktip_renderer("app_label","(about.Models.app) ") }, "name": "app", "value": "<br/>" });
    var name_disp152 = new Ext.form.DisplayField({ "always_enabled": true, "anchor": "-20", "autoHeight": true, "disabled": true, "fieldLabel": "name", "listeners": { "render": Lino.quicktip_renderer("name","(about.Models.name) ") }, "name": "name", "value": "<br/>" });
    var docstring_disp153 = new Ext.form.DisplayField({ "always_enabled": true, "anchor": "-20", "autoHeight": true, "disabled": true, "fieldLabel": "docstring", "listeners": { "render": Lino.quicktip_renderer("docstring","(about.Models.docstring) ") }, "name": "docstring", "value": "<br/>" });
    var rows154 = new Ext.form.NumberField({ "anchor": "-20", "autoHeight": true, "disabled": true, "fieldLabel": "Rows", "listeners": { "render": Lino.quicktip_renderer("Rows","(about.Models.rows) ") }, "name": "rows" });
    var main_1_panel155 = new Ext.Panel({ "autoHeight": true, "autoScroll": false, "border": false, "frame": false, "hideCheckBoxLabels": true, "items": [ { "autoHeight": true, "flex": 31, "items": app_disp151, "labelAlign": "top", "layout": "form", "xtype": "panel" }, { "autoHeight": true, "flex": 31, "items": name_disp152, "labelAlign": "top", "layout": "form", "xtype": "panel" }, { "autoHeight": true, "flex": 31, "items": docstring_disp153, "labelAlign": "top", "layout": "form", "xtype": "panel" }, { "autoHeight": true, "flex": 5, "items": rows154, "labelAlign": "top", "layout": "form", "xtype": "panel" } ], "labelAlign": "top", "labelWidth": 90, "layout": "hbox", "layoutConfig": { "align": "stretchmax" } });
    var about_FieldsByModel_grid164 = new Lino.about.FieldsByModel.GridPanel({ "containing_panel": this, "flex": 62, "hide_top_toolbar": true, "listeners": { "render": Lino.quicktip_renderer("Fields","(about.about.FieldsByModel) ") }, "master_panel": this, "preview_limit": 15, "tools": [ Lino.show_in_own_window_button(Lino.about.FieldsByModel.grid) ] });
    var main_panel165 = new Ext.Panel({ "autoScroll": false, "bodyBorder": false, "border": false, "frame": true, "hideCheckBoxLabels": true, "items": [ main_1_panel155, about_FieldsByModel_grid164 ], "labelAlign": "top", "layout": "vbox", "layoutConfig": { "align": "stretch" } });
    this.items = main_panel165;
    this.before_row_edit = function(record) {
      about_FieldsByModel_grid164.on_master_changed();
    }
    Lino.about.Models.DetailFormPanel.superclass.initComponent.call(this);
  }
});


Lino.countries.Places.DetailFormPanel = Ext.extend(Lino.FormPanel,{
  layout: 'fit',
  auto_save: true,
  initComponent : function() {
    var name47 = new Ext.form.TextField({ "allowBlank": false, "anchor": "-20", "autoHeight": true, "fieldLabel": "D\u00e9signation", "listeners": { "render": Lino.quicktip_renderer("D\u00e9signation","(countries.Places.name) ") }, "maxLength": 200, "name": "name", "selectOnFocus": true });
    var name_nl48 = new Ext.form.TextField({ "anchor": "-20", "autoHeight": true, "fieldLabel": "D\u00e9signation (nl)", "listeners": { "render": Lino.quicktip_renderer("D\u00e9signation (nl)","(countries.Places.name_nl) ") }, "maxLength": 200, "name": "name_nl", "selectOnFocus": true });
    var name_de49 = new Ext.form.TextField({ "anchor": "-20", "autoHeight": true, "fieldLabel": "D\u00e9signation (de)", "listeners": { "render": Lino.quicktip_renderer("D\u00e9signation (de)","(countries.Places.name_de) ") }, "maxLength": 200, "name": "name_de", "selectOnFocus": true });
    var country50 = new Lino.TwinCombo({ "allowBlank": false, "anchor": "-20", "autoHeight": true, "emptyText": "Choisir Pays...", "fieldLabel": "Pays", "hiddenName": "countryHidden", "listeners": { "render": Lino.quicktip_renderer("Pays","(countries.Places.country) ") }, "name": "country", "onTrigger2Click": function(e){ Lino.show_fk_detail(this,Lino.countries.Countries.detail,Lino.countries.Countries.insert)}, "pageSize": 20, "selectOnFocus": true, "store": new Lino.ComplexRemoteComboStore({ "proxy": new Ext.data.HttpProxy({ "method": "GET", "url": "/choices/countries/Places/country" }) }) });
    var inscode51 = new Ext.form.TextField({ "anchor": "-20", "autoHeight": true, "boxMinWidth": Lino.chars2width(5), "fieldLabel": "<span style=\"border-bottom: 1px dotted #000000;\">INS code</span>", "listeners": { "render": Lino.quicktip_renderer("INS code","(countries.Places.inscode) The official code for this place used by statbel.fgov.be") }, "maxLength": 5, "name": "inscode", "selectOnFocus": true });
    var main_1_panel52 = new Ext.Panel({ "autoHeight": true, "autoScroll": false, "border": false, "frame": false, "hideCheckBoxLabels": true, "items": [ { "autoHeight": true, "flex": 23, "items": name47, "labelAlign": "top", "layout": "form", "xtype": "panel" }, { "autoHeight": true, "flex": 23, "items": name_nl48, "labelAlign": "top", "layout": "form", "xtype": "panel" }, { "autoHeight": true, "flex": 23, "items": name_de49, "labelAlign": "top", "layout": "form", "xtype": "panel" }, { "autoHeight": true, "flex": 22, "items": country50, "labelAlign": "top", "layout": "form", "xtype": "panel" }, { "autoHeight": true, "flex": 6, "items": inscode51, "labelAlign": "top", "layout": "form", "xtype": "panel" } ], "labelAlign": "top", "labelWidth": 153, "layout": "hbox", "layoutConfig": { "align": "stretchmax" } });
    var parent58 = new Lino.TwinCombo({ "anchor": "-20", "autoHeight": true, "emptyText": "Choisir Endroit...", "fieldLabel": "<span style=\"border-bottom: 1px dotted #000000;\">Part of</span>", "hiddenName": "parentHidden", "listeners": { "render": Lino.quicktip_renderer("Part of","(countries.Places.parent) The superordinate geographic place of which this place is a part.") }, "name": "parent", "onTrigger2Click": function(e){ Lino.show_fk_detail(this,Lino.countries.Places.detail,Lino.countries.Places.insert)}, "pageSize": 20, "selectOnFocus": true, "store": new Lino.ComplexRemoteComboStore({ "proxy": new Ext.data.HttpProxy({ "method": "GET", "url": "/choices/countries/Places/parent" }) }) });
    var type59 = new Lino.RemoteComboFieldElement({ "anchor": "-20", "autoHeight": true, "fieldLabel": "Type d'endroit", "hiddenName": "typeHidden", "listeners": { "render": Lino.quicktip_renderer("Type d'endroit","(countries.Places.type) ") }, "name": "type", "selectOnFocus": true, "store": new Lino.ComplexRemoteComboStore({ "proxy": new Ext.data.HttpProxy({ "method": "GET", "url": "/choices/countries/Places/type" }) }) });
    var id60 = new Ext.form.NumberField({ "anchor": "-20", "autoHeight": true, "fieldLabel": "ID", "listeners": { "render": Lino.quicktip_renderer("ID","(countries.Places.id) ") }, "name": "id", "selectOnFocus": true });
    var main_2_panel61 = new Ext.Panel({ "autoHeight": true, "autoScroll": false, "border": false, "frame": false, "hideCheckBoxLabels": true, "items": [ { "autoHeight": true, "flex": 57, "items": parent58, "labelAlign": "top", "layout": "form", "xtype": "panel" }, { "autoHeight": true, "flex": 28, "items": type59, "labelAlign": "top", "layout": "form", "xtype": "panel" }, { "autoHeight": true, "flex": 14, "items": id60, "labelAlign": "top", "layout": "form", "xtype": "panel" } ], "labelAlign": "top", "labelWidth": 135, "layout": "hbox", "layoutConfig": { "align": "stretchmax" } });
    var PlacesByPlace_grid97 = new Lino.countries.PlacesByPlace.GridPanel({ "containing_panel": this, "flex": 71, "hide_top_toolbar": true, "listeners": { "render": Lino.quicktip_renderer("Subdivisions","(countries.countries.PlacesByPlace) ") }, "master_panel": this, "preview_limit": 15, "tools": [ Lino.show_in_own_window_button(Lino.countries.PlacesByPlace.grid) ] });
    var main_panel98 = new Ext.Panel({ "autoScroll": false, "bodyBorder": false, "border": false, "frame": true, "hideCheckBoxLabels": true, "items": [ main_1_panel52, main_2_panel61, PlacesByPlace_grid97 ], "labelAlign": "top", "layout": "vbox", "layoutConfig": { "align": "stretch" } });
    this.items = main_panel98;
    this.before_row_edit = function(record) {
      type59.setContextValue('country', record ? record.data['countryHidden'] : undefined);
      PlacesByPlace_grid97.on_master_changed();
    }
    this.onRender = function(ct, position) {
      country50.on('change',Lino.chooser_handler(type59,'country'));
      Lino.countries.Places.DetailFormPanel.superclass.onRender.call(this, ct, position);
    }
    Lino.countries.Places.DetailFormPanel.superclass.initComponent.call(this);
  }
});


// js_render_GridPanel_class system.SiteConfigs
Lino.system.SiteConfigs.GridPanel = Ext.extend(Lino.GridPanel,{
  viewConfig : { "emptyText": "Pas de donn\u00e9es \u00e0 afficher.", "forceFit": true, "getRowClass": Lino.getRowClass },
  ls_url : "/system/SiteConfigs",
  ls_bbar_actions : [ { "auto_save": true, "iconCls": "x-tbar-html", "itemId": "show_as_html", "menu_item_text": "HTML", "overflowText": "HTML", "panel_btn_handler": Lino.list_action_handler('/system/SiteConfigs','show_as_html','GET',Lino.get_current_grid_config), "tooltip": "Show this table in Bootstrap3 interface" }, { "auto_save": true, "iconCls": "x-tbar-application_form", "itemId": "detail", "menu_item_text": "D\u00e9tail", "overflowText": "D\u00e9tail", "panel_btn_handler": Lino.show_detail, "tooltip": "Open a detail window on this record" }, { "auto_save": true, "itemId": "do_build", "menu_item_text": "Rebuild site cache", "overflowText": "Rebuild site cache", "panel_btn_handler": Lino.row_action_handler('do_build','GET',null), "text": "Rebuild site cache" } ],
  cell_edit : true,
  title : "Site configurations",
  gc_name : 0,
  stripeRows : true,
  disabled_actions_index : 7,
  ls_store_fields : [ { "name": "id", "type": "int" }, { "name": "default_build_method" }, 'default_build_methodHidden', { "dateFormat": "d.m.Y", "name": "simulate_today", "type": "date" }, { "name": "workflow_buttons" }, { "name": "description_column" }, { "name": "disabled_fields" }, { "name": "disabled_actions" }, { "name": "disable_editing" } ],
  pk_index : 0,
  ls_grid_configs : [  ],
  ls_id_property : "id",
  page_length : 20,
  initComponent : function() {
    this.ls_detail_handler = Lino.system.SiteConfigs.detail;
    var ww = this.containing_window;
    var id166 = new Ext.form.NumberField({ "selectOnFocus": true });
    var default_build_method167 = new Lino.ChoicesFieldElement({ "forceSelection": true, "selectOnFocus": true, "store": [['','<br>']].concat(Lino.printing.BuildMethods) });
    var simulate_today168 = new Lino.DateField({ "selectOnFocus": true });
    var workflow_buttons_disp169 = new Ext.form.DisplayField({ "always_enabled": true, "disabled": true, "hidden": true, "value": "<br/>" });
    var description_column_disp170 = new Ext.form.DisplayField({ "always_enabled": true, "disabled": true, "hidden": true, "value": "<br/>" });
    this.before_row_edit = function(record) {
    };
    this.ls_columns = [ new Lino.NullNumberColumn({ "colIndex": 0, "dataIndex": "id", "editable": true, "editor": id166, "filter": { "type": "numeric" }, "format": "0", "header": "ID", "sortable": true, "tooltip": "(system.SiteConfigs.id) ", "width": Lino.chars2width(6) }), { "colIndex": 1, "dataIndex": "default_build_method", "editable": true, "editor": default_build_method167, "filter": { "type": "string" }, "header": "M\u00e9thode de constuction par d\u00e9fault", "sortable": true, "tooltip": "(system.SiteConfigs.default_build_method) ", "width": Lino.chars2width(20) }, { "colIndex": 2, "dataIndex": "simulate_today", "editable": true, "editor": simulate_today168, "filter": { "dateFormat": "d.m.Y", "type": "date" }, "format": "d.m.Y", "header": "Simulated date", "sortable": true, "tooltip": "(system.SiteConfigs.simulate_today) ", "width": Lino.chars2width(14), "xtype": "datecolumn" }, { "colIndex": 3, "dataIndex": "workflow_buttons", "editable": false, "header": "\u00c9tat", "hidden": true, "sortable": false, "tooltip": "(system.SiteConfigs.workflow_buttons) ", "width": Lino.chars2width(31) }, { "colIndex": 4, "dataIndex": "description_column", "editable": false, "header": "Description", "hidden": true, "sortable": false, "tooltip": "(system.SiteConfigs.description_column) ", "width": Lino.chars2width(31) } ];
    Lino.system.SiteConfigs.GridPanel.superclass.initComponent.call(this);
  }
});

Lino.system.SiteConfigs.show_as_html = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/system/SiteConfigs", "GET", pk, "show_as_html", params, Lino.get_current_grid_config);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.system.SiteConfigs.submit_detail = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/system/SiteConfigs", "GET", pk, "submit_detail", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.system.SiteConfigs.grid_put = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/system/SiteConfigs", "GET", pk, "grid_put", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.system.SiteConfigs.grid_post = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/system/SiteConfigs", "GET", pk, "grid_post", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.system.SiteConfigs.submit_insert = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/system/SiteConfigs", "GET", pk, "submit_insert", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};

Lino.system.SiteConfigs.detailPanel = Ext.extend(Lino.system.SiteConfigs.DetailFormPanel,{
  empty_title: "D\u00e9tail",
  save_action_name: "submit_detail",
  ls_bbar_actions: [ { "auto_save": true, "itemId": "do_build", "menu_item_text": "Rebuild site cache", "overflowText": "Rebuild site cache", "panel_btn_handler": Lino.row_action_handler('do_build','GET',null), "text": "Rebuild site cache" } ],
  ls_url: "/system/SiteConfigs",
  action_name: "detail",
  initComponent : function() {
    this.ls_detail_handler = Lino.system.SiteConfigs.detail;
    Lino.system.SiteConfigs.detailPanel.superclass.initComponent.call(this);
  }
});

Lino.system.SiteConfigs.detail = new Lino.WindowAction({  }, function(){
  var p = { "hide_top_toolbar": true, "is_main_window": true };
  return new Lino.system.SiteConfigs.detailPanel(p);
});
Lino.system.SiteConfigs.grid = new Lino.WindowAction({  }, function(){
  var p = { "hide_top_toolbar": true, "is_main_window": true };
  return new Lino.system.SiteConfigs.GridPanel(p);
});
Lino.system.SiteConfigs.validate = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/system/SiteConfigs", "GET", pk, "validate", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.system.SiteConfigs.do_build = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/system/SiteConfigs", "GET", pk, "do_build", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};

// js_render_GridPanel_class countries.Countries
Lino.countries.Countries.GridPanel = Ext.extend(Lino.GridPanel,{
  viewConfig : { "emptyText": "Pas de donn\u00e9es \u00e0 afficher.", "forceFit": true, "getRowClass": Lino.getRowClass },
  ls_url : "/countries/Countries",
  ls_bbar_actions : [ { "auto_save": true, "iconCls": "x-tbar-html", "itemId": "show_as_html", "menu_item_text": "HTML", "overflowText": "HTML", "panel_btn_handler": Lino.list_action_handler('/countries/Countries','show_as_html','GET',Lino.get_current_grid_config), "tooltip": "Show this table in Bootstrap3 interface" }, { "auto_save": true, "iconCls": "x-tbar-application_form", "itemId": "detail", "menu_item_text": "D\u00e9tail", "overflowText": "D\u00e9tail", "panel_btn_handler": Lino.show_detail, "tooltip": "Open a detail window on this record" } ],
  cell_edit : true,
  title : "Pays",
  gc_name : 0,
  stripeRows : true,
  disabled_actions_index : 12,
  ls_store_fields : [ { "name": "name" }, { "name": "name_nl" }, { "name": "name_de" }, { "name": "isocode" }, { "name": "short_code" }, { "name": "iso3" }, { "name": "inscode" }, { "name": "actual_country" }, 'actual_countryHidden', { "name": "workflow_buttons" }, { "name": "description_column" }, { "name": "disabled_fields" }, { "name": "disabled_actions" }, { "name": "disable_editing" } ],
  pk_index : 3,
  ls_grid_configs : [  ],
  ls_id_property : "isocode",
  page_length : 20,
  initComponent : function() {
    this.ls_detail_handler = Lino.countries.Countries.detail;
    this.ls_insert_handler = Lino.countries.Countries.insert;
    var ww = this.containing_window;
    var name172 = new Ext.form.TextField({ "allowBlank": false, "maxLength": 200, "selectOnFocus": true });
    var name_nl173 = new Ext.form.TextField({ "maxLength": 200, "selectOnFocus": true });
    var name_de174 = new Ext.form.TextField({ "maxLength": 200, "selectOnFocus": true });
    var isocode175 = new Ext.form.TextField({ "allowBlank": false, "boxMinWidth": Lino.chars2width(4), "maxLength": 4, "selectOnFocus": true });
    var short_code176 = new Ext.form.TextField({ "boxMinWidth": Lino.chars2width(4), "hidden": true, "maxLength": 4, "selectOnFocus": true });
    var iso3177 = new Ext.form.TextField({ "boxMinWidth": Lino.chars2width(3), "hidden": true, "maxLength": 3, "selectOnFocus": true });
    var inscode178 = new Ext.form.TextField({ "boxMinWidth": Lino.chars2width(3), "hidden": true, "maxLength": 3, "selectOnFocus": true });
    var actual_country179 = new Lino.RemoteComboFieldElement({ "emptyText": "Choisir Pays...", "hidden": true, "pageSize": 20, "selectOnFocus": true, "store": new Lino.ComplexRemoteComboStore({ "proxy": new Ext.data.HttpProxy({ "method": "GET", "url": "/choices/countries/Countries/actual_country" }) }) });
    var workflow_buttons_disp180 = new Ext.form.DisplayField({ "always_enabled": true, "disabled": true, "hidden": true, "value": "<br/>" });
    var description_column_disp181 = new Ext.form.DisplayField({ "always_enabled": true, "disabled": true, "hidden": true, "value": "<br/>" });
    this.before_row_edit = function(record) {
    };
    this.ls_columns = [ { "colIndex": 0, "dataIndex": "name", "editable": true, "editor": name172, "filter": { "type": "string" }, "header": "D\u00e9signation", "sortable": true, "tooltip": "(countries.Countries.name) ", "width": Lino.chars2width(22) }, { "colIndex": 1, "dataIndex": "name_nl", "editable": true, "editor": name_nl173, "filter": { "type": "string" }, "header": "D\u00e9signation (nl)", "sortable": true, "tooltip": "(countries.Countries.name_nl) ", "width": Lino.chars2width(22) }, { "colIndex": 2, "dataIndex": "name_de", "editable": true, "editor": name_de174, "filter": { "type": "string" }, "header": "D\u00e9signation (de)", "sortable": true, "tooltip": "(countries.Countries.name_de) ", "width": Lino.chars2width(22) }, { "colIndex": 3, "dataIndex": "isocode", "editable": true, "editor": isocode175, "filter": { "type": "string" }, "header": "ISO code", "sortable": true, "tooltip": "(countries.Countries.isocode)         The two-letter code for this country as defined by ISO 3166-1.\n        For countries that no longer exist it may be a 4-letter code.", "width": Lino.chars2width(11) }, { "colIndex": 4, "dataIndex": "short_code", "editable": true, "editor": short_code176, "filter": { "type": "string" }, "header": "Short code", "hidden": true, "sortable": true, "tooltip": "(countries.Countries.short_code) A short abbreviation for regional usage. Obsolete.", "width": Lino.chars2width(11) }, { "colIndex": 5, "dataIndex": "iso3", "editable": true, "editor": iso3177, "filter": { "type": "string" }, "header": "ISO-3 code", "hidden": true, "sortable": true, "tooltip": "(countries.Countries.iso3) The three-letter code for this country as defined by ISO 3166-1.", "width": Lino.chars2width(5) }, { "colIndex": 6, "dataIndex": "inscode", "editable": true, "editor": inscode178, "filter": { "type": "string" }, "header": "INS code", "hidden": true, "sortable": true, "tooltip": "(countries.Countries.inscode) The official code for this country used by statbel.fgov.be", "width": Lino.chars2width(11) }, { "colIndex": 7, "dataIndex": "actual_country", "editable": true, "editor": actual_country179, "filter": { "type": "string" }, "header": "Actual country", "hidden": true, "renderer": Lino.fk_renderer('actual_countryHidden','Lino.countries.Countries.detail'), "sortable": true, "tooltip": "(countries.Countries.actual_country) Select the actual country if this row represents a refugee status or a former country.", "width": Lino.chars2width(21) }, { "colIndex": 8, "dataIndex": "workflow_buttons", "editable": false, "header": "\u00c9tat", "hidden": true, "sortable": false, "tooltip": "(countries.Countries.workflow_buttons) ", "width": Lino.chars2width(31) }, { "colIndex": 9, "dataIndex": "description_column", "editable": false, "header": "Description", "hidden": true, "sortable": false, "tooltip": "(countries.Countries.description_column) ", "width": Lino.chars2width(31) } ];
    Lino.countries.Countries.GridPanel.superclass.initComponent.call(this);
  }
});

Lino.countries.Countries.show_as_html = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/countries/Countries", "GET", pk, "show_as_html", params, Lino.get_current_grid_config);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.countries.Countries.submit_detail = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/countries/Countries", "GET", pk, "submit_detail", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};

Lino.countries.Countries.insertPanel = Ext.extend(Lino.countries.Countries.InsertFormPanel,{
  empty_title: "Nouveau",
  hide_navigator: true,
  save_action_name: "submit_insert",
  ls_bbar_actions: [  ],
  ls_url: "/countries/Countries",
  action_name: "insert",
  initComponent : function() {
    this.ls_detail_handler = Lino.countries.Countries.detail;
    this.ls_insert_handler = Lino.countries.Countries.insert;
    Lino.countries.Countries.insertPanel.superclass.initComponent.call(this);
  }
});

Lino.countries.Countries.insert = new Lino.WindowAction({ "autoHeight": true, "draggable": true, "maximizable": true, "maximized": false, "modal": true, "width": Lino.chars2width(60) }, function(){
  var p = { "hide_top_toolbar": true, "is_main_window": true };
  return new Lino.countries.Countries.insertPanel(p);
});
Lino.countries.Countries.grid_put = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/countries/Countries", "GET", pk, "grid_put", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.countries.Countries.grid_post = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/countries/Countries", "GET", pk, "grid_post", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.countries.Countries.submit_insert = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/countries/Countries", "GET", pk, "submit_insert", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};

Lino.countries.Countries.detailPanel = Ext.extend(Lino.countries.Countries.DetailFormPanel,{
  empty_title: "D\u00e9tail",
  save_action_name: "submit_detail",
  ls_bbar_actions: [  ],
  ls_url: "/countries/Countries",
  action_name: "detail",
  initComponent : function() {
    this.ls_detail_handler = Lino.countries.Countries.detail;
    this.ls_insert_handler = Lino.countries.Countries.insert;
    Lino.countries.Countries.detailPanel.superclass.initComponent.call(this);
  }
});

Lino.countries.Countries.detail = new Lino.WindowAction({  }, function(){
  var p = { "is_main_window": true };
  return new Lino.countries.Countries.detailPanel(p);
});
Lino.countries.Countries.delete_selected = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/countries/Countries", "GET", pk, "delete_selected", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.countries.Countries.grid = new Lino.WindowAction({  }, function(){
  var p = { "is_main_window": true };
  return new Lino.countries.Countries.GridPanel(p);
});
Lino.countries.Countries.validate = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/countries/Countries", "GET", pk, "validate", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};

// js_render_GridPanel_class countries.Places
Lino.countries.Places.GridPanel = Ext.extend(Lino.GridPanel,{
  viewConfig : { "emptyText": "Pas de donn\u00e9es \u00e0 afficher.", "forceFit": true, "getRowClass": Lino.getRowClass },
  ls_url : "/countries/Places",
  ls_bbar_actions : [ { "auto_save": true, "iconCls": "x-tbar-html", "itemId": "show_as_html", "menu_item_text": "HTML", "overflowText": "HTML", "panel_btn_handler": Lino.list_action_handler('/countries/Places','show_as_html','GET',Lino.get_current_grid_config), "tooltip": "Show this table in Bootstrap3 interface" }, { "auto_save": true, "iconCls": "x-tbar-application_form", "itemId": "detail", "menu_item_text": "D\u00e9tail", "overflowText": "D\u00e9tail", "panel_btn_handler": Lino.show_detail, "tooltip": "Open a detail window on this record" } ],
  cell_edit : true,
  title : "Endroits",
  gc_name : 0,
  stripeRows : true,
  disabled_actions_index : 15,
  ls_store_fields : [ { "name": "country" }, 'countryHidden', { "name": "name" }, { "name": "name_nl" }, { "name": "name_de" }, { "name": "type" }, 'typeHidden', { "name": "zip_code" }, { "name": "parent" }, 'parentHidden', { "name": "id", "type": "int" }, { "name": "inscode" }, { "name": "workflow_buttons" }, { "name": "description_column" }, { "name": "disabled_fields" }, { "name": "disabled_actions" }, { "name": "disable_editing" } ],
  pk_index : 10,
  ls_grid_configs : [  ],
  ls_id_property : "id",
  page_length : 20,
  initComponent : function() {
    this.ls_detail_handler = Lino.countries.Places.detail;
    this.ls_insert_handler = Lino.countries.Places.insert;
    var ww = this.containing_window;
    var country183 = new Lino.RemoteComboFieldElement({ "allowBlank": false, "emptyText": "Choisir Pays...", "pageSize": 20, "selectOnFocus": true, "store": new Lino.ComplexRemoteComboStore({ "proxy": new Ext.data.HttpProxy({ "method": "GET", "url": "/choices/countries/Places/country" }) }) });
    var name184 = new Ext.form.TextField({ "allowBlank": false, "maxLength": 200, "selectOnFocus": true });
    var name_nl185 = new Ext.form.TextField({ "maxLength": 200, "selectOnFocus": true });
    var name_de186 = new Ext.form.TextField({ "maxLength": 200, "selectOnFocus": true });
    var type187 = new Lino.RemoteComboFieldElement({ "selectOnFocus": true, "store": new Lino.ComplexRemoteComboStore({ "proxy": new Ext.data.HttpProxy({ "method": "GET", "url": "/choices/countries/Places/type" }) }) });
    var zip_code188 = new Ext.form.TextField({ "boxMinWidth": Lino.chars2width(8), "maxLength": 8, "selectOnFocus": true });
    var parent189 = new Lino.RemoteComboFieldElement({ "emptyText": "Choisir Endroit...", "pageSize": 20, "selectOnFocus": true, "store": new Lino.ComplexRemoteComboStore({ "proxy": new Ext.data.HttpProxy({ "method": "GET", "url": "/choices/countries/Places/parent" }) }) });
    var id190 = new Ext.form.NumberField({ "hidden": true, "selectOnFocus": true });
    var inscode191 = new Ext.form.TextField({ "boxMinWidth": Lino.chars2width(5), "hidden": true, "maxLength": 5, "selectOnFocus": true });
    var workflow_buttons_disp192 = new Ext.form.DisplayField({ "always_enabled": true, "disabled": true, "hidden": true, "value": "<br/>" });
    var description_column_disp193 = new Ext.form.DisplayField({ "always_enabled": true, "disabled": true, "hidden": true, "value": "<br/>" });
    this.before_row_edit = function(record) {
      type187.setContextValue('country', record ? record.data['countryHidden'] : undefined);
    };
    this.onRender = function(ct, position) {
      country183.on('change',Lino.chooser_handler(type187,'country'));
      Lino.countries.Places.GridPanel.superclass.onRender.call(this, ct, position);
    }
    this.ls_columns = [ { "colIndex": 0, "dataIndex": "country", "editable": true, "editor": country183, "filter": { "type": "string" }, "header": "Pays", "renderer": Lino.fk_renderer('countryHidden','Lino.countries.Countries.detail'), "sortable": true, "tooltip": "(countries.Places.country) ", "width": Lino.chars2width(21) }, { "colIndex": 1, "dataIndex": "name", "editable": true, "editor": name184, "filter": { "type": "string" }, "header": "D\u00e9signation", "sortable": true, "tooltip": "(countries.Places.name) ", "width": Lino.chars2width(22) }, { "colIndex": 2, "dataIndex": "name_nl", "editable": true, "editor": name_nl185, "filter": { "type": "string" }, "header": "D\u00e9signation (nl)", "sortable": true, "tooltip": "(countries.Places.name_nl) ", "width": Lino.chars2width(22) }, { "colIndex": 3, "dataIndex": "name_de", "editable": true, "editor": name_de186, "filter": { "type": "string" }, "header": "D\u00e9signation (de)", "sortable": true, "tooltip": "(countries.Places.name_de) ", "width": Lino.chars2width(22) }, { "colIndex": 4, "dataIndex": "type", "editable": true, "editor": type187, "filter": { "type": "string" }, "header": "Type d'endroit", "sortable": true, "tooltip": "(countries.Places.type) ", "width": Lino.chars2width(11) }, { "colIndex": 5, "dataIndex": "zip_code", "editable": true, "editor": zip_code188, "filter": { "type": "string" }, "header": "zip code", "sortable": true, "tooltip": "(countries.Places.zip_code) ", "width": Lino.chars2width(10) }, { "colIndex": 6, "dataIndex": "parent", "editable": true, "editor": parent189, "filter": { "type": "string" }, "header": "Part of", "renderer": Lino.fk_renderer('parentHidden','Lino.countries.Places.detail'), "sortable": true, "tooltip": "(countries.Places.parent) The superordinate geographic place of which this place is a part.", "width": Lino.chars2width(21) }, new Lino.NullNumberColumn({ "colIndex": 7, "dataIndex": "id", "editable": true, "editor": id190, "filter": { "type": "numeric" }, "format": "0", "header": "ID", "hidden": true, "sortable": true, "tooltip": "(countries.Places.id) ", "width": Lino.chars2width(6) }), { "colIndex": 8, "dataIndex": "inscode", "editable": true, "editor": inscode191, "filter": { "type": "string" }, "header": "INS code", "hidden": true, "sortable": true, "tooltip": "(countries.Places.inscode) The official code for this place used by statbel.fgov.be", "width": Lino.chars2width(7) }, { "colIndex": 9, "dataIndex": "workflow_buttons", "editable": false, "header": "\u00c9tat", "hidden": true, "sortable": false, "tooltip": "(countries.Places.workflow_buttons) ", "width": Lino.chars2width(31) }, { "colIndex": 10, "dataIndex": "description_column", "editable": false, "header": "Description", "hidden": true, "sortable": false, "tooltip": "(countries.Places.description_column) ", "width": Lino.chars2width(31) } ];
    Lino.countries.Places.GridPanel.superclass.initComponent.call(this);
  }
});

Lino.countries.Places.show_as_html = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/countries/Places", "GET", pk, "show_as_html", params, Lino.get_current_grid_config);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.countries.Places.submit_detail = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/countries/Places", "GET", pk, "submit_detail", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};

Lino.countries.Places.insertPanel = Ext.extend(Lino.countries.Places.DetailFormPanel,{
  empty_title: "Nouveau",
  hide_navigator: true,
  save_action_name: "submit_insert",
  ls_bbar_actions: [  ],
  ls_url: "/countries/Places",
  action_name: "insert",
  initComponent : function() {
    this.ls_detail_handler = Lino.countries.Places.detail;
    this.ls_insert_handler = Lino.countries.Places.insert;
    Lino.countries.Places.insertPanel.superclass.initComponent.call(this);
  }
});

Lino.countries.Places.insert = new Lino.WindowAction({  }, function(){
  var p = { "hide_top_toolbar": true, "is_main_window": true };
  return new Lino.countries.Places.insertPanel(p);
});
Lino.countries.Places.grid_put = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/countries/Places", "GET", pk, "grid_put", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.countries.Places.grid_post = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/countries/Places", "GET", pk, "grid_post", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.countries.Places.submit_insert = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/countries/Places", "GET", pk, "submit_insert", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.countries.Places.duplicate = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/countries/Places", "GET", pk, "duplicate", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};

Lino.countries.Places.detailPanel = Ext.extend(Lino.countries.Places.DetailFormPanel,{
  empty_title: "D\u00e9tail",
  save_action_name: "submit_detail",
  ls_bbar_actions: [  ],
  ls_url: "/countries/Places",
  action_name: "detail",
  initComponent : function() {
    this.ls_detail_handler = Lino.countries.Places.detail;
    this.ls_insert_handler = Lino.countries.Places.insert;
    Lino.countries.Places.detailPanel.superclass.initComponent.call(this);
  }
});

Lino.countries.Places.detail = new Lino.WindowAction({  }, function(){
  var p = { "is_main_window": true };
  return new Lino.countries.Places.detailPanel(p);
});
Lino.countries.Places.delete_selected = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/countries/Places", "GET", pk, "delete_selected", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.countries.Places.grid = new Lino.WindowAction({  }, function(){
  var p = { "is_main_window": true };
  return new Lino.countries.Places.GridPanel(p);
});
Lino.countries.Places.validate = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/countries/Places", "GET", pk, "validate", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};

// js_render_GridPanel_class concepts.Concepts
Lino.concepts.Concepts.GridPanel = Ext.extend(Lino.GridPanel,{
  viewConfig : { "emptyText": "Pas de donn\u00e9es \u00e0 afficher.", "forceFit": true, "getRowClass": Lino.getRowClass },
  ls_url : "/concepts/Concepts",
  ls_bbar_actions : [ { "auto_save": true, "iconCls": "x-tbar-html", "itemId": "show_as_html", "menu_item_text": "HTML", "overflowText": "HTML", "panel_btn_handler": Lino.list_action_handler('/concepts/Concepts','show_as_html','GET',Lino.get_current_grid_config), "tooltip": "Show this table in Bootstrap3 interface" }, { "auto_save": true, "iconCls": "x-tbar-application_form", "itemId": "detail", "menu_item_text": "D\u00e9tail", "overflowText": "D\u00e9tail", "panel_btn_handler": Lino.show_detail, "tooltip": "Open a detail window on this record" } ],
  cell_edit : true,
  title : "Concepts ",
  gc_name : 0,
  stripeRows : true,
  disabled_actions_index : 8,
  ls_store_fields : [ { "name": "name" }, { "name": "name_nl" }, { "name": "name_de" }, { "name": "id", "type": "int" }, { "name": "abbr" }, { "name": "abbr_nl" }, { "name": "abbr_de" }, { "name": "disabled_fields" }, { "name": "disabled_actions" }, { "name": "disable_editing" } ],
  pk_index : 3,
  ls_grid_configs : [  ],
  ls_id_property : "id",
  page_length : 20,
  initComponent : function() {
    this.ls_detail_handler = Lino.concepts.Concepts.detail;
    this.ls_insert_handler = Lino.concepts.Concepts.insert;
    var ww = this.containing_window;
    var name195 = new Ext.form.TextField({ "allowBlank": false, "maxLength": 200, "selectOnFocus": true });
    var name_nl196 = new Ext.form.TextField({ "maxLength": 200, "selectOnFocus": true });
    var name_de197 = new Ext.form.TextField({ "maxLength": 200, "selectOnFocus": true });
    var id198 = new Ext.form.NumberField({ "selectOnFocus": true });
    var abbr199 = new Ext.form.TextField({ "maxLength": 30, "selectOnFocus": true });
    var abbr_nl200 = new Ext.form.TextField({ "maxLength": 30, "selectOnFocus": true });
    var abbr_de201 = new Ext.form.TextField({ "maxLength": 30, "selectOnFocus": true });
    this.before_row_edit = function(record) {
    };
    this.ls_columns = [ { "colIndex": 0, "dataIndex": "name", "editable": true, "editor": name195, "filter": { "type": "string" }, "header": "D\u00e9signation", "sortable": true, "tooltip": "(concepts.Concepts.name) ", "width": Lino.chars2width(22) }, { "colIndex": 1, "dataIndex": "name_nl", "editable": true, "editor": name_nl196, "filter": { "type": "string" }, "header": "D\u00e9signation (nl)", "sortable": true, "tooltip": "(concepts.Concepts.name_nl) ", "width": Lino.chars2width(22) }, { "colIndex": 2, "dataIndex": "name_de", "editable": true, "editor": name_de197, "filter": { "type": "string" }, "header": "D\u00e9signation (de)", "sortable": true, "tooltip": "(concepts.Concepts.name_de) ", "width": Lino.chars2width(22) }, new Lino.NullNumberColumn({ "colIndex": 3, "dataIndex": "id", "editable": true, "editor": id198, "filter": { "type": "numeric" }, "format": "0", "header": "ID", "sortable": true, "tooltip": "(concepts.Concepts.id) ", "width": Lino.chars2width(6) }), { "colIndex": 4, "dataIndex": "abbr", "editable": true, "editor": abbr199, "filter": { "type": "string" }, "header": "Abbr\u00e9viation", "sortable": true, "tooltip": "(concepts.Concepts.abbr) ", "width": Lino.chars2width(22) }, { "colIndex": 5, "dataIndex": "abbr_nl", "editable": true, "editor": abbr_nl200, "filter": { "type": "string" }, "header": "Abbr\u00e9viation (nl)", "sortable": true, "tooltip": "(concepts.Concepts.abbr_nl) ", "width": Lino.chars2width(22) }, { "colIndex": 6, "dataIndex": "abbr_de", "editable": true, "editor": abbr_de201, "filter": { "type": "string" }, "header": "Abbr\u00e9viation (de)", "sortable": true, "tooltip": "(concepts.Concepts.abbr_de) ", "width": Lino.chars2width(22) } ];
    Lino.concepts.Concepts.GridPanel.superclass.initComponent.call(this);
  }
});

Lino.concepts.Concepts.show_as_html = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/concepts/Concepts", "GET", pk, "show_as_html", params, Lino.get_current_grid_config);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.concepts.Concepts.submit_detail = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/concepts/Concepts", "GET", pk, "submit_detail", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};

Lino.concepts.Concepts.insertPanel = Ext.extend(Lino.concepts.Concepts.DetailFormPanel,{
  empty_title: "Nouveau",
  hide_navigator: true,
  save_action_name: "submit_insert",
  ls_bbar_actions: [  ],
  ls_url: "/concepts/Concepts",
  action_name: "insert",
  initComponent : function() {
    this.ls_detail_handler = Lino.concepts.Concepts.detail;
    this.ls_insert_handler = Lino.concepts.Concepts.insert;
    Lino.concepts.Concepts.insertPanel.superclass.initComponent.call(this);
  }
});

Lino.concepts.Concepts.insert = new Lino.WindowAction({  }, function(){
  var p = { "hide_top_toolbar": true, "is_main_window": true };
  return new Lino.concepts.Concepts.insertPanel(p);
});
Lino.concepts.Concepts.grid_put = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/concepts/Concepts", "GET", pk, "grid_put", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.concepts.Concepts.grid_post = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/concepts/Concepts", "GET", pk, "grid_post", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.concepts.Concepts.submit_insert = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/concepts/Concepts", "GET", pk, "submit_insert", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};

Lino.concepts.Concepts.detailPanel = Ext.extend(Lino.concepts.Concepts.DetailFormPanel,{
  empty_title: "D\u00e9tail",
  save_action_name: "submit_detail",
  ls_bbar_actions: [  ],
  ls_url: "/concepts/Concepts",
  action_name: "detail",
  initComponent : function() {
    this.ls_detail_handler = Lino.concepts.Concepts.detail;
    this.ls_insert_handler = Lino.concepts.Concepts.insert;
    Lino.concepts.Concepts.detailPanel.superclass.initComponent.call(this);
  }
});

Lino.concepts.Concepts.detail = new Lino.WindowAction({  }, function(){
  var p = { "is_main_window": true };
  return new Lino.concepts.Concepts.detailPanel(p);
});
Lino.concepts.Concepts.delete_selected = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/concepts/Concepts", "GET", pk, "delete_selected", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.concepts.Concepts.grid = new Lino.WindowAction({  }, function(){
  var p = { "is_main_window": true };
  return new Lino.concepts.Concepts.GridPanel(p);
});
Lino.concepts.Concepts.validate = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/concepts/Concepts", "GET", pk, "validate", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};

// js_render_GridPanel_class concepts.TopLevelConcepts
Lino.concepts.TopLevelConcepts.GridPanel = Ext.extend(Lino.GridPanel,{
  viewConfig : { "emptyText": "Pas de donn\u00e9es \u00e0 afficher.", "forceFit": true, "getRowClass": Lino.getRowClass },
  ls_url : "/concepts/TopLevelConcepts",
  ls_bbar_actions : [ { "auto_save": true, "iconCls": "x-tbar-html", "itemId": "show_as_html", "menu_item_text": "HTML", "overflowText": "HTML", "panel_btn_handler": Lino.list_action_handler('/concepts/TopLevelConcepts','show_as_html','GET',Lino.get_current_grid_config), "tooltip": "Show this table in Bootstrap3 interface" }, { "auto_save": true, "iconCls": "x-tbar-application_form", "itemId": "detail", "menu_item_text": "D\u00e9tail", "overflowText": "D\u00e9tail", "panel_btn_handler": Lino.show_detail, "tooltip": "Open a detail window on this record" } ],
  cell_edit : true,
  title : "Concepts primaires",
  gc_name : 0,
  stripeRows : true,
  disabled_actions_index : 8,
  ls_store_fields : [ { "name": "name" }, { "name": "name_nl" }, { "name": "name_de" }, { "name": "id", "type": "int" }, { "name": "abbr" }, { "name": "abbr_nl" }, { "name": "abbr_de" }, { "name": "disabled_fields" }, { "name": "disabled_actions" }, { "name": "disable_editing" } ],
  pk_index : 3,
  ls_grid_configs : [  ],
  ls_id_property : "id",
  page_length : 20,
  initComponent : function() {
    this.ls_detail_handler = Lino.concepts.TopLevelConcepts.detail;
    this.ls_insert_handler = Lino.concepts.TopLevelConcepts.insert;
    var ww = this.containing_window;
    var name203 = new Ext.form.TextField({ "allowBlank": false, "maxLength": 200, "selectOnFocus": true });
    var name_nl204 = new Ext.form.TextField({ "maxLength": 200, "selectOnFocus": true });
    var name_de205 = new Ext.form.TextField({ "maxLength": 200, "selectOnFocus": true });
    var id206 = new Ext.form.NumberField({ "selectOnFocus": true });
    var abbr207 = new Ext.form.TextField({ "maxLength": 30, "selectOnFocus": true });
    var abbr_nl208 = new Ext.form.TextField({ "maxLength": 30, "selectOnFocus": true });
    var abbr_de209 = new Ext.form.TextField({ "maxLength": 30, "selectOnFocus": true });
    this.before_row_edit = function(record) {
    };
    this.ls_columns = [ { "colIndex": 0, "dataIndex": "name", "editable": true, "editor": name203, "filter": { "type": "string" }, "header": "D\u00e9signation", "sortable": true, "tooltip": "(concepts.TopLevelConcepts.name) ", "width": Lino.chars2width(22) }, { "colIndex": 1, "dataIndex": "name_nl", "editable": true, "editor": name_nl204, "filter": { "type": "string" }, "header": "D\u00e9signation (nl)", "sortable": true, "tooltip": "(concepts.TopLevelConcepts.name_nl) ", "width": Lino.chars2width(22) }, { "colIndex": 2, "dataIndex": "name_de", "editable": true, "editor": name_de205, "filter": { "type": "string" }, "header": "D\u00e9signation (de)", "sortable": true, "tooltip": "(concepts.TopLevelConcepts.name_de) ", "width": Lino.chars2width(22) }, new Lino.NullNumberColumn({ "colIndex": 3, "dataIndex": "id", "editable": true, "editor": id206, "filter": { "type": "numeric" }, "format": "0", "header": "ID", "sortable": true, "tooltip": "(concepts.TopLevelConcepts.id) ", "width": Lino.chars2width(6) }), { "colIndex": 4, "dataIndex": "abbr", "editable": true, "editor": abbr207, "filter": { "type": "string" }, "header": "Abbr\u00e9viation", "sortable": true, "tooltip": "(concepts.TopLevelConcepts.abbr) ", "width": Lino.chars2width(22) }, { "colIndex": 5, "dataIndex": "abbr_nl", "editable": true, "editor": abbr_nl208, "filter": { "type": "string" }, "header": "Abbr\u00e9viation (nl)", "sortable": true, "tooltip": "(concepts.TopLevelConcepts.abbr_nl) ", "width": Lino.chars2width(22) }, { "colIndex": 6, "dataIndex": "abbr_de", "editable": true, "editor": abbr_de209, "filter": { "type": "string" }, "header": "Abbr\u00e9viation (de)", "sortable": true, "tooltip": "(concepts.TopLevelConcepts.abbr_de) ", "width": Lino.chars2width(22) } ];
    Lino.concepts.TopLevelConcepts.GridPanel.superclass.initComponent.call(this);
  }
});

Lino.concepts.TopLevelConcepts.show_as_html = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/concepts/TopLevelConcepts", "GET", pk, "show_as_html", params, Lino.get_current_grid_config);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.concepts.TopLevelConcepts.submit_detail = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/concepts/TopLevelConcepts", "GET", pk, "submit_detail", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};

Lino.concepts.TopLevelConcepts.insertPanel = Ext.extend(Lino.concepts.Concepts.DetailFormPanel,{
  empty_title: "Nouveau",
  hide_navigator: true,
  save_action_name: "submit_insert",
  ls_bbar_actions: [  ],
  ls_url: "/concepts/TopLevelConcepts",
  action_name: "insert",
  initComponent : function() {
    this.ls_detail_handler = Lino.concepts.TopLevelConcepts.detail;
    this.ls_insert_handler = Lino.concepts.TopLevelConcepts.insert;
    Lino.concepts.TopLevelConcepts.insertPanel.superclass.initComponent.call(this);
  }
});

Lino.concepts.TopLevelConcepts.insert = new Lino.WindowAction({  }, function(){
  var p = { "hide_top_toolbar": true, "is_main_window": true };
  return new Lino.concepts.TopLevelConcepts.insertPanel(p);
});
Lino.concepts.TopLevelConcepts.grid_put = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/concepts/TopLevelConcepts", "GET", pk, "grid_put", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.concepts.TopLevelConcepts.grid_post = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/concepts/TopLevelConcepts", "GET", pk, "grid_post", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.concepts.TopLevelConcepts.submit_insert = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/concepts/TopLevelConcepts", "GET", pk, "submit_insert", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};

Lino.concepts.TopLevelConcepts.detailPanel = Ext.extend(Lino.concepts.Concepts.DetailFormPanel,{
  empty_title: "D\u00e9tail",
  save_action_name: "submit_detail",
  ls_bbar_actions: [  ],
  ls_url: "/concepts/TopLevelConcepts",
  action_name: "detail",
  initComponent : function() {
    this.ls_detail_handler = Lino.concepts.TopLevelConcepts.detail;
    this.ls_insert_handler = Lino.concepts.TopLevelConcepts.insert;
    Lino.concepts.TopLevelConcepts.detailPanel.superclass.initComponent.call(this);
  }
});

Lino.concepts.TopLevelConcepts.detail = new Lino.WindowAction({  }, function(){
  var p = { "is_main_window": true };
  return new Lino.concepts.TopLevelConcepts.detailPanel(p);
});
Lino.concepts.TopLevelConcepts.delete_selected = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/concepts/TopLevelConcepts", "GET", pk, "delete_selected", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.concepts.TopLevelConcepts.grid = new Lino.WindowAction({  }, function(){
  var p = { "is_main_window": true };
  return new Lino.concepts.TopLevelConcepts.GridPanel(p);
});
Lino.concepts.TopLevelConcepts.validate = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/concepts/TopLevelConcepts", "GET", pk, "validate", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};

// js_render_GridPanel_class concepts.Links
Lino.concepts.Links.GridPanel = Ext.extend(Lino.GridPanel,{
  viewConfig : { "emptyText": "Pas de donn\u00e9es \u00e0 afficher.", "forceFit": true, "getRowClass": Lino.getRowClass },
  ls_url : "/concepts/Links",
  ls_bbar_actions : [ { "auto_save": true, "iconCls": "x-tbar-html", "itemId": "show_as_html", "menu_item_text": "HTML", "overflowText": "HTML", "panel_btn_handler": Lino.list_action_handler('/concepts/Links','show_as_html','GET',Lino.get_current_grid_config), "tooltip": "Show this table in Bootstrap3 interface" } ],
  cell_edit : true,
  title : "Links",
  gc_name : 0,
  stripeRows : true,
  disabled_actions_index : 10,
  ls_store_fields : [ { "name": "id", "type": "int" }, { "name": "type" }, 'typeHidden', { "name": "parent" }, 'parentHidden', { "name": "child" }, 'childHidden', { "name": "workflow_buttons" }, { "name": "description_column" }, { "name": "disabled_fields" }, { "name": "disabled_actions" }, { "name": "disable_editing" } ],
  pk_index : 0,
  ls_grid_configs : [  ],
  ls_id_property : "id",
  page_length : 20,
  initComponent : function() {
    var ww = this.containing_window;
    var id211 = new Ext.form.NumberField({ "selectOnFocus": true });
    var type212 = new Lino.ChoicesFieldElement({ "forceSelection": true, "selectOnFocus": true, "store": [['','<br>']].concat(Lino.concepts.LinkTypes) });
    var parent213 = new Lino.RemoteComboFieldElement({ "allowBlank": false, "emptyText": "Choisir Concept...", "pageSize": 20, "selectOnFocus": true, "store": new Lino.ComplexRemoteComboStore({ "proxy": new Ext.data.HttpProxy({ "method": "GET", "url": "/choices/concepts/Links/parent" }) }) });
    var child214 = new Lino.RemoteComboFieldElement({ "allowBlank": false, "emptyText": "Choisir Concept...", "pageSize": 20, "selectOnFocus": true, "store": new Lino.ComplexRemoteComboStore({ "proxy": new Ext.data.HttpProxy({ "method": "GET", "url": "/choices/concepts/Links/child" }) }) });
    var workflow_buttons_disp215 = new Ext.form.DisplayField({ "always_enabled": true, "disabled": true, "hidden": true, "value": "<br/>" });
    var description_column_disp216 = new Ext.form.DisplayField({ "always_enabled": true, "disabled": true, "hidden": true, "value": "<br/>" });
    this.before_row_edit = function(record) {
    };
    this.ls_columns = [ new Lino.NullNumberColumn({ "colIndex": 0, "dataIndex": "id", "editable": true, "editor": id211, "filter": { "type": "numeric" }, "format": "0", "header": "ID", "sortable": true, "tooltip": "(concepts.Links.id) ", "width": Lino.chars2width(6) }), { "colIndex": 1, "dataIndex": "type", "editable": true, "editor": type212, "filter": { "type": "string" }, "header": "Link Type", "sortable": true, "tooltip": "(concepts.Links.type) ", "width": Lino.chars2width(13) }, { "colIndex": 2, "dataIndex": "parent", "editable": true, "editor": parent213, "filter": { "type": "string" }, "header": "Concept", "renderer": Lino.fk_renderer('parentHidden','Lino.concepts.Concepts.detail'), "sortable": true, "tooltip": "(concepts.Links.parent) ", "width": Lino.chars2width(21) }, { "colIndex": 3, "dataIndex": "child", "editable": true, "editor": child214, "filter": { "type": "string" }, "header": "Concept", "renderer": Lino.fk_renderer('childHidden','Lino.concepts.Concepts.detail'), "sortable": true, "tooltip": "(concepts.Links.child) ", "width": Lino.chars2width(21) }, { "colIndex": 4, "dataIndex": "workflow_buttons", "editable": false, "header": "\u00c9tat", "hidden": true, "sortable": false, "tooltip": "(concepts.Links.workflow_buttons) ", "width": Lino.chars2width(31) }, { "colIndex": 5, "dataIndex": "description_column", "editable": false, "header": "Description", "hidden": true, "sortable": false, "tooltip": "(concepts.Links.description_column) ", "width": Lino.chars2width(31) } ];
    Lino.concepts.Links.GridPanel.superclass.initComponent.call(this);
  }
});

Lino.concepts.Links.show_as_html = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/concepts/Links", "GET", pk, "show_as_html", params, Lino.get_current_grid_config);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.concepts.Links.grid_put = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/concepts/Links", "GET", pk, "grid_put", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.concepts.Links.grid_post = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/concepts/Links", "GET", pk, "grid_post", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.concepts.Links.submit_insert = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/concepts/Links", "GET", pk, "submit_insert", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.concepts.Links.delete_selected = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/concepts/Links", "GET", pk, "delete_selected", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.concepts.Links.grid = new Lino.WindowAction({  }, function(){
  var p = { "is_main_window": true };
  return new Lino.concepts.Links.GridPanel(p);
});

// js_render_GridPanel_class belref.Main
Lino.belref.Main.GridPanel = Ext.extend(Lino.GridPanel,{
  viewConfig : { "emptyText": "Pas de donn\u00e9es \u00e0 afficher.", "forceFit": true, "getRowClass": Lino.getRowClass },
  ls_url : "/belref/Main",
  ls_bbar_actions : [ { "auto_save": true, "iconCls": "x-tbar-html", "itemId": "show_as_html", "menu_item_text": "HTML", "overflowText": "HTML", "panel_btn_handler": Lino.list_action_handler('/belref/Main','show_as_html','GET',Lino.get_current_grid_config), "tooltip": "Show this table in Bootstrap3 interface" }, { "auto_save": true, "iconCls": "x-tbar-application_form", "itemId": "detail", "menu_item_text": "D\u00e9tail", "overflowText": "D\u00e9tail", "panel_btn_handler": Lino.show_detail, "tooltip": "Open a detail window on this record" } ],
  cell_edit : true,
  title : "Concepts primaires",
  gc_name : 0,
  stripeRows : true,
  disabled_actions_index : 8,
  ls_store_fields : [ { "name": "name" }, { "name": "name_nl" }, { "name": "name_de" }, { "name": "id", "type": "int" }, { "name": "abbr" }, { "name": "abbr_nl" }, { "name": "abbr_de" }, { "name": "disabled_fields" }, { "name": "disabled_actions" }, { "name": "disable_editing" } ],
  pk_index : 3,
  ls_grid_configs : [  ],
  ls_id_property : "id",
  page_length : 20,
  initComponent : function() {
    this.ls_detail_handler = Lino.belref.Main.detail;
    this.ls_insert_handler = Lino.belref.Main.insert;
    var ww = this.containing_window;
    var name218 = new Ext.form.TextField({ "allowBlank": false, "maxLength": 200, "selectOnFocus": true });
    var name_nl219 = new Ext.form.TextField({ "maxLength": 200, "selectOnFocus": true });
    var name_de220 = new Ext.form.TextField({ "maxLength": 200, "selectOnFocus": true });
    var id221 = new Ext.form.NumberField({ "selectOnFocus": true });
    var abbr222 = new Ext.form.TextField({ "maxLength": 30, "selectOnFocus": true });
    var abbr_nl223 = new Ext.form.TextField({ "maxLength": 30, "selectOnFocus": true });
    var abbr_de224 = new Ext.form.TextField({ "maxLength": 30, "selectOnFocus": true });
    this.before_row_edit = function(record) {
    };
    this.ls_columns = [ { "colIndex": 0, "dataIndex": "name", "editable": true, "editor": name218, "filter": { "type": "string" }, "header": "D\u00e9signation", "sortable": true, "tooltip": "(belref.Main.name) ", "width": Lino.chars2width(22) }, { "colIndex": 1, "dataIndex": "name_nl", "editable": true, "editor": name_nl219, "filter": { "type": "string" }, "header": "D\u00e9signation (nl)", "sortable": true, "tooltip": "(belref.Main.name_nl) ", "width": Lino.chars2width(22) }, { "colIndex": 2, "dataIndex": "name_de", "editable": true, "editor": name_de220, "filter": { "type": "string" }, "header": "D\u00e9signation (de)", "sortable": true, "tooltip": "(belref.Main.name_de) ", "width": Lino.chars2width(22) }, new Lino.NullNumberColumn({ "colIndex": 3, "dataIndex": "id", "editable": true, "editor": id221, "filter": { "type": "numeric" }, "format": "0", "header": "ID", "sortable": true, "tooltip": "(belref.Main.id) ", "width": Lino.chars2width(6) }), { "colIndex": 4, "dataIndex": "abbr", "editable": true, "editor": abbr222, "filter": { "type": "string" }, "header": "Abbr\u00e9viation", "sortable": true, "tooltip": "(belref.Main.abbr) ", "width": Lino.chars2width(22) }, { "colIndex": 5, "dataIndex": "abbr_nl", "editable": true, "editor": abbr_nl223, "filter": { "type": "string" }, "header": "Abbr\u00e9viation (nl)", "sortable": true, "tooltip": "(belref.Main.abbr_nl) ", "width": Lino.chars2width(22) }, { "colIndex": 6, "dataIndex": "abbr_de", "editable": true, "editor": abbr_de224, "filter": { "type": "string" }, "header": "Abbr\u00e9viation (de)", "sortable": true, "tooltip": "(belref.Main.abbr_de) ", "width": Lino.chars2width(22) } ];
    Lino.belref.Main.GridPanel.superclass.initComponent.call(this);
  }
});

Lino.belref.Main.show_as_html = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/belref/Main", "GET", pk, "show_as_html", params, Lino.get_current_grid_config);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.belref.Main.submit_detail = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/belref/Main", "GET", pk, "submit_detail", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};

Lino.belref.Main.insertPanel = Ext.extend(Lino.concepts.Concepts.DetailFormPanel,{
  empty_title: "Nouveau",
  hide_navigator: true,
  save_action_name: "submit_insert",
  ls_bbar_actions: [  ],
  ls_url: "/belref/Main",
  action_name: "insert",
  initComponent : function() {
    this.ls_detail_handler = Lino.belref.Main.detail;
    this.ls_insert_handler = Lino.belref.Main.insert;
    Lino.belref.Main.insertPanel.superclass.initComponent.call(this);
  }
});

Lino.belref.Main.insert = new Lino.WindowAction({  }, function(){
  var p = { "hide_top_toolbar": true, "is_main_window": true };
  return new Lino.belref.Main.insertPanel(p);
});
Lino.belref.Main.grid_put = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/belref/Main", "GET", pk, "grid_put", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.belref.Main.grid_post = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/belref/Main", "GET", pk, "grid_post", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.belref.Main.submit_insert = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/belref/Main", "GET", pk, "submit_insert", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};

Lino.belref.Main.detailPanel = Ext.extend(Lino.concepts.Concepts.DetailFormPanel,{
  empty_title: "D\u00e9tail",
  save_action_name: "submit_detail",
  ls_bbar_actions: [  ],
  ls_url: "/belref/Main",
  action_name: "detail",
  initComponent : function() {
    this.ls_detail_handler = Lino.belref.Main.detail;
    this.ls_insert_handler = Lino.belref.Main.insert;
    Lino.belref.Main.detailPanel.superclass.initComponent.call(this);
  }
});

Lino.belref.Main.detail = new Lino.WindowAction({  }, function(){
  var p = { "is_main_window": true };
  return new Lino.belref.Main.detailPanel(p);
});
Lino.belref.Main.delete_selected = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/belref/Main", "GET", pk, "delete_selected", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.belref.Main.grid = new Lino.WindowAction({  }, function(){
  var p = { "is_main_window": true };
  return new Lino.belref.Main.GridPanel(p);
});
Lino.belref.Main.validate = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/belref/Main", "GET", pk, "validate", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};

// js_render_GridPanel_class countries.PlacesByPlace
Lino.countries.PlacesByPlace.GridPanel = Ext.extend(Lino.GridPanel,{
  viewConfig : { "emptyText": "Pas de donn\u00e9es \u00e0 afficher.", "forceFit": true, "getRowClass": Lino.getRowClass },
  ls_url : "/countries/PlacesByPlace",
  ls_bbar_actions : [ { "auto_save": true, "iconCls": "x-tbar-html", "itemId": "show_as_html", "menu_item_text": "HTML", "overflowText": "HTML", "panel_btn_handler": Lino.list_action_handler('/countries/PlacesByPlace','show_as_html','GET',Lino.get_current_grid_config), "tooltip": "Show this table in Bootstrap3 interface" }, { "auto_save": true, "iconCls": "x-tbar-application_form", "itemId": "detail", "menu_item_text": "D\u00e9tail", "overflowText": "D\u00e9tail", "panel_btn_handler": Lino.show_detail, "tooltip": "Open a detail window on this record" } ],
  cell_edit : true,
  title : "Subdivisions",
  gc_name : 0,
  stripeRows : true,
  disabled_actions_index : 15,
  ls_store_fields : [ { "name": "name" }, { "name": "name_nl" }, { "name": "name_de" }, { "name": "type" }, 'typeHidden', { "name": "zip_code" }, { "name": "id", "type": "int" }, { "name": "country" }, 'countryHidden', { "name": "inscode" }, { "name": "workflow_buttons" }, { "name": "description_column" }, { "name": "parent" }, 'parentHidden', { "name": "disabled_fields" }, { "name": "disabled_actions" }, { "name": "disable_editing" } ],
  pk_index : 6,
  ls_grid_configs : [  ],
  ls_id_property : "id",
  page_length : 20,
  initComponent : function() {
    this.ls_detail_handler = Lino.countries.PlacesByPlace.detail;
    this.ls_insert_handler = Lino.countries.PlacesByPlace.insert;
    var ww = this.containing_window;
    var name65 = new Ext.form.TextField({ "allowBlank": false, "maxLength": 200, "selectOnFocus": true });
    var name_nl66 = new Ext.form.TextField({ "maxLength": 200, "selectOnFocus": true });
    var name_de67 = new Ext.form.TextField({ "maxLength": 200, "selectOnFocus": true });
    var type68 = new Lino.RemoteComboFieldElement({ "selectOnFocus": true, "store": new Lino.ComplexRemoteComboStore({ "proxy": new Ext.data.HttpProxy({ "method": "GET", "url": "/choices/countries/PlacesByPlace/type" }) }) });
    var zip_code69 = new Ext.form.TextField({ "boxMinWidth": Lino.chars2width(8), "maxLength": 8, "selectOnFocus": true });
    var id70 = new Ext.form.NumberField({ "hidden": true, "selectOnFocus": true });
    var country71 = new Lino.RemoteComboFieldElement({ "allowBlank": false, "emptyText": "Choisir Pays...", "hidden": true, "pageSize": 20, "selectOnFocus": true, "store": new Lino.ComplexRemoteComboStore({ "proxy": new Ext.data.HttpProxy({ "method": "GET", "url": "/choices/countries/PlacesByPlace/country" }) }) });
    var inscode72 = new Ext.form.TextField({ "boxMinWidth": Lino.chars2width(5), "hidden": true, "maxLength": 5, "selectOnFocus": true });
    var workflow_buttons_disp73 = new Ext.form.DisplayField({ "always_enabled": true, "disabled": true, "hidden": true, "value": "<br/>" });
    var description_column_disp74 = new Ext.form.DisplayField({ "always_enabled": true, "disabled": true, "hidden": true, "value": "<br/>" });
    var parent75 = new Lino.RemoteComboFieldElement({ "emptyText": "Choisir Endroit...", "hidden": true, "pageSize": 20, "selectOnFocus": true, "store": new Lino.ComplexRemoteComboStore({ "proxy": new Ext.data.HttpProxy({ "method": "GET", "url": "/choices/countries/PlacesByPlace/parent" }) }) });
    this.before_row_edit = function(record) {
      type68.setContextValue('country', record ? record.data['countryHidden'] : undefined);
    };
    this.onRender = function(ct, position) {
      country71.on('change',Lino.chooser_handler(type68,'country'));
      Lino.countries.PlacesByPlace.GridPanel.superclass.onRender.call(this, ct, position);
    }
    this.ls_columns = [ { "colIndex": 0, "dataIndex": "name", "editable": true, "editor": name65, "filter": { "type": "string" }, "header": "D\u00e9signation", "sortable": true, "tooltip": "(countries.PlacesByPlace.name) ", "width": Lino.chars2width(22) }, { "colIndex": 1, "dataIndex": "name_nl", "editable": true, "editor": name_nl66, "filter": { "type": "string" }, "header": "D\u00e9signation (nl)", "sortable": true, "tooltip": "(countries.PlacesByPlace.name_nl) ", "width": Lino.chars2width(22) }, { "colIndex": 2, "dataIndex": "name_de", "editable": true, "editor": name_de67, "filter": { "type": "string" }, "header": "D\u00e9signation (de)", "sortable": true, "tooltip": "(countries.PlacesByPlace.name_de) ", "width": Lino.chars2width(22) }, { "colIndex": 3, "dataIndex": "type", "editable": true, "editor": type68, "filter": { "type": "string" }, "header": "Type d'endroit", "sortable": true, "tooltip": "(countries.PlacesByPlace.type) ", "width": Lino.chars2width(11) }, { "colIndex": 4, "dataIndex": "zip_code", "editable": true, "editor": zip_code69, "filter": { "type": "string" }, "header": "zip code", "sortable": true, "tooltip": "(countries.PlacesByPlace.zip_code) ", "width": Lino.chars2width(10) }, new Lino.NullNumberColumn({ "colIndex": 5, "dataIndex": "id", "editable": true, "editor": id70, "filter": { "type": "numeric" }, "format": "0", "header": "ID", "hidden": true, "sortable": true, "tooltip": "(countries.PlacesByPlace.id) ", "width": Lino.chars2width(6) }), { "colIndex": 6, "dataIndex": "country", "editable": true, "editor": country71, "filter": { "type": "string" }, "header": "Pays", "hidden": true, "renderer": Lino.fk_renderer('countryHidden','Lino.countries.Countries.detail'), "sortable": true, "tooltip": "(countries.PlacesByPlace.country) ", "width": Lino.chars2width(21) }, { "colIndex": 7, "dataIndex": "inscode", "editable": true, "editor": inscode72, "filter": { "type": "string" }, "header": "INS code", "hidden": true, "sortable": true, "tooltip": "(countries.PlacesByPlace.inscode) The official code for this place used by statbel.fgov.be", "width": Lino.chars2width(7) }, { "colIndex": 8, "dataIndex": "workflow_buttons", "editable": false, "header": "\u00c9tat", "hidden": true, "sortable": false, "tooltip": "(countries.PlacesByPlace.workflow_buttons) ", "width": Lino.chars2width(31) }, { "colIndex": 9, "dataIndex": "description_column", "editable": false, "header": "Description", "hidden": true, "sortable": false, "tooltip": "(countries.PlacesByPlace.description_column) ", "width": Lino.chars2width(31) }, { "colIndex": 10, "dataIndex": "parent", "editable": true, "editor": parent75, "filter": { "type": "string" }, "header": "Part of", "hidden": true, "renderer": Lino.fk_renderer('parentHidden','Lino.countries.Places.detail'), "sortable": true, "tooltip": "(countries.PlacesByPlace.parent) The superordinate geographic place of which this place is a part.", "width": Lino.chars2width(21) } ];
    Lino.countries.PlacesByPlace.GridPanel.superclass.initComponent.call(this);
  }
});

Lino.countries.PlacesByPlace.show_as_html = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/countries/PlacesByPlace", "GET", pk, "show_as_html", params, Lino.get_current_grid_config);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.countries.PlacesByPlace.submit_detail = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/countries/PlacesByPlace", "GET", pk, "submit_detail", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};

Lino.countries.PlacesByPlace.insertPanel = Ext.extend(Lino.countries.Places.DetailFormPanel,{
  empty_title: "Nouveau",
  hide_navigator: true,
  save_action_name: "submit_insert",
  ls_bbar_actions: [  ],
  ls_url: "/countries/PlacesByPlace",
  action_name: "insert",
  initComponent : function() {
    this.ls_detail_handler = Lino.countries.PlacesByPlace.detail;
    this.ls_insert_handler = Lino.countries.PlacesByPlace.insert;
    Lino.countries.PlacesByPlace.insertPanel.superclass.initComponent.call(this);
  }
});

Lino.countries.PlacesByPlace.insert = new Lino.WindowAction({  }, function(){
  var p = { "hide_top_toolbar": true, "is_main_window": true };
  return new Lino.countries.PlacesByPlace.insertPanel(p);
});
Lino.countries.PlacesByPlace.grid_put = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/countries/PlacesByPlace", "GET", pk, "grid_put", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.countries.PlacesByPlace.grid_post = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/countries/PlacesByPlace", "GET", pk, "grid_post", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.countries.PlacesByPlace.submit_insert = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/countries/PlacesByPlace", "GET", pk, "submit_insert", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.countries.PlacesByPlace.duplicate = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/countries/PlacesByPlace", "GET", pk, "duplicate", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};

Lino.countries.PlacesByPlace.detailPanel = Ext.extend(Lino.countries.Places.DetailFormPanel,{
  empty_title: "D\u00e9tail",
  save_action_name: "submit_detail",
  ls_bbar_actions: [  ],
  ls_url: "/countries/PlacesByPlace",
  action_name: "detail",
  initComponent : function() {
    this.ls_detail_handler = Lino.countries.PlacesByPlace.detail;
    this.ls_insert_handler = Lino.countries.PlacesByPlace.insert;
    Lino.countries.PlacesByPlace.detailPanel.superclass.initComponent.call(this);
  }
});

Lino.countries.PlacesByPlace.detail = new Lino.WindowAction({  }, function(){
  var p = { "is_main_window": true };
  return new Lino.countries.PlacesByPlace.detailPanel(p);
});
Lino.countries.PlacesByPlace.delete_selected = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/countries/PlacesByPlace", "GET", pk, "delete_selected", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.countries.PlacesByPlace.grid = new Lino.WindowAction({  }, function(){
  var p = { "is_main_window": true };
  return new Lino.countries.PlacesByPlace.GridPanel(p);
});
Lino.countries.PlacesByPlace.validate = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/countries/PlacesByPlace", "GET", pk, "validate", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};

// js_render_GridPanel_class countries.PlacesByCountry
Lino.countries.PlacesByCountry.GridPanel = Ext.extend(Lino.GridPanel,{
  viewConfig : { "emptyText": "Pas de donn\u00e9es \u00e0 afficher.", "forceFit": true, "getRowClass": Lino.getRowClass },
  ls_url : "/countries/PlacesByCountry",
  ls_bbar_actions : [ { "auto_save": true, "iconCls": "x-tbar-html", "itemId": "show_as_html", "menu_item_text": "HTML", "overflowText": "HTML", "panel_btn_handler": Lino.list_action_handler('/countries/PlacesByCountry','show_as_html','GET',Lino.get_current_grid_config), "tooltip": "Show this table in Bootstrap3 interface" }, { "auto_save": true, "iconCls": "x-tbar-application_form", "itemId": "detail", "menu_item_text": "D\u00e9tail", "overflowText": "D\u00e9tail", "panel_btn_handler": Lino.show_detail, "tooltip": "Open a detail window on this record" } ],
  cell_edit : true,
  title : "Endroits",
  gc_name : 0,
  stripeRows : true,
  disabled_actions_index : 15,
  ls_store_fields : [ { "name": "name" }, { "name": "name_nl" }, { "name": "name_de" }, { "name": "type" }, 'typeHidden', { "name": "zip_code" }, { "name": "id", "type": "int" }, { "name": "parent" }, 'parentHidden', { "name": "inscode" }, { "name": "workflow_buttons" }, { "name": "description_column" }, { "name": "country" }, 'countryHidden', { "name": "disabled_fields" }, { "name": "disabled_actions" }, { "name": "disable_editing" } ],
  pk_index : 6,
  ls_grid_configs : [  ],
  ls_id_property : "id",
  page_length : 20,
  initComponent : function() {
    this.ls_detail_handler = Lino.countries.PlacesByCountry.detail;
    this.ls_insert_handler = Lino.countries.PlacesByCountry.insert;
    var ww = this.containing_window;
    var name35 = new Ext.form.TextField({ "allowBlank": false, "maxLength": 200, "selectOnFocus": true });
    var name_nl36 = new Ext.form.TextField({ "maxLength": 200, "selectOnFocus": true });
    var name_de37 = new Ext.form.TextField({ "maxLength": 200, "selectOnFocus": true });
    var type38 = new Lino.RemoteComboFieldElement({ "selectOnFocus": true, "store": new Lino.ComplexRemoteComboStore({ "proxy": new Ext.data.HttpProxy({ "method": "GET", "url": "/choices/countries/PlacesByCountry/type" }) }) });
    var zip_code39 = new Ext.form.TextField({ "boxMinWidth": Lino.chars2width(8), "maxLength": 8, "selectOnFocus": true });
    var id40 = new Ext.form.NumberField({ "hidden": true, "selectOnFocus": true });
    var parent41 = new Lino.RemoteComboFieldElement({ "emptyText": "Choisir Endroit...", "hidden": true, "pageSize": 20, "selectOnFocus": true, "store": new Lino.ComplexRemoteComboStore({ "proxy": new Ext.data.HttpProxy({ "method": "GET", "url": "/choices/countries/PlacesByCountry/parent" }) }) });
    var inscode42 = new Ext.form.TextField({ "boxMinWidth": Lino.chars2width(5), "hidden": true, "maxLength": 5, "selectOnFocus": true });
    var workflow_buttons_disp43 = new Ext.form.DisplayField({ "always_enabled": true, "disabled": true, "hidden": true, "value": "<br/>" });
    var description_column_disp44 = new Ext.form.DisplayField({ "always_enabled": true, "disabled": true, "hidden": true, "value": "<br/>" });
    var country45 = new Lino.RemoteComboFieldElement({ "allowBlank": false, "emptyText": "Choisir Pays...", "hidden": true, "pageSize": 20, "selectOnFocus": true, "store": new Lino.ComplexRemoteComboStore({ "proxy": new Ext.data.HttpProxy({ "method": "GET", "url": "/choices/countries/PlacesByCountry/country" }) }) });
    this.before_row_edit = function(record) {
      var bp = this.get_base_params();
      type38.setContextValue('mk',bp['mk']);
      type38.setContextValue('mt',bp['mt']);
    };
    this.onRender = function(ct, position) {
      country45.on('change',Lino.chooser_handler(type38,'country'));
      Lino.countries.PlacesByCountry.GridPanel.superclass.onRender.call(this, ct, position);
    }
    this.ls_columns = [ { "colIndex": 0, "dataIndex": "name", "editable": true, "editor": name35, "filter": { "type": "string" }, "header": "D\u00e9signation", "sortable": true, "tooltip": "(countries.PlacesByCountry.name) ", "width": Lino.chars2width(22) }, { "colIndex": 1, "dataIndex": "name_nl", "editable": true, "editor": name_nl36, "filter": { "type": "string" }, "header": "D\u00e9signation (nl)", "sortable": true, "tooltip": "(countries.PlacesByCountry.name_nl) ", "width": Lino.chars2width(22) }, { "colIndex": 2, "dataIndex": "name_de", "editable": true, "editor": name_de37, "filter": { "type": "string" }, "header": "D\u00e9signation (de)", "sortable": true, "tooltip": "(countries.PlacesByCountry.name_de) ", "width": Lino.chars2width(22) }, { "colIndex": 3, "dataIndex": "type", "editable": true, "editor": type38, "filter": { "type": "string" }, "header": "Type d'endroit", "sortable": true, "tooltip": "(countries.PlacesByCountry.type) ", "width": Lino.chars2width(11) }, { "colIndex": 4, "dataIndex": "zip_code", "editable": true, "editor": zip_code39, "filter": { "type": "string" }, "header": "zip code", "sortable": true, "tooltip": "(countries.PlacesByCountry.zip_code) ", "width": Lino.chars2width(10) }, new Lino.NullNumberColumn({ "colIndex": 5, "dataIndex": "id", "editable": true, "editor": id40, "filter": { "type": "numeric" }, "format": "0", "header": "ID", "hidden": true, "sortable": true, "tooltip": "(countries.PlacesByCountry.id) ", "width": Lino.chars2width(6) }), { "colIndex": 6, "dataIndex": "parent", "editable": true, "editor": parent41, "filter": { "type": "string" }, "header": "Part of", "hidden": true, "renderer": Lino.fk_renderer('parentHidden','Lino.countries.Places.detail'), "sortable": true, "tooltip": "(countries.PlacesByCountry.parent) The superordinate geographic place of which this place is a part.", "width": Lino.chars2width(21) }, { "colIndex": 7, "dataIndex": "inscode", "editable": true, "editor": inscode42, "filter": { "type": "string" }, "header": "INS code", "hidden": true, "sortable": true, "tooltip": "(countries.PlacesByCountry.inscode) The official code for this place used by statbel.fgov.be", "width": Lino.chars2width(7) }, { "colIndex": 8, "dataIndex": "workflow_buttons", "editable": false, "header": "\u00c9tat", "hidden": true, "sortable": false, "tooltip": "(countries.PlacesByCountry.workflow_buttons) ", "width": Lino.chars2width(31) }, { "colIndex": 9, "dataIndex": "description_column", "editable": false, "header": "Description", "hidden": true, "sortable": false, "tooltip": "(countries.PlacesByCountry.description_column) ", "width": Lino.chars2width(31) }, { "colIndex": 10, "dataIndex": "country", "editable": true, "editor": country45, "filter": { "type": "string" }, "header": "Pays", "hidden": true, "renderer": Lino.fk_renderer('countryHidden','Lino.countries.Countries.detail'), "sortable": true, "tooltip": "(countries.PlacesByCountry.country) ", "width": Lino.chars2width(21) } ];
    Lino.countries.PlacesByCountry.GridPanel.superclass.initComponent.call(this);
  }
});

Lino.countries.PlacesByCountry.show_as_html = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/countries/PlacesByCountry", "GET", pk, "show_as_html", params, Lino.get_current_grid_config);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.countries.PlacesByCountry.submit_detail = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/countries/PlacesByCountry", "GET", pk, "submit_detail", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};

Lino.countries.PlacesByCountry.insertPanel = Ext.extend(Lino.countries.Places.DetailFormPanel,{
  empty_title: "Nouveau",
  hide_navigator: true,
  save_action_name: "submit_insert",
  ls_bbar_actions: [  ],
  ls_url: "/countries/PlacesByCountry",
  action_name: "insert",
  initComponent : function() {
    this.ls_detail_handler = Lino.countries.PlacesByCountry.detail;
    this.ls_insert_handler = Lino.countries.PlacesByCountry.insert;
    Lino.countries.PlacesByCountry.insertPanel.superclass.initComponent.call(this);
  }
});

Lino.countries.PlacesByCountry.insert = new Lino.WindowAction({  }, function(){
  var p = { "hide_top_toolbar": true, "is_main_window": true };
  return new Lino.countries.PlacesByCountry.insertPanel(p);
});
Lino.countries.PlacesByCountry.grid_put = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/countries/PlacesByCountry", "GET", pk, "grid_put", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.countries.PlacesByCountry.grid_post = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/countries/PlacesByCountry", "GET", pk, "grid_post", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.countries.PlacesByCountry.submit_insert = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/countries/PlacesByCountry", "GET", pk, "submit_insert", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.countries.PlacesByCountry.duplicate = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/countries/PlacesByCountry", "GET", pk, "duplicate", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};

Lino.countries.PlacesByCountry.detailPanel = Ext.extend(Lino.countries.Places.DetailFormPanel,{
  empty_title: "D\u00e9tail",
  save_action_name: "submit_detail",
  ls_bbar_actions: [  ],
  ls_url: "/countries/PlacesByCountry",
  action_name: "detail",
  initComponent : function() {
    this.ls_detail_handler = Lino.countries.PlacesByCountry.detail;
    this.ls_insert_handler = Lino.countries.PlacesByCountry.insert;
    Lino.countries.PlacesByCountry.detailPanel.superclass.initComponent.call(this);
  }
});

Lino.countries.PlacesByCountry.detail = new Lino.WindowAction({  }, function(){
  var p = { "is_main_window": true };
  return new Lino.countries.PlacesByCountry.detailPanel(p);
});
Lino.countries.PlacesByCountry.delete_selected = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/countries/PlacesByCountry", "GET", pk, "delete_selected", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.countries.PlacesByCountry.grid = new Lino.WindowAction({  }, function(){
  var p = { "is_main_window": true };
  return new Lino.countries.PlacesByCountry.GridPanel(p);
});
Lino.countries.PlacesByCountry.validate = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/countries/PlacesByCountry", "GET", pk, "validate", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};

// js_render_GridPanel_class concepts.Parents
Lino.concepts.Parents.GridPanel = Ext.extend(Lino.GridPanel,{
  viewConfig : { "emptyText": "Pas de donn\u00e9es \u00e0 afficher.", "forceFit": true, "getRowClass": Lino.getRowClass },
  ls_url : "/concepts/Parents",
  ls_bbar_actions : [ { "auto_save": true, "iconCls": "x-tbar-html", "itemId": "show_as_html", "menu_item_text": "HTML", "overflowText": "HTML", "panel_btn_handler": Lino.list_action_handler('/concepts/Parents','show_as_html','GET',Lino.get_current_grid_config), "tooltip": "Show this table in Bootstrap3 interface" } ],
  cell_edit : true,
  title : "Concepts subordonn\u00e9s",
  gc_name : 0,
  stripeRows : true,
  disabled_actions_index : 10,
  ls_store_fields : [ { "name": "id", "type": "int" }, { "name": "type" }, 'typeHidden', { "name": "parent" }, 'parentHidden', { "name": "workflow_buttons" }, { "name": "description_column" }, { "name": "child" }, 'childHidden', { "name": "disabled_fields" }, { "name": "disabled_actions" }, { "name": "disable_editing" } ],
  pk_index : 0,
  ls_grid_configs : [  ],
  ls_id_property : "id",
  page_length : 20,
  initComponent : function() {
    var ww = this.containing_window;
    var id129 = new Ext.form.NumberField({ "selectOnFocus": true });
    var type130 = new Lino.ChoicesFieldElement({ "forceSelection": true, "selectOnFocus": true, "store": [['','<br>']].concat(Lino.concepts.LinkTypes) });
    var parent131 = new Lino.RemoteComboFieldElement({ "allowBlank": false, "emptyText": "Choisir Concept...", "pageSize": 20, "selectOnFocus": true, "store": new Lino.ComplexRemoteComboStore({ "proxy": new Ext.data.HttpProxy({ "method": "GET", "url": "/choices/concepts/Parents/parent" }) }) });
    var workflow_buttons_disp132 = new Ext.form.DisplayField({ "always_enabled": true, "disabled": true, "hidden": true, "value": "<br/>" });
    var description_column_disp133 = new Ext.form.DisplayField({ "always_enabled": true, "disabled": true, "hidden": true, "value": "<br/>" });
    var child134 = new Lino.RemoteComboFieldElement({ "allowBlank": false, "emptyText": "Choisir Concept...", "hidden": true, "pageSize": 20, "selectOnFocus": true, "store": new Lino.ComplexRemoteComboStore({ "proxy": new Ext.data.HttpProxy({ "method": "GET", "url": "/choices/concepts/Parents/child" }) }) });
    this.before_row_edit = function(record) {
    };
    this.ls_columns = [ new Lino.NullNumberColumn({ "colIndex": 0, "dataIndex": "id", "editable": true, "editor": id129, "filter": { "type": "numeric" }, "format": "0", "header": "ID", "sortable": true, "tooltip": "(concepts.Parents.id) ", "width": Lino.chars2width(6) }), { "colIndex": 1, "dataIndex": "type", "editable": true, "editor": type130, "filter": { "type": "string" }, "header": "Link Type", "sortable": true, "tooltip": "(concepts.Parents.type) ", "width": Lino.chars2width(13) }, { "colIndex": 2, "dataIndex": "parent", "editable": true, "editor": parent131, "filter": { "type": "string" }, "header": "Concept", "renderer": Lino.fk_renderer('parentHidden','Lino.concepts.Concepts.detail'), "sortable": true, "tooltip": "(concepts.Parents.parent) ", "width": Lino.chars2width(21) }, { "colIndex": 3, "dataIndex": "workflow_buttons", "editable": false, "header": "\u00c9tat", "hidden": true, "sortable": false, "tooltip": "(concepts.Parents.workflow_buttons) ", "width": Lino.chars2width(31) }, { "colIndex": 4, "dataIndex": "description_column", "editable": false, "header": "Description", "hidden": true, "sortable": false, "tooltip": "(concepts.Parents.description_column) ", "width": Lino.chars2width(31) }, { "colIndex": 5, "dataIndex": "child", "editable": true, "editor": child134, "filter": { "type": "string" }, "header": "Concept", "hidden": true, "renderer": Lino.fk_renderer('childHidden','Lino.concepts.Concepts.detail'), "sortable": true, "tooltip": "(concepts.Parents.child) ", "width": Lino.chars2width(21) } ];
    Lino.concepts.Parents.GridPanel.superclass.initComponent.call(this);
  }
});

Lino.concepts.Parents.show_as_html = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/concepts/Parents", "GET", pk, "show_as_html", params, Lino.get_current_grid_config);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.concepts.Parents.grid_put = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/concepts/Parents", "GET", pk, "grid_put", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.concepts.Parents.grid_post = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/concepts/Parents", "GET", pk, "grid_post", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.concepts.Parents.submit_insert = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/concepts/Parents", "GET", pk, "submit_insert", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.concepts.Parents.delete_selected = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/concepts/Parents", "GET", pk, "delete_selected", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.concepts.Parents.grid = new Lino.WindowAction({  }, function(){
  var p = { "is_main_window": true };
  return new Lino.concepts.Parents.GridPanel(p);
});

// js_render_GridPanel_class concepts.Children
Lino.concepts.Children.GridPanel = Ext.extend(Lino.GridPanel,{
  viewConfig : { "emptyText": "Pas de donn\u00e9es \u00e0 afficher.", "forceFit": true, "getRowClass": Lino.getRowClass },
  ls_url : "/concepts/Children",
  ls_bbar_actions : [ { "auto_save": true, "iconCls": "x-tbar-html", "itemId": "show_as_html", "menu_item_text": "HTML", "overflowText": "HTML", "panel_btn_handler": Lino.list_action_handler('/concepts/Children','show_as_html','GET',Lino.get_current_grid_config), "tooltip": "Show this table in Bootstrap3 interface" } ],
  cell_edit : true,
  title : "Concepts sous-jacents",
  gc_name : 0,
  stripeRows : true,
  disabled_actions_index : 10,
  ls_store_fields : [ { "name": "id", "type": "int" }, { "name": "type" }, 'typeHidden', { "name": "child" }, 'childHidden', { "name": "workflow_buttons" }, { "name": "description_column" }, { "name": "parent" }, 'parentHidden', { "name": "disabled_fields" }, { "name": "disabled_actions" }, { "name": "disable_editing" } ],
  pk_index : 0,
  ls_grid_configs : [  ],
  ls_id_property : "id",
  page_length : 20,
  initComponent : function() {
    var ww = this.containing_window;
    var id137 = new Ext.form.NumberField({ "selectOnFocus": true });
    var type138 = new Lino.ChoicesFieldElement({ "forceSelection": true, "selectOnFocus": true, "store": [['','<br>']].concat(Lino.concepts.LinkTypes) });
    var child139 = new Lino.RemoteComboFieldElement({ "allowBlank": false, "emptyText": "Choisir Concept...", "pageSize": 20, "selectOnFocus": true, "store": new Lino.ComplexRemoteComboStore({ "proxy": new Ext.data.HttpProxy({ "method": "GET", "url": "/choices/concepts/Children/child" }) }) });
    var workflow_buttons_disp140 = new Ext.form.DisplayField({ "always_enabled": true, "disabled": true, "hidden": true, "value": "<br/>" });
    var description_column_disp141 = new Ext.form.DisplayField({ "always_enabled": true, "disabled": true, "hidden": true, "value": "<br/>" });
    var parent142 = new Lino.RemoteComboFieldElement({ "allowBlank": false, "emptyText": "Choisir Concept...", "hidden": true, "pageSize": 20, "selectOnFocus": true, "store": new Lino.ComplexRemoteComboStore({ "proxy": new Ext.data.HttpProxy({ "method": "GET", "url": "/choices/concepts/Children/parent" }) }) });
    this.before_row_edit = function(record) {
    };
    this.ls_columns = [ new Lino.NullNumberColumn({ "colIndex": 0, "dataIndex": "id", "editable": true, "editor": id137, "filter": { "type": "numeric" }, "format": "0", "header": "ID", "sortable": true, "tooltip": "(concepts.Children.id) ", "width": Lino.chars2width(6) }), { "colIndex": 1, "dataIndex": "type", "editable": true, "editor": type138, "filter": { "type": "string" }, "header": "Link Type", "sortable": true, "tooltip": "(concepts.Children.type) ", "width": Lino.chars2width(13) }, { "colIndex": 2, "dataIndex": "child", "editable": true, "editor": child139, "filter": { "type": "string" }, "header": "Concept", "renderer": Lino.fk_renderer('childHidden','Lino.concepts.Concepts.detail'), "sortable": true, "tooltip": "(concepts.Children.child) ", "width": Lino.chars2width(21) }, { "colIndex": 3, "dataIndex": "workflow_buttons", "editable": false, "header": "\u00c9tat", "hidden": true, "sortable": false, "tooltip": "(concepts.Children.workflow_buttons) ", "width": Lino.chars2width(31) }, { "colIndex": 4, "dataIndex": "description_column", "editable": false, "header": "Description", "hidden": true, "sortable": false, "tooltip": "(concepts.Children.description_column) ", "width": Lino.chars2width(31) }, { "colIndex": 5, "dataIndex": "parent", "editable": true, "editor": parent142, "filter": { "type": "string" }, "header": "Concept", "hidden": true, "renderer": Lino.fk_renderer('parentHidden','Lino.concepts.Concepts.detail'), "sortable": true, "tooltip": "(concepts.Children.parent) ", "width": Lino.chars2width(21) } ];
    Lino.concepts.Children.GridPanel.superclass.initComponent.call(this);
  }
});

Lino.concepts.Children.show_as_html = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/concepts/Children", "GET", pk, "show_as_html", params, Lino.get_current_grid_config);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.concepts.Children.grid_put = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/concepts/Children", "GET", pk, "grid_put", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.concepts.Children.grid_post = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/concepts/Children", "GET", pk, "grid_post", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.concepts.Children.submit_insert = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/concepts/Children", "GET", pk, "submit_insert", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.concepts.Children.delete_selected = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/concepts/Children", "GET", pk, "delete_selected", params, null);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.concepts.Children.grid = new Lino.WindowAction({  }, function(){
  var p = { "is_main_window": true };
  return new Lino.concepts.Children.GridPanel(p);
});

// js_render_GridPanel_class about.Models
Lino.about.Models.GridPanel = Ext.extend(Lino.GridPanel,{
  ls_url : "/about/Models",
  ls_bbar_actions : [ { "auto_save": true, "iconCls": "x-tbar-html", "itemId": "show_as_html", "menu_item_text": "HTML", "overflowText": "HTML", "panel_btn_handler": Lino.list_action_handler('/about/Models','show_as_html','GET',Lino.get_current_grid_config), "tooltip": "Show this table in Bootstrap3 interface" }, { "auto_save": true, "iconCls": "x-tbar-application_form", "itemId": "detail", "menu_item_text": "D\u00e9tail", "overflowText": "D\u00e9tail", "panel_btn_handler": Lino.show_detail, "tooltip": "Open a detail window on this record" } ],
  cell_edit : true,
  title : "Models",
  page_length : 20,
  gc_name : 0,
  stripeRows : true,
  disabled_actions_index : 5,
  ls_store_fields : [ { "name": "app" }, { "name": "name" }, { "name": "docstring" }, { "name": "rows" }, { "name": "detail_action" }, { "name": "disabled_actions" } ],
  ls_grid_configs : [  ],
  viewConfig : { "emptyText": "Pas de donn\u00e9es \u00e0 afficher.", "forceFit": true },
  disable_editing : true,
  initComponent : function() {
    this.ls_detail_handler = Lino.about.Models.detail;
    var ww = this.containing_window;
    var app_disp226 = new Ext.form.DisplayField({ "always_enabled": true, "disabled": true, "value": "<br/>" });
    var name_disp227 = new Ext.form.DisplayField({ "always_enabled": true, "disabled": true, "value": "<br/>" });
    var docstring_disp228 = new Ext.form.DisplayField({ "always_enabled": true, "disabled": true, "value": "<br/>" });
    var rows229 = new Ext.form.NumberField({ "disabled": true });
    var detail_action_disp230 = new Ext.form.DisplayField({ "always_enabled": true, "disabled": true, "value": "<br/>" });
    this.before_row_edit = function(record) {
    };
    this.ls_columns = [ { "colIndex": 0, "dataIndex": "app", "editable": false, "header": "app_label", "sortable": false, "tooltip": "(about.Models.app) ", "width": Lino.chars2width(31) }, { "colIndex": 1, "dataIndex": "name", "editable": false, "header": "name", "sortable": false, "tooltip": "(about.Models.name) ", "width": Lino.chars2width(31) }, { "colIndex": 2, "dataIndex": "docstring", "editable": false, "header": "docstring", "sortable": false, "tooltip": "(about.Models.docstring) ", "width": Lino.chars2width(31) }, new Lino.NullNumberColumn({ "colIndex": 3, "dataIndex": "rows", "editable": false, "format": "0", "header": "Rows", "sortable": false, "tooltip": "(about.Models.rows) ", "width": Lino.chars2width(6) }), { "colIndex": 4, "dataIndex": "detail_action", "editable": false, "header": "detail_action", "sortable": false, "tooltip": "(about.Models.detail_action) ", "width": Lino.chars2width(31) } ];
    Lino.about.Models.GridPanel.superclass.initComponent.call(this);
  }
});

Lino.about.Models.show_as_html = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/about/Models", "GET", pk, "show_as_html", params, Lino.get_current_grid_config);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};

Lino.about.Models.detailPanel = Ext.extend(Lino.about.Models.DetailFormPanel,{
  empty_title: "D\u00e9tail",
  save_action_name: "submit_detail",
  ls_bbar_actions: [  ],
  ls_url: "/about/Models",
  action_name: "detail",
  initComponent : function() {
    this.ls_detail_handler = Lino.about.Models.detail;
    Lino.about.Models.detailPanel.superclass.initComponent.call(this);
  }
});

Lino.about.Models.detail = new Lino.WindowAction({  }, function(){
  var p = { "is_main_window": true };
  return new Lino.about.Models.detailPanel(p);
});
Lino.about.Models.grid = new Lino.WindowAction({  }, function(){
  var p = { "is_main_window": true };
  return new Lino.about.Models.GridPanel(p);
});

// js_render_GridPanel_class about.FieldsByModel
Lino.about.FieldsByModel.GridPanel = Ext.extend(Lino.GridPanel,{
  ls_url : "/about/FieldsByModel",
  ls_bbar_actions : [ { "auto_save": true, "iconCls": "x-tbar-html", "itemId": "show_as_html", "menu_item_text": "HTML", "overflowText": "HTML", "panel_btn_handler": Lino.list_action_handler('/about/FieldsByModel','show_as_html','GET',Lino.get_current_grid_config), "tooltip": "Show this table in Bootstrap3 interface" } ],
  cell_edit : true,
  title : "Fields",
  page_length : 20,
  gc_name : 0,
  stripeRows : true,
  disabled_actions_index : 3,
  ls_store_fields : [ { "name": "name" }, { "name": "verbose_name" }, { "name": "help_text_column" }, { "name": "disabled_actions" } ],
  ls_grid_configs : [  ],
  viewConfig : { "emptyText": "Pas de donn\u00e9es \u00e0 afficher.", "forceFit": true },
  disable_editing : true,
  initComponent : function() {
    var ww = this.containing_window;
    var name_disp160 = new Ext.form.DisplayField({ "always_enabled": true, "disabled": true, "value": "<br/>" });
    var verbose_name_disp161 = new Ext.form.DisplayField({ "always_enabled": true, "disabled": true, "value": "<br/>" });
    var help_text_column_disp162 = new Ext.form.DisplayField({ "always_enabled": true, "disabled": true, "value": "<br/>" });
    this.before_row_edit = function(record) {
    };
    this.ls_columns = [ { "colIndex": 0, "dataIndex": "name", "editable": false, "header": "name", "sortable": false, "tooltip": "(about.FieldsByModel.name) ", "width": Lino.chars2width(31) }, { "colIndex": 1, "dataIndex": "verbose_name", "editable": false, "header": "verbose name", "sortable": false, "tooltip": "(about.FieldsByModel.verbose_name) ", "width": Lino.chars2width(31) }, { "colIndex": 2, "dataIndex": "help_text_column", "editable": false, "header": "help text", "sortable": false, "tooltip": "(about.FieldsByModel.help_text_column) ", "width": Lino.chars2width(31) } ];
    Lino.about.FieldsByModel.GridPanel.superclass.initComponent.call(this);
  }
});

Lino.about.FieldsByModel.show_as_html = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/about/FieldsByModel", "GET", pk, "show_as_html", params, Lino.get_current_grid_config);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.about.FieldsByModel.grid = new Lino.WindowAction({  }, function(){
  var p = { "is_main_window": true };
  return new Lino.about.FieldsByModel.GridPanel(p);
});

// js_render_GridPanel_class about.Inspector
Lino.about.Inspector.GridPanel = Ext.extend(Lino.GridPanel,{
  ls_url : "/about/Inspector",
  ls_bbar_actions : [ { "auto_save": true, "iconCls": "x-tbar-html", "itemId": "show_as_html", "menu_item_text": "HTML", "overflowText": "HTML", "panel_btn_handler": Lino.list_action_handler('/about/Inspector','show_as_html','GET',Lino.get_current_grid_config), "tooltip": "Show this table in Bootstrap3 interface" } ],
  cell_edit : true,
  title : "Inspector",
  page_length : 20,
  gc_name : 0,
  stripeRows : true,
  disabled_actions_index : 3,
  ls_store_fields : [ { "name": "i_name" }, { "name": "i_type" }, { "name": "i_value" }, { "name": "disabled_actions" } ],
  ls_grid_configs : [  ],
  viewConfig : { "emptyText": "Pas de donn\u00e9es \u00e0 afficher.", "forceFit": true },
  disable_editing : true,
  initComponent : function() {
    var ww = this.containing_window;
    var i_name_disp232 = new Ext.form.DisplayField({ "always_enabled": true, "disabled": true, "value": "<br/>" });
    var i_type_disp233 = new Ext.form.DisplayField({ "always_enabled": true, "disabled": true, "value": "<br/>" });
    var i_value_disp234 = new Ext.form.DisplayField({ "always_enabled": true, "disabled": true, "value": "<br/>" });
    this.before_row_edit = function(record) {
    };
    this.ls_columns = [ { "colIndex": 0, "dataIndex": "i_name", "editable": false, "header": "Nom", "sortable": false, "tooltip": "(about.Inspector.i_name) ", "width": Lino.chars2width(31) }, { "colIndex": 1, "dataIndex": "i_type", "editable": false, "header": "Type", "sortable": false, "tooltip": "(about.Inspector.i_type) ", "width": Lino.chars2width(31) }, { "colIndex": 2, "dataIndex": "i_value", "editable": false, "header": "Valeur", "sortable": false, "tooltip": "(about.Inspector.i_value) ", "width": Lino.chars2width(31) } ];
    Lino.about.Inspector.GridPanel.superclass.initComponent.call(this);
  }
});

Lino.about.Inspector.show_as_html = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/about/Inspector", "GET", pk, "show_as_html", params, Lino.get_current_grid_config);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.about.Inspector.grid = new Lino.WindowAction({  }, function(){
  var p = { "is_main_window": true };
  p.params_panel = new Lino.about.Inspector.ParamsPanel({});
  return new Lino.about.Inspector.GridPanel(p);
});

// js_render_GridPanel_class about.SourceFiles
Lino.about.SourceFiles.GridPanel = Ext.extend(Lino.GridPanel,{
  ls_url : "/about/SourceFiles",
  ls_bbar_actions : [ { "auto_save": true, "iconCls": "x-tbar-html", "itemId": "show_as_html", "menu_item_text": "HTML", "overflowText": "HTML", "panel_btn_handler": Lino.list_action_handler('/about/SourceFiles','show_as_html','GET',Lino.get_current_grid_config), "tooltip": "Show this table in Bootstrap3 interface" } ],
  cell_edit : true,
  title : "Source files",
  page_length : 20,
  gc_name : 0,
  stripeRows : true,
  disabled_actions_index : 3,
  ls_store_fields : [ { "name": "module_name" }, { "name": "code_lines", "type": "int" }, { "name": "doc_lines", "type": "int" }, { "name": "disabled_actions" } ],
  ls_grid_configs : [  ],
  viewConfig : { "emptyText": "Pas de donn\u00e9es \u00e0 afficher.", "forceFit": true },
  disable_editing : true,
  initComponent : function() {
    var ww = this.containing_window;
    var module_name236 = new Ext.form.TextField({ "disabled": true, "maxLength": null });
    var code_lines237 = new Ext.form.NumberField({ "disabled": true });
    var doc_lines238 = new Ext.form.NumberField({ "disabled": true });
    this.before_row_edit = function(record) {
    };
    this.ls_columns = [ { "colIndex": 0, "dataIndex": "module_name", "editable": false, "header": "module name", "sortable": false, "tooltip": "(about.SourceFiles.module_name) ", "width": Lino.chars2width(5) }, new Lino.NullNumberColumn({ "colIndex": 1, "dataIndex": "code_lines", "editable": false, "format": "0", "header": "Code", "sortable": false, "tooltip": "(about.SourceFiles.code_lines) ", "width": Lino.chars2width(6) }), new Lino.NullNumberColumn({ "colIndex": 2, "dataIndex": "doc_lines", "editable": false, "format": "0", "header": "doc", "sortable": false, "tooltip": "(about.SourceFiles.doc_lines) ", "width": Lino.chars2width(6) }) ];
    Lino.about.SourceFiles.GridPanel.superclass.initComponent.call(this);
  }
});

Lino.about.SourceFiles.show_as_html = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/about/SourceFiles", "GET", pk, "show_as_html", params, Lino.get_current_grid_config);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.about.SourceFiles.grid = new Lino.WindowAction({  }, function(){
  var p = { "is_main_window": true };
  return new Lino.about.SourceFiles.GridPanel(p);
});

Lino.about.About.showPanel = Ext.extend(Lino.about.About.DetailFormPanel,{
  empty_title: "\u00e0 propos",
  hide_navigator: true,
  save_action_name: "submit_detail",
  ls_bbar_actions: [  ],
  ls_url: "/about/About",
  initComponent : function() {
    this.ls_detail_handler = Lino.about.About.show;
    Lino.about.About.showPanel.superclass.initComponent.call(this);
  }
});

Lino.about.About.show = new Lino.WindowAction({ "draggable": true, "height": Lino.rows2height(20), "maximizable": true, "maximized": false, "modal": true, "width": Lino.chars2width(60) }, function(){
  var p = { "hide_top_toolbar": true, "is_main_window": true };
  return new Lino.about.About.showPanel(p);
});

Lino.about.About.showPanel = Ext.extend(Lino.about.About.DetailFormPanel,{
  empty_title: "\u00e0 propos",
  hide_navigator: true,
  save_action_name: "submit_detail",
  ls_bbar_actions: [  ],
  ls_url: "/about/About",
  initComponent : function() {
    this.ls_detail_handler = Lino.about.About.show;
    Lino.about.About.showPanel.superclass.initComponent.call(this);
  }
});

Lino.about.About.show = new Lino.WindowAction({ "draggable": true, "height": Lino.rows2height(20), "maximizable": true, "maximized": false, "modal": true, "width": Lino.chars2width(60) }, function(){
  var p = { "hide_top_toolbar": true, "is_main_window": true };
  return new Lino.about.About.showPanel(p);
});

// js_render_GridPanel_class system.PeriodEvents
Lino.system.PeriodEvents.GridPanel = Ext.extend(Lino.GridPanel,{
  viewConfig : { "emptyText": "Pas de donn\u00e9es \u00e0 afficher.", "forceFit": true },
  ls_url : "/system/PeriodEvents",
  ls_bbar_actions : [ { "auto_save": true, "iconCls": "x-tbar-html", "itemId": "show_as_html", "menu_item_text": "HTML", "overflowText": "HTML", "panel_btn_handler": Lino.list_action_handler('/system/PeriodEvents','show_as_html','GET',Lino.get_current_grid_config), "tooltip": "Show this table in Bootstrap3 interface" } ],
  cell_edit : true,
  title : "\u00c9v\u00e8nements observ\u00e9s",
  page_length : 20,
  stripeRows : true,
  disable_editing : true,
  disabled_actions_index : 5,
  ls_store_fields : [ { "name": "value" }, { "name": "name" }, { "name": "text" }, { "name": "remark" }, { "name": "None" }, { "name": "disabled_actions" } ],
  pk_index : 0,
  ls_grid_configs : [  ],
  ls_id_property : null,
  gc_name : 0,
  initComponent : function() {
    var ww = this.containing_window;
    var value240 = new Ext.form.TextField({ "disabled": true, "maxLength": 20 });
    var name241 = new Ext.form.TextField({ "disabled": true, "maxLength": 20 });
    var text242 = new Ext.form.TextField({ "disabled": true, "maxLength": 50 });
    var remark_disp243 = new Ext.form.DisplayField({ "always_enabled": true, "disabled": true, "hidden": true, "value": "<br/>" });
    this.before_row_edit = function(record) {
    };
    this.ls_columns = [ { "colIndex": 0, "dataIndex": "value", "editable": false, "header": "value", "sortable": false, "tooltip": "(system.PeriodEvents.value) ", "width": Lino.chars2width(22) }, { "colIndex": 1, "dataIndex": "name", "editable": false, "header": "name", "sortable": false, "tooltip": "(system.PeriodEvents.name) ", "width": Lino.chars2width(22) }, { "colIndex": 2, "dataIndex": "text", "editable": false, "header": "text", "sortable": false, "tooltip": "(system.PeriodEvents.text) ", "width": Lino.chars2width(22) }, { "colIndex": 3, "dataIndex": "remark", "editable": false, "header": "Remarque", "hidden": true, "sortable": false, "tooltip": "(system.PeriodEvents.remark) ", "width": Lino.chars2width(31) } ];
    Lino.system.PeriodEvents.GridPanel.superclass.initComponent.call(this);
  }
});

Lino.system.PeriodEvents.show_as_html = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/system/PeriodEvents", "GET", pk, "show_as_html", params, Lino.get_current_grid_config);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.system.PeriodEvents.grid = new Lino.WindowAction({  }, function(){
  var p = { "is_main_window": true };
  return new Lino.system.PeriodEvents.GridPanel(p);
});

// js_render_GridPanel_class concepts.LinkTypes
Lino.concepts.LinkTypes.GridPanel = Ext.extend(Lino.GridPanel,{
  viewConfig : { "emptyText": "Pas de donn\u00e9es \u00e0 afficher.", "forceFit": true },
  ls_url : "/concepts/LinkTypes",
  ls_bbar_actions : [ { "auto_save": true, "iconCls": "x-tbar-html", "itemId": "show_as_html", "menu_item_text": "HTML", "overflowText": "HTML", "panel_btn_handler": Lino.list_action_handler('/concepts/LinkTypes','show_as_html','GET',Lino.get_current_grid_config), "tooltip": "Show this table in Bootstrap3 interface" } ],
  cell_edit : true,
  title : "Link Types",
  page_length : 20,
  stripeRows : true,
  disable_editing : true,
  disabled_actions_index : 5,
  ls_store_fields : [ { "name": "value" }, { "name": "name" }, { "name": "text" }, { "name": "remark" }, { "name": "None" }, { "name": "disabled_actions" } ],
  pk_index : 0,
  ls_grid_configs : [  ],
  ls_id_property : null,
  gc_name : 0,
  initComponent : function() {
    var ww = this.containing_window;
    var value245 = new Ext.form.TextField({ "disabled": true, "maxLength": 20 });
    var name246 = new Ext.form.TextField({ "disabled": true, "maxLength": 20 });
    var text247 = new Ext.form.TextField({ "disabled": true, "maxLength": 50 });
    var remark_disp248 = new Ext.form.DisplayField({ "always_enabled": true, "disabled": true, "hidden": true, "value": "<br/>" });
    this.before_row_edit = function(record) {
    };
    this.ls_columns = [ { "colIndex": 0, "dataIndex": "value", "editable": false, "header": "value", "sortable": false, "tooltip": "(concepts.LinkTypes.value) ", "width": Lino.chars2width(22) }, { "colIndex": 1, "dataIndex": "name", "editable": false, "header": "name", "sortable": false, "tooltip": "(concepts.LinkTypes.name) ", "width": Lino.chars2width(22) }, { "colIndex": 2, "dataIndex": "text", "editable": false, "header": "text", "sortable": false, "tooltip": "(concepts.LinkTypes.text) ", "width": Lino.chars2width(22) }, { "colIndex": 3, "dataIndex": "remark", "editable": false, "header": "Remarque", "hidden": true, "sortable": false, "tooltip": "(concepts.LinkTypes.remark) ", "width": Lino.chars2width(31) } ];
    Lino.concepts.LinkTypes.GridPanel.superclass.initComponent.call(this);
  }
});

Lino.concepts.LinkTypes.show_as_html = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/concepts/LinkTypes", "GET", pk, "show_as_html", params, Lino.get_current_grid_config);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.concepts.LinkTypes.grid = new Lino.WindowAction({  }, function(){
  var p = { "is_main_window": true };
  return new Lino.concepts.LinkTypes.GridPanel(p);
});

// js_render_GridPanel_class system.YesNo
Lino.system.YesNo.GridPanel = Ext.extend(Lino.GridPanel,{
  viewConfig : { "emptyText": "Pas de donn\u00e9es \u00e0 afficher.", "forceFit": true },
  ls_url : "/system/YesNo",
  ls_bbar_actions : [ { "auto_save": true, "iconCls": "x-tbar-html", "itemId": "show_as_html", "menu_item_text": "HTML", "overflowText": "HTML", "panel_btn_handler": Lino.list_action_handler('/system/YesNo','show_as_html','GET',Lino.get_current_grid_config), "tooltip": "Show this table in Bootstrap3 interface" } ],
  cell_edit : true,
  title : "Oui ou non",
  page_length : 20,
  stripeRows : true,
  disable_editing : true,
  disabled_actions_index : 5,
  ls_store_fields : [ { "name": "value" }, { "name": "name" }, { "name": "text" }, { "name": "remark" }, { "name": "None" }, { "name": "disabled_actions" } ],
  pk_index : 0,
  ls_grid_configs : [  ],
  ls_id_property : null,
  gc_name : 0,
  initComponent : function() {
    var ww = this.containing_window;
    var value250 = new Ext.form.TextField({ "disabled": true, "maxLength": 20 });
    var name251 = new Ext.form.TextField({ "disabled": true, "maxLength": 20 });
    var text252 = new Ext.form.TextField({ "disabled": true, "maxLength": 50 });
    var remark_disp253 = new Ext.form.DisplayField({ "always_enabled": true, "disabled": true, "hidden": true, "value": "<br/>" });
    this.before_row_edit = function(record) {
    };
    this.ls_columns = [ { "colIndex": 0, "dataIndex": "value", "editable": false, "header": "value", "sortable": false, "tooltip": "(system.YesNo.value) ", "width": Lino.chars2width(22) }, { "colIndex": 1, "dataIndex": "name", "editable": false, "header": "name", "sortable": false, "tooltip": "(system.YesNo.name) ", "width": Lino.chars2width(22) }, { "colIndex": 2, "dataIndex": "text", "editable": false, "header": "text", "sortable": false, "tooltip": "(system.YesNo.text) ", "width": Lino.chars2width(22) }, { "colIndex": 3, "dataIndex": "remark", "editable": false, "header": "Remarque", "hidden": true, "sortable": false, "tooltip": "(system.YesNo.remark) ", "width": Lino.chars2width(31) } ];
    Lino.system.YesNo.GridPanel.superclass.initComponent.call(this);
  }
});

Lino.system.YesNo.show_as_html = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/system/YesNo", "GET", pk, "show_as_html", params, Lino.get_current_grid_config);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.system.YesNo.grid = new Lino.WindowAction({  }, function(){
  var p = { "is_main_window": true };
  return new Lino.system.YesNo.GridPanel(p);
});

// js_render_GridPanel_class system.Genders
Lino.system.Genders.GridPanel = Ext.extend(Lino.GridPanel,{
  viewConfig : { "emptyText": "Pas de donn\u00e9es \u00e0 afficher.", "forceFit": true },
  ls_url : "/system/Genders",
  ls_bbar_actions : [ { "auto_save": true, "iconCls": "x-tbar-html", "itemId": "show_as_html", "menu_item_text": "HTML", "overflowText": "HTML", "panel_btn_handler": Lino.list_action_handler('/system/Genders','show_as_html','GET',Lino.get_current_grid_config), "tooltip": "Show this table in Bootstrap3 interface" } ],
  cell_edit : true,
  title : "Genders",
  page_length : 20,
  stripeRows : true,
  disable_editing : true,
  disabled_actions_index : 5,
  ls_store_fields : [ { "name": "value" }, { "name": "name" }, { "name": "text" }, { "name": "remark" }, { "name": "None" }, { "name": "disabled_actions" } ],
  pk_index : 0,
  ls_grid_configs : [  ],
  ls_id_property : null,
  gc_name : 0,
  initComponent : function() {
    var ww = this.containing_window;
    var value255 = new Ext.form.TextField({ "disabled": true, "maxLength": 20 });
    var name256 = new Ext.form.TextField({ "disabled": true, "maxLength": 20 });
    var text257 = new Ext.form.TextField({ "disabled": true, "maxLength": 50 });
    var remark_disp258 = new Ext.form.DisplayField({ "always_enabled": true, "disabled": true, "hidden": true, "value": "<br/>" });
    this.before_row_edit = function(record) {
    };
    this.ls_columns = [ { "colIndex": 0, "dataIndex": "value", "editable": false, "header": "value", "sortable": false, "tooltip": "(system.Genders.value) ", "width": Lino.chars2width(22) }, { "colIndex": 1, "dataIndex": "name", "editable": false, "header": "name", "sortable": false, "tooltip": "(system.Genders.name) ", "width": Lino.chars2width(22) }, { "colIndex": 2, "dataIndex": "text", "editable": false, "header": "text", "sortable": false, "tooltip": "(system.Genders.text) ", "width": Lino.chars2width(22) }, { "colIndex": 3, "dataIndex": "remark", "editable": false, "header": "Remarque", "hidden": true, "sortable": false, "tooltip": "(system.Genders.remark) ", "width": Lino.chars2width(31) } ];
    Lino.system.Genders.GridPanel.superclass.initComponent.call(this);
  }
});

Lino.system.Genders.show_as_html = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/system/Genders", "GET", pk, "show_as_html", params, Lino.get_current_grid_config);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.system.Genders.grid = new Lino.WindowAction({  }, function(){
  var p = { "is_main_window": true };
  return new Lino.system.Genders.GridPanel(p);
});

// js_render_GridPanel_class countries.PlaceTypes
Lino.countries.PlaceTypes.GridPanel = Ext.extend(Lino.GridPanel,{
  viewConfig : { "emptyText": "Pas de donn\u00e9es \u00e0 afficher.", "forceFit": true },
  ls_url : "/countries/PlaceTypes",
  ls_bbar_actions : [ { "auto_save": true, "iconCls": "x-tbar-html", "itemId": "show_as_html", "menu_item_text": "HTML", "overflowText": "HTML", "panel_btn_handler": Lino.list_action_handler('/countries/PlaceTypes','show_as_html','GET',Lino.get_current_grid_config), "tooltip": "Show this table in Bootstrap3 interface" } ],
  cell_edit : true,
  title : "PlaceTypes",
  page_length : 20,
  stripeRows : true,
  disable_editing : true,
  disabled_actions_index : 5,
  ls_store_fields : [ { "name": "value" }, { "name": "name" }, { "name": "text" }, { "name": "remark" }, { "name": "None" }, { "name": "disabled_actions" } ],
  pk_index : 0,
  ls_grid_configs : [  ],
  ls_id_property : null,
  gc_name : 0,
  initComponent : function() {
    var ww = this.containing_window;
    var value260 = new Ext.form.TextField({ "disabled": true, "maxLength": 20 });
    var name261 = new Ext.form.TextField({ "disabled": true, "maxLength": 20 });
    var text262 = new Ext.form.TextField({ "disabled": true, "maxLength": 50 });
    var remark_disp263 = new Ext.form.DisplayField({ "always_enabled": true, "disabled": true, "hidden": true, "value": "<br/>" });
    this.before_row_edit = function(record) {
    };
    this.ls_columns = [ { "colIndex": 0, "dataIndex": "value", "editable": false, "header": "value", "sortable": false, "tooltip": "(countries.PlaceTypes.value) ", "width": Lino.chars2width(22) }, { "colIndex": 1, "dataIndex": "name", "editable": false, "header": "name", "sortable": false, "tooltip": "(countries.PlaceTypes.name) ", "width": Lino.chars2width(22) }, { "colIndex": 2, "dataIndex": "text", "editable": false, "header": "text", "sortable": false, "tooltip": "(countries.PlaceTypes.text) ", "width": Lino.chars2width(22) }, { "colIndex": 3, "dataIndex": "remark", "editable": false, "header": "Remarque", "hidden": true, "sortable": false, "tooltip": "(countries.PlaceTypes.remark) ", "width": Lino.chars2width(31) } ];
    Lino.countries.PlaceTypes.GridPanel.superclass.initComponent.call(this);
  }
});

Lino.countries.PlaceTypes.show_as_html = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/countries/PlaceTypes", "GET", pk, "show_as_html", params, Lino.get_current_grid_config);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.countries.PlaceTypes.grid = new Lino.WindowAction({  }, function(){
  var p = { "is_main_window": true };
  return new Lino.countries.PlaceTypes.GridPanel(p);
});

// js_render_GridPanel_class printing.BuildMethods
Lino.printing.BuildMethods.GridPanel = Ext.extend(Lino.GridPanel,{
  viewConfig : { "emptyText": "Pas de donn\u00e9es \u00e0 afficher.", "forceFit": true },
  ls_url : "/printing/BuildMethods",
  ls_bbar_actions : [ { "auto_save": true, "iconCls": "x-tbar-html", "itemId": "show_as_html", "menu_item_text": "HTML", "overflowText": "HTML", "panel_btn_handler": Lino.list_action_handler('/printing/BuildMethods','show_as_html','GET',Lino.get_current_grid_config), "tooltip": "Show this table in Bootstrap3 interface" } ],
  cell_edit : true,
  title : "BuildMethods",
  page_length : 20,
  stripeRows : true,
  disable_editing : true,
  disabled_actions_index : 5,
  ls_store_fields : [ { "name": "value" }, { "name": "name" }, { "name": "text" }, { "name": "remark" }, { "name": "None" }, { "name": "disabled_actions" } ],
  pk_index : 0,
  ls_grid_configs : [  ],
  ls_id_property : null,
  gc_name : 0,
  initComponent : function() {
    var ww = this.containing_window;
    var value265 = new Ext.form.TextField({ "disabled": true, "maxLength": 20 });
    var name266 = new Ext.form.TextField({ "disabled": true, "maxLength": 20 });
    var text267 = new Ext.form.TextField({ "disabled": true, "maxLength": 50 });
    var remark_disp268 = new Ext.form.DisplayField({ "always_enabled": true, "disabled": true, "hidden": true, "value": "<br/>" });
    this.before_row_edit = function(record) {
    };
    this.ls_columns = [ { "colIndex": 0, "dataIndex": "value", "editable": false, "header": "value", "sortable": false, "tooltip": "(printing.BuildMethods.value) ", "width": Lino.chars2width(22) }, { "colIndex": 1, "dataIndex": "name", "editable": false, "header": "name", "sortable": false, "tooltip": "(printing.BuildMethods.name) ", "width": Lino.chars2width(22) }, { "colIndex": 2, "dataIndex": "text", "editable": false, "header": "text", "sortable": false, "tooltip": "(printing.BuildMethods.text) ", "width": Lino.chars2width(22) }, { "colIndex": 3, "dataIndex": "remark", "editable": false, "header": "Remarque", "hidden": true, "sortable": false, "tooltip": "(printing.BuildMethods.remark) ", "width": Lino.chars2width(31) } ];
    Lino.printing.BuildMethods.GridPanel.superclass.initComponent.call(this);
  }
});

Lino.printing.BuildMethods.show_as_html = function(rp, pk, params) { 
  var h = function() { 
    Lino.run_row_action(rp, "/printing/BuildMethods", "GET", pk, "show_as_html", params, Lino.get_current_grid_config);
  };
  var panel = Ext.getCmp(rp);
  if(panel) panel.do_when_clean(true, h); else h();
};
Lino.printing.BuildMethods.grid = new Lino.WindowAction({  }, function(){
  var p = { "is_main_window": true };
  return new Lino.printing.BuildMethods.GridPanel(p);
});
