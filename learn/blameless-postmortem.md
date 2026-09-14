# Blameless Postmortem 🔍

## What it is

A review whose purpose is to learn how the system produced the outcome, conducted on the
premise that everyone involved acted reasonably given what they knew at the time.

"Blameless" does not mean nobody made a mistake. It means the mistake is treated as
information about the system rather than about the person, because the alternative - people
concealing what actually happened - costs more than any individual error.

## Origin & evidence

The practice comes from software operations, notably Etsy under John Allspaw, and is
codified in Google's SRE material as standard practice.

> Allspaw, J. (2012). *Blameless PostMortems and a Just Culture.* Code as Craft.
> https://www.etsy.com/codeascraft/blameless-postmortems/
>
> Beyer, B. et al. (eds) (2016). *Site Reliability Engineering*, chapter 15: Postmortem
> Culture. O'Reilly. https://sre.google/sre-book/postmortem-culture/

Its intellectual basis is Reason's system approach - see [Swiss Cheese and Latent
Conditions](./swiss-cheese-latent-conditions.md) - and the accompanying idea of a **just
culture**, which is not the absence of accountability but a consistent, known line between
error and recklessness.

The premise that everyone acted reasonably is not generosity, it is a correction for a
known distortion. Cook states it as hindsight bias: knowing the outcome makes the events
leading to it look more obvious than they could have been at the time, so the practitioner
appears to have ignored what was in fact invisible. He calls it the primary obstacle to
accident investigation.

> Cook, R. I. (2000). *How Complex Systems Fail*, proposition 8. Cognitive Technologies
> Laboratory, University of Chicago. https://how.complexsystems.fail/

The STELLA report adds an observation worth carrying: organisations often say *blameless*
when what they actually offer is **sanctionless** - no punishment, but blame still
assigned. People can tell the difference, and it determines what they tell you.

## How to run it

- **Start from a validated timeline.** Time, what the system showed, what the human did.
  Speculation comes after the facts, clearly labelled.
- **Ban counterfactuals.** "They should have checked" describes a world that did not
  happen and explains nothing. Ask what made the action reasonable at the time.
- **Interview for rationale, not just action.** Why did that look right then?
- **Name the layers that failed**, not the person who was last to touch it.
- **Actions are SMART** - **S**pecific · **M**easurable · **A**chievable · **R**elevant ·
  **T**ime-bound - each with one named owner and a date. "Be more careful" is rejected.
- **Prefer tooling and procedure fixes** over training and reminders. Memory is not a
  control.
- **Make it readable.** If nobody outside the incident ever reads it, it was documentation,
  not learning.

> Doran, G. T. (1981). *There's a S.M.A.R.T. way to write management's goals and
> objectives.* Management Review 70(11):35–36.

## Worked example

An engineer deletes a production index during cleanup. The blameful version: insufficient
care, action is a reminder to be careful. The blameless version asks why the cleanup script
had production credentials at all, why the index was indistinguishable from the temporary
ones by name, and why no confirmation was required - and produces three fixes that survive
the engineer leaving.

## Limits

The practice depends on being real: if people are quietly moved off teams after reviews,
the stated policy stops mattering. It also does not by itself explain how the system
normally succeeds; pair it with the Work-as-Done prompts in [Safety-II and
Work-as-Done](./safety-ii-wad-wai.md).
