# Fixation Error 🔒

## What it is

The failure to revise your assessment of a situation as new evidence arrives. Evidence
that contradicts your current picture is not weighed and rejected — it is missed,
discounted, or explained away as not really contradictory.

The trap is that the original assessment was usually *reasonable when you formed it*. This
is a failure of updating, not of care — and it strengthens under exactly the stress that
makes updating matter.

Three recognised shapes:

| Pattern | What it sounds like |
| :--- | :--- |
| **This and only this** | One hypothesis, pursued past the evidence against it |
| **Everything but this** | The correct explanation is the one never considered |
| **Everything is fine** | The problem itself is not acknowledged |

## Origin & evidence

De Keyser and Woods named the pattern from nuclear, aviation and medical operations, and
argued it is a major source of error in any dynamic, high-risk domain.

> De Keyser, V. & Woods, D. D. (1990). *Fixation errors: failures to revise situation
> assessment in dynamic and risky systems.* In Colombo, A. G. & Saiz de Bustamante, A.
> (eds), System Reliability Assessment. Dordrecht: Kluwer Academic, pp. 231–251.
> https://doi.org/10.1007/978-94-009-0649-5_11

The concept was taken up in anaesthesia crisis resource management, where it is taught as
cognitive lock-up or tunnel vision. Cuschieri's account of why it bites is the one worth
carrying: incidents *evolve* rather than arriving whole, so there is always an early,
defensible reading of the situation that later evidence should have overturned.

> Cuschieri, A. (2006). *Nature of human error: implications for surgical practice.*
> Annals of Surgery 244(5):642–648. https://pmc.ncbi.nlm.nih.gov/articles/PMC1856596/

## How to break it

You cannot detect your own fixation by introspection — that is what makes it fixation.
Every countermeasure is therefore external or pre-committed:

- **Decide the time-box before you start.** A limit set while calm is the only one that
  survives being inside the problem.
- **Say the hypothesis out loud**, with what would disprove it. An unstated hypothesis
  cannot be falsified by anyone, including you.
- **Let someone else look.** A second operator's value is not extra hands, it is a
  picture formed independently of yours.
- **Break state physically.** Stand up. The reset is what the 10-for-10 pause is for.

## Worked example

Latency spikes after a deploy. You conclude it is the deploy and start bisecting commits.
Thirty minutes in, a database alert fires; you read it as a downstream symptom of the slow
service and keep bisecting. It was a failing disk on the primary, and it had been alerting
since before the deploy. Nothing about the bisect was incompetent — the fault was that the
disk alert was filed as confirmation instead of contradiction.

## Limits

Naming the bias does not prevent it, and knowing the three patterns does not help you
recognise your own in the moment. The countermeasures that work are external or
pre-committed, which is why they belong on the card rather than here.
