# Jarvis Project

## Informazioni

Il progetto Jarvis è un'AI vocale in grado di aiutarti nelle task giornaliere di qualsiasi tipo. Jarvis è in grado di aprire applicazioni, scrivere testi, aprire siti, fare ricerche e ovviamente rispondere alle tue domande.
Nuovi aggiornamenti porteranno nuove funzioni e migliorie generali a Jarvis.

## Come funziona?

### Idea di base

```text
Utente: "Apri YouTube"
            │
            ▼
┌──────────────────────┐
│  AI riceve messaggio │
│  + lista tool        │
└────────┬─────────────┘
         │
         │ decide di usare "open_browser"
         │
         ▼
┌──────────────────────────────────────┐
│  Risponde con:                       │
│  tool_call: open_browser             │
│  args: { url: "https://youtube.com"} │
└────────┬─────────────────────────────┘
         │
         ▼
┌───────────────────────┐
│  Python esegue        │
│  webbrowser.open(url) │
│  → browser si apre    │
└────────┬──────────────┘
         │
         │ risultato: "Browser aperto"
         │
         ▼
┌──────────────────────┐
│  AI riceve risultato │
│  formula risposta    │
└────────┬─────────────┘
         │
         ▼
Jarvis: "Fatto! Ho aperto YouTube."
```

Jarvis viene attivato tramite comando vocale ed esegue le istruzioni date a voce.

## Installazione

Al momento non sono presenti file binari eseguibili.

Fino al momento della distribuzione è possibile eseguire il **codice sorgente** scaricando i requisiti necessari per far funzionare il programma:

1. Clona il repository:

    ```bash
    git clone https://github.com/Axel00x/jarvis-project

    cd jarvis-project
    ```

2. Installa i requisiti:

    ```bash
    pip install -r requirements.txt
    ```

3. Esegui il programma:

    ```bash
    python main.py
    ```
