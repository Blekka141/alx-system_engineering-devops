# 0x19. Postmortem

## DevOps/SysAdmin

**Project Duration:** June 3, 2024, 6:00 AM to June 10, 2024, 6:00 AM  
**Manual QA Review:** Request it when you are done with the project

## Concepts

For this project, we expect you to understand the following concept:

- On-call

## Background Context

Any software system will eventually fail, and that failure can stem from a wide range of possible factors: bugs, traffic spikes, security issues, hardware failures, natural disasters, human error… Failing is normal and actually a great opportunity to learn and improve. Any great Software Engineer must learn from their mistakes to make sure that they won’t happen again. Failing is fine, but failing twice because of the same issue is not.

A postmortem is a tool widely used in the tech industry. After any outage, the team(s) in charge of the system will write a summary that has two main goals:

1. To provide the rest of the company’s employees easy access to information detailing the cause of the outage. Often outages can have a huge impact on a company, so managers and executives have to understand what happened and how it will impact their work.
2. To ensure that the root cause(s) of the outage has been discovered and that measures are taken to make sure it will be fixed.

## Resources

Read or watch:

- [Incident Report, also referred to as a Postmortem](https://medium.com/@blekka141/my-first-postmortem-3fdd35ebc437)
- [The importance of an incident postmortem process](https://medium.com/@blekka141/my-first-postmortem-3fdd35ebc437)
- [What is an Incident Postmortem?](https://medium.com/@blekka141/my-first-postmortem-3fdd35ebc437)

## More Info

### Manual QA Review

It is your responsibility to request a review for your postmortem from a peer before the project’s deadline. If no peers have been reviewed, you should request a review from a TA or staff member.

## Requirements:

**Issue Summary** (that is often what executives will read) must contain:
- Duration of the outage with start and end times (including timezone)
- What was the impact (what service was down/slow? What were users experiencing? How many % of the users were affected?)
- What was the root cause

**Timeline** (format bullet point, format: time - keep it short, 1 or 2 sentences) must contain:
- When was the issue detected
- How was the issue detected (monitoring alert, an engineer noticed something, a customer complained…)
- Actions taken (what parts of the system were investigated, what were the assumptions on the root cause of the issue)
- Misleading investigation/debugging paths that were taken
- Which team/individuals was the incident escalated to
- How the incident was resolved

**Root cause and resolution** must contain:
- Explain in detail what was causing the issue
- Explain in detail how the issue was fixed

**Corrective and preventative measures** must contain:
- What are the things that can be improved/fixed (broadly speaking)
- A list of tasks to address the issue (be very specific, like a TODO, example: patch Nginx server, add monitoring on server memory…)

Be brief and straight to the point, between 400 to 600 words.

While postmortem format can vary, stick to this one so that you can get properly reviewed by your peers.

Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.

Add URLs here:

- [https://medium.com/@blekka141/my-first-postmortem-3fdd35ebc437](https://medium.com/@blekka141/my-first-postmortem-3fdd35ebc437)

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x19-postmortem`
- File: `README.md`

---

### Make people want to read your postmortem

We are constantly stormed by a quantity of information, it’s tough to get people to read you.

Make your post-mortem attractive by adding humor, a pretty diagram, or anything that would catch your audience's attention.

Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.

Add URLs here:

- [My First Postmortem](https://medium.com/@blekka141/my-first-postmortem-3fdd35ebc437)
- [My First Postmortem with Humour...Maybe?](https://medium.com/@blekka141/my-first-postmortem-with-humour-maybe-e42c823fa002)

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x19-postmortem`
- File: `README.md`


### Task 0:
## Issue Summary

**Duration of the Outage:**  
Start: 2024-04-18 09:30 SAST  
End: 2024-04-18 11:00 SAST  
**Impact:**  
Our internal email server experienced an outage, preventing employees from sending or receiving emails. This impacted approximately 90% of our staff, leading to significant communication delays and affecting workflow across multiple departments.  
**Root Cause:**  
A corrupted update to the email server software caused a critical service to fail, leading to the server becoming unresponsive.

## Timeline

- **09:30** - Issue detected through a monitoring alert indicating the email server was unresponsive.
- **09:35** - IT support engineer confirmed the email outage by attempting to access the server.
- **09:40** - Investigation began with checking the server's status and recent logs.
- **09:50** - Initial assumption was a network connectivity issue, leading to checks on network infrastructure.
- **10:00** - Misleading path: Restarted the server's network services, but the issue persisted.
- **10:10** - Checked server hardware for potential failures, but found all hardware components functional.
- **10:20** - Issue escalated to the system administration team.
- **10:30** - Detailed review of recent updates revealed a corrupted update package.
- **10:40** - Reverted the email server to the previous stable version.
- **10:50** - Restarted the email server and tested functionality.
- **11:00** - Service restored and monitored to confirm resolution.

## Root Cause and Resolution

**Root Cause:**  
The root cause was a corrupted update to the email server software. The update package was incomplete, causing a critical service required for the email server to function to fail upon installation. This failure rendered the email server unresponsive.

**Resolution:**  
The issue was resolved by identifying the corrupted update package and reverting the email server to the previous stable version. The system administration team then reinstalled the stable version of the email server software, ensuring all services were operational. The email server was restarted, and normal operations were confirmed.

## Corrective and Preventative Measures

**Improvements/Fixes:**

1. **Implement Update Validation:**  
   Introduce a validation process for all software updates to ensure packages are complete and not corrupted before installation.

2. **Enhance Monitoring:**  
   Improve monitoring systems to include alerts for software update issues and service health checks immediately after updates.

3. **Develop a Rollback Strategy:**  
   Create a robust rollback strategy to quickly revert to previous versions in case of update failures.

**Task List:**

- **Validate Update Packages:** Implement scripts to automatically validate update packages before deployment.
- **Improve Monitoring Tools:** Upgrade monitoring tools to provide real-time feedback on service health post-update.
- **Train IT and SysAdmin Teams:** Conduct training sessions on the new validation and rollback processes.
- **Review Update Policies:** Revise update policies to include mandatory validation checks.
- **Conduct Regular Audits:** Schedule regular audits of the update process to ensure compliance with new policies.

By addressing these measures, we aim to prevent similar incidents in the future and enhance the reliability of our email server.

### Task 1:
## The Day the Emails Stood Still 🛑📧
## Issue Summary

**Duration of the Outage:**
**Start:** 2024-04-18 09:30 SAST
**End:** 2024-04-18 11:00 SAST

**Impact:**
Imagine trying to send an urgent email, and nothing happens. This was our reality for 90% of our staff, who suddenly found themselves in a digital silence. Significant communication delays ensued, leading to chaos (and lots of coffee) across multiple departments.

**Root Cause:**
A corrupted update to our beloved email server software caused a critical service to fail. Our email server decided it needed a break and became unresponsive.
Timeline

- **09:30** - 🔔 Issue detected: Monitoring alert says, "Email server is taking a nap."
- **09:35** - 🕵️‍♂️ IT support confirms: "Yup, the server's out cold."
- **09:40** - 🔍 Investigation begins: Checking server status and logs.
- **09:50** - 🛠️ Initial assumption: "Must be a network issue, right?"
- **10:00** - 🌐 Misleading path: Restarted network services. "Nope, still napping."
- **10:10** - 🔧 Checked hardware: "Everything looks good here."
- **10:20** - 🚨 Escalated to sysadmin team.
- **10:30** - 📜 Detailed review: "Hey, this update package looks sketchy!"
- **10:40** - 🔄 Reverted to previous version: "Back to the old reliable."
- **10:50** - 🔄 Restarted email server: "Please wake up."
- **11:00** - 🎉 Service restored: "And we’re back online!"

**Root Cause and Resolution:**

**Root Cause:**
The email server update was corrupted, leading to a failure in a critical service. This was like trying to bake a cake without flour—disastrous and unresponsive.

**Resolution:**
We identified the bad update, reverted to the previous stable version, and reinstalled the good version. It was like hitting undo on a major typo.
Corrective and Preventative Measures

**Improvements/Fixes:**

1. **Implement Update Validation:**
   Think of this as the "spell-check" for our updates. No more corrupted packages slipping through.

2. **Enhance Monitoring:**
   Our monitoring now has eyes everywhere, even on those sneaky updates.

3. **Develop a Rollback Strategy:**
   We’ve installed a "panic button" to roll back to safer versions when things go wrong.

**Task List:**

- **Validate Update Packages:** Script the spell-check for updates.
- **Improve Monitoring Tools:** More sensors, more alerts, more peace of mind.
- **Train IT and SysAdmin Teams:** Training on the new "spell-check" and "panic button."
- **Review Update Policies:** Policies now require validation checks before hitting "install."
- **Conduct Regular Audits:** Regular "spell-check" reviews to ensure compliance.


By turning our disaster into a learning opportunity, we aim to prevent future incidents and ensure our email server stays reliable and robust.
