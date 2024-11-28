# Questo codice è stato creato da Guido Maria Caruso, 2024.

import sounddevice as sd
import numpy as np
from psychopy import visual, event, core
import pandas as pd
import os
import random
from openpyxl import load_workbook

def play_sound():
    duration = 1.0  
    frequency = 440.0  
    sample_rate = 44100  
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    sound_wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    sd.play(sound_wave, sample_rate)
    sd.wait()

def read_excel_alternative(file_path):
    wb = load_workbook(file_path)
    sheet = wb.active
    data = sheet.values
    columns = next(data)[0:]
    df = pd.DataFrame(data, columns=columns)
    return df

def run_experiment(num_trials):
    durations = [20, 25, 35, 45, 100]
    task_names = ['blocco_20s', 'blocco_25s', 'blocco_35s', 'blocco_45s', 'blocco_100s']

    fixed_trial = [0]
    random_trials = list(range(1, num_trials))
    random.shuffle(random_trials)
    trial_indices = fixed_trial + random_trials

    win = visual.Window([1366, 768], color=[0.5, 0.5, 0.5], fullscr=True)  

    results_file = r'C:\Users\SALVO DIANA\Desktop\counting GITHUB.xls'
    if os.path.isfile(results_file):
        df = read_excel_alternative(results_file)
    else:
        df = pd.DataFrame(columns=['Codice Partecipante', 'Task', 'Counting', 'VAS'])

    codice_soggetto = ''
    messaggio_codice = visual.TextStim(win, text='Inserisci il codice del soggetto:', color='black', height=0.05)
    input_box = visual.Rect(win, width=0.5, height=0.1, pos=(0, -0.3), fillColor='white')
    input_text = visual.TextStim(win, text=codice_soggetto, color='black', pos=(0, -0.3), height=0.05)

    while True:
        messaggio_codice.draw()
        input_box.draw()
        input_text.draw()
        win.flip()

        keys = event.getKeys()
        if 'return' in keys:
            if codice_soggetto:
                break
        elif keys:
            if keys[0] == 'backspace':
                codice_soggetto = codice_soggetto[:-1]
            else:
                codice_soggetto += keys[0]
            input_text.text = codice_soggetto

        if 'escape' in keys:
            win.close()
            core.quit()

    messaggio_benvenuto = visual.TextStim(win, text="Benvenuto/a!\n\nQuesto compito è costituito da 4 blocchi più uno di prova in cui familiarizzerai con il compito. Tra un blocco ed un altro puoi fare una pausa.\n\nPremere barra spaziatrice per continuare.", color='black', pos=(0, 0), height=0.06)
    messaggio_benvenuto.draw()
    win.flip()
    event.waitKeys(keyList=['space'])

    messaggio_introduttivo = visual.TextStim(win, text="Durante ciascun blocco sentirai due suoni (due BEEP) che costituiranno rispettivamente il segnale di INIZIO e il segnale di FINE del compito.\n\nDurante i due BEEP dovrai:\n\n - Rimanere rilassata/o\n\n - tenere gli OCCHI CHIUSI. \n\n - posizionare le MANI SUI BRACCIOLI. \n\n - NON ACCAVALLARE LE GAMBE \n\n - NON PARLARE.\n\ e \n - CONCENTRARTI SULLE TUE SENSAZIONI CORPOREE.\n\n Premi la barra spaziatrice per continuare.", color='black', pos=(0, 0), height=0.06)
    messaggio_introduttivo.draw()
    win.flip()
    event.waitKeys(keyList=['space'])

    messaggio_introduttivo2 = visual.TextStim(win, text="IMPORTANTE\n\n Durante i due BEEP il tuo compito sarà quello di CONTARE IL NUMERO DI BATTITI DEL TUO CUORE\n\n (NON POTRAI SENTIRE IL POLSO)\n\n\n Premi la barra spaziatrice per continuare.", color='black', pos=(0, 0), height=0.06)
    messaggio_introduttivo2.draw()
    win.flip()
    event.waitKeys(keyList=['space'])

    messaggio_introduttivo3 = visual.TextStim(win, text="Dopo aver ascoltato il secondo BEEP dovrai:\n\n - APRIRE GLI OCCHI\n\n - RIPORTARE il numero di battiti (del cuore) che hai PERCEPITO durante il periodo di tempo intercorso tra il primo ed il secondo BEEP.\n\n\n Premi barra spaziatrice per continuare.", color='black', pos=(0, 0), height=0.06)
    messaggio_introduttivo3.draw()
    win.flip()
    event.waitKeys(keyList=['space'])

    messaggio_prova = visual.TextStim(win, text="Ora faremo qualche prova per farti capire\n\n COME DARE LA RISPOSTA.\n\n\n Premi barra spaziatrice per continuare.", color='black', pos=(0, 0), height=0.06)
    messaggio_prova.draw()
    win.flip()
    event.waitKeys(keyList=['space'])

    messaggio_inserimento_prova = visual.TextStim(win, text='UTILIZZANDO LA TASTIERA NUMERICA DIGITA IL NUMERO DI BATTITI PERCEPITI (un numero a tuo piacimento) e premi INVIO per continuare:', color='black', pos=(0, 0.2), height=0.06)
    input_box_prova = visual.Rect(win, width=0.5, height=0.1, pos=(0, -0.1), fillColor='white')
    input_battiti_prova = ''
    input_text_prova = visual.TextStim(win, text=input_battiti_prova, color='black', pos=(0, -0.1))

    while True:
        messaggio_inserimento_prova.draw()
        input_box_prova.draw()
        input_text_prova.draw()
        win.flip()

        keys = event.getKeys()
        if 'return' in keys:
            break
        elif keys:
            if keys[0] == 'backspace':
                input_battiti_prova = input_battiti_prova[:-1]
            else:
                input_battiti_prova += keys[0]
            input_text_prova.text = input_battiti_prova

        if 'escape' in keys:
            win.close()
            core.quit()

    messaggio_controllo_segnale = visual.TextStim(win, text='Prima di continuare controlleremo che non ci siano problemi nella registrazione del segnale.\nPremi la barra spaziatrice per continuare.', color='black')
    messaggio_controllo_segnale.draw()
    win.flip()
    event.waitKeys(keyList=['space'])

    messaggio_inizio_blocco = visual.TextStim(win, text='Premi la BARRA SPAZIATRICE per iniziare il prossimo BLOCCO.', color='black')
    messaggio_inizio_blocco.draw()
    win.flip()
    event.waitKeys(keyList=['space'])


    for trial in trial_indices:
        istruzioni = visual.TextStim(win, text='CONCENTRATI, tra poco sentirai il primo BEEP', color='black')
        istruzioni.draw()
        win.flip()
        core.wait(2.5)

        play_sound()

        countdown = visual.TextStim(win, text='', pos=(0.9, -0.9), color='black')  
        cross = visual.TextStim(win, text='+', pos=(0, 0), color='black', height=0.1)  
        start_time = core.getTime()
        while core.getTime() - start_time < durations[trial]:
            remaining_time = int(durations[trial] - (core.getTime() - start_time))
            countdown.text = str(remaining_time)
            cross.draw()
            countdown.draw()
            win.flip()

        play_sound()

        
        event.clearEvents(eventType='keyboard')

        messaggio_inserimento = visual.TextStim(win, text='Inserisci il numero di battiti contati:', color='black', pos=(0, 0.2))
        input_box = visual.Rect(win, width=0.5, height=0.1, pos=(0, -0.1), fillColor='white')
        input_battiti = ''
        input_text = visual.TextStim(win, text=input_battiti, color='black', pos=(0, -0.1))

        while True:
            messaggio_inserimento.draw()
            input_box.draw()
            input_text.draw()
            win.flip()

            keys = event.getKeys()
            if 'return' in keys:
                try:
                    battiti_count = int(input_battiti)
                    data = {
                        'Codice Partecipante': [codice_soggetto],
                        'Counting': [battiti_count],
                        'Task': [task_names[trial]],
                        'VAS': [None]  
                    }
                    new_df = pd.DataFrame(data)
                    df = pd.concat([df, new_df], ignore_index=True)
                    break
                except ValueError:
                    print("Inserire un numero valido di battiti.")
            elif keys:
                if keys[0] == 'backspace':
                    input_battiti = input_battiti[:-1]
                else:
                    input_battiti += keys[0]
                input_text.text = input_battiti

            if 'escape' in keys:
                win.close()
                core.quit()

        messaggio_controllo_segnale = visual.TextStim(win, text='Prima di continuare controlleremo che non ci siano problemi nella registrazione del segnale.\nPremi la barra spaziatrice per continuare.', color='black')
        messaggio_controllo_segnale.draw()
        win.flip()
        event.waitKeys(keyList=['space'])


    istruzioni_vas = visual.TextStim(win, text='Indica secondo te quanto sei stato/a sicuro/a della stima dei battiti, utilizzando la linea che va da 0 (=per nulla sicura) a 100 (=estremamente sicura)', color='black', pos=(0, 0.5))
    vas_line = visual.Rect(win, width=1.5, height=0.05, fillColor='black', pos=(0, 0))
    vas_labels = [
        visual.TextStim(win, text='per nulla sicuro/a', color='black', pos=(-0.75, -0.1), height=0.05),
        visual.TextStim(win, text='estremamente sicuro/a', color='black', pos=(0.75, -0.1), height=0.05)
    ]

    vas_rating = None
    while vas_rating is None:
        istruzioni_vas.draw()
        vas_line.draw()
        for label in vas_labels:
            label.draw()
        win.flip()

        mouse = event.Mouse(win=win)
        if mouse.getPressed()[0]:
            mouse_pos = mouse.getPos()
            if -0.75 <= mouse_pos[0] <= 0.75 and -0.05 <= mouse_pos[1] <= 0.05:
                vas_rating = (mouse_pos[0] + 0.75) / 1.5 * 100
                df['VAS'].iloc[-num_trials:] = vas_rating 

                
                df.to_excel(results_file, index=False)

                
                messaggio_fine = visual.TextStim(win, text='Grazie per aver partecipato!', color='black')
                messaggio_fine.draw()
                win.flip()
                event.waitKeys(keyList=['space'])
                break

        if 'escape' in event.getKeys():
            win.close()
            core.quit()

    win.close()
    core.quit()

run_experiment(5)
