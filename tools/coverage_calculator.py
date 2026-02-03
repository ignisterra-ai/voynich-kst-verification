#!/usr/bin/env python3
"""
KST Coverage Calculator
=======================
Verify dictionary coverage claims for Voynich Manuscript transcription.

This tool calculates what percentage of words in a KST-cleaned transcription
are defined in the dictionary keys.

Usage:
    python coverage_calculator.py --input kst_data.tsv
    python coverage_calculator.py --input kst_data.tsv --dictionary custom_dict.json

Author: Kelly Liu / Ignis Terra AI Solution
License: Apache 2.0
"""

import argparse
import json
import csv
import sys
from pathlib import Path
from collections import Counter


def load_dictionary_keys(dict_path: str) -> set:
    """Load the dictionary keys and return set of defined words."""
    with open(dict_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    entries = data.get('entries', {})
    defined_words = {word for word, info in entries.items() if info.get('defined', False)}
    
    print(f"📖 Loaded dictionary: {len(defined_words)} defined entries")
    return defined_words


def extract_words_from_eva(eva_text: str) -> list:
    """Extract individual words from EVA_KS format text."""
    if not eva_text:
        return []
    
    # Split by period (KST word separator)
    words = eva_text.lower().split('.')
    
    # Clean and filter
    cleaned = []
    for word in words:
        # Remove special markers
        word = word.strip()
        if word.startswith('[') or word.startswith('<'):
            continue
        # Remove non-alphabetic characters
        word = ''.join(c for c in word if c.isalpha())
        if word:
            cleaned.append(word)
    
    return cleaned


def calculate_coverage(input_path: str, dictionary: set) -> dict:
    """Calculate coverage statistics for input TSV file."""
    total_words = 0
    defined_words = 0
    undefined_list = []
    word_freq = Counter()
    
    with open(input_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        header = next(reader, None)
        
        # Find EVA_KS column
        eva_col = None
        if header:
            for i, col in enumerate(header):
                if 'EVA_KS' in col.upper() or 'EVA_KST' in col.upper():
                    eva_col = i
                    break
            if eva_col is None:
                eva_col = 2  # Default position in KST format
        
        for row in reader:
            if len(row) <= eva_col:
                continue
            
            eva_text = row[eva_col]
            words = extract_words_from_eva(eva_text)
            
            for word in words:
                total_words += 1
                word_freq[word] += 1
                
                if word in dictionary:
                    defined_words += 1
                else:
                    # Try recursive decomposition (onion peeling)
                    if try_decompose(word, dictionary):
                        defined_words += 1
                    else:
                        undefined_list.append(word)
    
    coverage = (defined_words / total_words * 100) if total_words > 0 else 0
    
    return {
        'total_words': total_words,
        'defined_words': defined_words,
        'undefined_count': len(undefined_list),
        'coverage_percent': round(coverage, 2),
        'undefined_words': list(set(undefined_list))[:50],  # Top 50 unique
        'word_frequencies': word_freq.most_common(20)
    }


def try_decompose(word: str, dictionary: set, depth: int = 0) -> bool:
    """
    Try to decompose a word using the 'onion peeling' method.
    Returns True if the entire word can be composed from dictionary entries.
    """
    if depth > 10:  # Prevent infinite recursion
        return False
    
    if word in dictionary:
        return True
    
    if len(word) <= 1:
        return word in dictionary
    
    # Try splitting from longest prefix to shortest
    for i in range(len(word), 0, -1):
        prefix = word[:i]
        suffix = word[i:]
        
        if prefix in dictionary:
            if not suffix:
                return True
            if try_decompose(suffix, dictionary, depth + 1):
                return True
    
    return False


def main():
    parser = argparse.ArgumentParser(
        description='Calculate dictionary coverage for KST transcription data'
    )
    parser.add_argument(
        '--input', '-i',
        required=True,
        help='Path to KST TSV file'
    )
    parser.add_argument(
        '--dictionary', '-d',
        default='../data/dictionary_v15_keys.json',
        help='Path to dictionary keys JSON'
    )
    parser.add_argument(
        '--output', '-o',
        help='Optional: Save results to JSON file'
    )
    
    args = parser.parse_args()
    
    # Resolve paths
    input_path = Path(args.input)
    dict_path = Path(args.dictionary)
    
    if not input_path.exists():
        print(f"❌ Error: Input file not found: {input_path}")
        sys.exit(1)
    
    if not dict_path.exists():
        # Try relative to script location
        script_dir = Path(__file__).parent
        dict_path = script_dir / '..' / 'data' / 'dictionary_v15_keys.json'
    
    if not dict_path.exists():
        print(f"❌ Error: Dictionary not found: {dict_path}")
        sys.exit(1)
    
    print("=" * 60)
    print("🔮 KST Coverage Calculator")
    print("=" * 60)
    print(f"📄 Input: {input_path}")
    print(f"📖 Dictionary: {dict_path}")
    print()
    
    # Load dictionary
    dictionary = load_dictionary_keys(str(dict_path))
    
    # Calculate coverage
    print("⏳ Calculating coverage...")
    results = calculate_coverage(str(input_path), dictionary)
    
    # Display results
    print()
    print("=" * 60)
    print("📊 RESULTS")
    print("=" * 60)
    print(f"Total words processed:     {results['total_words']:,}")
    print(f"Words in dictionary:       {results['defined_words']:,}")
    print(f"Words not in dictionary:   {results['undefined_count']:,}")
    print(f"")
    print(f"✨ COVERAGE RATE:          {results['coverage_percent']}%")
    print("=" * 60)
    
    if results['undefined_words']:
        print()
        print("🔍 Sample undefined words (first 20):")
        for word in results['undefined_words'][:20]:
            print(f"   - {word}")
    
    print()
    print("📈 Top 10 most frequent words:")
    for word, count in results['word_frequencies'][:10]:
        status = "✅" if word in dictionary or try_decompose(word, dictionary) else "❌"
        print(f"   {status} {word}: {count}")
    
    # Save results if requested
    if args.output:
        output_path = Path(args.output)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"\n💾 Results saved to: {output_path}")
    
    print()
    print("🔥⚡💜 oror.sheey!")


if __name__ == '__main__':
    main()
