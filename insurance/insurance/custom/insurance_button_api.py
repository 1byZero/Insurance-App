import frappe

@frappe.whitelist()
def create_insurance_payment(sales_invoice):
    sales_invoice_doc = frappe.get_doc('Sales Invoice', sales_invoice)
    
    # Example: Fetch insurance policy details dynamically
    policy_doc = frappe.get_doc('Insurance Policy', sales_invoice_doc.policy_number)

    insurance_payment = frappe.get_doc({
        'doctype': 'Insurance Payment',
        'sales_invoice': sales_invoice_doc.name,
        'customer': sales_invoice_doc.customer,
        'amount': sales_invoice_doc.outstanding_amount,
        'posting_date': frappe.utils.nowdate(),
        'insurance_policy': policy_doc.policy_name,  # Example: dynamic value from related doc
        'policy_number': policy_doc.policy_number,   # Example: dynamic value from related doc
        'amount_insured': policy_doc.amount_insured, # Example: dynamic value from related doc
        'co_payment_amount': policy_doc.co_payment_amount, # Example: dynamic value from related doc
        'insurance_company_charges': policy_doc.insurance_company_charges # Example: dynamic value from related doc
    })
    
    insurance_payment.insert(ignore_permissions=True)
    insurance_payment.submit()

    return insurance_payment.name
