def symmetric_difference(set1, set2):
    """
    Find symmetric difference between two sets
    
    Args:
        set1 (set): First set
        set2 (set): Second set
    
    Returns:
        set: Symmetric difference of set1 and set2
    """
    return set1 ^ set2

def symmetric_difference_manual(set1, set2):
    """
    Manual implementation of symmetric difference using set operations
    
    Args:
        set1 (set): First set
        set2 (set): Second set
    
    Returns:
        set: Symmetric difference of set1 and set2
    """
    # Symmetric difference = (set1 ∪ set2) - (set1 ∩ set2)
    # OR: (set1 - set2) ∪ (set2 - set1)
    return (set1 - set2) | (set2 - set1)

def display_symmetric_difference(set1, set2, set1_name="Set A", set2_name="Set B"):
    """
    Display detailed information about symmetric difference
    
    Args:
        set1 (set): First set
        set2 (set): Second set
        set1_name (str): Name of first set
        set2_name (str): Name of second set
    """
    print(f"{set1_name}: {set1}")
    print(f"{set2_name}: {set2}")
    print(f"Union ({set1_name} ∪ {set2_name}): {set1 | set2}")
    print(f"Intersection ({set1_name} ∩ {set2_name}): {set1 & set2}")
    print(f"Difference ({set1_name} - {set2_name}): {set1 - set2}")
    print(f"Difference ({set2_name} - {set1_name}): {set2 - set1}")
    
    # Using built-in operator
    sym_diff_builtin = symmetric_difference(set1, set2)
    print(f"Symmetric Difference ({set1_name} Δ {set2_name}) using ^ operator: {sym_diff_builtin}")
    
    # Using manual implementation
    sym_diff_manual = symmetric_difference_manual(set1, set2)
    print(f"Symmetric Difference ({set1_name} Δ {set2_name}) manual method: {sym_diff_manual}")
    
    # Verify both methods give same result
    print(f"Methods produce same result: {sym_diff_builtin == sym_diff_manual}")
    
    return sym_diff_builtin

# Example usage with different data types
def main():
    print("🔍 Symmetric Difference Between Sets")
    print("=" * 50)
    
    # Example 1: Integer sets
    print("\n1. Integer Sets:")
    print("-" * 30)
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    result1 = display_symmetric_difference(set_a, set_b, "Set A", "Set B")
    
    # Example 2: String sets
    print("\n2. String Sets:")
    print("-" * 30)
    fruits1 = {"apple", "banana", "orange", "grape"}
    fruits2 = {"banana", "grape", "kiwi", "mango"}
    result2 = display_symmetric_difference(fruits1, fruits2, "Fruits 1", "Fruits 2")
    
    # Example 3: Mixed data types
    print("\n3. Mixed Data Types:")
    print("-" * 30)
    mixed1 = {1, "hello", 3.14, True}
    mixed2 = {"hello", 3.14, False, "world"}
    result3 = display_symmetric_difference(mixed1, mixed2, "Mixed 1", "Mixed 2")
    
    # Example 4: Empty sets
    print("\n4. Empty Sets:")
    print("-" * 30)
    empty_set = set()
    normal_set = {1, 2, 3}
    result4 = display_symmetric_difference(empty_set, normal_set, "Empty Set", "Normal Set")
    
    # Example 5: Identical sets
    print("\n5. Identical Sets:")
    print("-" * 30)
    identical1 = {10, 20, 30}
    identical2 = {10, 20, 30}
    result5 = display_symmetric_difference(identical1, identical2, "Identical 1", "Identical 2")
    
    # Example 6: Disjoint sets (no common elements)
    print("\n6. Disjoint Sets:")
    print("-" * 30)
    disjoint1 = {1, 3, 5}
    disjoint2 = {2, 4, 6}
    result6 = display_symmetric_difference(disjoint1, disjoint2, "Disjoint 1", "Disjoint 2")
    
    # Interactive example
    print("\n" + "=" * 50)
    print("🎯 Interactive Example")
    print("=" * 50)
    
    try:
        # Get user input
        input1 = input("Enter elements for first set (comma-separated): ")
        input2 = input("Enter elements for second set (comma-separated): ")
        
        # Convert input to sets
        user_set1 = set(item.strip() for item in input1.split(','))
        user_set2 = set(item.strip() for item in input2.split(','))
        
        print(f"\nYour sets:")
        result = display_symmetric_difference(user_set1, user_set2, "Your Set 1", "Your Set 2")
        
    except Exception as e:
        print(f"Error: {e}")

# Additional utility functions
def symmetric_difference_multiple(*sets):
    """
    Find symmetric difference of multiple sets
    
    Args:
        *sets: Variable number of sets
    
    Returns:
        set: Symmetric difference of all sets
    """
    if not sets:
        return set()
    
    result = sets[0]
    for s in sets[1:]:
        result = result ^ s
    return result

def demonstrate_multiple_sets():
    """Demonstrate symmetric difference with multiple sets"""
    print("\n" + "=" * 50)
    print("🧮 Symmetric Difference with Multiple Sets")
    print("=" * 50)
    
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    set3 = {5, 6, 7, 8}
    
    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")
    print(f"Set 3: {set3}")
    
    result = symmetric_difference_multiple(set1, set2, set3)
    print(f"Symmetric Difference of all sets: {result}")
    
    # Step by step calculation
    step1 = set1 ^ set2
    step2 = step1 ^ set3
    print(f"Step 1 (Set1 Δ Set2): {step1}")
    print(f"Step 2 (Result Δ Set3): {step2}")

if __name__ == "__main__":
    main()
    demonstrate_multiple_sets()