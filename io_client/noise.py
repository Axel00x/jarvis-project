import noisereduce as nr

def noise_cleaning(audio, sample_rate=16000):
    # Riduci prop_decrease per evitare voci metalliche
    clean_audio = nr.reduce_noise(
        y=audio,
        sr=sample_rate,
        prop_decrease=0.5,      # Meno aggressivo (0.5 invece di 0.9)
        stationary=True         # Salva la CPU!
    )
    return clean_audio