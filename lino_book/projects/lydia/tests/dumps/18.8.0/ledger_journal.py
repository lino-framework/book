# -*- coding: UTF-8 -*-
logger.info("Loading 8 objects to table ledger_journal...")
# fields: id, ref, seqno, name, build_method, template, trade_type, voucher_type, journal_group, auto_check_clearings, auto_fill_suggestions, force_sequence, account, partner, printed_name, dc, yearly_numbering, must_declare, sepa_account
loader.save(create_ledger_journal(1,u'SLS',1,['Sales invoices', 'Verkaufsrechnungen', 'Factures vente'],None,u'','S','sales.InvoicesByJournal','10',True,True,False,None,None,['Invoice', '', ''],True,True,True,None))
loader.save(create_ledger_journal(2,u'SLC',2,['Sales credit notes', 'Gutschriften Verkauf', 'Sales credit notes'],None,u'','S','sales.InvoicesByJournal','10',True,True,False,None,None,['Credit note', '', ''],False,True,True,None))
loader.save(create_ledger_journal(3,u'PRC',3,['Purchase invoices', 'Einkaufsrechnungen', 'Factures achat'],None,u'','P','ana.InvoicesByJournal','20',True,True,False,None,None,['Credit note', '', ''],False,True,True,None))
loader.save(create_ledger_journal(4,u'PMO',4,['Bestbank Payment Orders', 'Bestbank Payment Orders', 'Bestbank Payment Orders'],None,u'','B','finan.PaymentOrdersByJournal','40',True,True,False,3,100,['', '', ''],False,True,True,30))
loader.save(create_ledger_journal(5,u'CSH',5,['Cash', 'Kasse', 'Caisse'],None,u'',None,'finan.BankStatementsByJournal','40',True,True,False,13,None,['', '', ''],True,True,True,None))
loader.save(create_ledger_journal(6,u'BNK',6,['Bestbank', 'Bestbank', 'Bestbank'],None,u'',None,'finan.BankStatementsByJournal','40',True,True,False,12,None,['', '', ''],True,True,True,None))
loader.save(create_ledger_journal(7,u'MSC',7,['Miscellaneous Journal Entries', 'Diverse Buchungen', 'Op\xe9rations diverses'],None,u'',None,'finan.JournalEntriesByJournal','40',True,True,False,13,None,['', '', ''],True,True,True,None))
loader.save(create_ledger_journal(8,u'VAT',8,['VAT declarations', 'MwSt.-Erkl\xe4rungen', 'D\xe9clarations TVA'],None,u'','T','bevats.DeclarationsByJournal','50',True,True,False,10,None,['', '', ''],False,True,False,None))

loader.flush_deferred_objects()
