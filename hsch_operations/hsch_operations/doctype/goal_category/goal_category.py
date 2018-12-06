# -*- coding: utf-8 -*-
# Copyright (c) 2018, HSCH and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _


from frappe.utils.nestedset import NestedSet
class GoalCategory(NestedSet):
	nsm_parent_field = 'parent_goal_category';

	def on_update(self):
		self.validate_name_with_goal()
		super(GoalCategory, self).on_update()
		self.validate_one_root()

	def validate_name_with_goal(self):
		if frappe.db.exists("Goal", self.name):
			frappe.msgprint(_("A goal with the same name already exists"), raise_exception=1)

def get_parent_goal_categories(goal_category):
	lft, rgt = frappe.db.get_value("Goal Category", goal_category, ['lft', 'rgt'])

	return frappe.db.sql("""select name from `tabGoal Category`
		where lft <= %s and rgt >= %s
		order by lft asc""", (lft, rgt), as_dict=True)

def on_doctype_update():
	frappe.db.add_index("Goal Category", ["lft", "rgt"])


