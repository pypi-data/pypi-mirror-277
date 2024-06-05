#  Copyright (C) 2024. Hao Zheng
#  All rights reserved.

import gradio as gr


def create_ui():
    with gr.Blocks() as app:
        gr.Markdown("# OpenLRC 🎙📄")
        gr.Markdown('*Transcribe and translate voice into LRC file using Whisper and LLMs (GPT, Claude, et,al).*')


    return app


if __name__ == "__main__":
    create_ui().launch()
