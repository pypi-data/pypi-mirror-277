
import gradio as gr
from gradio_rangeslider import RangeSlider
from pathlib import Path

text = "## The range is: {min} to {max}"

docs = Path(__file__).parent / "docs.md"

with gr.Blocks() as demo:
    with gr.Tabs():
        with gr.Tab("Demo"):
            gr.Markdown("""## 🛝 RangeSlider

            ## Drag either end and see the selected endpoints update in real-time.
            """)
            slider = gr.Slider(minimum=0, maximum=100, value=50, interactive=True)
            range_slider = RangeSlider(minimum=0, maximum=100, value=(0, 500), interactive=True)
            with gr.Row():
                with gr.Column():
                    range_ = gr.Markdown(value=text.format(min=0, max=100))
                with gr.Column():
                    label = gr.JSON(label="Value on release")
            range_slider.change(lambda s: text.format(min=s[0], max=s[1]), range_slider, range_,
                                show_progress="hide", trigger_mode="always_last")
            range_slider.release(lambda s: dict(min=s[0], max=s[1]), range_slider, label)
            button = gr.Button("Break Range")
            button.click(lambda: (-10, 270), None, range_slider)
            gr.Examples([(20, 30), (40, 80)], inputs=[range_slider])
        with gr.Tab("Docs"):
            gr.Markdown(docs.read_text())


if __name__ == "__main__":
    demo.launch()
