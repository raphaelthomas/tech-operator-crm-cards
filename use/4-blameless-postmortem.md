# 🔍 Blameless Postmortem

Run this after an incident, **or after any change worth learning from** - including the ones that went fine.

## Setup

| | |
| :--- | :--- |
| **Goal** | Improve the system, not judge the person. |
| **Blame** | Shut it down. Rephrase as: *"What made this the reasonable choice at the time?"* |
| **Data first** | Start from the validated timeline. Ignore speculation. |
| **Chronology** | Per event: time (UTC) · what the system showed · what the human did. |

## Analysis

| | |
| :--- | :--- |
| **5 Whys** | Ask why until the answer is systemic. Never stop at human error. |
| **SHELL** | Cover every dimension: **S**oftware · **H**ardware · **E**nvironment · **L**iveware (the person) · **L**iveware-**L**iveware (between people). |
| **Work-as-done** | What did the operator actually do that was not in the runbook? |
| **Rationale** | Ask why it seemed right *then*, not whether it looks right now. |
| **Defences** | List every layer that should have caught this and did not. |

## Actions

| | |
| :--- | :--- |
| **SMART** | **S**pecific · **M**easurable · **A**chievable · **R**elevant · **T**ime-bound. "Be more careful" is rejected. |
| **Type** | Code/config · documentation · tooling · procedure. Prefer the last two. |
| **Owner** | One named person, one due date, tracked. |
| **Verify** | Prove the fix works before closing it. |
