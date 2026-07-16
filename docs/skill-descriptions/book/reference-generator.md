# Reference Generator

## Overview

The `reference-generator` skill creates exactly 10 curated references for each
textbook chapter. It stores them in a separate `references.md` file beside the
chapter, links that file from the chapter, and adds it to the chapter's MkDocs
navigation.

The fixed structure keeps the output predictable and maintainable:

1. References 1-3 are relevant Wikipedia articles.
2. References 4-5 are authoritative textbooks without URLs.
3. References 6-10 are verified online resources.

## When to Use

Use this skill when:

- Creating references for a new intelligent textbook
- Adding missing references to existing chapters
- Replacing inline chapter references with maintainable reference files
- Updating or repairing a chapter's curated source list

Run it after chapter content is finalized so the references can match the
chapter's actual concepts and learning objectives.

## Output Contract

For every chapter, the skill produces:

```text
docs/chapters/<chapter-slug>/
|-- index.md
`-- references.md
```

The `references.md` file contains exactly 10 numbered entries. The chapter's
`index.md` ends with one link:

```markdown
[See Annotated References](./references.md)
```

The chapter entry in `mkdocs.yml` includes the reference page as a child:

```yaml
- 1. Chapter Name:
  - Content: chapters/01-chapter-name/index.md
  - Annotated References: chapters/01-chapter-name/references.md
```

If a chapter already has an inline `## References` section, replace that section
with the single annotated-references link. Do not preserve two competing copies.

## Reference Positions

### Positions 1-3: Wikipedia

Choose substantial Wikipedia articles covering the chapter's central concepts.
These entries provide accessible, stable overviews and useful paths to related
material.

```markdown
1. [Concept Name](https://en.wikipedia.org/wiki/Concept_Name) - Wikipedia - Description of what the article covers and why it supports this chapter.
```

### Positions 4-5: Authoritative Textbooks

Use widely respected textbooks that cover the chapter topic in depth. Record the
title, edition when relevant, author, publisher, and a concise relevance note.
Do not add URLs to these entries; publisher and retailer links are more likely to
move or disappear.

```markdown
4. Textbook Title (Edition) - Author Name - Publisher - Description of the chapters or teaching approach that make this book useful here.
```

### Positions 6-10: Verified Online Resources

Use reputable tutorials, courses, documentation, or educational resources that
complement rather than repeat the Wikipedia entries. Verify each URL before
including it.

```markdown
6. [Resource Title](https://verified.example/resource) - Publisher - Description of the resource and its specific relevance to the chapter.
```

## Workflow

### 1. Read the Course Context

Read `docs/course-description.md` to understand:

- Subject matter
- Target audience
- Learning objectives

The audience influences the explanations and source selection, but not the
quantity: every chapter receives exactly 10 references.

### 2. Inspect the Chapters

List the chapter directories under `docs/chapters/`. Read each chapter's
`index.md` and identify its title, principal concepts, and objectives.

By default, process every chapter. When a user or invoking workflow supplies
specific chapter paths, process only those chapters.

### 3. Curate the Fixed Source Mix

Create 10 references in the required position groups. Avoid duplicate sources
within a chapter. Keep each relevance description between 20 and 40 words and
explain both what the resource covers and why it belongs in this chapter.

### Quality Criteria

- Wikipedia articles should be substantial rather than stubs, cover primary
  concepts, include useful diagrams, examples, or formulas, and link to related
  topics a learner may explore.
- Textbooks should be widely used, reputable, reasonably accessible, and cover
  the chapter's concepts in depth.
- Online resources should come from reputable educational or technical sources,
  provide practical examples or exercises, and complement rather than duplicate
  the Wikipedia entries.
- Relevance descriptions should name concrete features such as examples,
  exercises, or visualizations when those features are present.

Use domain-appropriate official documentation, educational institutions, and
reputable technical publishers as starting points. Named source lists are not a
substitute for checking relevance and the live URL.

### 4. Verify Online Links

Verify references 6-10 against the live pages before writing them. Replace dead,
misdirected, or inaccessible links with stronger sources.

### 5. Write the Chapter Reference File

Create `docs/chapters/<chapter-slug>/references.md` with this shape:

```markdown
# References: Chapter Title

1. [Wikipedia Article](https://en.wikipedia.org/wiki/Topic) - Wikipedia - Relevance description.
2. [Wikipedia Article](https://en.wikipedia.org/wiki/Topic_2) - Wikipedia - Relevance description.
3. [Wikipedia Article](https://en.wikipedia.org/wiki/Topic_3) - Wikipedia - Relevance description.
4. Textbook Title - Author - Publisher - Relevance description.
5. Textbook Title - Author - Publisher - Relevance description.
6. [Online Resource](https://example.com/resource) - Publisher - Relevance description.
7. [Online Resource](https://example.com/resource-2) - Publisher - Relevance description.
8. [Online Resource](https://example.com/resource-3) - Publisher - Relevance description.
9. [Online Resource](https://example.com/resource-4) - Publisher - Relevance description.
10. [Online Resource](https://example.com/resource-5) - Publisher - Relevance description.
```

### 6. Link the Chapter

Remove any inline `## References` section from the chapter and add the single
annotated-references link at the end.

### 7. Update Navigation Serially

By default, read the current `mkdocs.yml` immediately before editing. Collect
every reference-page navigation change owned by this run, then apply them in ONE
edit at the end. Follow the canonical rules in
`skills/book-installer/references/mkdocs-nav-editing.md`; do not let parallel
agents edit the same navigation file.

When an invoking workflow explicitly owns the navigation update, defer
navigation: do not edit `mkdocs.yml`. Return the complete `Annotated References`
entries so the caller can include them in its serialized edit.

### 8. Validate and Report

Before finishing, verify:

- Every chapter has exactly 10 entries
- Entries 1-3 are Wikipedia articles
- Entries 4-5 are textbooks without URLs
- Entries 6-10 have verified online URLs
- Each description explains chapter relevance in 20-40 words
- Each chapter links its reference file
- Each reference file appears in `mkdocs.yml`

Report the number of chapters processed, any URLs that could not be verified,
confirmation that navigation was updated, and a reminder to verify the site with
`mkdocs serve`.

## Why Separate Files

Per-chapter `references.md` files keep reference maintenance independent from
chapter prose. An agent can inspect or update a small reference file without
loading a full chapter, and repository tools can discover all reference files
with one glob. This is the only supported placement mode for this skill.

## Related Skills

- `course-description-analyzer` supplies audience and learning context.
- `chapter-content-generator` creates the chapter content references support.
- `book-installer` owns the canonical MkDocs navigation-editing rules.
- `book-installer` includes the `book-metrics` workflow that counts per-chapter
  reference files and entries.
