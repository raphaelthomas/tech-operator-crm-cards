# Sources

Every technique in `use/` traces to a named external origin. Nothing here is invented for
this repository, and nothing is a local house rule.

**Verified** means the claim has been checked against a publication. **Asserted** means it
is believed correct but has not yet been confirmed — see `TODO.md`.

## Always (0-start-here)

| Technique | Origin | Status |
| :--- | :--- | :--- |
| IMSAFE | FAA, *Pilot's Handbook of Aeronautical Knowledge* | asserted |
| Three-way communication | Nuclear power / naval reactor operations (INPO) | asserted |
| Sterile cockpit | FAA, 14 CFR 121.542 (1981) | asserted |
| PACE assertion ladder | Besco (1994), aviation CRM | asserted |
| Two-Challenge Rule | AHRQ TeamSTEPPS | asserted |
| Incident command roles | FEMA NIMS / US wildfire service | asserted |

## Before a change (1-before-change)

| Technique | Origin | Status |
| :--- | :--- | :--- |
| Time-Out | WHO Surgical Safety Checklist (2008) | asserted |
| Pre-mortem | Gary Klein, *Harvard Business Review* (2007) | asserted |
| Go/No-Go poll | NASA flight readiness review | asserted |
| Pre-committed abort trigger | Aviation V1 / rejected-takeoff briefing | verified |
| Two-person rule | Nuclear weapons handling; financial four-eyes principle | asserted |
| Point and call (*shisa kanko*) | Japanese railways | asserted |

## During an incident (2-during-incident)

| Technique | Origin | Status |
| :--- | :--- | :--- |
| 10 for 10 | Rall & Gaba, anaesthesia crisis resource management | asserted |
| FOR-DEC | DLR / Hörmann (1994) | asserted |
| Is / Is-Not | Kepner-Tregoe, *The Rational Manager* (1965) | asserted |
| Fixation error | De Keyser & Woods (1990) | verified |
| 17h awake ≈ 0.05% BAC | Dawson & Reid, *Nature* 388:235 (1997) | verified |
| Risk rises past hour 9 on shift | Folkard & Tucker (2003) | verified |
| Risk doubles across a continuous stretch | Tucker, Folkard & Macdonald, *Lancet* (2003) | verified |
| Extended shifts and error rates | Landrigan et al., *NEJM* 351:1838 (2004) | verified |
| "Escalation is not a sin" | Google SRE, *Managing Incidents* | verified |

## Handover (3-handover-brief)

| Technique | Origin | Status |
| :--- | :--- | :--- |
| SBAR | Kaiser Permanente, from US Navy submarine service | asserted |
| Check-back | AHRQ TeamSTEPPS | asserted |
| Explicit command acknowledgement | Google SRE, *Managing Incidents* | verified |

## Postmortem (4-blameless-postmortem)

| Technique | Origin | Status |
| :--- | :--- | :--- |
| Blameless postmortem | Allspaw / Etsy; Google SRE | asserted |
| 5 Whys | Toyota (Toyoda / Ohno) | asserted |
| Latent conditions, defence layers | James Reason (1990) | asserted |
| SHELL model | ICAO human factors framework | asserted |
| SMART | George Doran (1981) | asserted |
| Work-as-Done vs Work-as-Imagined | Hollnagel; SNAFUcatchers STELLA Report (2017) | asserted |

## Deliberately absent

No card prints a rollback threshold or an investigation time limit. Aviation computes V1
fresh for every takeoff and briefs it before the roll begins; the transferable discipline
is committing to a value in advance, not carrying a generic one. The cards therefore
require you to set and state those numbers, and supply none.
