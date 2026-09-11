# Surgical Time-Out 🛑

## What it is

An enforced pause immediately before an irreversible act, in which the whole team stops,
faces each other, and confirms out loud a short list of things everyone assumes are
already true.

Its power is not the list. It is that the pause is *mandatory and audible*, so the
assumptions become checkable by people other than the one holding the knife.

## Origin & evidence

Part of the WHO Surgical Safety Checklist, structured in three pauses: **sign in** before
anaesthesia, **time out** before incision, **sign out** before the patient leaves theatre.

The evidence is unusually strong for a piece of paper. In a study across eight hospitals in
eight countries, spanning rich and poor health systems, introducing the 19-item checklist
cut complications from **11.0% to 7.0%** and in-hospital death from **1.5% to 0.8%**.

> Haynes, A. B. et al. (2009). *A Surgical Safety Checklist to Reduce Morbidity and
> Mortality in a Global Population.* New England Journal of Medicine 360:491–499.
> https://doi.org/10.1056/NEJMsa0810119

Two design details do the work. The checklist is **spoken, not ticked** — the team hears
each other answer. And it includes an introduction round in which everyone states name and
role, which exists so that a junior person has already spoken once before they need to
speak up about something that matters.

## How to run it

Immediately before the irreversible step, everyone stops and confirms aloud:

- **Who** is running it, who is watching, who can call a stop.
- **What** exactly is changing, and on which system — read the target out.
- **Rollback**, and how long it takes.
- **The trigger** that means abort — see [Pre-Committed
  Triggers](./pre-committed-triggers.md).
- **Anything anyone is uneasy about.** Ask explicitly, by name, and wait.

Hold it when everybody is present and nobody is typing. A time-out read out while one
person keeps working is not a time-out.

## Worked example

Before dropping a table, the operator reads the statement aloud including the database
host. The reviewer notices the host is the read-replica's *primary*, not the staging box
everyone had been discussing for twenty minutes. Nothing was wrong with the plan; the
connection string was wrong, and it was only ever going to be caught by being said out
loud to someone else.

## Limits

Checklists decay into ritual. The observable warning sign is a time-out that nobody ever
fails — if no change has been stopped by one in a year, it has become a recitation.
Keep it short enough to mean something, and make stopping genuinely acceptable, or the
team will learn the answer is always yes.
