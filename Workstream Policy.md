# The WHATWG Workstream Policy

If this Workstream Policy conflicts with the [Intellectual Property Rights Policy](./IPR%20Policy.md), the [Intellectual Property Rights Policy](./IPR%20Policy.md) controls.

Whenever this Policy says to notify or contact the [Steering Group], this should be done via its issue tracker as defined in the [Steering Group Policy], unless stated otherwise. Informal notice is not sufficient.

## 1. Definitions

1. "<a id="def-editor">**Editor**</a>" means a person designated by the [Steering Group] as having authority to modify a [Living Standard]
     and other documents in a particular [Workstream], and to publish the
     [Living Standard Review Drafts][def-review-draft] in that [Workstream].

2. "<a id="def-living-standard">**Living Standard**</a>" means a single, unified technical specification, published by the WHATWG as a Living Standard, as modified from time to time by the [Editor] of the associated [Workstream]. [Living Standards][Living Standard] are intended to include only those features that are likely to be implemented in major browser engines and are suitable for adoption and implementation by other browser engine developers and integrators.

3. "<a id="def-inanimate-standards">**Inanimate Standards**</a>" are published Standards that are no longer under development by the
     WHATWG.

4. "<a id="def-incubation">**Incubation**</a>" means the work of exploring and developing technologies that require additional
     testing and refinement before browser engine developers can reasonably make a preliminary
     commitment to implement the technology in publicly distributed browsers.

5. "[Living Standard Review Draft][def-review-draft]" or "<a id="def-review-draft">**Review Draft**</a>" is a version of a [Living Standard] that is
     published as the reference for patent review and potential claim exclusion by [Workstream Participants].

6. "<a id="def-other-publications">**Other Publications**</a>" means any publication of the WHATWG other than [Living Standards][Living Standard] and Review
     Drafts.

7. "<a id="def-workstream">**Workstream**</a>" means a unified technical development effort (in most cases developing a single
     [Living Standard], more than one only if inextricably bound together). [Workstreams][Workstream] and
     [Contributions] are publicly visible.

8. "<a id="def-workstream-participant">**Workstream Participant**</a>" means any person or [Entity] that has executed a [Contributor and Workstream Participant Agreement].

9. "<a id="def-workstream-repsotiroy">**Workstream Repository**</a>" means the issue tracker and tidy Git repository with linear history that hosts development of a [Workstream]'s [Living Standards][Living Standard] and other products.

10. "<a id="def-workstream-scope">**Workstream Scope**</a>" means the technical scope of a [Workstream].

## 2. Workstreams

### 2.1. Workstreams in progress

The [Steering Group] maintains a [document](./Workstreams.md) listing active [Workstreams][Workstream] of the WHATWG , including their [Scope][Workstream Scope], appointed [Editor], and all [Living Standards][Living Standard] they
include.

### 2.2. Workstream publications

#### A. Living Standards

Each [Workstream] is dedicated to a single [Living Standard] (or, if unavoidable, two
or more inextricably interdependent [Living Standards][Living Standard]) and may also publish documents directly
associated with the [Living Standard]. A [Workstream] must publish its first [Review Draft][def-review-draft] no later than six months after formation.

#### B. Other publications

Works other than technical specifications may be proposed and published as
determined by the [Steering Group].

#### C. Editor discretion

Within the approved [Workstream Scope], the [Editor] evolves the [Living Standard] and other
publications of the [Workstream]. The [Workstream]'s [Editor] may add,
remove, merge or split [Living Standards][Living Standard] and other associated documents, so long as all
deliverables are still within the [Workstream's Scope][Workstream Scope].  If the change affects [Living Standards],
the [Editor] must notify the [Steering Group] 14 [Days] in advance of the change.

### 2.3. New Workstreams

#### A. Workstream Scope

The [Steering Group] approves new [Workstreams][Workstream] and determines the [Scope][Workstream Scope].

#### B. Workstream Proposals

1. Anyone can create a <a id="def-workstream-proposal">**Workstream Proposal**</a> by detailing a problem statement and proposed [Living Standard] that is likely to be implemented by the major browser engine developers; proposals must describe the work in sufficient detail to proceed with the development of a [Living Standard] within the WHATWG's stated purposes. [Workstreams][Workstream] are not intended for [Incubation](#def-incubation) or speculative projects.
1. A [Workstream Proposal] must be publicly available, including any referenced documents, and in English.
1. A [Workstream Proposal] must include the following:
   1. Proposed [Workstream] name.
   1. Statement of purpose, including problem to be solved, proposed solution, status of the proposed solution, and how it is consistent with the [WHATWG Principles] and appropriate for a [Workstream].
   1. Specific [Scope][Workstream Scope] of work (included and excluded).
   1. Proposed deliverables.
   1. Draft of the proposed [Living Standard] plus (optionally) a list of other proposed deliverables.
   1. A list of similar or related work being undertaken or proposed elsewhere and its relationship to the proposed [Workstream].
   1. Anticipated commencement date and timeline for work going forward.
   1. Anticipated [Workstream Participants].
   1. Description or list of those likely to implement or otherwise have an interest in the work.
   1. Expectations regarding long-term maintenance of the [Living Standard].
1. The [Steering Group] will consider and respond to all [Workstream Proposals][Workstream Proposal].

### 2.4. Workstream changes

1. [Workstreams][Workstream] may be modified by the [Steering Group], including but not limited to the following:
   1. The [Steering Group] may split a [Workstream] into multiple successor [Workstreams][Workstream], each with a [Scope][Workstream Scope] that does not exceed that of the input [Workstream]. The [Steering Group] must determine the [Scope][Workstream Scope] and [Living Standards][Living Standard] for each successor [Workstream]. In such cases, all [Participants][Workstream Participants] in the input [Workstream] automatically become [Participants][Workstream Participants] in each newly-created successor [Workstream].
   1. The [Steering Group] may merge multiple [Workstreams][Workstream] into a single successor [Workstream], whose [Scope][Workstream Scope] encompasses that of all input [Workstreams][Workstream] and which contains all [Living Standards][Living Standard] of the input [Workstreams][Workstream]. The [Steering Group] must determine the [Scope][Workstream Scope] of the successor [Workstream]. In such cases, the newly-created successor [Workstream] does not automatically gain the [Participants][Workstream Participants] of the input [Workstreams][Workstream]; the [Steering Group] should reach out to these [Participants][Workstream Participants] and encourage them to participate again.
   1. The [Steering Group] may modify a [Workstream Scope], in which event (a) the [Steering Group] must publish the proposed modifications at least 14 [Days] before they become effective, and (b) current and prospective [Workstream Participants] may provide feedback to the [Steering Group] (comments, proposed changes, objections, etc.).
   1. The [Steering Group] may terminate a [Workstream]. (Terminating a [Workstream] does not foreclose additional development; it only terminates the [Workstream] process as to a particular [Living Standard] and [Other Publications] of that [Workstream].)
1. [Editors][Editor] or [Participants][Workstream Participants] may propose [Scope][Workstream Scope] changes to the [Steering Group].


## 3. Living Standards

### 3.1. Contributions

#### A.

[Contributions] are deemed to have been made jointly by both the individual submitting the
[Contribution][Contributions] and any [Entity] identified in the [Contributor and Workstream Participant Agreement].

#### B.

A [Contributor][def-contributor] may withdraw a [Contribution][Contributions] to a [Workstream] by notice to the [Steering Group]
delivered before 45 [Days] have elapsed since the [Contribution][Contributions] was made.

### 3.2. Modifying the Living Standard

Only a [Workstream]'s [Editor] may modify the text of a [Workstream]'s
[Living Standards][Living Standard]. In doing so, [Editors][Editor] take into consideration the
factors set forth in [Working Mode](https://whatwg.org/working-mode). An [Editor] may appoint one
or more deputy editors authorized to modify the text on behalf of the
[Editor].

### 3.3. Timing

[Editors][Editor] update [Living Standards][Living Standard]; changes are publicly visible in the [repository][Workstream Repository].

### 3.4. Contribution validation

After the [IPR Policy] becomes effective, [Editors][Editor] are responsible for ensuring that material included in their [Living Standards][Living Standard] is governed by a
[Contributor and Workstream Participant Agreement].

### 3.5. Tagging

[Editors][Editor] must tag their [Living Standards][Living Standard]' text for identification as follows.

#### A. Objection Pending

[Editors][Editor] must tag text "Objection Pending" if a [Workstream Participant][Workstream Participants] has delivered a request for review and resolution by the [Steering Group].

#### B. Exclusion

[Editors][Editor] must tag text "Patent Exclusion Filed" if a [Patent Exclusion Notice]:

1. has been filed that identifies the text in question with sufficient precision for the [Editor] to tag the designated lines or components, and
2. has not been withdrawn or resolved.

The [Editor] is not required to include tags if, in the [Editor]'s judgment, the [Patent Exclusion Notice] is not sufficiently clear regarding precisely which text is in question; omission of a tag does not, however, affect the applicability or validity of the [Patent Exclusion Notice].

#### C. Optional tags

An [Editor] may, at the [Editor]'s discretion, also tag text such as the following:

1. [Editors][Editor] may tag text "Objection Pending" if:
    1. They anticipate substantive objections from a [Steering Group Member] , even if not yet formally registered.
    1. They anticipate substantive objections from a [Workstream Participant][Workstream Participants], even if not yet formally registered; or if a [Workstream Participant][Workstream Participants] has indicated their intent to request review by the [Steering Group].
    1. In the [Editor]'s judgment the text otherwise does not meet the WHATWG criteria or other criteria set forth by the [Steering Group].
1. [Editors][Editor] may tag text "Under Discussion" if:
    1. The text requires further development before it is stable, but is being retained (e.g., for purposes of completing the development because testing or user experience indicates problems with interoperability or function, or the text was recently introduced and is not yet fully integrated, etc.).

### 3.6. Reclassification

1. The [Steering Group] may reclassify [Living Standards][Living Standard], including but not limited to the following:
   1. No further development by the WHATWG ("[Inanimate][Inanimate Standards]" or other designation of the [Steering Group]).
   1. No longer published as a WHATWG [Living Standard] ("Depublished").

## 4. Review Drafts

### 4.1.

[Review Drafts][def-review-draft] serve as the reference for patent review and potential claim exclusion by
[Workstream Participants].

### 4.2.

[Editors][Editor] publish [Review Drafts][def-review-draft] approximately every six months.

#### A.

When an [Editor] publishes a [Review Draft][def-review-draft], they must post a note in the [Workstream Repository] and the
[Patent Exclusion Period] commences; no additional notice to [Workstream Participants] is required.

#### B.

[Review Drafts][def-review-draft] are substantially identical to the associated [Living Standard] except that, prior to
publication for review, [Review Drafts][def-review-draft] redact from the [Living Standard] text tagged "Objection
Pending" or "Under Discussion".

## 5. Roles and participation

### 5.1. Editors

#### A. Nature of the role

[Editors][Editor] are responsible for the technical content of their [Workstreams][Workstream], and
accordingly have sole authority to modify WHATWG documents in the [Workstream] for which they serve
as [Editor] (e.g., to adopt or adapt [Contributions], including their own; accept pull requests;
etc.), and to publish the associated [Living Standard], periodic [Review Drafts][def-review-draft], and documentation
(if any).

#### B. Qualifications

[Editors][Editor] must have command of the technical subject matter; [Editors][Editor] (and any
[Entity] with which they are affiliated) must be [Workstream Participants] in
the [Workstream] to which they are apponted.

#### C. Appointing and removing Editors

1. [Steering Group] appoints and may remove the [Editor] for each [Workstream].
1. [Editors][Editor] may resign by notice to the [Steering Group].

#### D. Rights, privileges, and obligations

[Editors][Editor] are responsible for ensuring that

1. Their WHATWG [Living Standards][Living Standard] are within the [Workstream Scope] and consistent with the [WHATWG Principles] and other criteria set by the [Steering Group];
1. after the [IPR Policy] becomes effective, only [Contributions] from those who have signed the [Contributor and Workstream Participant Agreement] are incorporated into a [Living Standard], and
1. there are no unresolved substantive objections from [Workstream Participants] before merging [Contributions] into or otherwise modifying a [Living Standard].
1. [Editors][Editor] also ensure that text of their [Living Standards][Living Standard] and [Review Drafts][def-review-draft] is tagged as required.

#### E. Relationships with other groups

1. [Editors][Editor] must respond to substantive issues raised by [Workstream Participants] in their [Workstreams][Workstream]. [Editors][Editor] have discretion to resolve issues based on available information.
1. If a [Workstream Participant][Workstream Participants] is not satisfied with an issue resolution, they may request that the [Editor] revisit the issue. If not satisfied with an [Editor]'s final response, [Workstream Participants] may appeal to the [Steering Group].
1. [Editors][Editor] may solicit input from [Workstream Participants], and may consider and respond to comments, suggestions, and objections from [Contributors][def-contributor] and the public.

#### F. Decision-making

1. [Editors][Editor] may commit changes to their [Living Standards][Living Standard] without further review, provided they are adhering to the requirements above.
1. The [Steering Group] may override an [Editor]'s decision, or remove an [Editor].

### 5.2. Workstream Participants

#### A. Prerequisites

[Workstream] participation is open to all.

#### B.

Each legal entity that participates in a [Workstream] must identify a single person to serve as primary contact with the [Steering Group] via the [Contributor and Workstream Participant Agreement]. [Entities][Entity] may change the primary contact using [the Workstream update interface](https://participate.whatwg.org/agreement-update).

#### C.

[Workstream Participants] specify which [Workstreams][Workstream] they are participating in via the [Contributor and Workstream Participant Agreement]. [Workstream Participants] may change the [Workstreams][Workstream] they participate in using [the Workstream update interface](https://participate.whatwg.org/agreement-update).

#### D.

[Workstream Participants] may participate in the development of [Living Standards][Living Standard] and provide input to
the [Editor] regarding adoption of [Contributions] and modifications to the [Living Standard].

#### E.

1. A [Workstream Participant][Workstream Participants] may discontinue participation in a [Workstream] at any time using [the Workstream update interface](https://participate.whatwg.org/agreement-update).

1. A [Workstream Participant][Workstream Participants] incurs no new obligations after a withdrawal or termination from a [Workstream], but obligations incurred up to that time (e.g., licensing obligations regarding [Contributions] and [Review Drafts][def-review-draft]) do not terminate.

#### F.

[Workstream Participants] may raise substantive issues for resolution by the [Steering Group] if not
resolved within the [Workstream] (e.g., [scope][Workstream Scope], direction, [Editor] decisions, and participation).

1. To raise an issue formally for review by the [Editor] and other [Workstream Participants], a [Workstream Participant][Workstream Participants] must:
   1. Identify the issue clearly (technical problem, interoperability issue, delta from [Workstream Scope], inconsistency with the [WHATWG Principles], etc.) and recommend a solution;
   1. Post the request for review in the [Workstream Repository]; and
   1. Endeavor to resolve the issue with the [Editor] or in concert with other [Workstream Participants].
1. If the [Workstream Participant][Workstream Participants] finds those efforts unsatisfactory, they may:
   1. Summarize the issue and the efforts to resolve it, and forward the summary and any supporting details to the [Steering Group], with a copy to the [Workstream] [Editor].
   1. The [Steering Group] may then invite the [Editor] and other [Workstream Participants] to comment, may request additional materials, schedule a meeting, or take other actions for its review.
1. The [Steering Group] will make its determination in its sole discretion.

#### G.

The [Steering Group] may remove a [Workstream Participant][Workstream Participants] [Entity] or individual.
For example, the [Steering Group] may remove a [Workstream Participant] for a violation of the WHATWG [Code of Conduct], for failure to comply with the [Contributor and Workstream Participant Agreement], or not complying with the [IPR Policy].
The [Steering Group]'s determination in each instance is final and non-appealable.

## 6. Publications

### 6.1. Notices

#### A. Living Standards

[Living Standards][Living Standard] must include the following notice, including the link:
> Copyright © YEAR WHATWG (Apple, Google, Mozilla, Microsoft). This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

In the text above, YEAR must be replaced by the current year at the time the [Living Standard] is published.

For each [Living Standard] that has had at least one [Review Draft][def-review-draft] published, it must also include the following notice:
> This is the Living Standard. Those interested in the patent-review version should view the Living
> Standard Review Draft.

In the text above, "Living Standard Review Draft" must link to the latest [Review Draft][def-review-draft].

#### B. Living Standard Review Drafts

[Living Standard Review Drafts][def-review-draft] must include the following notice, including the link:
> Copyright © YEAR WHATWG (Apple, Google, Mozilla, Microsoft). This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

In the text above, YEAR must be replaced by the current year at the time the [Living Standard Review Draft] is published.

In addition, [Living Standard Review Drafts][def-review-draft] must include the following notice:
> This is the Review Draft. It is published primarily for purposes of patent review by Workstream Participants; it mirrors the Living Standard closely, redacting only text that is identified as "Objection Pending" or "Confirmation Pending". Developers should refer to the Living Standard for the most current error corrections and other developments.
>
> For information regarding patent commitments, please see the IPR Policy and exclusion notices.

In the text above, "Living Standard" must link to the corresponding
[Living Standard], "IPR Policy" must link to the WHATWG [IPR Policy], and
"exclusion notices" must link to a location determined by the [Steering
Group] where patent exclusion notices are posted.

#### C. Source Code

Source Code published by the WHATWG bears text to be determined by the [Steering
Group].

#### D. Inanimate Standards

[Inanimate Standards] published by the WHATWG bear text to be determined on a
case-by-case basis by the [Steering Group].

#### E. Other Publications

[Other Publications] published by the WHATWG bear text to be determined by the
[Steering Group].

#### F. Repositories

The repositories for all WHATG publications and other deliverables
must include the text of the applicable license in a LICENSE file.

## 7. Antitrust

The WHATWG is a forum for voluntary development and promotion of standards, specifications,
technical requirements, code, best practices, and documentation for the web. No applicant
for participation in the WHATWG will be rejected for any anticompetitive purpose, and its
participants are free to join and participate freely in competing organizations and to develop and market competing
technologies, products, and services. Each participant in the WHATWG is responsible for
its compliance with all applicable laws, including antitrust and competition laws and
regulations, and must rely on independent legal counsel (and not any policy of the WHATWG)
regarding compliance. While participating in WHATWG activities, WHATWG participants should
not discuss any competitively sensitive, strategic commercial information in a way that
would be contrary to applicable competition laws. For example, such information may include
confidential, competitively sensitive information about business strategies, plans, or data
regarding sales, pricing, market share, marketing plans, business plans, and strategic
initiatives.

[def-contributor]: ./IPR%20Policy.md#def-contributor
[def-review-draft]: ./Workstream%20Policy.md#def-review-draft
[Code of Conduct]: https://whatwg.org/code-of-conduct
[Contributions]: ./IPR%20Policy.md#21-contribution
[Contributor and Workstream Participant Agreement]: https://participate-dot-whatwg-dot-org.now.sh/agreement
[Days]: ./IPR%20Policy.md#29-day
[Editor]: ./Workstream%20Policy.md#def-editor
[Entity]: https://participate-dot-whatwg-dot-org.now.sh/agreement#entity
[Inanimate Standards]: ./Workstream%20Policy.md#def-inanimate-standards
[IPR Policy]: ./IPR%20Policy.md
[Living Standard]: ./Workstream%20Policy.md#def-living-standard
[Other Publications]: ./Workstream%20Policy.md#def-other-publications
[Patent Exclusion Notice]: ./IPR%20Policy.md#27-patent-exclusion-notice
[Patent Exclusion Period]: ./IPR%20Policy.md#25-patent-exclusion-period
[Steering Group]: ./SG%20Agreement.md#def-steering-group
[Steering Group Member]: ./SG%20Agreement.md#def-steering-group-member
[Steering Group Policy]: ./SG%20Policy.md
[WHATWG Principles]: ./Principles.md
[Workstream]: ./Workstream%20Policy.md#def-workstream
[Workstream Participants]: ./Workstream%20Policy.md#def-workstream-participant
[Workstream Proposal]: ./Workstream%20Policy.md#def-workstream-proposal
[Workstream Repository]: ./Workstream%20Policy.md#def-workstream-repository
[Workstream Scope]: ./Workstream%20Policy.md#def-workstream-scope

<hr>

<small>Copyright © 2017 WHATWG (Apple, Google, Mozilla, Microsoft). This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).</small>
