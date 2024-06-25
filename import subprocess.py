import subprocess
import os

def sanitize_filename(filename):
    """
    Sanitize the filename to be file system and URL safe.
    """
    valid_chars = f"-_.() (string.ascii_letters)(string.digits)"
    return ''.join(c for c in filename if c in valid_chars)

def play_phoneme_audio(phoneme):
    """
    Use espeak-ng to generate audio for a given phoneme.
    """
    try:
        sanitized_phoneme = sanitize_filename(phoneme)
        if not sanitized_phoneme:
            print(f"Sanitized phoneme is empty for phoneme: {phoneme}")
            return None

        # Ensure the directory exists
        output_dir = os.path.join("static", "audio")
        os.makedirs(output_dir, exist_ok=True)

        output_audio_file = os.path.join(output_dir, f"{sanitized_phoneme}.wav")
        print(f"Generating audio for phoneme: {phoneme} at {output_audio_file}")

        subprocess.run(["espeak-ng", phoneme, "-w", output_audio_file], check=True)
        
        if os.path.exists(output_audio_file) and os.path.getsize(output_audio_file) > 0:
            print(f"Audio file generated: {output_audio_file}")
            return output_audio_file
        else:
            print(f"Failed to generate audio file: {output_audio_file}")
            return None
    except subprocess.CalledProcessError as e:
        print(f"Error generating audio for phoneme {phoneme}: {e}")
        return None

# Example test
phoneme = 'hello'
play_phoneme_audio(phoneme)
