# Safety-II and Work-as-Done 🔄

## What it is

Two ways of framing safety.

**Safety-I** treats safety as the *absence of failure*. You study accidents, find the
broken part, add a barrier. Almost everything else in these cards is Safety-I: checklists,
two-person rules, go/no-go gates.

**Safety-II** treats safety as the *presence of the capacity to succeed under varying
conditions*. Things go right and wrong for the same reason - people continuously adapting
to a system that never quite matches its description. So you study normal work, not only
the rare failures.

The operational handle is **Work-as-Imagined** versus **Work-as-Done**: the runbook versus
what the operator actually does. Every real system has a gap, and the claim that matters is
that the gap is usually not sloppiness but the adaptation keeping the thing running. An
engineer who skips step 4 and adds an undocumented check has generally found a defect in
step 4.

## Origin & evidence

Hollnagel introduced the Safety-I / Safety-II distinction as a reframing of safety
management.

> Hollnagel, E. (2014). *Safety-I and Safety-II: The Past and Future of Safety
> Management.* Farnham: Ashgate.
> https://erikhollnagel.com/books/safety-i-and-safety-ii.html

The software-specific work is the STELLA report, from a 2017 workshop run by Ohio State's
Cognitive Systems Engineering Laboratory with Etsy, IBM and IEX, studying real incidents at
those companies.

> SNAFUcatchers (2017). *STELLA: Report from the SNAFUcatchers Workshop on Coping With
> Complexity.* Ohio State University Cognitive Systems Engineering Laboratory.
> https://snafucatchers.github.io/

Three of its findings bear directly on how you run a review:

- **Expertise is model-updating, not knowledge.** As one participant put it, *"our skill
  is in being able to update our model efficiently and appropriately."*
- **"Blameless" usually means "sanctionless."** The report separates blame - attributing
  an outcome to a source - from sanction, the penalty. Organisations often promise the
  first while only delivering the second, and people can tell.
- **Write-only memory.** Incident libraries get written and never read. A postmortem
  nobody revisits has produced documentation, not learning.

## How to use it

In a postmortem, add the questions Safety-I does not ask:

- What did the operator actually do that was not in the runbook?
- What part of the procedure did someone skip, change or invent to make progress?
- Why did that seem right *at the time* - not whether it looks right now?
- Look at recent runs that **succeeded**. The adaptations holding the system together are
  visible there, and nowhere else.

## Worked example

A deploy fails, and the review finds the engineer ran a manual cache flush not in the
runbook. The Safety-I reading is an unauthorised step, so you add an approval gate. The
Safety-II reading asks why, and learns they had run that flush on the last eleven deploys
because the automated one silently no-ops on one shard. The runbook was wrong for a year;
the gate would have removed the only thing making deploys work.

## Limits

Safety-II is a perspective, not a drilled procedure like SBAR, and the Safety-I/II split is
contested - critics argue it caricatures traditional practice. Take the prompts above,
which stand on their own, and treat the theory as a lens rather than a method. It does not
replace barriers either: you still want the rollback tested.
