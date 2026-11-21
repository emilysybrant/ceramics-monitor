# Evanston Art Center ceramics class monitor

Checks the Evanston Art Center ceramics department page every 20 minutes for the appearance of **Spring 2027** classes. When detected, it sends one email and records that the alert has been sent so it does not repeatedly email.

Page monitored: https://www.evanstonartcenter.org/school/dept/adult-classes-department/ceramics

## One-time setup

1. Create a free account at [Resend](https://resend.com/) and generate an API key.
2. In this GitHub repository, open **Settings → Secrets and variables → Actions**.
3. Choose **New repository secret**.
4. Add a secret named `RESEND_API_KEY` and paste the API key as the value.
5. Add a second repository secret named `NOTIFY_EMAIL` with the notification recipient address as its value.
6. Open **Actions**, select **Check Spring 2027 ceramics classes**, and choose **Run workflow** once to test the setup.

The first email uses Resend's default `onboarding@resend.dev` sender. Resend may restrict test sending to the email address associated with the Resend account until a sending domain is verified. If so, use the same recipient address for the Resend account or verify a domain you control and update the sender in `notify.py`.

GitHub scheduled workflows are best-effort; a run can start later than the scheduled time during periods of high load. The 20-minute schedule is not a guaranteed delivery SLA.
