import gradio as gr


def greet(name):
    return f"Hello {name}! This is auto-deployed from GitHub."


demo = gr.Interface(fn=greet, inputs="text", outputs="text")
demo.launch()
