# Three-Way Communication 🔁

## What it is

A closed loop for any instruction that matters:

1. **Sender** states the message, clearly and specifically.
2. **Receiver** repeats it back — names and labels word-for-word, the rest in their own
   words.
3. **Sender** confirms it was heard correctly, or corrects it.

The third step is the one people skip, and it is the one that makes the loop closed. An
instruction that was only *sent* has not been communicated.

## Origin & evidence

Standard practice in commercial nuclear power operations, where it is one of a set of
human performance tools promoted by INPO and required when giving direction or exchanging
critical plant parameters. The same loop appears in naval reactor operations, in ICAO
radio phraseology as read-back/hear-back, and in healthcare as the TeamSTEPPS
**check-back**.

> Agency for Healthcare Research and Quality. *TeamSTEPPS: Check-Back.*
> https://www.ahrq.gov/teamstepps-program/index.html

The repeat-back deliberately mixes verbatim and paraphrase. Identifiers are echoed exactly
because a wrong one is catastrophic and easy to mishear; the rest is paraphrased because
that is what exposes whether the receiver actually understood, rather than merely heard.

## How to use it

- **Use full names.** "Restart `api-gateway-prod-3`", never "restart it".
- **Echo identifiers exactly.** Hostnames, ticket numbers, version tags.
- **Confirm out loud.** "Correct" — or "negative, it is prod-3, not prod-2."
- **Use it on the way up too.** Status reports back to a commander deserve the same loop.

## Worked example

> **IC:** "Sam, drain traffic from `eu-west-1b` only. Leave `1a` and `1c` up."
> **Sam:** "Draining `eu-west-1b` only, leaving `1a` and `1c` up."
> **IC:** "Correct. Go."

Twelve extra words. The failure it prevents — draining the wrong availability zone, or all
three — is the kind that turns a degradation into an outage.

## Limits

It costs time, and applying it to everything trains people to tune it out. Reserve it for
instructions that change state, name a target, or cannot be undone. It also only catches
*transmission* errors: a confidently wrong instruction, repeated back perfectly, is still
wrong. That failure needs [PACE and the Two-Challenge
Rule](./pace-and-two-challenge.md), not a check-back.
