import sounddevice as sd
import numpy as np
import webrtcvad
import collections
from faster_whisper import WhisperModel
from .noise import noise_cleaning

model = WhisperModel("large-v3", device="cuda", compute_type="float16")

def auto_listening(
    sample_rate=16000,
    silence_ms=1000,            # ms di silenzio per capire che hai finito
    frame_ms=30                 # dimensione frame per VAD
):
    vad = webrtcvad.Vad(2)  # aggressività 0-3
    frame_size = int(sample_rate * frame_ms / 1000)
    
    # Buffer scorrevole per rilevare silenzio
    silence_frames = int(silence_ms / frame_ms)
    ring_buffer = collections.deque(maxlen=silence_frames)
    
    frames_audio = []
    listening = False
    
    print("Attesa input vocale...")
    
    with sd.RawInputStream(samplerate=sample_rate, channels=1,
                            dtype="int16", blocksize=frame_size) as stream:
        while True:
            frame, _ = stream.read(frame_size)
            frame_bytes = bytes(frame)
            
            is_speech = vad.is_speech(frame_bytes, sample_rate)
            
            if is_speech:
                if not listening:
                    print("Sto ascoltando...")
                    listening = True
                frames_audio.append(np.frombuffer(frame_bytes, dtype=np.int16))
                ring_buffer.clear()
            else:
                if listening:
                    ring_buffer.append(frame_bytes)
                    frames_audio.append(np.frombuffer(frame_bytes, dtype=np.int16))
                    
                    if len(ring_buffer) == ring_buffer.maxlen:
                        print("Fine dell'ascolto.")
                        break
    
    if not frames_audio:
        return None
    
    audio = np.concatenate(frames_audio).astype(np.float32) / 32768.0
    return audio

def transcribe(audio):
    audio = noise_cleaning(audio) # Pulisce audio dal rumore di fondo
    segments, _ = model.transcribe(
        audio,
        language="it",
        beam_size=10,               # più alto = più accurato ma lento
        best_of=5,                  # prova 5 candidati e prende il migliore
        temperature=0.0,            # 0 = deterministico, meno allucinazioni
        condition_on_previous_text=False,  # evita che inventi parole basandosi sul contesto precedente
        vad_filter=True,
        vad_parameters=dict(
            min_silence_duration_ms=300,
            speech_pad_ms=200       # aggiunge un po' di audio prima/dopo il parlato
        )
    )
    return " ".join([seg.text for seg in segments]).strip()