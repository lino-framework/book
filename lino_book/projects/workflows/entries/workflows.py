## Copyright 2013-2018 Rumma & Ko Ltd
## This file is part of the Lino project.

from django.utils.translation import ugettext_lazy as _

from .choicelists import EntryStates
from .actions import WakeupEntry, StartEntry, FinishEntry


EntryStates.new.add_transition(
    _("Reopen"), required_states='done cancelled')
EntryStates.new.add_transition(WakeupEntry)
EntryStates.started.add_transition(StartEntry)
EntryStates.sleeping.add_transition(required_states="new")
EntryStates.done.add_transition(FinishEntry)
EntryStates.cancelled.add_transition(
    required_states='sleeping started',
    help_text=_("""This is a rather verbose help text for the action 
    which triggers transition from 'sleeping' or 'started' 
    to 'cancelled'."""),
    icon_name='cancel')

    
