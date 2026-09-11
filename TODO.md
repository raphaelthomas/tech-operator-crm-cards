# TODO

## Safety-II: integrate Work-as-Done into the cards

The STELLA Report (SNAFUcatchers, 2017) and resilience engineering hold that operators
are not a liability but the system's most flexible defence: they succeed by continuously
adapting to complexity. The gap between **Work-as-Imagined** (the runbook) and
**Work-as-Done** (what actually happens) is where that adaptation lives, and finding it
is more useful than cataloguing failures.

### Post-mortem card

- **Successful deviations.** Before investigating a failure, look at recent *successful*
  runs. What did the operator do that was not in the runbook? Those are the local patches
  holding the system together.
- **Procedure vs reality.** What part of the procedure did someone skip, change, or
  invent to make progress? That pinpoints where the documentation is wrong.
- **Experience as a resource.** Interview for rationale, not just actions — why did this
  seem right at the time?

### Before-change card

- **Local knowledge check.** Does anyone know environmental quirks or gotchas that are
  not in the runbook?
- **Capture what actually happened.** Record the commands actually used, even where they
  differed from the runbook, and feed them back into the documentation.

## learn/ backlog

Cards are self-sufficient — every mnemonic is spelled out on the card itself — so these
add origin, evidence and failure modes rather than anything operationally new.

### Phase B — referenced by 0-start-here and 1-before-change

- [ ] `imsafe.md`
- [ ] `three-way-communication.md` (with check-back and read-back)
- [ ] `sterile-cockpit.md`
- [ ] `pace-and-two-challenge.md`
- [ ] `ics-roles.md`
- [ ] `surgical-time-out.md`
- [ ] `pre-mortem.md`
- [ ] `go-no-go.md`
- [ ] `two-person-rule.md`
- [ ] `pointing-and-calling.md`

### Phase C — diagnosis and review

- [ ] `ten-for-ten.md`
- [ ] `is-is-not.md`
- [ ] `swiss-cheese-latent-conditions.md`
- [ ] `shell-model.md`
- [ ] `blameless-postmortem.md` (SMART folded in)

## Open

- [ ] Citation depth in `learn/`: full citations, or link plus a sentence?
- [ ] Verify the provenance claims in `SOURCES.md` that are still asserted rather than
      checked — only the fatigue sources have been confirmed against publications.
