import noisereduce as nr

def noise_cleaning(audio, sample_rate=16000):
    # Usa il primo mezzo secondo come profilo del rumore
    noise_sample = audio[:sample_rate // 2]
    
    clean_audio = nr.reduce_noise(
        y=audio,
        sr=sample_rate,
        y_noise=noise_sample,
        prop_decrease=0.9,      # quanto rumore rimuovere (0-1)
        stationary=False        # True per rumori costanti (ventola), False per rumori variabili
    )
    return clean_audio