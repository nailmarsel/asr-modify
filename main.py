import argparse

from modify import modify_audio
from transcribe import transcribe_audio

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Audio processing tool")
    subparsers = parser.add_subparsers(dest="command")

    # Subparser for modifying audio
    parser_modify = subparsers.add_parser("modify", help="Modify audio file")
    parser_modify.add_argument("input_file", nargs='?', default="audio_input/test_input_file.wav", help="Path to the input WAV file")
    parser_modify.add_argument("output_file", nargs='?', default="audio_output/test_output_file.wav", help="Path to the output WAV file")
    parser_modify.add_argument("--speed", type=float, default=1.0, help="Playback speed (default: 1.0)")
    parser_modify.add_argument("--volume", type=float, default=1.0, help="Volume multiplier (default: 1.0)")

    # Subparser for transcribing audio
    parser_transcribe = subparsers.add_parser("transcribe", help="Transcribe audio file to text")
    parser_transcribe.add_argument("input_file", nargs='?', default="audio_input/test_input_file.wav", help="Path to the input WAV file")
    parser_transcribe.add_argument("output_file", nargs='?', default="txt_output/test_output_file.txt", help="Path to the output TXT file")

    args = parser.parse_args()

    if args.command == "modify" and "wav" in args.input_file and "wav" in args.output_file:
        modify_audio(args.input_file, args.output_file, args.speed, args.volume)
    elif args.command == "transcribe" and "wav" in args.input_file:
        transcribe_audio(args.input_file, args.output_file)
    else:
        parser.print_help()