 odoo.define('create_task_from_portal.website_form', function (require) {
    "use strict";

//    var ajax = require('web.ajax');
//    var core = require('web.core');
//    var Dialog = require('web.Dialog');
//    var Widget = require('web.Widget');
//
//    var qweb = core.qweb;
//    var _t = core._t;
//
//    var projects = [];
//
    require('web.dom_ready');
//
//    var MyWidget = Widget.extend({
//        template: "create_task_from_portal.portal_create_task",
//        events: {
//            'click button': '_onClick',
//        },
//        xmlDependencies: ['/create_task_from_portal/static/src/xml/website_views.xml'],
//        init: function(parent) {
//            this._super(parent);
//            // stuff that you want to init before the rendering
//        },
//        start: function() {
//            // stuff you want to make after the rendering, `this.$el` holds a correct value
//            this.$("#button_create_new_task").click(
//                console.log("it works!")
//            );
//            projects = ["test", "test2"];
//            console.log("projects started", projects);
//        },
//        _onClick: function() {
//            console.log("onClick works");
//            new Dialog(this, {
//                title: _t('New Task'),
//                $content: qweb.render('create_task_from_portal.portal_create_task_form'),
//                buttons: [{
//                    text: _t('Submit Task'),
//                    close: true,
//                    click: function () {
//                        self.onFormSubmit();
//                    },
//                }],
//            }).open();
//        },
//        onFormSubmit: function() {
//            console.log("onFormSubmit works");
//        },
//    });
//
//    var my_widget = new MyWidget(this);
//    my_widget.appendTo($(".pull-right"));

    $('#custom_form_button').click(function() {
        var checkExist = setInterval(function() {
            if ($('span#o_website_form_result').is('.text-success')) {
                clearInterval(checkExist);
                $('.o_create_task').modal('hide');
                window.location.reload();
            }
        }, 100);
    });

});