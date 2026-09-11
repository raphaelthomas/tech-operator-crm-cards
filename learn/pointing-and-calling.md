# Pointing and Calling 👉

## What it is

Before acting, point at the thing and say what it is out loud. *"Signal — green."*
*"Target host — prod-db-3."*

The gesture and the voice are not theatre. Confirming silently is a single mental act and
easy to perform on autopilot; pointing and speaking forces eye, hand and voice into
agreement, and a mismatch between them is noticeable in a way a mistaken thought is not.

## Origin & evidence

Japanese railways, known as *shisa kanko*. It began in the early 1900s with steam
locomotive crews calling signal status to each other; the pointing was added decades later.
It is now standard across Japanese rail and has been adopted by transit systems including
New York and Toronto.

> Gordenker, A. (2008). *JR gestures.* The Japan Times, 21 October.
> https://www.japantimes.co.jp/news/2008/10/21/reference/jr-gestures/

The evidence here is adoption rather than a trial: a century of continuous use across one
of the world's busiest and safest rail networks, retained through complete generational
turnover of staff and equipment, and independently picked up by transit operators abroad.
A frequently quoted figure of an 85% error reduction traces to a 1994 Railway Technical
Research Institute study, but it reaches English-language sources through secondary
reporting rather than the research itself, so it is not relied on here.

## How to use it

- **Read the target aloud before executing**, not the intent. "Deleting namespace
  `checkout` on cluster `prod-eu`", not "cleaning up the old one".
- **Point at the screen.** Alone at a laptop this feels ridiculous. Do it anyway — the
  physical act is the mechanism, not the ceremony.
- **Say the identifier that would be catastrophic if wrong**: environment, host, table,
  branch.
- **Use it for reading, not just writing.** Calling out a dashboard value before acting on
  it catches "I saw what I expected to see".

## Worked example

`kubectl` context reads `prod-eu` while the plan, the ticket and the last twenty minutes of
conversation all concerned staging. Said silently, the mind supplies "staging" because
that is the context it has been holding. Said aloud, the word "prod" collides audibly with
the plan — and with anyone else in the room.

## Limits

It defends against slips — doing the wrong thing while intending the right thing. It does
nothing about mistakes, where the plan itself is wrong: calling out "prod" confidently is
no help when prod was always the wrong target. Pair it with a second person
([Two-Person Rule](./two-person-rule.md)), whose value is an independent picture rather
than a second pair of eyes on yours.

Quantified evidence in English is also thin. The practice is unusually well attested by
adoption, but if you want a controlled trial before committing to something, this is not
the technique that will give you one.
