# Pre-mortem ⚰️

## What it is

Before starting, declare that the thing has already failed - not that it *might* fail -
and ask everyone why. The grammatical shift from "what could go wrong" to "what *did* go
wrong" is the entire technique.

## Origin & evidence

Gary Klein's method, built on a finding by Mitchell, Russo and Pennington that
**prospective hindsight** - imagining an event has already occurred - *"increases the
ability to correctly identify reasons for future outcomes by 30%."*

> Klein, G. (2007). *Performing a Project Premortem.* Harvard Business Review
> 85(9):18–19.
> http://homepages.se.edu/cvonbergen/files/2013/01/Performing-a-Project-Premortem.pdf

Klein's stated target is not analysis but *permission*. Projects fail partly because
"too many people are reluctant to speak up about their reservations during the
all-important planning phase". A premortem makes dissent the assigned task, so raising a
concern stops being an act of disloyalty. He notes it also reduces the
"damn-the-torpedoes attitude often assumed by people who are overinvested in a project".

## How to run it

Klein's procedure, which is specific and worth following exactly:

1. Brief the plan first.
2. The leader states that it has **failed spectacularly**. Past tense, not hypothetical.
3. Everyone writes down every reason they can think of, **independently and silently** -
   especially the ones they would normally not raise for fear of being impolitic.
4. Each person reads out **one** reason in turn, starting with the person running the
   change, until the lists are exhausted.
5. Revise the plan.

The independent writing before any speaking is what stops the first confident voice from
anchoring the room.

## Worked example

Before a database migration the lead says: "It's Monday morning. The migration failed, we
were down four hours, and we're in an incident review. Why?" The list includes the
expected - schema lock, replica lag - and one nobody would have volunteered: the only
person who has run this before is on a flight during the window. That was known to three
people in the room and mentioned by none until failure was assumed.

## Limits

It surfaces failure modes people already suspect, so it will not find genuine unknowns, and
it does not replace testing the rollback. Its value also depends on the plan actually
changing as a result; premortems that never change anything stop being taken seriously.
