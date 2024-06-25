# # import subprocess
# # import re
# # import os
# # import string

# # def sanitize_filename(filename):
# #     """
# #     Sanitize the filename to be file system and URL safe.
# #     """
# #     valid_chars = f"-_.() {string.ascii_letters}{string.digits}"
# #     return ''.join(c for c in filename if c in valid_chars)

# # def get_phonemes(text):
# #     """
# #     Use the espeak-ng CLI tool to get the phonemes for the given text.
# #     """
# #     try:
# #         # Call the espeak-ng command and capture the output
# #         output = subprocess.check_output(["espeak-ng", "--ipa", text])
        
# #         # Decode the output manually to avoid encoding issues
# #         output = output.decode('utf-8')
        
# #         # Extract the phonemes from the output
# #         phonemes = re.findall(r'\S+', output)
        
# #         return phonemes
# #     except subprocess.CalledProcessError as e:
# #         print(f"Error running espeak-ng: {e}")
# #         return []

# # def play_phoneme_audio(phoneme):
# #     """
# #     Use espeak-ng to generate audio for a given phoneme.
# #     """
# #     try:
# #         sanitized_phoneme = sanitize_filename(phoneme)
# #         output_audio_file = f"{sanitized_phoneme}.wav"
# #         subprocess.run(["espeak-ng", phoneme, "-w", output_audio_file], check=True)
# #         return output_audio_file
# #     except subprocess.CalledProcessError as e:
# #         print(f"Error generating audio for phoneme {phoneme}: {e}")
# #         return None

# # def analyze_phonemes(text):
# #     phonemes = get_phonemes(text)
# #     analysis_results = []
    
# #     for phoneme in phonemes:
# #         phoneme_cleaned = phoneme.strip('[]')
# #         audio_file = play_phoneme_audio(phoneme_cleaned)
# #         analysis_results.append({
# #             "phoneme": phoneme_cleaned,
# #             "audio_file": audio_file,
# #             "feedback": generate_phoneme_analysis(phoneme_cleaned)
# #         })
    
# #     return analysis_results

# # def generate_phoneme_analysis(phoneme):
# #     # Add detailed analysis for each phoneme
# #     analysis = {
# #            's': "The 's' sound is a voiceless alveolar sibilant. It's produced by placing the tip of the tongue close to the ridge behind the upper front teeth and letting the air flow out with a hissing sound. Example: 's' in 'see'.",
# #         't': "The 't' sound is a voiceless alveolar stop. It's produced by placing the tip of the tongue against the ridge behind the upper front teeth and releasing the air quickly. Example: 't' in 'top'.",
# #         'r': "The 'r' sound is a voiced alveolar approximant. It's produced by curling the tip of the tongue slightly without touching the roof of the mouth. Example: 'r' in 'run'.",
# #         'l': "The 'l' sound is a voiced alveolar lateral approximant. It's produced by placing the tip of the tongue against the ridge behind the upper front teeth and letting the air flow around the sides of the tongue. Example: 'l' in 'look'.",
# #         'g': "The 'g' sound is a voiced velar stop. It's produced by raising the back of the tongue to the soft part of the roof of the mouth and releasing the air. Example: 'g' in 'go'.",
# #         'd': "The 'd' sound is a voiced alveolar stop. It's produced by placing the tip of the tongue against the ridge behind the upper front teeth and releasing a voiced sound. Example: 'd' in 'dog'.",
# #         'k': "The 'k' sound is a voiceless velar stop. It's produced by raising the back of the tongue to the soft part of the roof of the mouth and releasing the air quickly. Example: 'k' in 'cat'.",
# #         'f': "The 'f' sound is a voiceless labiodental fricative. It's produced by placing the top front teeth lightly on the lower lip and blowing air out. Example: 'f' in 'fish'.",
# #         'v': "The 'v' sound is a voiced labiodental fricative. It's produced by placing the top front teeth lightly on the lower lip and voicing out. Example: 'v' in 'van'.",
# #         'b': "The 'b' sound is a voiced bilabial stop. It's produced by bringing both lips together and releasing air to make the sound. Example: 'b' in 'bat'.",
# #         'p': "The 'p' sound is a voiceless bilabial stop. It's produced by bringing both lips together and releasing air quickly. Example: 'p' in 'pat'.",
# #         'm': "The 'm' sound is a voiced bilabial nasal. It's produced by pressing the lips together and humming. Example: 'm' in 'man'.",
# #         'n': "The 'n' sound is a voiced alveolar nasal. It's produced by placing the tip of the tongue against the ridge behind the upper front teeth and humming. Example: 'n' in 'net'.",
# #         'ʃ': "The 'ʃ' sound is a voiceless postalveolar fricative. It's produced by placing the tip of the tongue close to the ridge behind the upper front teeth, but slightly further back than for 's', and letting the air flow out with a hissing sound. Example: 'sh' in 'shoe'.",
# #         'ʒ': "The 'ʒ' sound is a voiced postalveolar fricative. It's produced by placing the tip of the tongue close to the ridge behind the upper front teeth, but slightly further back than for 's', and voicing out. Example: 's' in 'measure'.",
# #         'θ': "The 'θ' sound is a voiceless dental fricative. It's produced by placing the tip of the tongue against the upper front teeth and blowing air out. Example: 'th' in 'think'.",
# #         'ð': "The 'ð' sound is a voiced dental fricative. It's produced by placing the tip of the tongue against the upper front teeth and voicing out. Example: 'th' in 'this'.",
# #         'ʧ': "The 'ʧ' sound is a voiceless postalveolar affricate. It's produced by combining the 't' and 'ʃ' sounds. Example: 'ch' in 'chair'.",
# #         'ʤ': "The 'ʤ' sound is a voiced postalveolar affricate. It's produced by combining the 'd' and 'ʒ' sounds. Example: 'j' in 'jump'.",
# #         'ɪ': "The 'ɪ' sound is a near-close near-front unrounded vowel. It's produced by positioning the tongue close to the roof of the mouth but not as close as for the 'i' sound. Example: 'i' in 'sit'.",
# #         'i': "The 'i' sound is a close front unrounded vowel. It's produced by positioning the tongue as close to the roof of the mouth as possible without creating a constriction. Example: 'ee' in 'see'.",
# #         'æ': "The 'æ' sound is a near-open front unrounded vowel. It's produced by positioning the tongue low in the mouth. Example: 'a' in 'cat'.",
# #         'ɛ': "The 'ɛ' sound is an open-mid front unrounded vowel. It's produced by positioning the tongue mid-way between an open and close position. Example: 'e' in 'bed'.",
# #         'ɑ': "The 'ɑ' sound is an open back unrounded vowel. It's produced by positioning the tongue low and at the back of the mouth. Example: 'a' in 'father'.",
# #         'ɔ': "The 'ɔ' sound is an open-mid back rounded vowel. It's produced by positioning the tongue mid-way between an open and close position and rounding the lips. Example: 'aw' in 'saw'.",
# #         'u': "The 'u' sound is a close back rounded vowel. It's produced by positioning the tongue as close to the roof of the mouth as possible and rounding the lips. Example: 'oo' in 'food'.",
# #         'ʊ': "The 'ʊ' sound is a near-close near-back rounded vowel. It's produced by positioning the tongue close to the roof of the mouth but not as close as for the 'u' sound. Example: 'u' in 'put'.",
# #         'ə': "The 'ə' sound is a mid-central vowel, also known as a schwa. It's produced by relaxing the tongue and letting the sound come from the middle of the mouth. Example: 'a' in 'sofa'.",
# #         'ɚ': "The 'ɚ' sound is a rhotacized mid-central vowel. It's produced by curling the tip of the tongue towards the roof of the mouth. Example: 'er' in 'teacher'.",
# #         'h': "The 'h' sound is a voiceless glottal fricative. It's produced by blowing air through the vocal cords without vibrating them. Example: 'h' in 'hat'.",
# #         'w': "The 'w' sound is a voiced labio-velar approximant. It's produced by rounding the lips and voicing out. Example: 'w' in 'water'.",
# #         'j': "The 'j' sound is a voiced palatal approximant. It's produced by raising the middle part of the tongue close to the roof of the mouth and voicing out. Example: 'y' in 'yes'.",
# #         'ŋ': "The 'ŋ' sound is a voiced velar nasal. It's produced by raising the back of the tongue to the soft part of the roof of the mouth and letting the sound come through the nose. Example: 'ng' in 'sing'.",
# #         'z': "The 'z' sound is a voiced alveolar fricative. It's produced by placing the tip of the tongue close to the ridge behind the upper front teeth and letting the air flow out with a buzzing sound. Example: 'z' in 'zoo'.",
# #         'ʔ': "The 'ʔ' sound is a glottal stop. It's produced by briefly stopping the airflow by closing the vocal cords. Example: the sound between the syllables of 'uh-oh'.",
# #         'ʍ': "The 'ʍ' sound is a voiceless labio-velar fricative. It's produced by rounding the lips and blowing air out without voicing. Example: 'wh' in 'which'.",
    
# #     }
# #     return analysis.get(phoneme, "No specific analysis for this phoneme.")

# # if __name__ == "__main__":
# #     # Example usage
# #     text = "Hello, world!"
# #     analysis = analyze_phonemes(text)
# #     for result in analysis:
# #         print(f"Phoneme: {result['phoneme']}, Feedback: {result['feedback']}")
# #         if result['audio_file']:
# #             print(f"Audio file generated: {result['audio_file']}")










# import subprocess
# import re
# import os
# import string
# import logging

# # Ensure logging is set up
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# def sanitize_filename(filename):
#     """
#     Sanitize the filename to be file system and URL safe.
#     """
#     valid_chars = f"-_.() {string.ascii_letters}{string.digits}"
#     return ''.join(c for c in filename if c in valid_chars)

# def get_phonemes(text):
#     """
#     Use the espeak-ng CLI tool to get the phonemes for the given text.
#     """
#     try:
#         # Call the espeak-ng command and capture the output
#         output = subprocess.check_output(["espeak-ng", "--ipa", text])
        
#         # Decode the output manually to avoid encoding issues
#         output = output.decode('utf-8')
        
#         # Extract the phonemes from the output
#         phonemes = re.findall(r'\S+', output)
        
#         return phonemes
#     except subprocess.CalledProcessError as e:
#         logging.error(f"Error running espeak-ng: {e}")
#         return []

# def play_phoneme_audio(phoneme):
#     """
#     Use espeak-ng to generate audio for a given phoneme.
#     """
#     try:
#         sanitized_phoneme = sanitize_filename(phoneme)
#         if not sanitized_phoneme:
#             logging.error(f"Sanitized phoneme is empty for phoneme: {phoneme}")
#             return None

#         # Ensure the directory exists
#         output_dir = os.path.join("static", "audio")
#         os.makedirs(output_dir, exist_ok=True)

#         output_audio_file = os.path.join(output_dir, f"{sanitized_phoneme}.wav")
#         logging.info(f"Generating audio for phoneme: {phoneme} at {output_audio_file}")

#         subprocess.run(["espeak-ng", phoneme, "-w", output_audio_file], check=True)
        
#         if os.path.exists(output_audio_file) and os.path.getsize(output_audio_file) > 0:
#             logging.info(f"Audio file generated: {output_audio_file}")
#             return output_audio_file
#         else:
#             logging.error(f"Failed to generate audio file: {output_audio_file}")
#             return None
#     except subprocess.CalledProcessError as e:
#         logging.error(f"Error generating audio for phoneme {phoneme}: {e}")
#         return None

# def analyze_phonemes(text):
#     words = text.split()
#     analysis_results = []

#     for word in words:
#         phonemes = get_phonemes(word)
#         for phoneme in phonemes:
#             phoneme_cleaned = phoneme.strip('[]')
#             audio_file = play_phoneme_audio(phoneme_cleaned)
#             analysis_results.append({
#                 "word": word,
#                 "phoneme": phoneme_cleaned,
#                 "audio_file": audio_file,
#                 "feedback": generate_phoneme_analysis(phoneme_cleaned)
#             })
    
#     return analysis_results

# # def generate_phoneme_analysis(phoneme):
# #     # Add detailed analysis for each phoneme
# #     analysis = {
# #         # Your phoneme analysis dictionary
# #     }
# #     return analysis.get(phoneme, f"No specific analysis for this phoneme. Example word: '{phoneme}'")



# def generate_phoneme_analysis(phoneme):
#     # Add detailed analysis for each phoneme
#     analysis = {
#         's': "The 's' sound is a voiceless alveolar sibilant. It's produced by placing the tip of the tongue close to the ridge behind the upper front teeth and letting the air flow out with a hissing sound. Example: 's' in 'see'.",
#         't': "The 't' sound is a voiceless alveolar stop. It's produced by placing the tip of the tongue against the ridge behind the upper front teeth and releasing the air quickly. Example: 't' in 'top'.",
#         'r': "The 'r' sound is a voiced alveolar approximant. It's produced by curling the tip of the tongue slightly without touching the roof of the mouth. Example: 'r' in 'run'.",
#         'l': "The 'l' sound is a voiced alveolar lateral approximant. It's produced by placing the tip of the tongue against the ridge behind the upper front teeth and letting the air flow around the sides of the tongue. Example: 'l' in 'look'.",
#         'g': "The 'g' sound is a voiced velar stop. It's produced by raising the back of the tongue to the soft part of the roof of the mouth and releasing the air. Example: 'g' in 'go'.",
#         'd': "The 'd' sound is a voiced alveolar stop. It's produced by placing the tip of the tongue against the ridge behind the upper front teeth and releasing a voiced sound. Example: 'd' in 'dog'.",
#         'k': "The 'k' sound is a voiceless velar stop. It's produced by raising the back of the tongue to the soft part of the roof of the mouth and releasing the air quickly. Example: 'k' in 'cat'.",
#         'f': "The 'f' sound is a voiceless labiodental fricative. It's produced by placing the top front teeth lightly on the lower lip and blowing air out. Example: 'f' in 'fish'.",
#         'v': "The 'v' sound is a voiced labiodental fricative. It's produced by placing the top front teeth lightly on the lower lip and voicing out. Example: 'v' in 'van'.",
#         'b': "The 'b' sound is a voiced bilabial stop. It's produced by bringing both lips together and releasing air to make the sound. Example: 'b' in 'bat'.",
#         'p': "The 'p' sound is a voiceless bilabial stop. It's produced by bringing both lips together and releasing air quickly. Example: 'p' in 'pat'.",
#         'm': "The 'm' sound is a voiced bilabial nasal. It's produced by pressing the lips together and humming. Example: 'm' in 'man'.",
#         'n': "The 'n' sound is a voiced alveolar nasal. It's produced by placing the tip of the tongue against the ridge behind the upper front teeth and humming. Example: 'n' in 'net'.",
#         'ʃ': "The 'ʃ' sound is a voiceless postalveolar fricative. It's produced by placing the tip of the tongue close to the ridge behind the upper front teeth, but slightly further back than for 's', and letting the air flow out with a hissing sound. Example: 'sh' in 'shoe'.",
#         'ʒ': "The 'ʒ' sound is a voiced postalveolar fricative. It's produced by placing the tip of the tongue close to the ridge behind the upper front teeth, but slightly further back than for 's', and voicing out. Example: 's' in 'measure'.",
#         'θ': "The 'θ' sound is a voiceless dental fricative. It's produced by placing the tip of the tongue against the upper front teeth and blowing air out. Example: 'th' in 'think'.",
#         'ð': "The 'ð' sound is a voiced dental fricative. It's produced by placing the tip of the tongue against the upper front teeth and voicing out. Example: 'th' in 'this'.",
#         'ʧ': "The 'ʧ' sound is a voiceless postalveolar affricate. It's produced by combining the 't' and 'ʃ' sounds. Example: 'ch' in 'chair'.",
#         'ʤ': "The 'ʤ' sound is a voiced postalveolar affricate. It's produced by combining the 'd' and 'ʒ' sounds. Example: 'j' in 'jump'.",
#         'ɪ': "The 'ɪ' sound is a near-close near-front unrounded vowel. It's produced by positioning the tongue close to the roof of the mouth but not as close as for the 'i' sound. Example: 'i' in 'sit'.",
#         'i': "The 'i' sound is a close front unrounded vowel. It's produced by positioning the tongue as close to the roof of the mouth as possible without creating a constriction. Example: 'ee' in 'see'.",
#         'æ': "The 'æ' sound is a near-open front unrounded vowel. It's produced by positioning the tongue low in the mouth. Example: 'a' in 'cat'.",
#         'ɛ': "The 'ɛ' sound is an open-mid front unrounded vowel. It's produced by positioning the tongue mid-way between an open and close position. Example: 'e' in 'bed'.",
#         'ɑ': "The 'ɑ' sound is an open back unrounded vowel. It's produced by positioning the tongue low and at the back of the mouth. Example: 'a' in 'father'.",
#         'ɔ': "The 'ɔ' sound is an open-mid back rounded vowel. It's produced by positioning the tongue mid-way between an open and close position and rounding the lips. Example: 'aw' in 'saw'.",
#         'u': "The 'u' sound is a close back rounded vowel. It's produced by positioning the tongue as close to the roof of the mouth as possible and rounding the lips. Example: 'oo' in 'food'.",
#         'ʊ': "The 'ʊ' sound is a near-close near-back rounded vowel. It's produced by positioning the tongue close to the roof of the mouth but not as close as for the 'u' sound. Example: 'u' in 'put'.",
#         'ə': "The 'ə' sound is a mid-central vowel, also known as a schwa. It's produced by relaxing the tongue and letting the sound come from the middle of the mouth. Example: 'a' in 'sofa'.",
#         'ɚ': "The 'ɚ' sound is a rhotacized mid-central vowel. It's produced by curling the tip of the tongue towards the roof of the mouth. Example: 'er' in 'teacher'.",
#         'h': "The 'h' sound is a voiceless glottal fricative. It's produced by blowing air through the vocal cords without vibrating them. Example: 'h' in 'hat'.",
#         'w': "The 'w' sound is a voiced labio-velar approximant. It's produced by rounding the lips and voicing out. Example: 'w' in 'water'.",
#         'j': "The 'j' sound is a voiced palatal approximant. It's produced by raising the middle part of the tongue close to the roof of the mouth and voicing out. Example: 'y' in 'yes'.",
#         'ŋ': "The 'ŋ' sound is a voiced velar nasal. It's produced by raising the back of the tongue to the soft part of the roof of the mouth and letting the sound come through the nose. Example: 'ng' in 'sing'.",
#         'z': "The 'z' sound is a voiced alveolar fricative. It's produced by placing the tip of the tongue close to the ridge behind the upper front teeth and letting the air flow out with a buzzing sound. Example: 'z' in 'zoo'.",
#         'ʔ': "The 'ʔ' sound is a glottal stop. It's produced by briefly stopping the airflow by closing the vocal cords. Example: the sound between the syllables of 'uh-oh'.",
#         'ʍ': "The 'ʍ' sound is a voiceless labio-velar fricative. It's produced by rounding the lips and blowing air out without voicing. Example: 'wh' in 'which'.",
#         'ˈɪn': "The 'ˈɪn' sound is a stressed near-close near-front unrounded vowel. Example: 'in'.",
#         'ˈeɪ': "The 'ˈeɪ' sound is a stressed close-mid front unrounded vowel. Example: 'a'.",
#         'bˈɜːd': "The 'bˈɜːd' sound is a voiced bilabial stop followed by a stressed open-mid central unrounded vowel. Example: 'bird'.",
#         'ðˈə': "The 'ðˈə' sound is a voiced dental fricative followed by a stressed mid-central vowel. Example: 'the'.",
#         'dˈɒɡ': "The 'dˈɒɡ' sound is a voiced alveolar stop followed by a stressed open back rounded vowel. Example: 'dog'.",
#     }
#     return analysis.get(phoneme, f"No specific analysis for this phoneme. Example word: '{phoneme}'")



# import subprocess
# import re
# import os
# import string
# import logging

# # Ensure logging is set up
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# def sanitize_filename(filename):
#     """
#     Sanitize the filename to be file system and URL safe.
#     """
#     valid_chars = f"-_.() {string.ascii_letters}{string.digits}"
#     return ''.join(c for c in filename if c in valid_chars)

# def get_phonemes(text):
#     """
#     Use the espeak-ng CLI tool to get the phonemes for the given text.
#     """
#     try:
#         # Call the espeak-ng command and capture the output
#         output = subprocess.check_output(["espeak-ng", "--ipa", text])
        
#         # Decode the output manually to avoid encoding issues
#         output = output.decode('utf-8')
        
#         # Extract the phonemes from the output
#         phonemes = re.findall(r'\S+', output)
        
#         return phonemes
#     except subprocess.CalledProcessError as e:
#         logging.error(f"Error running espeak-ng: {e}")
#         return []

# def play_phoneme_audio(phoneme):
#     """
#     Use espeak-ng to generate audio for a given phoneme.
#     """
#     try:
#         sanitized_phoneme = sanitize_filename(phoneme)
#         if not sanitized_phoneme:
#             logging.error(f"Sanitized phoneme is empty for phoneme: {phoneme}")
#             return None

#         # Ensure the directory exists
#         output_dir = os.path.join("static", "audio")
#         os.makedirs(output_dir, exist_ok=True)

#         output_audio_file = os.path.join(output_dir, f"{sanitized_phoneme}.wav")
#         logging.info(f"Generating audio for phoneme: {phoneme} at {output_audio_file}")

#         subprocess.run(["espeak-ng", phoneme, "-w", output_audio_file], check=True)
        
#         if os.path.exists(output_audio_file) and os.path.getsize(output_audio_file) > 0:
#             logging.info(f"Audio file generated: {output_audio_file}")
#             return output_audio_file
#         else:
#             logging.error(f"Failed to generate audio file: {output_audio_file}")
#             return None
#     except subprocess.CalledProcessError as e:
#         logging.error(f"Error generating audio for phoneme {phoneme}: {e}")
#         return None

# def analyze_phonemes(text):
#     words = text.split()
#     analysis_results = []

#     for word in words:
#         phonemes = get_phonemes(word)
#         for phoneme in phonemes:
#             phoneme_cleaned = phoneme.strip('[]')
#             audio_file = play_phoneme_audio(phoneme_cleaned)
#             analysis_results.append({
#                 "word": word,
#                 "phoneme": phoneme_cleaned,
#                 "audio_file": audio_file,
#                 "feedback": generate_phoneme_analysis(phoneme_cleaned)
#             })
    
#     return analysis_results

# def generate_phoneme_analysis(phoneme):
#     # Add detailed analysis for each phoneme
#     analysis = {
#         's': "The 's' sound is a voiceless alveolar sibilant. It's produced by placing the tip of the tongue close to the ridge behind the upper front teeth and letting the air flow out with a hissing sound. Example: 's' in 'see'.",
#         't': "The 't' sound is a voiceless alveolar stop. It's produced by placing the tip of the tongue against the ridge behind the upper front teeth and releasing the air quickly. Example: 't' in 'top'.",
#         'r': "The 'r' sound is a voiced alveolar approximant. It's produced by curling the tip of the tongue slightly without touching the roof of the mouth. Example: 'r' in 'run'.",
#         'l': "The 'l' sound is a voiced alveolar lateral approximant. It's produced by placing the tip of the tongue against the ridge behind the upper front teeth and letting the air flow around the sides of the tongue. Example: 'l' in 'look'.",
#         'g': "The 'g' sound is a voiced velar stop. It's produced by raising the back of the tongue to the soft part of the roof of the mouth and releasing the air. Example: 'g' in 'go'.",
#         'd': "The 'd' sound is a voiced alveolar stop. It's produced by placing the tip of the tongue against the ridge behind the upper front teeth and releasing a voiced sound. Example: 'd' in 'dog'.",
#         'k': "The 'k' sound is a voiceless velar stop. It's produced by raising the back of the tongue to the soft part of the roof of the mouth and releasing the air quickly. Example: 'k' in 'cat'.",
#         'f': "The 'f' sound is a voiceless labiodental fricative. It's produced by placing the top front teeth lightly on the lower lip and blowing air out. Example: 'f' in 'fish'.",
#         'v': "The 'v' sound is a voiced labiodental fricative. It's produced by placing the top front teeth lightly on the lower lip and voicing out. Example: 'v' in 'van'.",
#         'b': "The 'b' sound is a voiced bilabial stop. It's produced by bringing both lips together and releasing air to make the sound. Example: 'b' in 'bat'.",
#         'p': "The 'p' sound is a voiceless bilabial stop. It's produced by bringing both lips together and releasing air quickly. Example: 'p' in 'pat'.",
#         'm': "The 'm' sound is a voiced bilabial nasal. It's produced by pressing the lips together and humming. Example: 'm' in 'man'.",
#         'n': "The 'n' sound is a voiced alveolar nasal. It's produced by placing the tip of the tongue against the ridge behind the upper front teeth and humming. Example: 'n' in 'net'.",
#         'ʃ': "The 'ʃ' sound is a voiceless postalveolar fricative. It's produced by placing the tip of the tongue close to the ridge behind the upper front teeth, but slightly further back than for 's', and letting the air flow out with a hissing sound. Example: 'sh' in 'shoe'.",
#         'ʒ': "The 'ʒ' sound is a voiced postalveolar fricative. It's produced by placing the tip of the tongue close to the ridge behind the upper front teeth, but slightly further back than for 's', and voicing out. Example: 's' in 'measure'.",
#         'θ': "The 'θ' sound is a voiceless dental fricative. It's produced by placing the tip of the tongue against the upper front teeth and blowing air out. Example: 'th' in 'think'.",
#         'ð': "The 'ð' sound is a voiced dental fricative. It's produced by placing the tip of the tongue against the upper front teeth and voicing out. Example: 'th' in 'this'.",
#         'ʧ': "The 'ʧ' sound is a voiceless postalveolar affricate. It's produced by combining the 't' and 'ʃ' sounds. Example: 'ch' in 'chair'.",
#         'ʤ': "The 'ʤ' sound is a voiced postalveolar affricate. It's produced by combining the 'd' and 'ʒ' sounds. Example: 'j' in 'jump'.",
#         'ɪ': "The 'ɪ' sound is a near-close near-front unrounded vowel. It's produced by positioning the tongue close to the roof of the mouth but not as close as for the 'i' sound. Example: 'i' in 'sit'.",
#         'i': "The 'i' sound is a close front unrounded vowel. It's produced by positioning the tongue as close to the roof of the mouth as possible without creating a constriction. Example: 'ee' in 'see'.",
#         'æ': "The 'æ' sound is a near-open front unrounded vowel. It's produced by positioning the tongue low in the mouth. Example: 'a' in 'cat'.",
#         'ɛ': "The 'ɛ' sound is an open-mid front unrounded vowel. It's produced by positioning the tongue mid-way between an open and close position. Example: 'e' in 'bed'.",
#         'ɑ': "The 'ɑ' sound is an open back unrounded vowel. It's produced by positioning the tongue low and at the back of the mouth. Example: 'a' in 'father'.",
#         'ɔ': "The 'ɔ' sound is an open-mid back rounded vowel. It's produced by positioning the tongue mid-way between an open and close position and rounding the lips. Example: 'aw' in 'saw'.",
#         'u': "The 'u' sound is a close back rounded vowel. It's produced by positioning the tongue as close to the roof of the mouth as possible and rounding the lips. Example: 'oo' in 'food'.",
#         'ʊ': "The 'ʊ' sound is a near-close near-back rounded vowel. It's produced by positioning the tongue close to the roof of the mouth but not as close as for the 'u' sound. Example: 'u' in 'put'.",
#         'ə': "The 'ə' sound is a mid-central vowel, also known as a schwa. It's produced by relaxing the tongue and letting the sound come from the middle of the mouth. Example: 'a' in 'sofa'.",
#         'ɚ': "The 'ɚ' sound is a rhotacized mid-central vowel. It's produced by curling the tip of the tongue towards the roof of the mouth. Example: 'er' in 'teacher'.",
#         'h': "The 'h' sound is a voiceless glottal fricative. It's produced by blowing air through the vocal cords without vibrating them. Example: 'h' in 'hat'.",
#         'w': "The 'w' sound is a voiced labio-velar approximant. It's produced by rounding the lips and voicing out. Example: 'w' in 'water'.",
#         'j': "The 'j' sound is a voiced palatal approximant. It's produced by raising the middle part of the tongue close to the roof of the mouth and voicing out. Example: 'y' in 'yes'.",
#         'ŋ': "The 'ŋ' sound is a voiced velar nasal. It's produced by raising the back of the tongue to the soft part of the roof of the mouth and letting the sound come through the nose. Example: 'ng' in 'sing'.",
#         'z': "The 'z' sound is a voiced alveolar fricative. It's produced by placing the tip of the tongue close to the ridge behind the upper front teeth and letting the air flow out with a buzzing sound. Example: 'z' in 'zoo'.",
#         'ʔ': "The 'ʔ' sound is a glottal stop. It's produced by briefly stopping the airflow by closing the vocal cords. Example: the sound between the syllables of 'uh-oh'.",
#         'ʍ': "The 'ʍ' sound is a voiceless labio-velar fricative. It's produced by rounding the lips and blowing air out without voicing. Example: 'wh' in 'which'.",
#         'ˈɪn': "The 'ˈɪn' sound is a stressed near-close near-front unrounded vowel. Example: 'in'.",
#         'ˈeɪ': "The 'ˈeɪ' sound is a stressed close-mid front unrounded vowel. Example: 'a'.",
#         'bˈɜːd': "The 'bˈɜːd' sound is a voiced bilabial stop followed by a stressed open-mid central unrounded vowel. Example: 'bird'.",
#         'ðˈə': "The 'ðˈə' sound is a voiced dental fricative followed by a stressed mid-central vowel. Example: 'the'.",
#         'dˈɒɡ': "The 'dˈɒɡ' sound is a voiced alveolar stop followed by a stressed open back rounded vowel. Example: 'dog'.",
#     }
#     return analysis.get(phoneme, f"No specific analysis for this phoneme. Example word: '{phoneme}'")





import subprocess
import re
import os
import string
import logging

# Ensure logging is set up
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def sanitize_filename(filename):
    valid_chars = f"-_.() {string.ascii_letters}{string.digits}"
    return ''.join(c for c in filename if c in valid_chars)

def get_phonemes(text):
    try:
        output = subprocess.check_output(["espeak-ng", "--ipa", text])
        output = output.decode('utf-8')
        phonemes = re.findall(r'\S+', output)
        return phonemes
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running espeak-ng: {e}")
        return []

def play_phoneme_audio(phoneme):
    try:
        sanitized_phoneme = sanitize_filename(phoneme)
        if not sanitized_phoneme:
            logging.error(f"Sanitized phoneme is empty for phoneme: {phoneme}")
            return None

        output_dir = os.path.join("static", "audio")
        os.makedirs(output_dir, exist_ok=True)

        output_audio_file = os.path.join(output_dir, f"{sanitized_phoneme}.wav")
        logging.info(f"Generating audio for phoneme: {phoneme} at {output_audio_file}")

        subprocess.run(["espeak-ng", phoneme, "-w", output_audio_file], check=True)
        
        if os.path.exists(output_audio_file) and os.path.getsize(output_audio_file) > 0:
            logging.info(f"Audio file generated: {output_audio_file}")
            return f"audio/{sanitized_phoneme}.wav"
        else:
            logging.error(f"Failed to generate audio file: {output_audio_file}")
            return None
    except subprocess.CalledProcessError as e:
        logging.error(f"Error generating audio for phoneme {phoneme}: {e}")
        return None

def analyze_phonemes(text):
    words = text.split()
    analysis_results = []

    for word in words:
        phonemes = get_phonemes(word)
        for phoneme in phonemes:
            phoneme_cleaned = phoneme.strip('[]')
            audio_file = play_phoneme_audio(phoneme_cleaned)
            analysis_results.append({
                "word": word,
                "phoneme": phoneme_cleaned,
                "audio_file": audio_file,
                "feedback": generate_phoneme_analysis(phoneme_cleaned)
            })
    
    return analysis_results

def generate_phoneme_analysis(phoneme):
    analysis = {
        's': "The 's' sound is a voiceless alveolar sibilant. It's produced by placing the tip of the tongue close to the ridge behind the upper front teeth and letting the air flow out with a hissing sound. Example: 's' in 'see'.",
        't': "The 't' sound is a voiceless alveolar stop. It's produced by placing the tip of the tongue against the ridge behind the upper front teeth and releasing the air quickly. Example: 't' in 'top'.",
        'r': "The 'r' sound is a voiced alveolar approximant. It's produced by curling the tip of the tongue slightly without touching the roof of the mouth. Example: 'r' in 'run'.",
        'l': "The 'l' sound is a voiced alveolar lateral approximant. It's produced by placing the tip of the tongue against the ridge behind the upper front teeth and letting the air flow around the sides of the tongue. Example: 'l' in 'look'.",
        'g': "The 'g' sound is a voiced velar stop. It's produced by raising the back of the tongue to the soft part of the roof of the mouth and releasing the air. Example: 'g' in 'go'.",
        'd': "The 'd' sound is a voiced alveolar stop. It's produced by placing the tip of the tongue against the ridge behind the upper front teeth and releasing a voiced sound. Example: 'd' in 'dog'.",
        'k': "The 'k' sound is a voiceless velar stop. It's produced by raising the back of the tongue to the soft part of the roof of the mouth and releasing the air quickly. Example: 'k' in 'cat'.",
        'f': "The 'f' sound is a voiceless labiodental fricative. It's produced by placing the top front teeth lightly on the lower lip and blowing air out. Example: 'f' in 'fish'.",
        'v': "The 'v' sound is a voiced labiodental fricative. It's produced by placing the top front teeth lightly on the lower lip and voicing out. Example: 'v' in 'van'.",
        'b': "The 'b' sound is a voiced bilabial stop. It's produced by bringing both lips together and releasing air to make the sound. Example: 'b' in 'bat'.",
        'p': "The 'p' sound is a voiceless bilabial stop. It's produced by bringing both lips together and releasing air quickly. Example: 'p' in 'pat'.",
        'm': "The 'm' sound is a voiced bilabial nasal. It's produced by pressing the lips together and humming. Example: 'm' in 'man'.",
        'n': "The 'n' sound is a voiced alveolar nasal. It's produced by placing the tip of the tongue against the ridge behind the upper front teeth and humming. Example: 'n' in 'net'.",
        'ʃ': "The 'ʃ' sound is a voiceless postalveolar fricative. It's produced by placing the tip of the tongue close to the ridge behind the upper front teeth, but slightly further back than for 's', and letting the air flow out with a hissing sound. Example: 'sh' in 'shoe'.",
        'ʒ': "The 'ʒ' sound is a voiced postalveolar fricative. It's produced by placing the tip of the tongue close to the ridge behind the upper front teeth, but slightly further back than for 's', and voicing out. Example: 's' in 'measure'.",
        'θ': "The 'θ' sound is a voiceless dental fricative. It's produced by placing the tip of the tongue against the upper front teeth and blowing air out. Example: 'th' in 'think'.",
        'ð': "The 'ð' sound is a voiced dental fricative. It's produced by placing the tip of the tongue against the upper front teeth and voicing out. Example: 'th' in 'this'.",
        'ʧ': "The 'ʧ' sound is a voiceless postalveolar affricate. It's produced by combining the 't' and 'ʃ' sounds. Example: 'ch' in 'chair'.",
        'ʤ': "The 'ʤ' sound is a voiced postalveolar affricate. It's produced by combining the 'd' and 'ʒ' sounds. Example: 'j' in 'jump'.",
        'ɪ': "The 'ɪ' sound is a near-close near-front unrounded vowel. It's produced by positioning the tongue close to the roof of the mouth but not as close as for the 'i' sound. Example: 'i' in 'sit'.",
        'i': "The 'i' sound is a close front unrounded vowel. It's produced by positioning the tongue as close to the roof of the mouth as possible without creating a constriction. Example: 'ee' in 'see'.",
        'æ': "The 'æ' sound is a near-open front unrounded vowel. It's produced by positioning the tongue low in the mouth. Example: 'a' in 'cat'.",
        'ɛ': "The 'ɛ' sound is an open-mid front unrounded vowel. It's produced by positioning the tongue mid-way between an open and close position. Example: 'e' in 'bed'.",
        'ɑ': "The 'ɑ' sound is an open back unrounded vowel. It's produced by positioning the tongue low and at the back of the mouth. Example: 'a' in 'father'.",
        'ɔ': "The 'ɔ' sound is an open-mid back rounded vowel. It's produced by positioning the tongue mid-way between an open and close position and rounding the lips. Example: 'aw' in 'saw'.",
        'u': "The 'u' sound is a close back rounded vowel. It's produced by positioning the tongue as close to the roof of the mouth as possible and rounding the lips. Example: 'oo' in 'food'.",
        'ʊ': "The 'ʊ' sound is a near-close near-back rounded vowel. It's produced by positioning the tongue close to the roof of the mouth but not as close as for the 'u' sound. Example: 'u' in 'put'.",
        'ə': "The 'ə' sound is a mid-central vowel, also known as a schwa. It's produced by relaxing the tongue and letting the sound come from the middle of the mouth. Example: 'a' in 'sofa'.",
        'ɚ': "The 'ɚ' sound is a rhotacized mid-central vowel. It's produced by curling the tip of the tongue towards the roof of the mouth. Example: 'er' in 'teacher'.",
        'h': "The 'h' sound is a voiceless glottal fricative. It's produced by blowing air through the vocal cords without vibrating them. Example: 'h' in 'hat'.",
        'w': "The 'w' sound is a voiced labio-velar approximant. It's produced by rounding the lips and voicing out. Example: 'w' in 'water'.",
        'j': "The 'j' sound is a voiced palatal approximant. It's produced by raising the middle part of the tongue close to the roof of the mouth and voicing out. Example: 'y' in 'yes'.",
        'ŋ': "The 'ŋ' sound is a voiced velar nasal. It's produced by raising the back of the tongue to the soft part of the roof of the mouth and letting the sound come through the nose. Example: 'ng' in 'sing'.",
        'z': "The 'z' sound is a voiced alveolar fricative. It's produced by placing the tip of the tongue close to the ridge behind the upper front teeth and letting the air flow out with a buzzing sound. Example: 'z' in 'zoo'.",
        'ʔ': "The 'ʔ' sound is a glottal stop. It's produced by briefly stopping the airflow by closing the vocal cords. Example: the sound between the syllables of 'uh-oh'.",
        'ʍ': "The 'ʍ' sound is a voiceless labio-velar fricative. It's produced by rounding the lips and blowing air out without voicing. Example: 'wh' in 'which'.",
        'ˈɪn': "The 'ˈɪn' sound is a stressed near-close near-front unrounded vowel. Example: 'in'.",
        'ˈeɪ': "The 'ˈeɪ' sound is a stressed close-mid front unrounded vowel. Example: 'a'.",
        'bˈɜːd': "The 'bˈɜːd' sound is a voiced bilabial stop followed by a stressed open-mid central unrounded vowel. Example: 'bird'.",
        'ðˈə': "The 'ðˈə' sound is a voiced dental fricative followed by a stressed mid-central vowel. Example: 'the'.",
        'dˈɒɡ': "The 'dˈɒɡ' sound is a voiced alveolar stop followed by a stressed open back rounded vowel. Example: 'dog'.",
    }
    return analysis.get(phoneme, f"No specific analysis for this phoneme. Example word: '{phoneme}'")

