# Bug Report — Pretty Good AI Agent (Pivot Point Orthopedics)

---

## Bug 1 — Garbled Date of Birth on Profile Creation
**Severity:** High
**Call:** transcript-CAac61180da614c8e38efb2c1baac7e903.txt
**Details:** When creating a new demo patient profile, the agent said "Your patient profile has been created successfully for demo purposes. I have your date of birth is 742. 000?" — the date of birth is completely garbled and nonsensical. This appears to be a data formatting or TTS rendering issue where a numeric value is being read incorrectly. A patient hearing this would be confused and lose trust in the system.

---

## Bug 2 — Opening Greeting Repeated 3 Times
**Severity:** Medium
**Call:** transcript-CAdac1fa3d89e5705191730150ccac4122.txt
**Details:** The agent played its full opening greeting ("This call may be recorded for quality and training purposes. Thanks for calling Pivot Point Orthopedics...") three consecutive times before proceeding. This is likely caused by duplicate webhook triggers or a race condition in the call setup. It creates a poor first impression and wastes the patient's time.

---

## Bug 3 — Date of Birth Verification Loop
**Severity:** High
**Call:** transcript-CAdac1fa3d89e5705191730150ccac4122.txt
**Details:** After the patient provided their full name and date of birth, the agent asked for the date of birth again three separate times ("Please tell me your date of birth. Please tell me your date of birth." and then "Please provide your date of birth.") before finally acknowledging it. The agent appeared to not register the patient's spoken response on the first two attempts, causing a frustrating loop.

---

## Bug 4 — Agent Confirms Identity Then Immediately Rejects It
**Severity:** High
**Call:** transcript-CAdac1fa3d89e5705191730150ccac4122.txt
**Details:** After the patient confirmed their name and DOB, the agent said "I have your name as Sarah Johnson and your date of birth as March 15th, 1988. Is that correct?" — the patient confirmed — and then the agent immediately said "The birthday does not match our records, but for demo purposes, I'll accept it." This contradictory flow (ask → confirm → reject) is confusing and logically broken. If the birthday doesn't match, the agent should flag it before asking the patient to confirm.

---

## Bug 5 — Cannot View Existing Appointment Details
**Severity:** Medium
**Call:** transcript-CAb77df4b718714a4e7b41c2f03669b18f.txt
**Details:** When the patient asked "could you tell me what date that appointment is for?", the agent responded "I can help with that but I'm not able to view the booked appointment details from here." The agent should be able to retrieve and share the patient's existing appointment information — this is a basic capability gap that forces patients to call back or wait for support.

---

## Bug 6 — Live Support Transfer Loops Back to AI Test Line
**Severity:** Critical
**Call:** transcript-CAb77df4b718714a4e7b41c2f03669b18f.txt, transcript-CA57e91f856311b2ea0ae27f45330d9b61.txt
**Details:** When the agent transfers to "live support," the call is immediately answered by a recording saying "Hello, you've reached the pretty good AI test line, goodbye" and hangs up. This happens consistently across multiple calls. The transfer destination appears to route back to the same test system rather than an actual support queue, leaving patients stranded with no resolution.

---

## Bug 7 — Agent Books Appointment Without Collecting Patient Identity First
**Severity:** Medium
**Call:** transcript-CA3244b00c1970a0689f83710f1ea6e80e.txt
**Details:** In several calls, the agent engaged in appointment scheduling discussion (agreeing to "Tuesday at 2pm" or "Tuesday at 12pm") without ever asking for the patient's name or date of birth. A valid appointment booking should require identity verification first. These bookings would have no patient record attached to them.

---

## Bug 8 — Duplicate Appointment Conflict Not Handled Gracefully
**Severity:** Medium
**Call:** transcript-CAfc52efbb2d64f0fef05f443260a03982.txt
**Details:** When the agent detected an existing appointment of the same type, it said "I can't book a new 1 right now. Since you already have that type of appointment on file. I can connect you to our patient support team. However, I'm a pretty good Ai and can do many of the things and operator can do. You want to give me a try?" — this response is self-contradictory. The agent offers to connect to support and then immediately tries to retain the patient instead of following through. Additionally, the phrase "I'm a pretty good Ai" breaks the persona of a medical office assistant.

---

## Bug 9 — Agent Uses Informal/Unprofessional Language
**Severity:** Low
**Call:** Multiple calls
**Details:** The agent repeatedly used informal language including "Yeah, that works", "Yeah, sure. Let's do on Tuesday", and "I'm now that's all" — these are not appropriate for a medical office context. Additionally, transcription artifacts like "I'm a pretty good Ai" and "A Lubin Live support" suggest the TTS/STT pipeline has quality issues that leak into responses.

---

## Bug 10 — Appointment Confirmed Without Doctor or Exact Date
**Severity:** Medium
**Call:** transcript-CA3244b00c1970a0689f83710f1ea6e80e.txt
**Details:** The agent confirmed an appointment for "Tuesday at 2pm" and "Tuesday at 12pm" in the same call without specifying which Tuesday, which doctor, or what the appointment type was officially recorded as. A complete appointment confirmation should include the full date, time, provider name, appointment type, and what to bring.

---

## Summary Table

| # | Bug | Severity |
|---|-----|----------|
| 1 | Garbled DOB on profile creation | High |
| 2 | Opening greeting repeated 3x | Medium |
| 3 | DOB verification loop (asked 3 times) | High |
| 4 | Confirms identity then immediately rejects it | High |
| 5 | Cannot view existing appointment details | Medium |
| 6 | Live support transfer loops back to AI | Critical |
| 7 | Books appointment without identity verification | Medium |
| 8 | Duplicate appointment conflict handled poorly | Medium |
| 9 | Informal/unprofessional language | Low |
| 10 | Appointment confirmed without full details | Medium |
