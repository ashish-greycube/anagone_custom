from __future__ import unicode_literals
import frappe

no_cache = 1


def get_context(context):
    context.customers = frappe.db.sql("select * from tabCustomer")
    context.activeUser = frappe.session.user
