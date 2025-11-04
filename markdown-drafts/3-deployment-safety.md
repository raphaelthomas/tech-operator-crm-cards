# 🚀 Tech Operator Deployment Safety Card

## 🗣️  BRIEFING - COMMIT & CLARIFY (AIM-C)

This step establishes a shared mental model and defines the failure points through active verification.

| Mnemonic | Focus | Action / Shared Understanding |
| :--- | :--- | :--- |
| **A**im | **Goal** | **State the objective:** What are we achieving and why is it important? |
| **I**ntent | **Method** | **Review the main plan:** Walk through the steps, who is executing, and what tools are used. |
| **M**ishaps | **Risks** | **Identify 2-3 biggest risks:** Where will the system most likely fail? |
| **C**ontingency | **Plan B** | **Establish Triggers:** What are the **exact conditions** that mandate a **ROLLBACK** or a pivot to an **ALTERNATE** plan? |
| **Close the Loop** | **Confirmation** | **Mandate Confirmation:** Directly ask key team members to **verbally repeat** the Contingency Triggers or key risks. (Example: "Monitor, what is our rollback trigger?" The monitor must reply.) |

## 🚦 VERIFICATION - CHECKLIST & GO/NO-GO

This step requires objective, verifiable evidence before proceeding. **All checks must be GREEN.**

| 🎯 **Phase A: System Readiness Checks** | **VERIFY YES/NO** |
| :--- | :--- |
| **Rollback Path** | Is the **rollback script/procedure** fully validated (e.g., against staging) and ready to execute **immediately**? |
| **System Capacity** | Is system resource usage (CPU/Memory/Disk) currently **below 60%** and stable? (Prevents cascading failure.) |
| **Monitoring Validation** | Is the **dashboard verified** to be displaying live, accurate data for the impacted services? |
| **Test Coverage** | Has the deployment passed **smoke/integration tests** in a pre-production environment **today**? |
| **Artifact Check** | Is the final deployment artifact (e.g., container hash, version tag) **verified and approved**? |
| **Go/No-Go Call** | All key stakeholders must give a **verbal "GO"** immediately before execution. |

| 🎯 **Phase B: Human & Process Checks** | **VERIFY YES/NO** |
| :--- | :--- |
| **Tool Access** | Does the **Operator** have verified, current access and credentials for the target environment? |
| **Runbook Status** | Is the **runbook version** correct, printed/digital copy present, and the **Operator** familiar with Step 1? |
| **Contingency Clarity** | Has every team member confirmed understanding of the **Contingency Triggers (Plan B)?** |

## 🚧 EXECUTION DISCIPLINE

| RULE | ACTION / REQUIREMENT |
| :--- | :--- |
| **Time Synchronization** | **Start a common, visible timer** now. All status reports and time-based triggers must reference this time. |
| **Sterile Cockpit** | During the deployment sequence, **restrict all communication** to only essential command execution and status updates. Silence non-essential comms. |
| **Two-Person Rule** | Designate an **Operator** and a **Monitor**. The Monitor verifies the command *before* execution and watches metrics *during* execution. |
| **Stop-Point Checks** | Define **3-5 mandatory, objective checks** (e.g., latency, error rates) that must be **GREEN** before proceeding to the next deployment phase. |

## 🛑 IMMEDIATE FAILURE PROTOCOL

| RULE | ACTION / RATIONALE |
| :--- | :--- |
| **The 5-Minute Rule** | If the system does not return to a defined "Green" state by the **Contingency Trigger Time**, **initiate the ROLLBACK plan immediately.** |
| **Rollback Action** | Upon receiving the first unexpected alert: **1. Announce "ROLLING BACK NOW!" 2. Capture logs/metrics (if time allows). 3. Execute rollback.** |
| **Rollback Verification** | Do not declare the process finished until you have validated that the rollback is **complete** and the system has returned to the state *before* the deployment attempt. |
