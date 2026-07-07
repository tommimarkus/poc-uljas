# Uljas — architecture gallery

`index.html` is a **self-contained** viewer for the 24 architecture views of the
Ulosottolaitos *Uljas* information-system-applicant message interface. Every diagram
is inlined, so the single file works on GitHub Pages, any static host, or opened
straight from disk — no build step, no external assets, no network.

- **Browse** the plates in the left register, grouped by notation: **K** = konteksti &
  prosessit (ArchiMate 3.2), **T** = tietomallit (UML 2.5), **S** = sekvenssit (UML 2.5).
- **Zoom** each plate, **toggle** light/dark, and **deep-link** a view with `#<id>`
  (e.g. `index.html#seq-submission`) to share one diagram.

The visual language (tokens, typography, components) is documented in [DESIGN.md](DESIGN.md).

## Publish on GitHub Pages (free, zero-config)

1. Push this `docs/` folder to `main` (already done).
2. Repo **Settings → Pages → Build and deployment**: Source = **Deploy from a branch**,
   Branch = **main**, Folder = **/docs**. Save.
3. The gallery goes live at `https://<owner>.github.io/<repo>/` in a minute or two.

## Regenerate

`index.html` is built from the model's own sources — `architecture/uljas.dediren/`
(`project.json` titles/questions, `generated/svg/*.svg`, `generated/render-metadata/*.json`
counts). After re-rendering the model, rebuild with:

```
python3 docs/build-gallery.py
```

## Note on contents

The gallery embeds the project's **own** ArchiMate/UML diagrams. The source documents
they were modelled from (Ulosottolaitos PDFs/schemas under `input/`) are **git-ignored**
and are never published here.
