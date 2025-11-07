# SBAR(C) Communication Protocol: Structured Handover and Update 💬

The **SBAR(C)** model (Situation, Background, Assessment, Recommendation, Checkback) is a foundational communication technique for providing critical information quickly, concisely, and reliably. It is highly effective in technology incident management for escalating issues or passing control to a new Incident Commander.

---

## The Five Steps of SBAR(C)

| **Mnemonic** | **Full Meaning** | **Description & Application** |
| :--- | :--- | :--- |
| **S**ITUATION 🚨 | **What is happening right now?** | **(The 30-Second Hook)** Define the core problem and its immediate impact. Keep it current and direct. *Example: "Service A is completely down. Customers are seeing a 503 error on checkout."* |
| **B**ACKGROUND | **The necessary context.** | **(The Why/How)** Provide brief, relevant history. What caused this? What have we checked? *Example: "A new database schema migration (v2.1) was deployed 10 minutes ago. We tried rolling it back, but the rollback failed."* |
| **A**SSESSMENT 🧠 | **What is your analysis?** | **(Your Best Guess)** State what you believe the problem is and how severe it is. This is your professional judgment, not just raw data. *Example: "Assessment: This is a data incompatibility issue. We need a manual data repair before the application can start."* |
| **R**ECOMMENDATION | **What do you need?** | **(The Action Request)** State clearly and directly the next step, the resources you need, or the decision you require from the recipient. *Example: "Recommendation: I need the senior database engineer immediately to write the manual repair script."* |
| **(C) CHECKBACK** 👂 | **Verify Receipt.** | **(Closing the Loop)** The person receiving the information must repeat the key actions or information back to confirm understanding. *Example: Recipient: "Understood. Get the senior DB engineer for a manual repair script. Correct?" Sender: "Correct."* |

---

## Practical Example: Escalating a Broken Deploy

A junior operator calls a senior engineer:

1.  **SITUATION:** "We have a P1. The user service is completely offline due to the latest release."
2.  **BACKGROUND:** "Deployment D14 failed 5 minutes ago. It's hanging on the Kubernetes health check. The logs show a missing environment variable that was required for the update."
3.  **ASSESSMENT:** "I believe the deployment manifest is incorrect, and the previous version is now stuck in a bad state due to dependency locks."
4.  **RECOMMENDATION:** "I need you to look at the manifest files and authorize a force-delete of the deployment so we can manually roll back to the stable tag."
5.  **CHECKBACK:** *Senior Engineer: "So, I need to review the manifest and authorize a force-delete/manual rollback. Is that correct?"*



# SBARC Communication Protocol: Structured Handover and Update 💬

## 1. Introduction: What It Is

The **SBARC** model (Situation, Background, Assessment, Recommendation, Checkback) is a foundational communication technique for providing critical information quickly, concisely, and reliably. It standardizes the message structure to prevent miscommunication, especially during escalation or handover to a new Incident Commander.

---

## 2. Theory and Background

SBAR originated in nursing to ensure critical patient data was transferred accurately and efficiently between medical staff. Its use in technical operations ensures that the recipient of a message receives the full context needed to make the next decision, eliminating time wasted asking clarifying questions. The addition of **Checkback (C)**, borrowed directly from Crew Resource Management (CRM), ensures the loop is closed and the message was understood correctly by the recipient.

| **Mnemonic** | **Purpose** | **Focus** |
| :--- | :--- | :--- |
| **S**ITUATION 🚨 | The immediate state. | What is the problem *right now*? |
| **B**ACKGROUND | Necessary context. | What led to this? What have you tried? |
| **A**SSESSMENT 🧠 | Your professional judgment. | What do you *believe* the problem is? |
| **R**ECOMMENDATION | Call for action/resource. | What do you need the recipient to do next? |
| **C**HECKBACK 👂 | Confirmation. | Did the recipient understand the ask? |

---

## 3. Example: Escalating a Broken Deploy

**Operator A to New Incident Commander (IC B):**

1.  **SITUATION:** "IC B, we have a P1. The entire European API endpoint is reporting a 100% failure rate."
2.  **BACKGROUND:** "This started 45 minutes ago. It correlates with a failed deployment (v3.1) in the EU region. We have tried a full rollback, but the deployment system is stuck in a zombie state and won't clear the old version."
3.  **ASSESSMENT:** "I assess this as a K8s deployment system fault, not a code problem. The immediate risk is a massive financial penalty for SLA breach."
4.  **RECOMMENDATION:** "I recommend you take command and immediately contact the senior DevOps engineer for manual K8s cluster intervention."
5.  **CHECKBACK:** **IC B:** "Understood. I'm taking command. My first action is contacting senior DevOps for manual K8s intervention. Correct?" **Operator A:** "Correct."
