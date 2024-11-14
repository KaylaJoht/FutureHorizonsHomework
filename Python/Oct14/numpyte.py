# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 15:55:00 2024

@author: kayla
"""

try:
    import numpy as np
except ImportError:
    raise ImportError("You can't proceed into the cave without NumPy!")
    
    
sw_vial = None

# Reassign sw_vial to a NumPy array of 10 zeros
### BEGIN SOLUTION
sw_vial = np.zeros(10)
### END SOLUTION

print(sw_vial)


'''TEST
assert sw_vial is not None, "sw_vial must be assigned to something!"
### BEGIN HIDDEN TESTS
type(sw_vial), "sw_vial must be a NumPy array!"
sw_vial.shape "sw_vial must be a 1D array of length 10!"
np.all(sw_vial == 0) "sw_vial must be an array of zeros!"
### END HIDDEN TESTS
print("Success!")
'''

sw_ampoule = np.zeros(6)
print(f"The size of sw_ampoule is: {sw_ampoule.size}")
print(f"The size of sw_vial is: {sw_vial.size}")

# Concatenate sw_ampoule onto sw_vial and delete sw_vial
### BEGIN SOLUTION
sw_vial = np.concatenate((sw_vial, sw_ampoule))
del sw_ampoule
### END SOLUTION

print("The size of sw_vial is now:", sw_vial.size)

'''TEST
assert isinstance(sw_vial, np.ndarray), "sw_vial must be a NumPy array!"
### BEGIN HIDDEN TESTS
sw_vial.shape, "sw_vial must be a 1D array of length 16!"
np.all(sw_vial == 0), "sw_vial must be an array of zeros!"
"sw_ampoule" not in locals(), "sw_ampoule must be deleted!"
### END HIDDEN TESTS
print("Success!")
'''

print(f"The shape of sw_vial is: {sw_vial.shape}.")
# Reshape sw_vial to have a shape of (8, 2)
### BEGIN SOLUTION
sw_vial = sw_vial.reshape(8,2)
### END SOLUTION

print(f"Now the shape of sw_vial is: {sw_vial.shape}.")
print(sw_vial)

'''TEST
assert isinstance(sw_vial, np.ndarray), "sw_vial must be a NumPy array!"
### BEGIN HIDDEN TESTS
assert sw_vial.shape == (8, 2), "sw_vial must be a 2D array of shape (8, 2)!"
assert np.all(sw_vial == 0), "sw_vial must be an array of zeros!"
### END HIDDEN TESTS
print("Success!")
'''


# This is the bridge - planks that you can safely stop on have a sum greater than 10
BRIDGE = np.array([
    [2, 5],
    [4, 5],
    [6, 2],
    [3, 7],
    [1, 3],
    [5, 2],
    [2, 5],
    [4, 5],
    [6, 8],
    [3, 7],
    [1, 3],
    [5, 6]
])


# Find the indices in the bridge where the sum of the two items in each row is greater than 10.
# bridge_indices should return a 1-D array.
bridge_indices = None
### BEGIN SOLUTION
bridge_indices = np.where(BRIDGE.sum(axis=1)>10)[0]
### END SOLUTION

print(bridge_indices)

'''TEST
assert bridge_indices is not None, "bridge_indices must be assigned to something!"
### BEGIN HIDDEN TESTS
assert isinstance(bridge_indices, np.ndarray), "bridge_indices must be a NumPy array!"
assert bridge_indices.shape == (2,), "bridge_indices must be a 1D array of length 2!"
### END HIDDEN TESTS
print("Success!")
'''


fj_vial = np.ones((sw_vial.shape[0], bridge_indices.shape[0]))

print(fj_vial)


morse = {
       '.-': 'A',
       '-...': 'B',
       '-.-.': 'C',
       '-..': 'D',
       '.': 'E',
       '..-.': 'F',
       '--.': 'G',
       '....': 'H',
       '..': 'I',
       '.---': 'J',
       '-.-': 'K',
       '.-..': 'L',
       '--': 'M',
       '-.': 'N',
       '---': 'O',
       '.--.': 'P',
       '--.-': 'Q',
       '.-.': 'R',
       '...': 'S',
       '-': 'T',
       '..-': 'U',
       '...-': 'V',
       '.--': 'W',
       '-..-': 'X',
       '-.--': 'Y',
       '--..': 'Z',
       '.----': '1',
       '..---': '2',
       '...--': '3',
       '....-': '4',
       '.....': '5',
       '-....': '6',
       '--...': '7',
       '---..': '8',
       '----.': '9',
       '-----': '0',
       '--..--': ', ',
       '.-.-.-': '.',
       '..--..': '?',
       '-..-.': '/',
       '-....-': '-',
       '-.--.': '(',
       '-.--.-': ')'
}

signal = np.array(['.--', '....', '---', '.-..', '..', '...-', '.', '...', '..', '-.',
       '.-', '.--.', '..', '-.', '.', '.-', '.--.', '.--.', '.-..', '.',
       '..-', '-.', '-..', '.', '.-.', '-', '....', '.', '...', '.', '.-',
       '..--..'])



# Translate the ENCRYPTED_SIGNAL using the morse dictionary and a list comprehension
translated_signal = None
### BEGIN SOLUTION
translated_signal = [morse[code] for code in signal]
### END SOLUTION

print(translated_signal)


'''TEST
assert translated_signal is not None, "translated_signal must be assigned to something!"
### BEGIN HIDDEN TESTS
assert isinstance(translated_signal, list), "translated_signal must be a list!"
assert len(translated_signal) == len(signal), "translated_signal must be the same length as signal!"
### END HIDDEN TESTS
'''


signal_response = None
### BEGIN SOLUTION
signal_response = 'SPONGEBOB SQUAREPANTS'
### END SOLUTION

print(signal_response)


solution_flask = None

### BEGIN SOLUTION
solution_flask = np.dstack((sw_vial, fj_vial)).reshape(8,4)
### END SOLUTION

print(solution_flask)

'''TEST
assert solution_flask is not None, "solution_flask must be assigned to something!"
### BEGIN HIDDEN TESTS
assert isinstance(solution_flask, np.ndarray), "solution_flask must be a NumPy array!"
assert solution_flask.shape == (8, 4), "solution_flask must be a 2D array of shape (8, 4)!"
assert np.isnan(solution_flask).any() == False, "solution_flask should not contain any NaN values!"
assert np.isinf(solution_flask).any() == False, "solution_flask should not contain any infinite values!"
assert (solution_flask >= 0).all(), "solution_flask should not contain any negative values!"
### END HIDDEN TESTS
print("Success!")
'''


# Distill the solution flask by: 
# - slicing the first 6 rows of solution_flask to distilled_solution,
# - multiplying these rows by 2 (broadcasting),
# - and finding the sum of the entire matrix.

distilled_solution = None
### BEGIN SOLUTION
distilled_solution = solution_flask[0:6] * 2
distilled_solution = distilled_solution.sum()
### END SOLUTION

print(distilled_solution)

'''TEST
assert distilled_solution is not None, "distilled_solution must be assigned to something!"
### BEGIN HIDDEN TESTS
assert isinstance(distilled_solution, np.float64), "distilled_solution must be a NumPy float64!"
assert int(distilled_solution) == 24, "distilled_solution must be equal to the answer!"
print(f"""
Success!
You've distilled the Witskey to its purest form and drop it onto the golden sponge.
You hear a rumbling in the distance, and the cave begins to shake.
The sponge begins to glow, and you feel a rush of energy as you absorb the solution.
You hear a voice in your head, as if just waking from a deep, deep slumber.
'Who... who am I?'
You shout at the top of your lungs, 
      '{signal_response}'!
The cave shakes even more violently, and you hear a loud crash.
Looking up, you see the ceiling above you beginning to crumble.
There is no exit, and you are trapped. It seems as if all is lost.
You cover your head and accept that all is lost. Then, you hear,
    'I am... I am... {signal_response}! AND I AM READY!'
You are swept up by powerful hands and carried out of the cave, through the falling debris.
You emerge from the cave, and the hands set you down on the ground.
You look up to see a giant yellow sponge with a square face.
'You have freed me from my slumber, and I am eternally grateful.
I will grant you one wish, anything you desire.'
You think for a moment, and then you say,
'The NumPyte Shard! Is it destroyed?' The cave is rubble, and you fear the worst.
The sponge looks at you, and then looks down at the ground.
'The NumPyte Shard can never be destroyed...
So long as it lives on in the hearts of adventurers like you.'
And with that, the great sponge ascends into the sky, and you are left alone.
You glance down at the ground, and see a small crystal shaped like a simple, perfect hamburger.
You pick it up and feel a surge of energy, and you know that you possess the ~NumPyte Shard~.
With your toolkit and newfound power in hand, you set off on your next adventure in the land of Datalore.
""")
### END HIDDEN TESTS
'''

