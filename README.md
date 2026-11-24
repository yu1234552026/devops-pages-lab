# Hi, I'm yu1234552026

DevOps · GitHub Pages · Continuous delivery

This site turns my GitHub activity into a published page. Every release is built with Jekyll and checked before deployment.

## Recent activity
<!--START_SECTION:activity-->
1. 🗣 Commented on a review of PR #18 in [hambur0427/a10-leakguard](https://github.com/hambur0427/a10-leakguard/pull/18#pullrequestreviewcomment-4682628461)
2. 🗣 Commented on a review of PR #17 in [hambur0427/a10-leakguard](https://github.com/hambur0427/a10-leakguard/pull/17#pullrequestreviewcomment-4682402443)
3. 🗣 Commented on a review of PR #17 in [hambur0427/a10-leakguard](https://github.com/hambur0427/a10-leakguard/pull/17#pullrequestreviewcomment-4682402432)
4. 🔀 Merged PR #18 in [hambur0427/a10-leakguard](https://github.com/hambur0427/a10-leakguard/pull/18)
5. ❌ Closed issue #15 in [hambur0427/a10-leakguard](https://github.com/hambur0427/a10-leakguard/issues/15)
6. 🔎 Updated PR #17 in [hambur0427/a10-leakguard](https://github.com/hambur0427/a10-leakguard/pull/17#pullrequestreview-6042296563)
7. 🔎 Created PR #18 in [hambur0427/a10-leakguard](https://github.com/hambur0427/a10-leakguard/pull/18#pullrequestreview-6042591730)
8. 🔎 Created PR #18 in [hambur0427/a10-leakguard](https://github.com/hambur0427/a10-leakguard/pull/18#pullrequestreview-6042590796)
9. 📥 Opened PR #18 in [hambur0427/a10-leakguard](https://github.com/hambur0427/a10-leakguard/pull/18)
10. 🔎 Created PR #17 in [hambur0427/a10-leakguard](https://github.com/hambur0427/a10-leakguard/pull/17#pullrequestreview-6042296563)
<!--END_SECTION:activity-->

## Release safety

The pipeline builds the site, validates the README markers and generated HTML, and checks local links. Deployment depends on a successful validation job. A broken local link is used to demonstrate that the gate blocks an unsafe release.

## Project links

- [Source repository](https://github.com/yu1234552026/devops-pages-lab)
- [Workflow runs](https://github.com/yu1234552026/devops-pages-lab/actions)
- [Release safety notes](release-safety.html)

## Reproduce the demonstration

Run **Build, validate and deploy** manually with `demonstrate_failure` enabled. The build adds a link to a nonexistent local page. Validation must fail and deployment must be skipped. Run again with the option disabled to deploy a valid build. The demonstration never commits a broken link to the source.
