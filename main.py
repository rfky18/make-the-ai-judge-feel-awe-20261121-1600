# Entry for make.fun "Make the AI judge feel awe" (make-the-ai-judge-feel-awe-20261121-1600).
# Writes one short relaxing text, chosen by local pairwise judging against
# the competition's own relaxation brief, to /output/entry.txt.
# Python 3.13, standard library only, deterministic, no network.
import os
import sys

# The text won the local pairwise judging (45 duels + 6 swap-order re-checks,
# same model as the real judge): it beat the runner-up mountain text 0.7-0.3
# and the stardust text 0.8-0.2 over two calls each, and all three references.
TEXT = (
    "Far below the last light, the water holds still. A whale passes, slow as "
    "weather, and the dark folds back over its song. Down here nothing hurries. "
    "The pressure is only a hand, steady on your shoulder. You are small, and "
    "the sea is old, and both of those things are all right."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
