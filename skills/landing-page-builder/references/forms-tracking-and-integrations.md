# Forms, Tracking, and Integrations

## Form design

Choose fields based on the decision:

- low-friction opt-in: minimum identity and delivery field;
- consultation: contact plus one or two qualification inputs;
- application: only fields used in qualification;
- property or valuation: necessary property data plus contact and consent;
- event: registration and logistics needs.

Specify:

- required versus optional;
- validation;
- conditional fields;
- error and success messages;
- consent text and checkbox behavior;
- hidden source/UTM fields;
- duplicate handling;
- spam protection;
- accessibility labels.

Do not bundle email, SMS and call consent ambiguously.

## CRM map

Define:

- lead source and campaign;
- lifecycle stage;
- interest/offer;
- language;
- market/geography;
- consent channel and timestamp;
- owner;
- tags;
- next task;
- qualification data;
- exit/suppression status.

## Notifications and handoff

Specify:

- who receives the lead;
- channel;
- response SLA;
- fallback when delivery fails;
- human takeover;
- stop conditions for automation.

## Tracking

At minimum:

- page view;
- form start when useful;
- form submit;
- successful CRM receipt when observable;
- booking, application or purchase;
- thank-you view;
- download/access;
- qualified outcome and offline close when available.

Use UTMs consistently and avoid duplicate conversions across browser, server and thank-you events.

## Integration verification

Test:

- required fields;
- invalid input;
- successful submission;
- CRM mapping;
- notification;
- thank-you state;
- delivery link;
- tracking event;
- mobile;
- duplicate and retry behavior.

Do not submit to a live external system without authorization. Use a test record or clearly defined safe test path.
