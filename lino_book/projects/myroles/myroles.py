from lino_xl.lib.xl.user_types import *

from lino.api import dd, rt
from lino_xl.lib.polls.roles import PollsUser

AllPolls = rt.models.polls.AllPolls
AllPolls.required_roles = dd.login_required(PollsUser)
