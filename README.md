# Hi, I'm yu1234552026

DevOps · GitHub Pages · Continuous delivery

This site turns my GitHub activity into a published page. Every release is built with Jekyll and checked before deployment.

## Recent activity
<!--START_SECTION:activity-->
1. 📝 Committed to main in [yu1234552026/devops-pages-lab](https://github.com/yu1234552026/devops-pages-lab/commit/f33a991abf7dc6af356fdef454f5b5431d58bdcd)
2. 📝 Committed to main in [yu1234552026/devops-pages-lab](https://github.com/yu1234552026/devops-pages-lab/commit/0947fb4c9be1cda0d9c639ef4a77f40033ac3355)
3. 📝 Committed to main in [yu1234552026/devops-pages-lab](https://github.com/yu1234552026/devops-pages-lab/commit/92f184b83842337ecac16be81d1c30af74922ff2)
4. 📝 Committed to main in [yu1234552026/devops-pages-lab](https://github.com/yu1234552026/devops-pages-lab/commit/acb8b9adbee233533bbab8d6a79185c230c5b94b)
5. 🎉 Created a new branch main in [yu1234552026/devops-pages-lab](https://github.com/yu1234552026/devops-pages-lab/tree/main)
6. 📝 Committed to master in [yu1234552026/activity-log](https://github.com/yu1234552026/activity-log/commit/576b0c017455e2e83cc8ea81267b1f074d89bce4)
7. 📝 Committed to master in [yu1234552026/activity-log](https://github.com/yu1234552026/activity-log/commit/fe71baea7f35930aa2ed2fdb587188c69418abda)
8. 📝 Committed to master in [yu1234552026/activity-log](https://github.com/yu1234552026/activity-log/commit/c0c156d26461834538a1a24ef8a477546c54433c)
9. 📝 Committed to master in [yu1234552026/activity-log](https://github.com/yu1234552026/activity-log/commit/3d353153c2ee294025b3d457d8c19ac8e794af15)
10. 📝 Committed to master in [yu1234552026/activity-log](https://github.com/yu1234552026/activity-log/commit/8dc330ea8f93558d0c45d34d7fec114ea2758b98)
<!--END_SECTION:activity-->

## Release safety

The pipeline builds the site, validates the README markers and generated HTML, and checks local links. Deployment depends on a successful validation job. A broken local link is used to demonstrate that the gate blocks an unsafe release.

## Project links

- [Source repository](https://github.com/yu1234552026/devops-pages-lab)
- [Workflow runs](https://github.com/yu1234552026/devops-pages-lab/actions)
- [Release safety notes](release-safety.html)

## Reproduce the demonstration

Run **Build, validate and deploy** manually with `demonstrate_failure` enabled. The build adds a link to a nonexistent local page. Validation must fail and deployment must be skipped. Run again with the option disabled to deploy a valid build. The demonstration never commits a broken link to the source.
