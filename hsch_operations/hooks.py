# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "hsch_operations"
app_title = "HSCH Operations"
app_publisher = "HSCH"
app_description = "HSCH Operations"
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "contact@gdsplusltd.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/hsch_operations/css/hsch_operations.css"
# app_include_js = "/assets/hsch_operations/js/hsch_operations.js"

# include js, css files in header of web template
# web_include_css = "/assets/hsch_operations/css/hsch_operations.css"
# web_include_js = "/assets/hsch_operations/js/hsch_operations.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "hsch_operations.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "hsch_operations.install.before_install"
# after_install = "hsch_operations.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "hsch_operations.notifications.get_notification_config"

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
# 	"Goal Achievement": {
# 		"validate": "hsch_operations.hsch_operations.goal_achievement.fetch_achievement_template"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"hsch_operations.tasks.all"
# 	],
# 	"daily": [
# 		"hsch_operations.tasks.daily"
# 	],
# 	"hourly": [
# 		"hsch_operations.tasks.hourly"
# 	],
# 	"weekly": [
# 		"hsch_operations.tasks.weekly"
# 	]
# 	"monthly": [
# 		"hsch_operations.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "hsch_operations.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "hsch_operations.event.get_events"
# }

