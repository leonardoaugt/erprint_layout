# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "erprint_layouts"
app_title = "Erprint Layouts"
app_publisher = "sleonardoaugusto"
app_description = "Print Layouts customized"
app_icon = "octicon octicon-file-directory"
app_color = "#5d65f7"
app_email = "sleonardoaugusto@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erprint_layouts/css/erprint_layouts.css"
# app_include_js = "/assets/erprint_layouts/js/erprint_layouts.js"

# include js, css files in header of web template
# web_include_css = "/assets/erprint_layouts/css/erprint_layouts.css"
# web_include_js = "/assets/erprint_layouts/js/erprint_layouts.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

fixtures = [
    {"dt": "Print Format",
        "filters": [[
            "doc_type", "in", ("Quotation")
        ]]
    },
    ]

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "erprint_layouts.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erprint_layouts.install.before_install"
# after_install = "erprint_layouts.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erprint_layouts.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"erprint_layouts.tasks.all"
# 	],
# 	"daily": [
# 		"erprint_layouts.tasks.daily"
# 	],
# 	"hourly": [
# 		"erprint_layouts.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erprint_layouts.tasks.weekly"
# 	]
# 	"monthly": [
# 		"erprint_layouts.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "erprint_layouts.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erprint_layouts.event.get_events"
# }

