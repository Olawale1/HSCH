# -*- coding: utf-8 -*-
# Copyright (c) 2018, HSCH and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

from frappe.utils import flt, getdate

from frappe import _
from frappe.model.mapper import get_mapped_doc
from frappe.model.document import Document
from erpnext.hr.utils import set_employee_name

class GoalAchievement(Document):
	def validate(self):
		if not self.status:
			self.status = "Draft"

		if not self.goals:
			frappe.throw(_("Goals cannot be empty"))

		set_employee_name(self)
		self.validate_dates()
		self.validate_existing_goal_achievement()

	def get_employee_name(self):
		self.employee_name = frappe.db.get_value("Employee", self.employee, "employee_name")
		return self.employee_name

	def validate_dates(self):
		if getdate(self.start_date) > getdate(self.end_date):
			frappe.throw(_("End Date can not be less than Start Date"))

	def validate_existing_goal_achievement(self):
		chk = frappe.db.sql("""select name from `tabGoal Achievement` where department=%s
			and (status='Submitted' or status='Completed')
			and ((start_date>=%s and start_date<=%s)
			or (end_date>=%s and end_date<=%s))""",
			(self.employee,self.start_date,self.end_date,self.start_date,self.end_date))
		if chk:
			frappe.throw(_("Goal Achievement {0} created for Department {1} in the given date range").format(chk[0][0], self.department))

	def on_submit(self):
		frappe.db.set(self, 'status', 'Submitted')

	def on_cancel(self):
		frappe.db.set(self, 'status', 'Cancelled')

@frappe.whitelist()
def fetch_achievement_template(source_name, target_doc=None):
	target_doc = get_mapped_doc("Goal Template", source_name, {
		"Goal Template": {
			"doctype": "Goal Achievement",
		},
		"Goal Template Item": {
			"doctype": "Goal Achievement Item",
		}
	}, target_doc)

	return target_doc

