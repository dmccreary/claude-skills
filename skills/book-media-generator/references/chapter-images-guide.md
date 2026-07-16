# Chapter Image Sourcing Guide

> Active replacement for the archived standalone skill `chapter-image-enhancer`.

Use this guide to add real photographs, maps, or archival media to an intelligent
textbook when a specific image does instructional work that the chapter's prose,
data, or semantic diagrams cannot do as well. Zero new images is a valid and
often preferable outcome.

This workflow helps collect evidence about licensing and provenance. It is not
legal advice. When rights are unclear, do not publish the file.

## When To Use

Use this route when:

- the user asks for sourced photographs, maps, or archival media;
- a learner must inspect a real object, place, organism, document, or event;
- a historical or geographic claim is materially clearer with primary visual
  evidence; or
- an existing external image needs a provenance and attribution audit.

Do not use this route merely because a chapter is text-heavy. Prefer a local
teaching diagram, first-party screenshot, table, or interactive when it explains
the concept better. Do not add decorative stock imagery to satisfy a quota.

## Output Contract

An approved image produces all of the following:

1. the optimized local media file;
2. descriptive alt text and a useful caption;
3. a visible attribution near the image or in an adjacent credits section;
4. a machine-readable provenance record; and
5. verification that the rendered page, source link, attribution, dimensions,
   and file size are correct.

Store provenance in `image-credits.yml` beside the chapter images unless the
project already has a canonical media ledger. Record at least:

```yaml
- file: example.jpg
  source_page: https://commons.wikimedia.org/wiki/File:Example.jpg
  direct_url: https://upload.wikimedia.org/example.jpg
  creator: Example Creator
  license_id: CC BY 4.0
  license_url: https://creativecommons.org/licenses/by/4.0/
  retrieved_at: 2026-07-16
  modifications: resized to 1200px; JPEG quality 82
  sha256: <digest of the committed file>
```

Do not treat a caption alone as adequate provenance. File pages and metadata can
change; the ledger preserves what was reviewed at publication time.

## Source And Rights Policy

Every candidate is reviewed individually. A source being hosted by Wikimedia
Commons or a government domain is not itself a license.

### Routine Automated Reuse

The workflow may proceed after metadata verification for:

- CC0;
- an explicit public-domain dedication or verified public-domain status; and
- CC BY, with creator, license version, license URL, and modifications recorded.

### Manual Rights Review Required

Stop for project-owner review before publishing:

- CC BY-SA, CC BY-NC, or CC BY-NC-SA;
- any NoDerivatives license, including CC BY-ND and CC BY-NC-ND;
- GFDL, multi-license, custom-license, or unknown-license files;
- works containing identifiable people, trademarks, private property, or other
  non-copyright restrictions relevant to the intended use; and
- any candidate whose creator, source page, or license version is missing.

Do not infer that CC BY-SA material is compatible with a CC BY-NC-SA textbook.
Creative Commons publishes license compatibility rules at
<https://creativecommons.org/compatible-licenses/> and explains adaptation,
collection, and ShareAlike obligations at <https://creativecommons.org/faq/>.
Whether an image is merely collected with a book or adapted into a larger work
can matter, so uncertain cases require review rather than a blanket table.

### Government Sources

A work prepared by an officer or employee of the United States government as
part of official duties is generally not protected by U.S. copyright under
17 U.S.C. 105. A federal website can still host contractor, grantee, donated,
transferred, or third-party material. Confirm authorship and the item-specific
rights statement. The government may also own copyrights transferred to it.

State, local, university, and foreign-government works are not automatically
public domain under this rule. Review their item-specific terms.

## Workflow

### 1. Define The Teaching Job

Read the chapter and identify a concrete learner need. For each proposed image,
write one sentence answering:

> What will the learner be able to notice, compare, locate, or judge because
> this image is present?

Reject the candidate if the answer is only "the page looks more visual." Rank
the remaining candidates against local diagrams, first-party screenshots,
tables, and interactives. Adding no external media is a successful audit.

### 2. Find Candidate Media

Prefer, in order:

1. first-party evidence owned by the project;
2. verified CC0 or public-domain collections;
3. CC BY media with complete attribution metadata; and
4. manually reviewed restricted or ShareAlike candidates.

Wikimedia Commons is useful for discovery, but Commons provides no warranty and
asks reusers to verify each file's status. Follow its reuse guidance at
<https://commons.wikimedia.org/wiki/Commons:Reusing_content_outside_Wikimedia/en>.

Use the included, tested Commons metadata helper. Supply a monitored project
contact in the User-Agent so Wikimedia can reach the operator if the client
misbehaves:

```bash
python3 skills/book-media-generator/scripts/images/commons_metadata.py \
  --title "File:Example.jpg" \
  --contact "mailto:maintainer@example.org" \
  --output /tmp/example-commons-metadata.json
```

The helper queries `https://commons.wikimedia.org/w/api.php` with
`iiprop=url|extmetadata` and `formatversion=2`. It converts HTML-formatted
extended metadata to reviewable plain text, requires a source page and creator,
recognizes only the routine-reuse license set from this guide, and requires an
official Creative Commons license URL for CC0 and CC BY. Other licenses stop
with a manual-review error. HTTP 429 responses honor `Retry-After` for at most
three attempts.

The MediaWiki `imageinfo` documentation lists `extmetadata` and related fields:
<https://www.mediawiki.org/wiki/API:Imageinfo>.

The API result is evidence to review, not an automatic permission decision.
Open the source page and check for warnings, multiple licenses, special terms,
or metadata that is only meaningful as rendered HTML.

### 3. Approve Or Reject Each Candidate

For each candidate, verify:

- it satisfies the teaching job;
- the source page identifies the creator and rights status;
- the license permits the intended use and modifications;
- attribution requirements can be met;
- non-copyright restrictions have been considered; and
- the source URL, license URL, retrieval date, and intended modifications are
  ready for the provenance ledger.

If a Commons file came from Flickr or another upstream source, review the
Commons record and any available source history. Do not claim that one page is
automatically authoritative if the records conflict.

### 4. Download And Verify The File

Download sequentially with a descriptive User-Agent. Honor `Retry-After` on
HTTP 429 responses instead of using a fixed retry claim. Confirm that the
response is an expected image type before writing it, then compute a SHA-256
digest for the provenance record.

Create the project's conventional chapter-image directory, for example:

```text
docs/img/chapters/XX-chapter-name/
```

Never guess a Wikimedia hash path. Use the API-provided URL.

### 5. Optimize Without Losing Meaning

Use Pillow or the project's existing image pipeline. Preserve the original
aspect ratio, color meaning, labels, and accessibility-relevant detail. Do not
crop documentary evidence merely to fit a layout. Record every transformation.

Reasonable starting targets, subject to the project's performance budget:

- photographs: 1200px maximum display width, efficient JPEG or WebP;
- diagrams and maps: lossless format when labels or transparency require it;
- thumbnails: separate derivative rather than destructive replacement; and
- all files: dimensions and byte size checked after encoding.

### 6. Insert With Context And Attribution

Place the image where the learner needs the evidence, not automatically after
every H2. Introduce it in the prose and explain what to inspect.

```markdown
![Descriptive alt text that conveys the relevant visual evidence](../../img/chapters/XX-name/example.jpg)
*What the learner should notice. [Creator and source file](https://example.com/source-file) ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)); resized from the original.*
```

Use empty alt text only when the image is genuinely decorative and conveys no
information. If it is decorative, reconsider whether it belongs in the book.

Maintain an `## Image Credits` section when the project uses consolidated
credits, but keep the machine-readable provenance ledger as the audit source.

### 7. Verify The Published Result

Run the project's tests and strict documentation build. Then inspect the
rendered page at desktop and mobile widths. Verify independently that:

- the image loads and is legible;
- the aspect ratio is correct and no important content is cropped;
- alt text and caption serve different, useful purposes;
- attribution and license links resolve to the reviewed sources;
- the provenance ledger matches the committed file's SHA-256;
- dimensions and byte size meet the project budget; and
- the image still performs the teaching job in context.

A successful build proves only that the site compiled. It does not prove
rights, attribution, accessibility, visual quality, or instructional value.

## Failure Modes

1. **Image quotas:** adding three to six images because a recipe says so creates
   decoration and maintenance debt. Zero is valid.
2. **Host-as-license reasoning:** neither `*.gov` nor Commons guarantees that a
   particular file is reusable.
3. **Blanket compatibility claims:** ShareAlike, NonCommercial, NoDerivatives,
   collection, and adaptation questions require license-specific review.
4. **Missing provenance:** a caption without source URL, license URL, retrieval
   date, modifications, and digest is difficult to audit later.
5. **API success as permission:** metadata can be missing, stale, conflicting,
   or incomplete. Review the rendered source page.
6. **Destructive optimization:** crops or conversions can remove labels,
   transparency, detail, or evidentiary context.
7. **Build-only verification:** compilation cannot establish legal,
   accessibility, performance, or teaching quality.

## Completion Report

Report:

- teaching jobs considered;
- candidates approved and rejected, with reasons;
- files added or intentionally not added;
- provenance-ledger path;
- tests, build, link, and rendered-page checks performed; and
- any item left for manual rights review.
