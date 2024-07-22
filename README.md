## Консольное приложение на Python для работы с аудиофайлами формата WAV

### Сборка решения:
```
docker-compose build
```

### Для запуска modify нужно выполнить команду:
```
docker-compose run audio-processing modify --volume 3 --speed 0.5
docker-compose run audio-processing modify /app/audio_input/test_input_file.wav /app/audio_output/test_output_file.wav --speed 1.5 --volume 1.2
```
Если volume и speed не будут указаны, аудио останется неизменным. Установлены default значения для input_file и output_file (audio_input/test_input_file.wav и audio_output/test_output_file.wav).

### Для запуска transcribe выполнить команду:
```
docker-compose run audio-processing transcribe
docker-compose run audio-processing transcribe /app/audio_input/test_input_file.wav /app/txt_output/test_output_file.txt
```
Установлены default значения для input_file и output_file (audio_input/test_input_file.wav и txt_output/test_output_file.txt)

В папке audio_input загружен аудиофайл с сайта и записанные мной аудио для распознавания.

Возможна работа офлайн, но для этого нужно запустить хотя бы один раз с интернетом, чтобы модель Whisper скачалась. Я работал с Whisper Small. Модель можно поменять в файле download_model.py 
```
model = whisper.load_model("ваша версия Whisper из списка ['tiny','base','small','medium','large']")
```
Модель скачается один раз, далее будет использоваться скаченная версия. 
