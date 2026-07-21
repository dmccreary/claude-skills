# Reference Generator

## Overview

The reference-generator skill generates curated reference lists for educational textbook chapters. Every chapter receives exactly **10 references**, stored in a separate `references.md` file per chapter for token-efficient maintenance.

References are never just a list of Wikipedia links. The reference set is split across three roles: Wikipedia articles for reliable overviews, textbooks that credit the specific authors behind influential explanations, and verified online resources for practical depth.

## Purpose

This skill automates the creation of high-quality, curated reference lists that enhance textbook credibility, point students toward deeper learning, and — distinctively — give credit to the textbook authors who pioneered the clearest or most influential way of teaching each chapter's concepts.

## Key Features

- **Exactly 10 References Per Chapter**: consistent structure across every chapter
- **Wikipedia First**: references 1-3, for stable, reliable overviews
- **Credited Textbook Authors**: references 4-5, naming the author behind a specific innovative analogy, derivation, notation, or diagram — not just "an authoritative textbook"
- **Verified Online Resources**: references 6-10, tutorials and courses with working links checked via WebFetch
- **Separate Reference Files**: `references.md` per chapter, keeping chapter edits cheap and references batch-processable

## When to Use

Use this skill when:

- Creating a new intelligent textbook that needs chapter references
- Adding references to an existing textbook
- Updating or expanding references for educational content
- A user explicitly requests reference generation

## Reference Structure (10 Per Chapter)

### References 1-3: Wikipedia Articles

Chosen for the chapter's primary concepts — substantial articles (not stubs) with diagrams, examples, or formulas.

### References 4-5: Textbooks Crediting Innovative Authors

These two slots exist specifically to credit people, not just cite sources. For each chapter's key concepts, identify the author most associated with an innovative or influential way of teaching it — a distinctive analogy, derivation, notation, worked example, or diagram that other authors have since adopted, or that students consistently find clarifying. The description must name the specific innovation, e.g.:

> *Textbook Title (Edition) — Author Name — Publisher — Author Name pioneered [specific analogy/derivation/notation] for [concept], now widely adopted because [why it clarifies the idea].*

If no single author stands out as the originator of a distinctive approach, choose the textbook most often praised in reviews, syllabi, or educator discussion for making the concept unusually clear — and say so explicitly rather than defaulting to a generic "authoritative textbook" citation. No URLs (they break); title, author, publisher only.

### References 6-10: Online Resources

Verified tutorials, courses, and educational sites that complement (not duplicate) the Wikipedia references. Every URL is checked with WebFetch before inclusion.

## Workflow Steps

### Step 1: Analyze the Course Description

Read `/docs/course-description.md` for subject matter, target audience, and learning objectives.

### Step 2: Identify Chapter Structure

```bash
ls docs/chapters/
```

For each chapter, read `index.md` for title, key concepts, and learning objectives.

### Step 3: Generate 10 References Per Chapter

Follow the 1-3 / 4-5 / 6-10 structure above.

### Step 4: Verify Online URLs

For references 6-10:

```python
WebFetch(url=reference_url, prompt="Is this page accessible? What is the main topic?")
```

### Step 5: Write Reference Files

Create `docs/chapters/XX-chapter-name/references.md` with the 10 formatted references.

### Step 6: Update Chapter Files

Replace any existing `## References` section in each chapter's `index.md` with a single link:

```markdown
[See Annotated References](./references.md)
```

### Step 7: Update mkdocs.yml Navigation

Nest an `Annotated References:` entry under each chapter, following the nav-editing rules in `book-installer`'s `references/mkdocs-nav-editing.md`.

## Reference Format Example

```markdown
1. [Karnaugh map](https://en.wikipedia.org/wiki/Karnaugh_map) - Wikipedia - Detailed explanation of K-map theory, grouping rules, and don't-care conditions. Essential foundation for the simplification techniques covered in this chapter.

4. Digital Design (5th Edition) - M. Morris Mano - Pearson - Mano popularized the grid-based K-map grouping method with adjacency highlighting, now the standard visual approach for teaching Boolean minimization.

6. [All About Circuits: Karnaugh Mapping](https://www.allaboutcircuits.com/textbook/digital/chpt-8/karnaugh-mapping/) - All About Circuits - Step-by-step tutorial with worked K-map examples and interactive grouping exercises.
```

## Quality Checklist

Before finalizing references, ensure:

- [ ] Exactly 10 references per chapter
- [ ] References 1-3 are Wikipedia articles
- [ ] References 4-5 are textbooks (no URLs) that name the specific author and the innovative explanation/analogy/derivation they're credited with
- [ ] References 6-10 have verified working URLs
- [ ] All descriptions are 20-40 words
- [ ] Descriptions explain relevance to chapter
- [ ] No duplicate sources across references
- [ ] Proper formatting throughout

## Integration with Other Skills

- **course-description-analyzer**: Determines subject matter and audience that guide reference selection
- **chapter-content-generator**: References support chapter content
- **glossary-generator**: Reference definitions align with glossary
- **learning-graph-generator**: References support concept dependencies

## Tools Used

- **WebSearch**: Find authoritative sources and identify authors credited with specific teaching innovations
- **WebFetch**: Verify URLs are accessible and extract metadata
- **Glob**: Find all chapter directories and reference files
- **Write / Edit**: Create reference files and update chapter index files and mkdocs.yml

## Finish

After generating references:

1. Report the number of chapters processed
2. List any URLs that failed verification
3. Confirm mkdocs.yml was updated
4. Remind user to verify the site builds: `mkdocs serve`
