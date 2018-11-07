##########################################################
###   Python script to downsample FreeSound data to 8 KHz
##########################################################

import os
import librosa
import sounddevice as sd
import soundfile as sf



wavDir_in ='C:\\MUIT_TSA\\AUDIO_CHALLENGE\\Data\\audio_train\\'
wavDir_out ='C:\\MUIT_TSA\\AUDIO_CHALLENGE\\Data\\SUB_SAMPLING\\Data\\audio_train16\\'

for dirName, subdirList, fileList in os.walk(wavDir_in):

        for fName in fileList:

            print('Processing File: ',fName)

            y, sr = librosa.load(wavDir_in+ '\\' + fName, sr=44100)
            #sd.play(y,44000)
            if y.shape[0] != 0:
                y_8k = librosa.resample(y, sr, 8000)
            else:
                y_8=y
            #sd.play(y_8k, 8000)
            #librosa.output.write_wav( \
            #    wavDir_out + '\\' + fName, y_8k, 8000)

            sf.write( \
                wavDir_out + '\\' + fName, y_8k, 8000, 'PCM_16')
            # Copy wav file to WavTest
            # First empty WavTest


            #copyfile(dirName+ '\\' + fName,
            #         Dir_path_to_data + fName)

