# WHATWG Stages

**See [all features using the Stages process](https://github.com/search?q=org%3Awhatwg+label%3A%22stage%3A+1%22%2C%22stage%3A+2%22%2C%22stage%3A+3%22%2C%22stage%3A+4%22&type=issues) and their current states.**

The WHATWG's approach to "documenting reality" is ideal for nailing down [fundamental parts of the platform](https://spec.whatwg.org/) and improving interoperability and developer satisfaction. It can sometimes be daunting for new [Contributors](./IPR%20Policy.md#contributor), who don't know how to reliably get implementer feedback or editor time commitment. The WHATWG Stages process is an optional, opt-in process that both new and established [Contributors](./IPR%20Policy.md#contributor) can use if they want to get more formal signals on support for their [Contribution](./IPR%20Policy.md#21-contribution). This tool is generally used for medium-to-large [Contributions](./IPR%20Policy.md#21-contribution); it's not expected to be used for each [Contribution](./IPR%20Policy.md#21-contribution).

Stages asks for explicit implementer involvement at multiple checkpoints, starting from notification that the problem is being worked on, then sign-off on the rough API and specification, and finally agreement on the full specification text. These checkpoints are also useful to the broader community, helping web developers monitor the [Contributions](./IPR%20Policy.md#21-contribution) that are moving through the various stages. By explicitly signaling a [Contribution](./IPR%20Policy.md#21-contribution)'s progress, including implementer involvement, the community has a better idea of what is going on in the WHATWG.

These checkpoints are modeled loosely on the [TC39 process](https://tc39.es/process-document/), which uses the concept of _stages_. Each subsequent stage implies a larger degree of consensus from the community, willingness to engage, implement, and eventually ship the feature in browser engines; and signals progress to web developers, drawing attention to incubations that have grown community support behind them.

## Terminology

* <dfn>Stage</dfn>: each successive stage is closer to an integrated [Contribution](./IPR%20Policy.md#21-contribution) and interoperable implementation. These stages are tracked on the issues in the relevant WHATWG GitHub repository, using labels ("stage 0", "stage 1", etc.). The stages are described in the Stages overview below.
* <dfn>Browser engine</dfn>: an independent implementation of the web platform (i.e., Chromium, Gecko, and WebKit at present).
* <dfn>Implementation interest</dfn>: a direct signal from a browser engine that a feature is on the roadmap to implement, as defined in the [Working Mode](./Working%20Mode.md#additions).
* <dfn>Browser engine representatives</dfn>: persons delegated by a browser engine to indicate implementer interest.

## Process

* Any [Contribution](./IPR%20Policy.md#21-contribution) effectively starts at Stage 0 without any approvals, by a community member filing a new issue on a relevant WHATWG standard.
* It is expected that the [Contributor](./IPR%20Policy.md#contributor) will champion the [Contribution](./IPR%20Policy.md#21-contribution), through answering questions asynchronously, providing feedback when requested, and consideration of important open questions at triage meetings.
* Anyone can review and submit feedback on [Contributions](./IPR%20Policy.md#21-contribution).
* Stage level is tracked with labels on issues on the relevant standard — “stage 0”, “stage 1”, etc.
* Stage labels (other than stage 0) should only be added by browser engine representatives, or by Editors of the relevant standard, once necessary support for a level has been demonstrated.
* This process is subject to and governed by [WHATWG Policies](./Policies.md), including the [Intellectual Property Rights Policy](./IPR%20Policy.md).
* **Advancing stages**
    * The [Contributor](./IPR%20Policy.md#contributor) should bring the [Contribution](./IPR%20Policy.md#21-contribution) to the WHATWG to advance to the next stage by setting an “Agenda+” label on the tracking issue, and showing up to (or ensuring someone will show up to) the next triage meeting to discuss. Advancing to a new stage requires support for the decision by at least two implementers (via their browser engine representatives), and there should not be any strong implementer objections ([per the working mode](./Working%20Mode.md#additions)). This support can also be gathered in any public manner, e.g., GitHub issue comments, triage meetings, etc. 
    * Positive support to advance a stage does **not** imply:
        * Commitment to eventually support a subsequent stage.
        * That the particular solution approach at the time of the signal or support will be the one eventually standardized (unless the advancement is to the Standardized stage).
    * A negative response to advancing a stage does **not** imply:
        * That the [Contribution](./IPR%20Policy.md#21-contribution) cannot continue in its current stage.
        * That a future request for support to advance a stage with a revised solution won’t succeed.
        * That all browsers will delay shipping the feature.
        * That the feature cannot continue to be incubated outside of the WHATWG.
    * A [Contribution](./IPR%20Policy.md#21-contribution) can advance directly to later stages without going through the earlier stages, if it's already mature enough and has sufficient support to do so.
* **Regressing stages**
    * The browser engine representatives may review [Contributions](./IPR%20Policy.md#21-contribution) and decide to regress stages — for example, if implementer support has been retracted for a particular solution (regressing from stage 3 to stage 2), or even if support has been retracted for solving the problem (i.e., a regression from stage 2 to stage 1). This situation is expected to be unusual, and should come with a very strong justification.

## Stages overview

<table>
 <thead>
  <tr>
   <th>Name
   <th>Entrance criteria
   <th>This stage signifies
   <th>Specification quality at entrance
 </thead>
 <tbody>
  <tr id="stage0">
   <td>Stage 0<a class="self-link" href="#stage0"></a><br>(Proposal)
   <td>—
   <td>
    <ul>
     <li>That the proposer intends to use the stage process to work on their idea, with the goal of it landing in WHATWG Living Standard(s).
    </ul>
   <td>
    <ul>
     <li>An explainer describing the problem to be solved, including sketching use cases and scenarios. This explainer can exist anywhere, including in a GitHub issue or a personal repository.
    </ul>
  <tr id="stage1">
   <td>Stage 1<a class="self-link" href="#stage1"></a><br>(Incubation)
   <td>
    <ul>
     <li>A comprehensive explainer for the <a href="./IPR%20Policy.md#21-contribution">Contribution</a>, in a standards organization-approved incubation venue such as a <a href="https://www.w3.org/community/groups/">W3C CG</a> or a branch of an existing WHATWG Standard.
     <li>Consensus that the WHATWG is interested in exploring solutions in this problem space.
     <li>(At least) one implementer interested in doing prototyping work.
     <li>Identification of the <a href="./IPR%20Policy.md#contributor">Contributor</a>.
     <li>Identification of a relevant WHATWG Workstream and Standard that will host the <a href="./IPR%20Policy.md#21-contribution">Contribution</a>, and notification of the Workstream Editor(s).
    </ul>
   <td>
    <ul>
     <li>Consensus that the problem is worth solving, and is within the scope of the WHATWG.
     <li>Commitment from the community to do work on the specification, which includes: review the specification and discussion about API improvements and adjustments.
     <li>The WHATWG commits to hosting a specification draft in a repository or branch (if the <a href="./IPR%20Policy.md#contributor">Contributor</a> requests it).
    </ul>
   <td>
    <ul>
     <li>The explainer follows the guidelines at <a href="https://tag.w3.org/explainers/">https://tag.w3.org/explainers/</a>.
    </ul>
  <tr id="stage2">
   <td>Stage 2<a class="self-link" href="#stage2"></a><br>(Iteration)
   <td>
    <ul>
     <li>A draft specification for the <a href="./IPR%20Policy.md#21-contribution">Contribution</a>, in a standards organization-approved incubation venue (see stage 1).
     <li>Consensus that the rough API shape defined in the draft specification is the right approach to solve the problem, pending any significant problems found during this stage.
    </ul>
   <td>
    <ul>
     <li>The WHATWG expects the <a href="./IPR%20Policy.md#21-contribution">Contribution</a> to be developed and eventually included in the relevant WHATWG standard.
     <li>This stage also demonstrates commitment from the community to review the specification, and commitment from the <a href="./IPR%20Policy.md#contributor">Contributor</a> to drive the addition of comprehensive tests, ideally with a prototype in at least one browser engine.
    </ul>
   <td>
    <ul>
     <li>The draft specification uses Web IDL to define any new JavaScript APIs, roughly matches the style of the standard it's expected to merge into, and has a processing model, including full algorithms. However, there may be rough edges or TODOs in the processing model.
    </ul>
  <tr id="stage3">
   <td>Stage 3<a class="self-link" href="#stage3"></a><br>(Committed)
   <td>
    <ul>
     <li>Complete specification text.
     <li>Support of at least two implementers to land the <a href="./IPR%20Policy.md#21-contribution">Contribution</a> in the standard, pending editorial revisions.
     <li>During this stage, a PR to the relevant WHATWG Living Standard will be created.
    </ul>
   <td>
    <ul>
     <li>The solution is complete and no further work is possible without implementation experience, significant usage and external feedback.
     <li>Any substantial design changes from the specification draft after reaching this stage should be highlighted in a way that gives all involved browser engines a chance to comment.
     <li>An Editor of the relevant WHATWG Living Standard will perform a full review of the pull request to add the <a href="./IPR%20Policy.md#21-contribution">Contribution</a>, with an expectation of landing soon.
    </ul>
   <td>
    <ul>
     <li>Specification is complete: all data structures, processing model, and API are fully described. (It may still have small issues that will be identified by editor review during this stage.)
     <li>Full specification and comprehensive tests are completed; pull request template is filled out with all checkboxes checked.
    </ul>
  <tr id="stage4">
   <td>Stage 4<a class="self-link" href="#stage4"></a><br>(Standard)  
   <td>
    <ul>
     <li>Editor’s comments on the pull request have all been resolved, and the pull request for the <a href="./IPR%20Policy.md#21-contribution">Contribution</a> has been merged by the Editor.
    </ul>
   <td>
    <ul>
     <li>The pull request has been approved to <a href="https://whatwg.org/working-mode#changes">change</a> a WHATWG Living Standard.
    </ul>
   <td>
    <ul>
     <li>The <a href="./IPR%20Policy.md#21-contribution">Contribution</a> is merged into the WHATWG Living Standard.
    </ul>
 </tbody>
</table>
