from __future__ import unicode_literals
import frappe

no_cache = 1


def get_context(context):
    activeUser = frappe.session.user
    if activeUser == "Administrator":
        context.customers = frappe.db.sql("select * from tabSeguimiento")
    else:
	context.customers = null
