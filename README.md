Create task from portal
=======================

Known issues / Roadmap
----------------------
* Rewrite css file so it does not includes the important.
* Include name within option project.user_id.id. This is now impossible because of a security issue. Probably because the name field is not whitelisted for use in forms.
* Find a better way to filter on stage_id new in the form.
* Find a better way to inherit controllers/main.py: inherit only the part that is changed; not the entire function.
* Make use of Odoo's widget function in JavaScript instead of jQuery. 