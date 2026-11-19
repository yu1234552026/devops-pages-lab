# Hi, I'm yu1234552026

DevOps · GitHub Pages · Continuous delivery

This site turns my GitHub activity into a published page. Every release is built with Jekyll and checked before deployment.

## Recent activity
<!--START_SECTION:activity-->
1. 📝 Committed to task2/security-verification-20261118 in [hambur0427/a10-leakguard](https://github.com/hambur0427/a10-leakguard/commit/d303b86061838f3e87e3903ad2a123a0c9c0b4d3)
2. 🎉 Created a new branch task2/security-verification-20261118 in [hambur0427/a10-leakguard](https://github.com/hambur0427/a10-leakguard/tree/task2/security-verification-20261118)
3. 🔀 Merged PR #13 in [hambur0427/a10-leakguard](https://github.com/hambur0427/a10-leakguard/pull/13)
4. 🗣 Commented on issue #6 in [hambur0427/a10-leakguard](https://github.com/hambur0427/a10-leakguard/issues/6#issuecomment-6955160462)
5. 🗣 Commented on issue #7 in [hambur0427/a10-leakguard](https://github.com/hambur0427/a10-leakguard/issues/7#issuecomment-6955161176)
6. 📥 Opened PR #13 in [hambur0427/a10-leakguard](https://github.com/hambur0427/a10-leakguard/pull/13)
7. Added [hambur0427/a10-leakguard](https://github.com/hambur0427/a10-leakguard)
8. 📝 Committed to main in [yu1234552026/a9-devsecops-lab](https://github.com/yu1234552026/a9-devsecops-lab/commit/349033a9f0f80512387ea7d6389eded13bfe27ea)
9. 📝 Committed to main in [yu1234552026/a9-devsecops-lab](https://github.com/yu1234552026/a9-devsecops-lab/commit/d467d0e3e754e287c4cb83088d057dc3b13cbe53)
10. 📝 Committed to main in [yu1234552026/a9-devsecops-lab](https://github.com/yu1234552026/a9-devsecops-lab/commit/2bcc5bd37bd2bf8b8e0ea1d407c1c89122fd4a76)
<!--END_SECTION:activity-->

## Release safety

The pipeline builds the site, validates the README markers and generated HTML, and checks local links. Deployment depends on a successful validation job. A broken local link is used to demonstrate that the gate blocks an unsafe release.

## Project links

- [Source repository](https://github.com/yu1234552026/devops-pages-lab)
- [Workflow runs](https://github.com/yu1234552026/devops-pages-lab/actions)
- [Release safety notes](release-safety.html)

## Reproduce the demonstration

Run **Build, validate and deploy** manually with `demonstrate_failure` enabled. The build adds a link to a nonexistent local page. Validation must fail and deployment must be skipped. Run again with the option disabled to deploy a valid build. The demonstration never commits a broken link to the source.
