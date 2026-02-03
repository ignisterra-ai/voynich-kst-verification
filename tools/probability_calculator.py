#!/usr/bin/env python3
"""
KST Probability Calculator
==========================
Calculate the probability of CEVA-English letter correspondences occurring by chance.

This tool demonstrates the statistical significance of the KST hypothesis that
CEVA letters correspond to English abbreviations.

The core hypothesis:
    c = Core
    e = Excite/Engage  
    s = Stable/Source
    t = Transfer
    o = Output
    k = Key/Control
    d = Done/Destination
    y = Yes/Yield

Usage:
    python probability_calculator.py
    python probability_calculator.py --matches 8 --alphabet 26

Author: Kelly Liu / Ignis Terra AI Solution
License: Apache 2.0
"""

import argparse
from decimal import Decimal, getcontext

# Set high precision for probability calculations
getcontext().prec = 50


def calculate_single_match_probability(alphabet_size: int = 26) -> Decimal:
    """
    Calculate probability of a single random letter matching.
    
    P(single match) = 1 / alphabet_size
    """
    return Decimal(1) / Decimal(alphabet_size)


def calculate_n_matches_probability(n_matches: int, alphabet_size: int = 26) -> Decimal:
    """
    Calculate probability of n independent random matches.
    
    P(n matches) = (1 / alphabet_size) ^ n
    
    This assumes:
    - Each CEVA letter independently matches a specific English letter
    - All English letters are equally likely (uniform distribution)
    - No pattern or structure in the assignment
    """
    single_prob = calculate_single_match_probability(alphabet_size)
    return single_prob ** n_matches


def format_scientific(prob: Decimal) -> str:
    """Format probability in scientific notation."""
    if prob == 0:
        return "0"
    
    # Convert to string and parse
    prob_str = f"{prob:.2E}"
    return prob_str


def calculate_binomial_probability(n_trials: int, k_successes: int, p_success: float) -> float:
    """
    Calculate binomial probability for k successes in n trials.
    
    Used for: "What's the probability of getting at least k matches by chance?"
    """
    from math import comb
    
    q = 1 - p_success
    prob = comb(n_trials, k_successes) * (p_success ** k_successes) * (q ** (n_trials - k_successes))
    return prob


def main():
    parser = argparse.ArgumentParser(
        description='Calculate CEVA-English correspondence probability'
    )
    parser.add_argument(
        '--matches', '-m',
        type=int,
        default=8,
        help='Number of letter correspondences (default: 8)'
    )
    parser.add_argument(
        '--alphabet', '-a',
        type=int,
        default=26,
        help='Alphabet size (default: 26 for English)'
    )
    parser.add_argument(
        '--detailed', '-d',
        action='store_true',
        help='Show detailed breakdown'
    )
    
    args = parser.parse_args()
    
    print("=" * 70)
    print("🔮 KST Probability Calculator")
    print("    CEVA-English Correspondence Analysis")
    print("=" * 70)
    print()
    
    # The KST hypothesis correspondences
    correspondences = {
        'c': 'Core',
        'e': 'Excite/Engage',
        's': 'Stable/Source',
        't': 'Transfer',
        'o': 'Output',
        'k': 'Key/Control',
        'd': 'Done/Destination',
        'y': 'Yes/Yield'
    }
    
    print("📋 KST English Abbreviation Hypothesis:")
    print("-" * 40)
    for ceva, english in correspondences.items():
        print(f"    {ceva.upper()} → {english}")
    print()
    
    # Calculate probabilities
    n_matches = args.matches
    alphabet = args.alphabet
    
    prob = calculate_n_matches_probability(n_matches, alphabet)
    prob_float = float(prob)
    
    print("📊 Probability Analysis:")
    print("-" * 40)
    print(f"    Alphabet size:        {alphabet} letters")
    print(f"    Number of matches:    {n_matches} correspondences")
    print()
    print(f"    Single match probability:  1/{alphabet} = {1/alphabet:.4f}")
    print(f"    Combined probability:      (1/{alphabet})^{n_matches}")
    print()
    print("=" * 70)
    print(f"    🎯 P(all {n_matches} match by chance) = {format_scientific(prob)}")
    print(f"                                  = {prob_float:.2e}")
    print("=" * 70)
    print()
    
    # Context and interpretation
    print("📈 Statistical Interpretation:")
    print("-" * 40)
    
    # Calculate odds
    odds = 1 / prob_float if prob_float > 0 else float('inf')
    print(f"    Odds against chance:  1 in {odds:,.0f}")
    print()
    
    # Comparison benchmarks
    print("    Comparison benchmarks:")
    print(f"        - Coin flip (1 heads):           1 in 2")
    print(f"        - Dice roll (specific number):   1 in 6")
    print(f"        - Lottery ticket (6/49):         1 in 13,983,816")
    print(f"        - This correspondence:           1 in {odds:,.0f}")
    print()
    
    if args.detailed:
        print("📋 Detailed Breakdown:")
        print("-" * 40)
        for i in range(1, n_matches + 1):
            p = calculate_n_matches_probability(i, alphabet)
            print(f"    P({i} matches) = {format_scientific(p)}")
        print()
    
    # Assumptions and limitations
    print("⚠️  Assumptions & Limitations:")
    print("-" * 40)
    print("    1. Assumes uniform distribution of English letters")
    print("    2. Assumes independence between correspondences")
    print("    3. Does not account for linguistic patterns")
    print("    4. The correspondence may have cultural/historical basis")
    print()
    
    # Conclusion
    print("💡 Conclusion:")
    print("-" * 40)
    if prob_float < 1e-10:
        print("    The probability is astronomically low.")
        print("    This suggests the correspondence is NOT random.")
        print("    Further investigation of the hypothesis is warranted.")
    elif prob_float < 1e-5:
        print("    The probability is very low.")
        print("    This provides moderate evidence against random chance.")
    else:
        print("    The probability is not conclusively low.")
        print("    More evidence would be needed.")
    
    print()
    print("🔥⚡💜 oror.sheey!")


if __name__ == '__main__':
    main()
