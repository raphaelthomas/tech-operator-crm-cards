# Two-Person Rule 👥

## What it is

For irreversible or high-consequence actions, two authorised people must be present and
must both concur before it proceeds. One person alone cannot do it, by design.

## Origin & evidence

Nuclear weapons custody. The US Department of Defense extended the concept across all
nuclear weapons operations by mid-1962; US Air Force policy defines the two-person concept
as preventing accidental or malicious launch by a single individual. Minuteman crews
require both operators to independently validate a launch order against a sealed
authenticator before acting.

> US Air Force Instruction 91-104, *Nuclear Surety Tamper Control and Detection
> Programs.* https://www.doctrine.af.mil/

The related **no-lone zone** is the physical form: an area a single unaccompanied person
may not enter, where the two people must maintain visual contact with each other and with
the critical component.

Finance and software know the same idea as the **four-eyes principle** - dual
authorisation for payments, code review before merge, two approvals on a production change.

The design intent is worth being precise about: it is not that two people are better at
noticing errors than one. It is that the second person is **not permitted to be a
formality**. They are accountable for concurring, which is why sealed authenticators and
independent validation exist rather than a second signature.

## How to use it

- **Define the list in advance**: deletes, migrations, secret rotation, DNS, IAM, anything
  touching money or customer data. Deciding case by case means deciding under pressure.
- **The second person forms their own picture.** If they are reading your terminal over
  your shoulder, you have one picture and two people.
- **They must be able to say no** without needing to win the argument - see
  [PACE](./pace-and-two-challenge.md).
- **Pair it with [pointing and calling](./pointing-and-calling.md).** The operator reads
  the command aloud; the reviewer confirms against their own understanding of the intent.
- **Solo, it does not exist.** There is no self-administered two-person rule. Either defer
  the action or wake someone.

## Worked example

A DNS change is reviewed by a colleague who reads the diff, sees a plausible record, and
approves. The record is correct; the *zone* is the production apex rather than the staging
subdomain. Reviewing the diff reproduced the author's framing. Asking "which zone does
this land in, and what breaks if it's wrong?" would not have.

## Limits

Approvals given without real review provide little protection while still creating
confidence. The rule also doubles the cost of every guarded action, so a long list invites
workarounds. Guard the genuinely irreversible, and make clear that the reviewer is being
asked to concur rather than to witness.
