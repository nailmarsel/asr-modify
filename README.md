## Консольное приложение на Python для работы с аудиофайлами формата WAV

### Установка необходимых библиотек:
```
pip install -r requirements.txt
```

### Для запуска modify выполнить команду:
```
python main.py modify --volume 3 --speed 0.5
python main.py modify audio_input/test_input_file.wav audio_output/test_output_file.wav --speed 1.5
```
Если volume и speed не будут указаны, аудио останется неизменным. Установлены default значения для input_file и output_file (audio_input/test_input_file.wav и audio_output/test_output_file.wav).

### Для запуска transcribe выполнить команду:
```
python main.py transcribe
python main.py transcribe audio_input/record_out.wav txt_output/record_out.txt 
```
Установлены default значения для input_file и output_file (audio_input/test_input_file.wav и txt_output/test_output_file.txt)

В папке audio_input загружен аудиофайл с сайта и записанные мной аудио для распознавания.

Возможна работа офлайн, но для этого нужно запустить хотя бы один раз с интернетом, чтобы модель Whisper скачалась
