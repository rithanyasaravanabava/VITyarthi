def check_ph_safety(ph, min_safe=4.0, max_safe=7.5):
    """
    Checks if the given pH is within the safe range for IV fluids.
    
    Args:
    - ph (float): The pH value to check.
    - min_safe (float): Minimum safe pH (default 4.0).
    - max_safe (float): Maximum safe pH (default 7.5).
    
    Returns:
    - str: Safety status message.
    """
    if min_safe <= ph <= max_safe:
        return f"pH {ph} is safe for IV fluids."
    else:
        return f"Warning: pH {ph} is outside the safe range ({min_safe}-{max_safe}). Adjust or consult a pharmacist."

def calculate_mixed_ph(ph1, vol1, ph2, vol2):
    """
    Calculates the approximate pH of a mixture of two fluids using volume-weighted average.
    Note: This is a simplification; actual pH mixing involves acid-base equilibria.
    
    Args:
    - ph1 (float): pH of first fluid.
    - vol1 (float): Volume of first fluid (in mL).
    - ph2 (float): pH of second fluid.
    - vol2 (float): Volume of second fluid (in mL).
    
    Returns:
    - float: Approximate mixed pH.
    """
    # Convert pH to [H+] concentration for calculation
    h1 = 10 ** (-ph1)
    h2 = 10 ** (-ph2)
    total_vol = vol1 + vol2
    mixed_h = (h1 * vol1 + h2 * vol2) / total_vol
    mixed_ph = -math.log10(mixed_h)
    return round(mixed_ph, 2)

# Example usage
import math

# Check a single pH
print(check_ph_safety(6.0))  # Safe
print(check_ph_safety(8.0))  # Warning

# Calculate mixed pH (e.g., mixing saline pH 5.5 with dextrose pH 4.0)
mixed_ph = calculate_mixed_ph(5.5, 500, 4.0, 500)
print(f"Mixed pH: {mixed_ph}")
print(check_ph_safety(mixed_ph))
def check_ph_safety(ph, min_safe=4.0, max_safe=7.5):
    """
    Checks if the given pH is within the safe range for IV fluids.
    
    Args:
    - ph (float): The pH value to check.
    - min_safe (float): Minimum safe pH (default 4.0).
    - max_safe (float): Maximum safe pH (default 7.5).
    
    Returns:
    - str: Safety status message.
    """
    if min_safe <= ph <= max_safe:
        return f"pH {ph} is safe for IV fluids."
    else:
        return f"Warning: pH {ph} is outside the safe range ({min_safe}-{max_safe}). Adjust or consult a pharmacist."

def calculate_mixed_ph(ph1, vol1, ph2, vol2):
    """
    Calculates the approximate pH of a mixture of two fluids using volume-weighted average.
    Note: This is a simplification; actual pH mixing involves acid-base equilibria.
    
    Args:
    - ph1 (float): pH of first fluid.
    - vol1 (float): Volume of first fluid (in mL).
    - ph2 (float): pH of second fluid.
    - vol2 (float): Volume of second fluid (in mL).
    
    Returns:
    - float: Approximate mixed pH.
    """
    # Convert pH to [H+] concentration for calculation
    h1 = 10 ** (-ph1)
    h2 = 10 ** (-ph2)
    total_vol = vol1 + vol2
    mixed_h = (h1 * vol1 + h2 * vol2) / total_vol
    mixed_ph = -math.log10(mixed_h)
    return round(mixed_ph, 2)
