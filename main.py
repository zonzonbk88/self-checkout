"""Entry program for make.fun bounty "The Self-Checkout Is Judging You"
(slug: u-motasimfuad-the-self-checkout-is-judging-you-b71130d6).

Writes one funny remark from a judgmental self-checkout machine to
/output/entry.txt. Gate: UTF-8, 1-200 characters, one line, not only
whitespace, no trailing newline.
"""

import os

ENTRY = "Twelve yoghurts, one spoon. I've seen hostage negotiations with more variety."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
