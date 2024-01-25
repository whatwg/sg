# Stages - tool for encouraging attention to incubation features

## What problems are we trying to solve?

The WHATWG has historically operated in a very lightweight, minimal-process fashion. This works very well in some cases, especially when implementers and editors are all engaged. However, we've found that it can be problematic for newcomers, who don't know how to reliably get implementer feedback or editor time commitment. This can discourage contributions, and it can lead to frustration when implementer/editor feedback arrives late in the process after the contributor feels "close to done".

The WHATWG's "document reality" approach has been effective for nailing down HTML, DOM, XHR, and similar fundamental parts of the platform and improving interoperability and developer satisfaction. Additionally, when enthusiastic editors have been involved, new APIs for developers have been effectively incubated within WHATWG, with speculative text included in living standards even before multiple implementations were created. (For example: Fetch, Storage, Encoding, and URL.) But there is not a clear on-ramp for incubation efforts for contributors who aren't already editors, especially for additions to existing specs.

The stage process described here is an optional, opt-in process that a feature proposer can use if they want to get more formal signals about how their feature is progressing. It asks for explicit implementer involvement at multiple stages, starting from notification that the problem is being worked on, then sign-off on the rough API and specification, and finally agreement on the full specification text. This can be more helpful than the current practice of using a single boolean checkbox for implementer interest, which implementers usually are unwilling to hand out until the very end. Like with the previous practice, if not enough implementers agree to work on a problem, the proposer can keep incubating their idea outside of the WHATWG, including by shipping it speculatively in a browser.

These sorts of explicit signals are also useful to the broader community, not just to the contributor. JavaScript developers are very keenly aware of what is making its way through TC39. They do this by monitoring the proposals that are moving through the various stages, tweeting about stage advancements, giving talks about upcoming stage 2 proposals, etc. By explicitly signaling a proposal's progress, including implementer involvement, the community will have a better idea of what is going on in WHATWG-land.

This is generally used for medium-to-large new features; it's not expected that it will be used for every feature.

# Details

This document formalizes some signal checkpoints for new features in existing WHATWG specs. These checkpoints are modeled loosely on the [TC39 process](https://tc39.es/process-document/), which uses the concept of _stages_. Each subsequent stage implies a larger degree of consensus from the community, willingness to engage, and/or intent to implement and ship the feature in browser engines, and signals progress to web developers.  These checkpoints are not required for all features; this is simply a way to ensure that attention is appropriately drawn to incubations that have grown community support behind them.

Terminology:

* _Stage_: each successive stage is closer to a landed spec and interoperable implementation.  These stages are tracked on the issues in the relevant WHATWG Github repository, using labels ("stage 0", "stage 1", etc.)
* _Browser engine_: an independent implementation of the web platform (e.g. Chromium, WebKit and Gecko at present).
* _Implementation interest_: a direct signal from a browser engine that a feature is on the roadmap to implement [Ed: same as in [current process](https://whatwg.org/working-mode#additions)].
* _Browser engine representatives_: persons delegated by a browser engine to indicate implementation interest.
* _Proposal champion_: person/organization that proposed and will advance a feature through the stages, typically including writing the specification, researching use cases, and prototyping.

Process:

* Any proposal effectively starts at Stage 0 without any approvals, by a community member filing a new issue on a relevant WHATWG spec.
* In order to drive a proposal forward, it is expected that a community member will step up to champion the proposal, through answering questions asynchronously, providing feedback when requested, and consideration of important open questions at triage meetings.
* Stage level is tracked with labels on issues in the relevant specifications — “stage 0”, “stage 1”, etc.
* Stage labels (other than stage 0) should only be added by browser engine representatives, or by Editors on the relevant specification, after showing the necessary support for a level.
* **Advancing stages**
    * The feature champion should bring the proposal to the WHATWG to advance to the next stage by setting an “Agenda+” label on the tracking issue, and showing up to (or ensuring someone will show up to) the next triage meeting to discuss. Advancing to a new stagerequires support for the decision by at least two implementers (via their browser engine representatives), and there should not be any strong implementer objections ([per the working mode](https://whatwg.org/working-mode#additions)). This support can also be gathered in any public manner, e.g. GitHub issue comments, triage meetings, etc. 
    * Positive support to advance a stage does **not** imply:
        * Commitment to eventually support a subsequent stage
        * That the particular solution approach at the time of the signal or support will be the one eventually standardized (unless the advancement is to the Standardized stage)
    * A negative response to advancing a stage does **not** imply:
        * That the feature cannot continue in its current stage
        * That a future request for support to advance a stage with a revised solution won’t succeed
        * That all browsers will delay shipping the feature
        * That the feature cannot continue to be incubated outside of the WHATWG
    * A proposal can advance directly to later stages without going through the earlier stages, if it's already mature enough and has sufficient support to do so.
* **Regressing stages**
    * The browser engine representatives may review proposals and decide to regress stages—for example, if implementer support has been retracted for a particular solution (regressing from stage 3 to stage 2), or even if support has been retracted for solving the problem (i.e. a regression from stage 2 to stage 1). This situation is expected to be unusual, and should come with a very strong justification.

<table>
  <tr>
   <td>
Stage Name
   </td>
   <td>Entrance criteria
   </td>
   <td>This stage signifies
   </td>
   <td>Spec quality at entrance
   </td>
  </tr>
  <tr>
   <td>Stage 0
<p>
(Proposal)
   </td>
   <td>(None)
   </td>
   <td>That the proposer intends to use the stage process to work on their idea, with the goal of it landing in WHATWG Living Standard(s).
   </td>
   <td>An explainer describing the  user/developer problem to be solved, including sketching use cases and scenarios. This explainer can exist anywhere, including e.g. a GitHub issue, or a personal repository.
   </td>
  </tr>
  <tr>
   <td>Stage 1
<p>
(Incubation)
   </td>
   <td>A comprehensive explainer for the feature, in a standards organization-approved incubation venue such as a <a href="https://www.w3.org/community/groups/">W3C CG</a> or a branch of an existing WHATWG Standard.
<p>
Consensus that the WHATWG is interested in exploring solutions in this problem space.
<p>
(At least) one implementer interested in doing prototyping work.
<p>
Identification of the feature's champion. \
 \
Identification of a relevant WHATWG Workstream and Standard that will host the feature, and notification of the Workstream Editor(s).
   </td>
   <td>Consensus that the problem is worth solving, and is within the scope of the WHATWG.
<p>
Commitment from the spec community to do work on the specification, which includes: review the spec and discussion about API improvements and adjustments. \
 \
The WHATWG commits to hosting a specification draft in a repository or branch (if the champion requests it).
   </td>
   <td>The explainer follows the guidelines at <a href="https://tag.w3.org/explainers/">https://tag.w3.org/explainers/</a>.
   </td>
  </tr>
  <tr>
   <td>Stage 2
<p>
(Iteration)
   </td>
   <td>A draft specification for the feature, in a standards organization-approved incubation venue (see stage 1).
<p>
Consensus that the rough API shape defined in the draft specification is the right approach to solve the problem, pending any significant problems found during this stage.
   </td>
   <td>The WHATWG expects the feature to be developed and eventually included in the relevant WHATWG standard.
<p>
This stage also demonstrates commitment from the spec community to review the specification, and commitment from the champion to drive the addition of comprehensive tests, ideally with a prototype in at least one browser engine. \

   </td>
   <td>The draft specification uses Web IDL to define any new JavaScript APIs, roughly matches the style of the standard it's expected to merge into, and has a processing model, including full algorithms. However, there may be rough edges or TODOs in the processing model.
   </td>
  </tr>
  <tr>
   <td>Stage 3
<p>
(Committed)
   </td>
   <td>Complete spec text.
<p>
Support of at least two implementers to land the feature in the standard, pending editorial revisions.
<p>
During this stage, a PR to the relevant WHATWG Living Standard will be created.
   </td>
   <td>The solution is complete and no further work is possible without implementation experience, significant usage and external feedback.
<p>
Any substantial design changes from the spec draft after reaching this stage should be highlighted in a way that gives all involved browser engines a chance to comment.
<p>
An Editor of the relevant WHATWG Living Standard will perform a full review of the PR to add the feature, with an expectation of landing soon.
   </td>
   <td>Spec is complete: all semantics, syntax and API are fully described. (It may still have small issues that will be identified by editor review during this stage.)
<p>
Full specification and comprehensive tests are completed; pull request template is filled out with all checkboxes checked.
   </td>
  </tr>
  <tr>
   <td>Stage 4 (Standard)
   </td>
   <td>Editor’s comments on PR have all been resolved, and the PR for the feature has been merged by the Editor.
   </td>
   <td>The PR has been approved to <a href="https://whatwg.org/working-mode#changes">change</a> a WHATWG Living Standard.
   </td>
   <td>The feature is merged into the WHATWG Living Standard.
   </td>
  </tr>
</table>