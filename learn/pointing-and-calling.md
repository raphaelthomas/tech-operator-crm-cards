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

The widely cited figure is a **1994 Railway Technical Research Institute study finding
that pointing and calling reduced mistakes on a simple task by almost 85%.**

> Gordenker, A. (2008). *JR gestures.* The Japan Times, 21 October.
> https://www.japantimes.co.jp/news/2008/10/21/reference/jr-gestures/

**A provenance caveat:** that 85% figure reaches English-language sources through this
newspaper report rather than through the study itself, which is not readily available in
English. The number is repeated widely and consistently, but it has not been verified here
against the primary research. Treat the technique as well-established practice and the
specific figure as reported rather than confirmed.

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
