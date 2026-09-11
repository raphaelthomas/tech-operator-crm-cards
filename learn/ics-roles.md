# Incident Command Roles 👥

## What it is

In any incident large enough to need more than one person, name the roles out loud and
keep them separate:

| Role | Owns | Does not |
| :--- | :--- | :--- |
| **Commander** | The plan, the decisions, who does what | Touch the keyboard |
| **Comms** | Stakeholders, customers, status updates | Diagnose |
| **Operations** | Executing changes | Field questions from outside |

One person doing all three is the default failure mode of a small team, and it fails
predictably: the person diagnosing stops answering stakeholders, so stakeholders interrupt
the person diagnosing.

## Origin & evidence

The Incident Command System came out of **FIRESCOPE**, a federally funded response to the
1970 Southern California wildfires — 773 fires across 13 days, 576,508 acres, 722 homes
and 16 deaths — where the problem was not firefighting capability but the absence of any
agreed way for agencies to organise together. ICS introduced common terminology, a clear
chain of command, and a structure that scales up and down with the incident.

FEMA recognised it in 1987, and after the September 11 attacks it was folded into the
National Incident Management System, now the US standard across all hazards.

> Federal Emergency Management Agency. *National Incident Management System.*
> https://www.fema.gov/emergency-managers/nims

Two ICS principles matter more than the org chart. **Span of control** is deliberately
small — roughly three to seven reports, five as the target — because a commander tracking
more than that is no longer commanding. And the structure is **modular**: for a small
incident one person legitimately holds several roles, but they are still *named*, so
everyone knows which hat is being worn and what is not being covered.

## How to use it

- **Say the roles aloud** at the start, and in the channel. Unstated roles are not roles.
- **Protect the operator.** Questions go to comms, never directly to the person executing.
- **The commander decides and does not type.** The moment they start debugging, nobody is
  holding the plan.
- **Hand over explicitly** — see [SBAR(C)](./sbarc.md).
- **Solo? Still name them.** Knowing you are wearing all three hats tells you which one you
  are currently dropping.

## Worked example

Three engineers, no roles declared. All three are in the database logs; nobody has told
support, so support escalates to the VP, who joins the call and asks for a status from
whoever is most senior — who is mid-query and now context-switching. The outage is
technically unchanged and operationally much worse.

## Limits

ICS is designed for incidents with scale, and a three-role structure is overhead on a short
one. Use it when the incident outlives one person's attention, and let small things stay
small.
