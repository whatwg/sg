# Stages

The WHATWG's "document reality" approach has been effective for nailing down [fundamental parts of the platform](https://spec.whatwg.org/) and improving interoperability and developer satisfaction. However, our process can sometimes be daunting for newcomers, who don't know how to reliably get implementer feedback or editor time commitment. This can discourage contributions, and it can lead to frustration when implementer/editor feedback arrives late in the process after the contributor feels "close to done".

The stage process described here is an additional tool designed to help provide a clear on-ramp for incubation efforts for contributors who aren't already editors, especially for additions to existing specs.  Stages are an optional, opt-in process that a feature proposer can use if they want to get more formal signals about how their feature is progressing. It asks for explicit implementer involvement at multiple stages, starting from notification that the problem is being worked on, then sign-off on the rough API and specification, and finally agreement on the full specification text. 

Stage signals are also useful to the broader community, helping developers monitor the proposals that are moving through the various stages.  By explicitly signaling a proposal's progress, including implementer involvement, the community has a better idea of what is going on in the WHATWG.

This tool is generally used for medium-to-large new features; it's not expected that explicit stage progression will be used for every feature.

# Details

This document formalizes some signal checkpoints for new features in existing WHATWG Living Standards. These checkpoints are modeled loosely on the [TC39 process](https://tc39.es/process-document/), which uses the concept of _stages_. Each subsequent stage implies a larger degree of consensus from the community, willingness to engage and/or implement and ship the feature in browser engines, and signals progress to web developers.  These checkpoints are not required for all features; this is simply a way to ensure that attention is appropriately drawn to incubations that have grown community support behind them.

## Terminology

* <dfn>Stage</dfn>: each successive stage is closer to a landed spec and interoperable implementation.  These stages are tracked on the issues in the relevant WHATWG GitHub repository, using labels ("stage 0", "stage 1", etc.)
* <dfn>Browser engine</dfn>: an independent implementation of the web platform (e.g. Chromium, WebKit and Gecko at present).
* <dfn>Implementation interest</dfn>: a direct signal from a browser engine that a feature is on the roadmap to implement, as defined in [working mode](https://whatwg.org/working-mode#additions)].
* <dfn>Browser engine representatives</dfn>: persons delegated by a browser engine to indicate implementation interest.
* <dfn>Proposal champion</dfn>: person/organization that proposed and will advance a feature through the stages, typically including writing the specification, researching use cases, and prototyping.

## Process

* Any proposal effectively starts at Stage 0 without any approvals, by a community member filing a new issue on a relevant WHATWG spec.
* In order to drive a proposal forward, it is expected that a community member will step up to champion the proposal, through answering questions asynchronously, providing feedback when requested, and consideration of important open questions at triage meetings.
* Stage level is tracked with labels on issues in the relevant specifications — “stage 0”, “stage 1”, etc.
* Stage labels (other than stage 0) should only be added by browser engine representatives, or by Editors on the relevant specification, after showing the necessary support for a level.
* **Advancing stages**
    * The feature champion should bring the proposal to the WHATWG to advance to the next stage by setting an “Agenda+” label on the tracking issue, and showing up to (or ensuring someone will show up to) the next triage meeting to discuss. Advancing to a new stage requires support for the decision by at least two implementers (via their browser engine representatives), and there should not be any strong implementer objections ([per the working mode](https://whatwg.org/working-mode#additions)). This support can also be gathered in any public manner, e.g. GitHub issue comments, triage meetings, etc. 
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
 <thead>
  <tr>
   <th>
Stage Name
   </th>
   <th>Entrance criteria
   </th>
   <th>This stage signifies
   </th>
   <th>Spec quality at entrance
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>Stage 0
<p>
(Proposal)
   </td>
   <td>(None)
   </td>
   <td><ul><li>That the proposer intends to use the stage process to work on their idea, with the goal of it landing in WHATWG Living Standard(s).</ul>
   </td>
   <td><ul><li>An explainer describing the  user/developer problem to be solved, including sketching use cases and scenarios. This explainer can exist anywhere, including e.g. a GitHub issue, or a personal repository.</ul>
   </td>
  </tr>
  <tr>
   <td>Stage 1
<p>
(Incubation)
   </td>
   <td><ul><li>A comprehensive explainer for the feature, in a standards organization-approved incubation venue such as a <a href="https://www.w3.org/community/groups/">W3C CG</a> or a branch of an existing WHATWG Standard.</li>
<li>Consensus that the WHATWG is interested in exploring solutions in this problem space.</li>
<li>(At least) one implementer interested in doing prototyping work.</li>
<li>Identification of the feature's champion.</li>
<li>Identification of a relevant WHATWG Workstream and Standard that will host the feature, and notification of the Workstream Editor(s).</li></ul>
   </td>
   <td>
<ul><li>Consensus that the problem is worth solving, and is within the scope of the WHATWG.</li>
<li>Commitment from the spec community to do work on the specification, which includes: review the spec and discussion about API improvements and adjustments.</li>
<li>The WHATWG commits to hosting a specification draft in a repository or branch (if the champion requests it).</li></ul>
   </td>
   <td><ul><li>The explainer follows the guidelines at <a href="https://tag.w3.org/explainers/">https://tag.w3.org/explainers/</a>.</li></ul>
   </td>
  </tr>
  <tr>
   <td>Stage 2
<p>
(Iteration)
   </td>
   <td><ul><li>A draft specification for the feature, in a standards organization-approved incubation venue (see stage 1).</li>
<li>Consensus that the rough API shape defined in the draft specification is the right approach to solve the problem, pending any significant problems found during this stage.</li></ul>
   </td>
   <td><ul><li>The WHATWG expects the feature to be developed and eventually included in the relevant WHATWG standard.</li>
<li>This stage also demonstrates commitment from the spec community to review the specification, and commitment from the champion to drive the addition of comprehensive tests, ideally with a prototype in at least one browser engine.</li></ul>
   </td>
   <td><ul><li>The draft specification uses Web IDL to define any new JavaScript APIs, roughly matches the style of the standard it's expected to merge into, and has a processing model, including full algorithms. However, there may be rough edges or TODOs in the processing model.</li></ul>
   </td>
  </tr>
  <tr>
   <td>Stage 3
<p>
(Committed)
   </td>
   <td><ul><li>Complete spec text.</li>
<li>Support of at least two implementers to land the feature in the standard, pending editorial revisions.</li>
<li>During this stage, a PR to the relevant WHATWG Living Standard will be created.</li></ul>
   </td>
   <td><ul><li>The solution is complete and no further work is possible without implementation experience, significant usage and external feedback.</li>
<li>Any substantial design changes from the spec draft after reaching this stage should be highlighted in a way that gives all involved browser engines a chance to comment.</li>
<li>An Editor of the relevant WHATWG Living Standard will perform a full review of the PR to add the feature, with an expectation of landing soon.</li></ul>
   </td>
   <td><ul><li>Spec is complete: all semantics, syntax and API are fully described. (It may still have small issues that will be identified by editor review during this stage.)</li>
<li>Full specification and comprehensive tests are completed; pull request template is filled out with all checkboxes checked.</li></ul>
   </td>
  </tr>
  <tr>
   <td>Stage 4 (Standard)
   </td>
   <td><ul><li>Editor’s comments on PR have all been resolved, and the PR for the feature has been merged by the Editor.</li></ul>
   </td>
   <td><ul><li>The PR has been approved to <a href="https://whatwg.org/working-mode#changes">change</a> a WHATWG Living Standard.</li></ul>
   </td>
   <td><ul><li>The feature is merged into the WHATWG Living Standard.</li></ul>
   </td>
  </tr>
 </tbody>
</table>