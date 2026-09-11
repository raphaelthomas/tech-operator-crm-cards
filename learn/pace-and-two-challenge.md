# PACE and the Two-Challenge Rule 📢

## What it is

A ladder for raising a concern to someone senior, escalating only as far as you need:

| Step | You say |
| :--- | :--- |
| **P**robe | Ask. "What are we expecting this command to do?" |
| **A**lert | Name the risk. "That looks like it targets prod, not staging." |
| **C**hallenge | Demand a stop. "Stop. I need you to check the target before you run it." |
| **E**mergency | Act. Pull the change, page someone above them, whatever prevents the harm. |

The **Two-Challenge Rule** is the companion: if you have voiced a concern twice and it has
not been acknowledged, you are obliged to escalate to someone else. The trigger is
*unacknowledged*, not *disagreed with* - a reasoned "I hear you, do it anyway" is an
answer; silence is not.

## Origin & evidence

PACE comes from aviation CRM, developed by Besco to give junior crew a graduated way to
intervene with a captain who is not performing to standard. It has since been adopted
widely in medicine, where some versions render the E as *Escalate* rather than *Emergency*.

> Besco, R. O. (1994). *To intervene or not to intervene? The co-pilot's catch 22.*
> http://picma.info/sites/default/files/Documents/Background/Besco%20Co-pilots%20dilemma.PDF

The Two-Challenge Rule is from TeamSTEPPS, the US Department of Defense and AHRQ teamwork
programme, itself derived from aviation and nuclear practice. AHRQ frames it as a tool for
overcoming *"our natural tendency to believe the team leader must always know what they
are doing, even when the actions taken depart from established guidelines."*

> Agency for Healthcare Research and Quality. *TeamSTEPPS: Two-Challenge Rule.*
> https://www.ahrq.gov/teamstepps-program/curriculum/mutual/tools/rule.html

Both exist because the hard problem is not noticing the error. It is saying so to someone
senior, and being heard.

## How to use it

- **Start low.** A probe costs nothing and is usually enough; most concerns dissolve at
  the first question.
- **Escalate on silence, not on disagreement.**
- **Be specific and behavioural.** "That host is prod" beats "are you sure about this?"
- **Say the word "stop"** at the challenge step. Ambiguity is what the ladder exists to
  remove.
- **If you are senior, make it cheap.** Say out loud at the start of a change that you
  expect to be challenged, and thank people who do it - including the times they were
  wrong.

## Worked example

> **Probe:** "What environment is that kubeconfig pointing at?"
> - no answer, typing continues.
> **Alert:** "I think that context is prod. Deleting that namespace takes checkout down."
> - "It's fine."
> **Challenge:** "Stop. Do not press enter. Print the context and read it out."

Two unacknowledged concerns would have meant paging the on-call lead, whatever the
seniority in the room.

## Limits

The ladder does not by itself create the conditions for using it. Where challenges are
poorly received, people stop at the probe step. How the senior person responds to the first
challenge largely determines whether there is a second.
