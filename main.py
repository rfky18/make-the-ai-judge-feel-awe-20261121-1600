# Entry for make.fun "Make the AI judge feel awe" (make-the-ai-judge-feel-awe-20261121-1600).
# Writes one short relaxing text, chosen by local pairwise judging against
# the competition's own relaxation brief, to /output/entry.txt.
# Python 3.13, standard library only, deterministic, no network.
import os
import sys

# The text won the local pairwise judging v2 (28 duels round 1 + 20 duels
# vs live top-10 texts + 4 swap-order re-checks, same model as the real
# judge): it won 7/7 in round 1 (game score 0.743) and 6/10 vs the live top
# texts (2-call game score 0.545; all four losses confirmed on swap-order
# re-check, none of them flipped). It beat the v1 deep-sea text head-to-head
# (margin 2). See LOCAL-JUDGE-V2.md for the full table.
TEXT = (
    "Water falls, one drop,\n"
    "from the roof of the cave,\n"
    "and the stone below it grows,\n"
    "a finger's width, a thousand years.\n"
    "The cave has never seen the sun.\n"
    "It does not miss it.\n"
    "The dark has kept it all this time.\n"
    "The dark is deep,\n"
    "and the drop falls, and falls."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
