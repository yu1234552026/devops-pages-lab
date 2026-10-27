---
layout: default
title: Release safety
---

# Release safety

## Technique: gated deployment

Each push to `main` runs three jobs in sequence: build, validate, deploy. Jekyll expands `index.md` with `{% raw %}{% include_relative README.md %}{% endraw %}`. The build artifact then passes to a separate validation job. The deploy job requires validation to succeed and publishes the same artifact without rebuilding it.

## What the gate checks

- Exactly one ordered pair of README activity markers exists.
- The homepage was generated and contains the activity heading.
- Liquid include instructions have been expanded.
- Each HTML document passes HTML structural validation using html-validate.
- Local links, asset references and fragment identifiers resolve inside the generated site.
- The homepage links to a stylesheet.

External links are not fetched by this gate. This avoids blocking releases because a third-party service is temporarily unavailable, but means external-link health needs separate monitoring.

## Deliberate failure

The manual `demonstrate_failure` option inserts a broken local link into the generated homepage before the artifact is uploaded. The same validator used for ordinary deployments rejects that artifact. The deploy job is skipped, so the existing live website remains available. No broken source file is merged and the next ordinary run builds cleanly.

## Limits and next steps

The gate detects the checks implemented here; it does not prove accessibility, factual accuracy or availability after deployment. A next improvement is to check `version.txt` on the live site against the deployed commit SHA, then add a versioned release asset for rollback. Those are future improvements and are not claimed as completed techniques.

[Back to the activity homepage](index.html)
