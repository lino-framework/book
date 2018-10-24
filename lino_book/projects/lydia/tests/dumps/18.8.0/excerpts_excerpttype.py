# -*- coding: UTF-8 -*-
logger.info("Loading 10 objects to table excerpts_excerpttype...")
# fields: id, name, build_method, template, attach_to_email, email_template, certifying, remark, body_template, content_type, primary, backward_compat, print_recipient, print_directly, shortcut
loader.save(create_excerpts_excerpttype(1,['Terms & conditions', 'Nutzungsbestimmungen', 'Terms & conditions'],u'appypdf',u'TermsConditions.odt',False,u'',False,u'',u'',contacts_Person,False,False,True,True,None))
loader.save(create_excerpts_excerpttype(2,['Payment reminder', 'Zahlungserinnerung', 'Rappel de paiement'],u'weasy2pdf',u'payment_reminder.weasy.html',False,u'',False,u'',u'',contacts_Partner,False,False,True,True,None))
loader.save(create_excerpts_excerpttype(3,['VAT declaration', 'MwSt.-Erkl\xe4rung', 'VAT declaration'],u'weasy2pdf',u'default.weasy.html',False,u'',True,u'',u'',bevats_Declaration,False,False,True,True,None))
loader.save(create_excerpts_excerpttype(4,['Special Belgian VAT declaration', 'Special Belgian VAT declaration', 'Special Belgian VAT declaration'],None,u'',False,u'',True,u'',u'',bevats_Declaration,True,False,True,True,None))
loader.save(create_excerpts_excerpttype(5,['Enrolment', 'Einschreibung', 'Inscription'],None,u'',False,u'',True,u'',u'',courses_Enrolment,True,False,True,True,None))
loader.save(create_excerpts_excerpttype(6,['Bank Statement', 'Kontoauszug', 'Bank Statement'],None,u'',False,u'',True,u'',u'',finan_BankStatement,True,False,True,True,None))
loader.save(create_excerpts_excerpttype(7,['Journal Entry', 'Diverse Buchung', 'Journal Entry'],None,u'',False,u'',True,u'',u'',finan_JournalEntry,True,False,True,True,None))
loader.save(create_excerpts_excerpttype(8,['Payment Order', 'Zahlungsauftrag', 'Payment Order'],None,u'',False,u'',True,u'',u'',finan_PaymentOrder,True,False,True,True,None))
loader.save(create_excerpts_excerpttype(9,['Product invoice', 'Produktrechnung', 'Product invoice'],None,u'',False,u'',True,u'',u'',sales_VatProductInvoice,True,False,True,True,None))
loader.save(create_excerpts_excerpttype(10,['Accounting Report', 'Buchhaltungsbericht', 'Accounting Report'],u'weasy2pdf',u'',False,u'',True,u'',u'',sheets_Report,True,False,True,True,None))

loader.flush_deferred_objects()
