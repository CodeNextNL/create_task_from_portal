odoo.define('create_task_from_portal.website_form', function (require) {
    "use strict";

    require('web.dom_ready');

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