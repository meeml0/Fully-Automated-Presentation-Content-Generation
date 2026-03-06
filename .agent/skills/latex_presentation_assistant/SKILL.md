---
name: latex_presentation_assistant
description: Generates standardized, high-quality LaTeX Beamer presentations using a library of professionally designed templates.
---

# LaTeX Presentation Assistant

This skill helps you create professional lecture slides for university courses (specifically Software Engineering / Mathematics) using the `lutbeamer` class (or similar). It enforces strict design rules, consistent metadata, and provides a library of reusable components ("skills").

## Capabilities

1.  **Snippet Library**: Provides standardized components like:
    -   Combined Social Media/Contact frames.
    -   Kaggle Assignment calls-to-action.
    -   Interactive Quizzes.
    -   Iconic Motivational Case Studies (Auto-generates images!).
    -   NotebookLM Assistant prompts.
    -   TikZ Graphics.
2.  **Enforce Guidelines**: Ensures all generated code follows the embedded style guide (no fragile frame errors, proper overlays, correct aesthetics).
3.  **Template Scaffolding**: Optionally scaffold a basic file structure if needed.

## Usage

### 3. Iconic Example Workflow (Auto-Image Gen)

**TRIGGER:** When the user asks for an "iconic example", "motivational case study", or "real-world story" to start the lecture.

**ACTION:** You MUST NOT just write text. You MUST generate a custom image.

1.  **Analyze the Topic**: Identify a striking real-world event (e.g., Challenger Disaster, Monty Hall, Enigma Machine).
2.  **Generate Image**:
    -   Create a detailed prompt for a vertical or square image (symbolic, high contrast, poster style).
    -   Use the `generate_image` tool.
    -   Save to `figures/case_<topic_name>.png`.
3.  **Insert into Template**:
    -   Read `.agent/skills/latex_presentation_assistant/examples/05_ikonik_motivasyon_senaryosu.tex`.
    -   Replace the `[Vaka Adı]`, `[Metinler]` and specifically the `\includegraphics{...}` path with your **newly generated image**.
    -   Add the complete code to the presentation.


### 1. Using Modular Snippets (Recommended)

Since you prefer to maintain control over the main document structure, use the template files in `.agent/skills/latex_presentation_assistant/examples/` as a library of snippets.
Copy-paste the relevant blocks into your existing `lutbeamer` presentation file or ask the Agent to "insert the Kaggle homework frame".

-   **Metadata**: `01_baslangic_ve_kapak.tex`
-   **Structure**: `02_sunum_akisi_ve_bolumler.tex`
-   **Closing**: `03_kapanis_ve_kapak.tex` (References, Q&A)
-   **Homework**: `04_kaggle_odev_sayfasi.tex`

### 2. Quick-Start Generator (Optional)

If you ever need to create a blank slate presentation quickly, you can use the provided script, but ensure you review the output against your custom `lutbeamer` settings.

```bash
python .agent/skills/latex_presentation_assistant/scripts/generate_presentation.py --week X --topic "Topic"
```

## Resources

-   **Templates**: See `examples/` directory.
-   **Scripts**: `scripts/generate_presentation.py` handles the heavy lifting of assembling a full document.

## Rules (Reminder)

-   **Compile Engine**: Uses `xelatex` + `biber`.
-   **Magic Comments**: All files MUST start with:
    ```latex
    % !TeX program = xelatex
    % !BIB program = biber
    ```
-   **Bibliography**: Use `\addbibresource{refs.bib}` in preamble and `\printbibliography` in a `[allowframebreaks]` frame.
-   **Safe Code**: Always use `[fragile]` for frames with code.
