# Hi, I'm yu1234552026

DevOps · GitHub Pages · Continuous delivery

This site turns my GitHub activity into a published page. Every release is built with Jekyll and checked before deployment.

## Recent activity
<!--START_SECTION:activity-->
1. 🗣 Commented on issue #6 in [hambur0427/a10-leakguard](https://github.com/hambur0427/a10-leakguard/issues/6#issuecomment-6955160462)
2. 🗣 Commented on issue #7 in [hambur0427/a10-leakguard](https://github.com/hambur0427/a10-leakguard/issues/7#issuecomment-6955161176)
3. 📥 Opened PR #13 in [hambur0427/a10-leakguard](https://github.com/hambur0427/a10-leakguard/pull/13)
4. Added [hambur0427/a10-leakguard](https://github.com/hambur0427/a10-leakguard)
5. 📝 Committed to main in [yu1234552026/a9-devsecops-lab](https://github.com/yu1234552026/a9-devsecops-lab/commit/349033a9f0f80512387ea7d6389eded13bfe27ea)
6. 📝 Committed to main in [yu1234552026/a9-devsecops-lab](https://github.com/yu1234552026/a9-devsecops-lab/commit/d467d0e3e754e287c4cb83088d057dc3b13cbe53)
7. 📝 Committed to main in [yu1234552026/a9-devsecops-lab](https://github.com/yu1234552026/a9-devsecops-lab/commit/2bcc5bd37bd2bf8b8e0ea1d407c1c89122fd4a76)
8. 🎉 Created a new branch main in [yu1234552026/a9-devsecops-lab](https://github.com/yu1234552026/a9-devsecops-lab/tree/main)
9. 📝 Committed to main in [yu1234552026/a9-devsecops-lab](https://github.com/yu1234552026/a9-devsecops-lab/commit/28d07ccffda9c817188812cfcb2178c78637b5f2)
10. 📝 Committed to main in [yu1234552026/a9-devsecops-lab](https://github.com/yu1234552026/a9-devsecops-lab/commit/cce6acb2a5948b0f2c74c1ad746c4b13facbc235)
<!--END_SECTION:activity-->

## Release safety

The pipeline builds the site, validates the README markers and generated HTML, and checks local links. Deployment depends on a successful validation job. A broken local link is used to demonstrate that the gate blocks an unsafe release.

## Project links

- [Source repository](https://github.com/yu1234552026/devops-pages-lab)
- [Workflow runs](https://github.com/yu1234552026/devops-pages-lab/actions)
- [Release safety notes](release-safety.html)

## Reproduce the demonstration

Run **Build, validate and deploy** manually with `demonstrate_failure` enabled. The build adds a link to a nonexistent local page. Validation must fail and deployment must be skipped. Run again with the option disabled to deploy a valid build. The demonstration never commits a broken link to the source.
