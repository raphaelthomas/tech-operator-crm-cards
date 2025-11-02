That's an excellent next step. For a pocket card—a truly compact, high-stress aid—the key is ruthless efficiency. We need to strip anything that is too conceptual and replace it with direct, proven actions.

Here is a breakdown of what could be stripped and a list of practical, proven tools to add to the **Post-Incident Review (PIR) / Debrief** pocket card.

-----

## ✂️ What Could Be Stripped (Concept Overload)

The goal is to keep only the functional tools and the two most critical mandates.

| Item to Strip | Rationale for Removal | Action |
| :--- | :--- | :--- |
| **Attendance (P1)** | Too procedural for a stress aid. Attendance rules are set by policy, not on the card. | **Strip.** (Keep the "Facilitator Rule" on the card). |
| **Timeline Initiation (P1)** | Procedural detail ("within 48 hours") that doesn't help the user *during* the debrief. | **Strip.** |
| **Question Categories (P1)** | Conceptual—the categories (*Active Failure, Latent Condition, etc.*) are the theory behind the card. The **Modified 5 Whys** covers this function practically. | **Strip.** (Keep the core mandate: **"Human error is a symptom."**) |
| **Learning/Knowledge Gap (P1)** | Redundant. This is captured naturally by the **Modified 5 Whys** and the **Actionable Outcomes** section. | **Strip.** |

-----

## ➕ What Could Be Added (Practical, Proven Tools)

The additions focus on structured data gathering and analysis, taken from established safety investigation methods.

### 1\. 📊 The Data Analysis Tool: Chronology Checklist

This is the most critical first step for any PIR and helps the team move from a subjective story to an objective timeline.

  * **Tool:** **Chronology Checklist**
  * **Action:** Mandate the capturing of three pieces of data for every critical event:
      * **Timestamp (Z):** When did it happen (in UTC/Zulu time)?
      * **Observation:** What did the *system* show? (Metric spike, log entry, alert).
      * **Action:** What did the *human* do? (Command run, decision made, team member contacted).
  * **Card Wording:** **"PIR START: Establish Chronology (Time, Observation, Action)."**

### 2\. ❓ The Discovery Tool: The 4 Ps

This tool ensures the analysis covers all critical dimensions of the failure, moving beyond just the code.

  * **Tool:** **The 4 Ps** (for Latent Condition Discovery)
  * **Action:** Ensure the discussion examines:
      * **Procedures:** Did the runbook/policy fail?
      * **People:** Were the training, communication, or staffing levels adequate?
      * **Plant/Product:** Did the tool, monitoring, or underlying infrastructure fail?
      * **Priorities:** Did organizational pressures (speed, cost) contribute to the failure?
  * **Card Wording:** **"Latent Condition Search: Check 4 Ps (Procedure, People, Plant/Product, Priorities)."**

-----

## 📝 Revised PIR Pocket Card Template (Markdown)

This template is significantly condensed and focuses only on high-value, actionable procedures.

### 📝 PIR Pocket Card: Systemic Learning (Page 1 of 2)

| 👥 **MANDATES & SETUP** | **ACTION / REMINDER** |
| :--- | :--- |
| **PIR Goal** | **System Improvement, not individual punishment.** Honesty is mandatory. |
| **Blameless Culture** | Facilitator Rule: **Shut down** all blame. Rephrase accusations: **"What led us to believe this action was the correct choice at the time?"** |
| **Data First** | **Fact-check:** Start with the validated timeline. **Ignore speculation.** |
| **PIR Start** | **Establish Chronology:** For every key event, log: **Time (Z), Observation (System), Action (Human).** |

-----

### 🛠️ ANALYSIS TOOLBOX

| Tool | Purpose | How to Apply |
| :--- | :--- | :--- |
| **Modified 5 Whys** | **Drive past human error** to the systemic flaw. | Start with the Active Failure and ask **"Why?"** repeatedly, stopping only when the answer is a **systemic or procedural gap** (e.g., lack of automation, staffing pressure). |
| **Latent Condition Search** | **Check 4 Ps:** Ensure analysis covers all dimensions of failure:<br>1. **Procedures** (Runbook/Policy)<br>2. **People** (Training/Staffing/Comms)<br>3. **Plant/Product** (Tooling/Monitoring/Infra)<br>4. **Priorities** (Org. Pressure/Tradeoffs) |

-----

### 📝 PIR Pocket Card: Learning & Action (Page 2 of 2)

| 🟢 **SYSTEMIC OUTCOMES** | **REQUIREMENT** |
| :--- | :--- |
| **Mandate** | **Human error is a symptom, not a cause.** Do not stop the investigation at the person. |
| **Actionable Outcomes** | List every layer of defense that **should have caught the incident** but failed (e.g., Monitoring, Automated Testing, Runbook). |
| **Categorization** | Assign all actions a type: **Code/Config Fix, Documentation Update, Automation/Tooling, Training/Procedure Change.** (Prioritize the last two). |
| **SMART Follow-up** | All actions must be **S**pecific, **M**easurable, **A**chievable, **R**elevant, and **T**ime-bound. Vague actions ("Be more careful") are rejected. |
| **Ownership** | Every action must have a single **named owner** and a **due date** logged in a tracking system. |
| **Verification Loop** | Before closing an action item, **verify the fix** (e.g., by simulating the failure or running a specific test). |
