Linked objects
==============

"Lino" is also an acronym of the words **Linked objects** (as we said
in :doc:`/about/name`). This can help us to reflect about some values
behind Lino.

Every software application has a "model" of its "world", i.e. of the
things it is designed to manage.  We call this a **database
schema**. Such a schema mainly consists of "objects" and the
"relations" or "links" between them. The idea of using *linked
objects* for this modelization has been first formulated by
Edgar F. Codd in 1969 in his `relational database model
<https://en.wikipedia.org/wiki/Relational_model>`_.

But even 50 years later this idea is still some kind of expert
knowledge, known to database engineers but not to normal people.

Since the early 1990s I have often observed that application
developers seem to hide from the end-users the fact that their
application is basically "nothing but a collection of linked objects".
As if they were ashamed to admit that what they are doing is *that*
easy.

**Yes, Lino applications are that easy.** They feature a transparent
view of their database schema, leading to end-users being intuitively
aware of the structure behind what they are doing.  One Lino
application developer who understood this, wrote: "The development is
so terribly easy, that one customer looked at the code and started to
code Layouts and modify models by himself and I almost felt no
developer is needed anymore :-)"

**No, there is no reason to be ashamed.** The world will always need
professional developers because the gory details require some
experience, and because it is an art to make the right choices on what
to take into account and what to ignore.
  
Lino encourages **communicatio between end-users and developers**.
There are lots of developers who are very competent but unable to
communicate with end-users.  This is where specialization becomes
absurd, because a software application makes no sense without its
users.

When end-users are intuitively aware of the structure behind what they
are doing, this leads to better communication between developers and
end-users because **they speak the same language**.  Of course there
are certain differences in vocabulary, but they stop to completely
miss the point of what the other is talking about.

Lino applications give their users a **feeling of being able** to do
it themselves.  This motivates them to think about how they actually
*would* do it themselves.  The developer then just implements what
they ask, no more need to translate their language or to analyze their
"true needs", because the users understand what is possible and
correctly analyze what they really need.


